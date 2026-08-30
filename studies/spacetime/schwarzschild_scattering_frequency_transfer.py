#!/usr/bin/env python3
"""Static-endpoint frequency transfer for finite Schwarzschild null scattering.

This is a bounded project derivation and negative identifiability control. It is
not a detector model and supplies no evidence for UMCH or an ell0 value.
"""
import argparse
import importlib.util
import json
import math
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / "schwarzschild-scattering-frequency-transfer-results.json"
STATUS = "SCHWARZSCHILD_STATIC_ENDPOINT_FREQUENCY_TRANSFER_FIXES_AFFINE_NORMALIZATION_RELATIVE_TO_EXTERNAL_CLOCK_BUT_RETAINS_GEOMETRIC_SCALE_BLINDNESS_NOT_ELL0"
GATE = "PHYSICAL_SOURCE_CLOCK_SPECTRUM_ABSORBER_RESPONSE_SCREEN_PREPARATION_VECTOR_READOUT_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED"
SCOPE = "FOUR_DIMENSIONAL_SCHWARZSCHILD_EQUATORIAL_FUTURE_NULL_FINITE_SCATTERING_STATIC_ENDPOINT_TETRADS_SOURCE_LOCAL_FREQUENCY_TOY_CLOCK_FULL_SCREEN_PHASE_MAP_NO_DETECTOR"


def _load(name, filename):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


jac = _load("frequency_transfer_jacobi", "schwarzschild_null_scattering_jacobi.py")
mat = jac.m


def _maxabs(A):
    return max((abs(x) for row in A for x in row), default=0.0)


def _sub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def _diag_rate(rate):
    return [[1.0 if i == j and i < 2 else rate if i == j else 0.0 for j in range(4)] for i in range(4)]


def _similarity(P, D):
    return mat.mm(D, mat.mm(P, jac.inverse(D)))


def _f(M, r):
    if M <= 0.0 or r <= 2.0 * M:
        raise ValueError("static tetrad requires M>0 and r>2M")
    return 1.0 - 2.0 * M / r


def static_frequency_transfer(M, r_source, r_observer, omega_source):
    if omega_source <= 0.0:
        raise ValueError("source frequency must be positive")
    fs = _f(M, r_source)
    fo = _f(M, r_observer)
    energy = omega_source * math.sqrt(fs)
    omega_observer = energy / math.sqrt(fo)
    return {
        "M": M,
        "r_source": r_source,
        "r_observer": r_observer,
        "omega_source": omega_source,
        "omega_observer": omega_observer,
        "transfer_ratio": omega_observer / omega_source,
        "source_killing_energy": energy,
        "observer_killing_energy": omega_observer * math.sqrt(fo),
        "classification": "STATIC_TETRAD_FREQUENCY_TRANSFER_KNOWN_GEOMETRIC_RELATION",
    }


def validate_endpoint_frequencies(M, r_source, r_observer, omega_source, omega_observer, tolerance=1e-12):
    expected = static_frequency_transfer(M, r_source, r_observer, omega_source)
    if abs(omega_observer - expected["omega_observer"]) > tolerance:
        raise ValueError("independent endpoint frequencies violate conserved Killing energy")
    return expected


def _rescaled_profile(profile, tangent_scale):
    if tangent_scale <= 0.0:
        raise ValueError("tangent scale must be positive")
    samples = []
    for item in profile["samples"]:
        z = dict(item)
        z["lambda"] = item["lambda"] / tangent_scale
        z["K"] = [[tangent_scale * tangent_scale * x for x in row] for row in item["K"]]
        samples.append(z)
    return {**profile, "samples": samples, "tangent_scale": tangent_scale}


def affine_frequency_control(M=1.0, rho=4.0, R=12.0, omega_source=0.2, n=80):
    transfer = static_frequency_transfer(M, R * M, R * M, omega_source)
    a = transfer["source_killing_energy"]
    base_profile = jac.profile_control(M, rho, R, 1, n)
    scaled_profile = _rescaled_profile(base_profile, a)
    _, P_base, _ = jac._phase_from_profile(base_profile)
    _, P_scaled, residuals = jac._phase_from_profile(scaled_profile)
    D = _diag_rate(a)
    expected = _similarity(P_base, D)
    ratios = []
    profile_residual = 0.0
    for old, new in zip(base_profile["samples"], scaled_profile["samples"]):
        for i in range(2):
            if abs(old["K"][i][i]) > 1e-15:
                ratios.append(new["K"][i][i] / old["K"][i][i])
            profile_residual = max(profile_residual, abs(new["K"][i][i] - a * a * old["K"][i][i]))
    return {
        "omega_source": omega_source,
        "omega_observer": transfer["omega_observer"],
        "tangent_scale": a,
        "profile_quadratic_ratio": sum(ratios) / len(ratios),
        "profile_scaling_residual": profile_residual,
        "P_project_anchor": P_base,
        "P_source_frequency": P_scaled,
        "rate_similarity": D,
        "raw_rate_map_difference": _maxabs(_sub(P_scaled, P_base)),
        "converted_phase_map_residual": _maxabs(_sub(P_scaled, expected)),
        "symplectic_residual": residuals["symplectic_residual"],
        "classification": "SOURCE_LOCAL_FREQUENCY_FIXES_AFFINE_NORMALIZATION_RELATIVE_TO_EXTERNAL_CLOCK",
    }


def _frequency_phase_map(M, rho, R, omega_source, n):
    base = jac.profile_control(M, rho, R, 1, n)
    a = omega_source * math.sqrt(1.0 - 2.0 / R)
    _, P, _ = jac._phase_from_profile(_rescaled_profile(base, a))
    return P, a


def _dimensionless_frequency_map(M, rho, R, nu_source, n):
    P, _ = _frequency_phase_map(M, rho, R, nu_source / M, n)
    # lambda_frequency scales as M^2 at fixed nu_source; use M^2 d/dlambda.
    C = _diag_rate(M * M)
    return _similarity(P, C)


def geometric_scale_control(M=1.0, rho=4.0, R=12.0, nu_source=0.2, factor=1.7, n=80):
    if factor <= 0.0:
        raise ValueError("scale factor must be positive")
    P0, a0 = _frequency_phase_map(M, rho, R, nu_source / M, n)
    P1, a1 = _frequency_phase_map(factor * M, rho, R, nu_source / (factor * M), n)
    D = _diag_rate(1.0 / (factor * factor))
    expected = _similarity(P0, D)
    return {
        "factor": factor,
        "nu_source": nu_source,
        "omega_source_reference": nu_source / M,
        "omega_source_scaled": nu_source / (factor * M),
        "tangent_scale_ratio": a1 / a0,
        "dimensionless_frequency_transfer_residual": abs((factor * M) * (nu_source / (factor * M)) - M * (nu_source / M)),
        "rate_similarity": D,
        "converted_phase_map_residual": _maxabs(_sub(P1, expected)),
        "classification": "GEOMETRIC_SCALE_BLIND_AT_FIXED_DIMENSIONLESS_SOURCE_FREQUENCY",
    }


def external_frequency_standard_control(M=1.0, rho=4.0, R=12.0, omega_source=0.2, factor=1.7, n=60):
    P0 = _dimensionless_frequency_map(M, rho, R, M * omega_source, n)
    P1 = _dimensionless_frequency_map(factor * M, rho, R, factor * M * omega_source, n)
    return {
        "factor": factor,
        "omega_source_held_fixed": omega_source,
        "nu_source_reference": M * omega_source,
        "nu_source_scaled": factor * M * omega_source,
        "varying_product": "M_TIMES_OMEGA_SOURCE",
        "raw_output_difference": _maxabs(_sub(P1, P0)),
        "classification": "EXTERNAL_FREQUENCY_STANDARD_DIRECTION_NOT_INTERIOR_GEOMETRIC_SCALE",
        "ell0_identified": False,
    }


def _feature(M, rho, R, nu_source, n):
    P = _dimensionless_frequency_map(M, rho, R, nu_source, n)
    return [P[i][j] for i in range(4) for j in range(4)]


def _rank(columns, tolerance=1e-7):
    basis = []
    for column in columns:
        v = column[:]
        for q in basis:
            dot = sum(a * b for a, b in zip(v, q))
            v = [a - dot * b for a, b in zip(v, q)]
        length = math.sqrt(sum(x * x for x in v))
        if length > tolerance:
            basis.append([x / length for x in v])
    return len(basis)


def rank_control(M=1.0, rho=4.0, R=12.0, nu_source=0.2, n=60, step=1e-4):
    columns = []
    for parameter in ("rho", "R", "log_M"):
        if parameter == "rho":
            plus = _feature(M, rho + step, R, nu_source, n)
            minus = _feature(M, rho - step, R, nu_source, n)
        elif parameter == "R":
            plus = _feature(M, rho, R + step, nu_source, n)
            minus = _feature(M, rho, R - step, nu_source, n)
        else:
            plus = _feature(M * math.exp(step), rho, R, nu_source, n)
            minus = _feature(M * math.exp(-step), rho, R, nu_source, n)
        columns.append([(a - b) / (2.0 * step) for a, b in zip(plus, minus)])
    norms = [math.sqrt(sum(x * x for x in column)) for column in columns]
    return {
        "parameters": ["rho", "R", "log_M"],
        "rank_shape_boundary": _rank(columns[:2]),
        "rank_with_log_M": _rank(columns),
        "column_norms": norms,
        "log_M_column_norm": norms[2],
        "scale_null_direction": [0, 0, 1],
        "global_injectivity": "NOT_ESTABLISHED",
        "classification": "LOCAL_RANK_NOT_GLOBAL_IDENTIFIABILITY_AND_GEOMETRIC_SCALE_COLUMN_NULL",
    }


def build_result(n=80):
    return {
        "UMCH": "UNPROVEN",
        "status": STATUS,
        "scope": SCOPE,
        "gate": GATE,
        "classification": "PROJECT_DERIVATION_AND_TOY_STATIC_CLOCK_CONTROL_WITH_NEGATIVE_AFFINE_AND_GEOMETRIC_SCALE_IDENTIFIABILITY_RESULT",
        "primary_object": "FULL_SCREEN_PHASE_MAP_REMAINS_PRIMARY",
        "screen_order": ["polar", "in-plane"],
        "optical_profile": "diag(-1,+1) 3 M b^2/r^5 AT E_INFINITY=1",
        "frequency_transfer": static_frequency_transfer(1.0, 12.0, 9.0, 0.2),
        "equal_endpoint_transfer": static_frequency_transfer(1.0, 12.0, 12.0, 0.2),
        "affine_frequency": affine_frequency_control(n=n),
        "geometric_scale": geometric_scale_control(n=n),
        "external_frequency_standard": external_frequency_standard_control(n=max(40, n // 2)),
        "rank": rank_control(n=max(40, n // 2)),
        "source_clock": "TOY_EXTERNAL_FREQUENCY_STANDARD_NOT_DETECTOR_DERIVED",
        "independent_channels": False,
        "ell0_identified": False,
        "structural_dead_end": "NOT_DECLARED",
        "detection": "NO_POSITIVE_DETECTION_CLAIM",
        "maximum_interpretation": "CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE",
        "review": "DIRECT_REVIEW_NO_SUBAGENT",
    }


def render(result):
    return json.dumps(result, indent=2, sort_keys=True) + "\n"


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args(argv)
    text = render(build_result())
    if args.check:
        if not OUT.exists() or OUT.read_text() != text:
            print("artifact mismatch", file=sys.stderr)
            return 1
        return 0
    OUT.write_text(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
