#!/usr/bin/env python3
"""Finite static-endpoint clock phase joined to Schwarzschild scattering optics.

Bounded project derivation and negative identifiability control. No physical
clock, emitter, absorber or detector model is supplied; this is not UMCH evidence.
"""
import argparse
import importlib.util
import json
import math
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / "schwarzschild-scattering-clock-phase-results.json"
STATUS = "SCHWARZSCHILD_STATIC_ENDPOINT_CLOCK_PHASE_ADDS_CROSS_CHANNEL_SHAPE_BUT_RETAINS_EXTERNAL_FREQUENCY_AND_GEOMETRIC_SCALE_BLINDNESS_NOT_ELL0"
GATE = "PHYSICAL_CLOCK_REALIZATION_SOURCE_COHERENCE_EMISSION_ABSORPTION_SCREEN_PREPARATION_VECTOR_READOUT_JOINT_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED"
SCOPE = "FOUR_DIMENSIONAL_SCHWARZSCHILD_EQUATORIAL_FUTURE_NULL_FINITE_SCATTERING_EQUAL_RADIUS_STATIC_ENDPOINT_CLOCK_TOY_SOURCE_FREQUENCY_FULL_SCREEN_PHASE_MAP_NO_DETECTOR"


def _load(name, filename):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


jac = _load("clock_phase_jacobi", "schwarzschild_null_scattering_jacobi.py")
ft = _load("clock_phase_frequency", "schwarzschild_scattering_frequency_transfer.py")


def _trap(values, h):
    return h * (0.5 * values[0] + sum(values[1:-1]) + 0.5 * values[-1])


def _maxabs_matrix(A, B):
    return max(abs(A[i][j] - B[i][j]) for i in range(len(A)) for j in range(len(A[0])))


def _identity_residual(P):
    return max(abs(P[i][j] - (1.0 if i == j else 0.0)) for i in range(4) for j in range(4))


def _validate(M, rho, R, nu_source, n):
    if M <= 0.0 or not (R > rho > 3.0):
        raise ValueError("require M>0 and R>rho>3")
    if nu_source <= 0.0 or n < 8:
        raise ValueError("require positive nu_source and n>=8")


def _timing_integrand(y, rho, beta):
    x = rho + y * y
    f = 1.0 - 2.0 / x
    if y == 0.0:
        qprime = 2.0 * beta * beta * (rho - 3.0) / rho**4
        return 2.0 / (f * math.sqrt(qprime))
    q = 1.0 - beta * beta * f / (x * x)
    return 2.0 * y / (f * math.sqrt(max(q, 1e-30)))


def elapsed_time(M=1.0, rho=4.0, R=12.0, n=400):
    _validate(M, rho, R, 1.0, n)
    beta = rho / math.sqrt(1.0 - 2.0 / rho)
    ymax = math.sqrt(R - rho)
    h = ymax / n
    half_over_M = _trap([_timing_integrand(i * h, rho, beta) for i in range(n + 1)], h)
    delta_t_over_M = 2.0 * half_over_M
    delta_tau_over_M = math.sqrt(1.0 - 2.0 / R) * delta_t_over_M
    return {
        "M": M,
        "rho": rho,
        "R": R,
        "beta": beta,
        "delta_t": M * delta_t_over_M,
        "delta_t_over_M": delta_t_over_M,
        "delta_tau": M * delta_tau_over_M,
        "delta_tau_over_M": delta_tau_over_M,
        "turning_integrand_limit": _timing_integrand(0.0, rho, beta),
    }


def _direct_cutoff_time(rho, R, panels=200000, epsilon=1e-8):
    beta = rho / math.sqrt(1.0 - 2.0 / rho)
    lo = rho + epsilon
    h = (R - lo) / panels
    total = 0.0
    for i in range(panels):
        x = lo + (i + 0.5) * h
        f = 1.0 - 2.0 / x
        q = 1.0 - beta * beta * f / (x * x)
        total += 1.0 / (f * math.sqrt(q))
    # Leading omitted endpoint integral from q=q'(rho)(x-rho).
    qprime = 2.0 * beta * beta * (rho - 3.0) / rho**4
    missing = 2.0 * math.sqrt(epsilon) / ((1.0 - 2.0 / rho) * math.sqrt(qprime))
    return 2.0 * (h * total + missing)


def elapsed_time_control(M=1.0, rho=4.0, R=12.0, n=400):
    fine = elapsed_time(M, rho, R, n)
    coarse = elapsed_time(M, rho, R, n // 2)
    direct = _direct_cutoff_time(rho, R)
    return {
        **fine,
        "mesh_doubling_residual": abs(fine["delta_t_over_M"] - coarse["delta_t_over_M"]),
        "direct_cutoff_delta_t_over_M": direct,
        "direct_cutoff_residual": abs(fine["delta_t_over_M"] - direct),
        "direct_cutoff_epsilon": 1e-8,
        "direct_cutoff_panels": 200000,
    }


def clock_phase(M=1.0, rho=4.0, R=12.0, nu_source=0.2, n=400):
    t = elapsed_time(M, rho, R, n)
    return {**t, "nu_source": nu_source, "omega_source": nu_source / M, "phase": nu_source * t["delta_tau_over_M"]}


def _converted_map(M, rho, R, nu_source, n):
    return ft._dimensionless_frequency_map(M, rho, R, nu_source, n)


def clock_controls(M=1.0, rho=4.0, R=12.0, nu_source=0.2, n=80):
    p = clock_phase(M, rho, R, nu_source, n)
    p2 = clock_phase(M, rho, R, 2.0 * nu_source, n)
    plus = jac.profile_control(M, rho, R, 1, n)
    minus = jac.profile_control(M, rho, R, -1, n)
    return {
        "phase": p["phase"],
        "frequency_linearity_residual": abs(p2["phase"] - 2.0 * p["phase"]),
        "orientation_phase_residual": 0.0,
        "optical_orientation_labels": [plus["orientation"], minus["orientation"]],
        "classification": "CLOCK_SCALAR_ORIENTATION_EVEN_RAW_SCREEN_ORIENTATION_RETAINED",
    }


def zero_window_control(M=1.0, rho=4.0, nu_source=0.2, n=80):
    coarse_R = rho + 0.02
    fine_R = rho + 0.005
    coarse_P = _converted_map(M, rho, coarse_R, nu_source, n)
    fine_P = _converted_map(M, rho, fine_R, nu_source, n)
    return {
        "coarse_R_minus_rho": coarse_R - rho,
        "fine_R_minus_rho": fine_R - rho,
        "coarse_phase": clock_phase(M, rho, coarse_R, nu_source, n)["phase"],
        "fine_phase": clock_phase(M, rho, fine_R, nu_source, n)["phase"],
        "coarse_map_identity_residual": _identity_residual(coarse_P),
        "fine_map_identity_residual": _identity_residual(fine_P),
        "classification": "ZERO_WINDOW_PROTOCOL_LIMIT_NOT_HOLONOMY_NOT_EVIDENCE",
    }


def geometric_scale_control(M=1.0, rho=4.0, R=12.0, nu_source=0.2, factor=1.7, n=80):
    t0 = clock_phase(M, rho, R, nu_source, n)
    t1 = clock_phase(factor * M, rho, R, nu_source, n)
    P0 = _converted_map(M, rho, R, nu_source, n)
    P1 = _converted_map(factor * M, rho, R, nu_source, n)
    return {
        "factor": factor,
        "nu_source": nu_source,
        "omega_source_reference": nu_source / M,
        "omega_source_scaled": nu_source / (factor * M),
        "dimensionless_time_residual": abs(t1["delta_tau_over_M"] - t0["delta_tau_over_M"]),
        "clock_phase_residual": abs(t1["phase"] - t0["phase"]),
        "converted_phase_map_residual": _maxabs_matrix(P1, P0),
        "classification": "GEOMETRIC_DILATION_NULL_DIRECTION_AT_FIXED_DIMENSIONLESS_SOURCE_FREQUENCY",
    }


def external_frequency_standard_control(M=1.0, rho=4.0, R=12.0, omega_source=0.2, factor=1.7, n=80):
    p0 = clock_phase(M, rho, R, M * omega_source, n)
    p1 = clock_phase(factor * M, rho, R, factor * M * omega_source, n)
    return {
        "factor": factor,
        "omega_source_fixed": omega_source,
        "nu_source_reference": M * omega_source,
        "nu_source_scaled": factor * M * omega_source,
        "clock_phase_reference": p0["phase"],
        "clock_phase_scaled": p1["phase"],
        "clock_phase_difference": abs(p1["phase"] - p0["phase"]),
        "classification": "EXTERNAL_FREQUENCY_STANDARD_DIRECTION_NOT_INTERIOR_GEOMETRIC_SCALE",
    }


def _feature(M, rho, R, nu_source, n):
    phase = clock_phase(M, rho, R, nu_source, n)["phase"]
    P = _converted_map(M, rho, R, nu_source, n)
    return [phase] + [x for row in P for x in row]


def _rank(columns, tol=1e-7):
    basis = []
    for column in columns:
        v = list(column)
        for q in basis:
            projection = sum(a * b for a, b in zip(v, q))
            v = [a - projection * b for a, b in zip(v, q)]
        norm = math.sqrt(sum(a * a for a in v))
        if norm > tol:
            basis.append([a / norm for a in v])
    return len(basis)


def rank_control(M=1.0, rho=4.0, R=12.0, nu_source=0.2, n=60, h=1e-4):
    columns = []
    for p in range(3):
        if p == 0:
            fp = _feature(M, rho + h, R, nu_source, n); fm = _feature(M, rho - h, R, nu_source, n)
        elif p == 1:
            fp = _feature(M, rho, R + h, nu_source, n); fm = _feature(M, rho, R - h, nu_source, n)
        else:
            fp = _feature(M * math.exp(h), rho, R, nu_source, n); fm = _feature(M * math.exp(-h), rho, R, nu_source, n)
        columns.append([(a - b) / (2.0 * h) for a, b in zip(fp, fm)])
    norms = [math.sqrt(sum(x * x for x in c)) for c in columns]
    return {
        "parameters": ["rho", "R", "log_M"],
        "feature": "CLOCK_PHASE_PLUS_FLATTENED_FREQUENCY_CONVERTED_FULL_4X4_PHASE_MAP",
        "column_norms": norms,
        "rank_shape_boundary": _rank(columns[:2]),
        "rank_with_log_M": _rank(columns),
        "log_M_column_norm": norms[2],
        "scale_null_direction": [0.0, 0.0, 1.0],
        "global_injectivity": "NOT_ESTABLISHED",
        "statistical_independence": "NOT_ESTABLISHED_WITHOUT_JOINT_COVARIANCE",
    }


def build_result():
    M, rho, R, nu_source, n = 1.0, 4.0, 12.0, 0.2, 80
    timing = elapsed_time_control(M, rho, R, 400)
    phase = clock_phase(M, rho, R, nu_source, 400)
    P = _converted_map(M, rho, R, nu_source, n)
    return {
        "status": STATUS,
        "gate": GATE,
        "scope": SCOPE,
        "classification": "PROJECT_DERIVATION_TOY_EXTERNAL_CLOCK_NEGATIVE_IDENTIFIABILITY_CONTROL",
        "geometry": {"M": M, "rho": rho, "R": R, "beta": timing["beta"], "branches": ["incoming", "turning", "outgoing"], "endpoint_motion": "STATIC_EQUAL_RADIUS"},
        "normalization": {"nu_source": nu_source, "omega_source": nu_source / M, "affine_anchor": "SOURCE_LOCAL_FREQUENCY_RELATIVE_TO_TOY_EXTERNAL_STATIC_CLOCK", "clock_convention": "DELTA_TAU_ENDPOINT_EQUALS_SQRT_F_R_TIMES_DELTA_T", "phase_convention": "PHI_CLOCK_EQUALS_NU_SOURCE_TIMES_DELTA_TAU_OVER_M"},
        "elapsed_time_control": timing,
        "joint_record": {"Phi_clock": phase["phase"], "P_frequency_converted": P, "screen_order": ["polar", "in-plane"], "primary_object": "CLOCK_PHASE_PLUS_FULL_TRANSPORTED_SCREEN_PHASE_MAP"},
        "clock_controls": clock_controls(M, rho, R, nu_source, n),
        "zero_window_control": zero_window_control(M, rho, nu_source, n),
        "geometric_scale_control": geometric_scale_control(M, rho, R, nu_source, 1.7, n),
        "external_frequency_standard_control": external_frequency_standard_control(M, rho, R, 0.2, 1.7, n),
        "rank_control": rank_control(M, rho, R, nu_source, 60),
        "source_scope": ["Schwarzschild2003Translation", "Darwin1959GravityField", "Sachs1961"],
        "source_non_support": "NO_SOURCE_ESTABLISHES_COMPLETE_ENDPOINT_CLOCK_PROTOCOL_SOURCE_COHERENCE_EMISSION_ABSORPTION_SCREEN_PREPARATION_VECTOR_READOUT_JOINT_COVARIANCE_ELL0_UMCH_EVIDENCE_OR_DETECTION",
        "ell0_identified": False,
        "UMCH": "UNPROVEN",
        "detection": "NO_POSITIVE_DETECTION_CLAIM",
        "maximum_interpretation": "CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE",
        "structural_dead_end": "NOT_DECLARED",
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
        print(STATUS)
        return 0
    OUT.write_text(text)
    print(STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
