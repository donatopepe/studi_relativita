#!/usr/bin/env python3
"""Toy coherent I/Q readout for finite Schwarzschild null scattering.

Bounded project derivation and negative identifiability control. Source, local
oscillator, receiver and gains are declared toys, not physical detector models.
"""
import argparse
import importlib.util
import json
import math
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / "schwarzschild-scattering-coherent-readout-results.json"
STATUS = "SCHWARZSCHILD_COHERENT_ENDPOINT_IQ_READOUT_IS_SOURCE_LO_GAIN_NUISANCE_AND_RETAINS_GEOMETRIC_SCALE_BLINDNESS_NOT_ELL0"
GATE = "PHYSICAL_SOURCE_COHERENCE_EMISSION_ABSORPTION_POLARIZATION_SCREEN_COUPLING_RECEIVER_TRANSFER_CALIBRATED_NOISE_JOINT_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED"
SCOPE = "FOUR_DIMENSIONAL_SCHWARZSCHILD_EQUATORIAL_FUTURE_NULL_FINITE_SCATTERING_EQUAL_RADIUS_STATIC_ENDPOINT_TOY_COHERENT_IQ_FULL_SCREEN_PHASE_MAP_NO_PHYSICAL_DETECTOR"


def _load(name, filename):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


cp = _load("coherent_readout_clock_phase", "schwarzschild_scattering_clock_phase.py")


def _maxabs_vector(a, b):
    return max(abs(x - y) for x, y in zip(a, b))


def _maxabs_matrix(A, B):
    return max(abs(A[i][j] - B[i][j]) for i in range(len(A)) for j in range(len(A[0])))


def _identity_residual(P):
    return max(abs(P[i][j] - (1.0 if i == j else 0.0)) for i in range(4) for j in range(4))


def iq_readout(phase, A_source=1.3, phi_source=0.4, gain=0.8, phi_lo=-0.2, propagation_gain=1.0):
    if A_source <= 0.0 or gain <= 0.0 or propagation_gain <= 0.0:
        raise ValueError("require positive source, receiver and propagation gains")
    amplitude = A_source * gain * propagation_gain
    relative_phase = phase + phi_source - phi_lo
    return {
        "y_IQ": [amplitude * math.cos(relative_phase), amplitude * math.sin(relative_phase)],
        "amplitude": amplitude,
        "relative_phase": relative_phase,
        "A_source": A_source,
        "phi_source": phi_source,
        "receiver_gain": gain,
        "phi_LO": phi_lo,
        "propagation_gain": propagation_gain,
    }


def quotient_representative(y):
    norm = math.hypot(y[0], y[1])
    if norm == 0.0:
        raise ValueError("quotient requires nonzero I/Q vector")
    return [1.0, 0.0]


def nuisance_controls(phase):
    base = iq_readout(phase)
    shifted = iq_readout(phase, phi_source=0.4 + 0.73, phi_lo=-0.2 + 0.73)
    compensated = iq_readout(phase, A_source=1.3 * 2.0, gain=0.8 / 2.0)
    I, Q = base["y_IQ"]
    J = [[I, -Q, I, Q], [Q, I, Q, -I]]
    phase_null = [0.0, 1.0, 0.0, 1.0]
    amplitude_null = [1.0, 0.0, -1.0, 0.0]

    def residual(v):
        return max(abs(sum(J[i][j] * v[j] for j in range(4))) for i in range(2))

    return {
        "parameters": ["log_A_source", "phi_source", "log_G", "phi_LO"],
        "jacobian": J,
        "nuisance_jacobian_rank": cp._rank(J),
        "phase_null_direction": phase_null,
        "amplitude_null_direction": amplitude_null,
        "phase_null_residual": residual(phase_null),
        "amplitude_null_residual": residual(amplitude_null),
        "common_phase_residual": _maxabs_vector(base["y_IQ"], shifted["y_IQ"]),
        "source_gain_compensation_residual": _maxabs_vector(base["y_IQ"], compensated["y_IQ"]),
        "classification": "SOURCE_LO_PHASE_AND_SOURCE_RECEIVER_GAIN_HAVE_EXACT_NUISANCE_NULL_DIRECTIONS",
    }


def quotient_control(phase):
    reference = iq_readout(phase)["y_IQ"]
    transformed = iq_readout(phase, A_source=2.7, phi_source=-1.1, gain=1.9, phi_lo=0.6)["y_IQ"]
    q0 = quotient_representative(reference)
    q1 = quotient_representative(transformed)
    return {
        "reference_representative": q0,
        "transformed_representative": q1,
        "representative_residual": _maxabs_vector(q0, q1),
        "classification": "UNRESTRICTED_POSITIVE_GAIN_AND_PHASE_QUOTIENT_REMOVES_SCALAR_CARRIER_IQ_CONTENT",
    }


def _raw_record(M, rho, R, nu_source, n=80):
    phase = cp.clock_phase(M, rho, R, nu_source, n)["phase"]
    P = cp._converted_map(M, rho, R, nu_source, n)
    readout = iq_readout(phase)
    return {**readout, "Phi_clock": phase, "P_frequency_converted": P}


def zero_window_control(M=1.0, rho=4.0, nu_source=0.2, n=80):
    coarse = _raw_record(M, rho, rho + 0.02, nu_source, n)
    fine = _raw_record(M, rho, rho + 0.005, nu_source, n)
    return {
        "coarse_clock_phase": coarse["Phi_clock"],
        "fine_clock_phase": fine["Phi_clock"],
        "coarse_map_identity_residual": _identity_residual(coarse["P_frequency_converted"]),
        "fine_map_identity_residual": _identity_residual(fine["P_frequency_converted"]),
        "fine_raw_iq_norm": math.hypot(*fine["y_IQ"]),
        "classification": "ZERO_WINDOW_GEOMETRY_LIMIT_DOES_NOT_REMOVE_ARBITRARY_SOURCE_LO_CARRIER_PHASE",
    }


def geometric_scale_control(M=1.0, rho=4.0, R=12.0, nu_source=0.2, factor=1.7, n=80):
    reference = _raw_record(M, rho, R, nu_source, n)
    scaled = _raw_record(factor * M, rho, R, nu_source, n)
    return {
        "scale_factor": factor,
        "iq_residual": _maxabs_vector(reference["y_IQ"], scaled["y_IQ"]),
        "clock_phase_residual": abs(reference["Phi_clock"] - scaled["Phi_clock"]),
        "converted_phase_map_residual": _maxabs_matrix(reference["P_frequency_converted"], scaled["P_frequency_converted"]),
        "quotient_residual": _maxabs_vector(quotient_representative(reference["y_IQ"]), quotient_representative(scaled["y_IQ"])),
        "classification": "GEOMETRIC_DILATION_NULL_DIRECTION_AT_FIXED_DIMENSIONLESS_SOURCE_FREQUENCY",
    }


def external_frequency_standard_control(M=1.0, rho=4.0, R=12.0, omega_source=0.2, factor=1.7, n=80):
    reference = _raw_record(M, rho, R, M * omega_source, n)
    scaled = _raw_record(factor * M, rho, R, factor * M * omega_source, n)
    return {
        "omega_source": omega_source,
        "nu_source_reference": M * omega_source,
        "nu_source_scaled": factor * M * omega_source,
        "iq_difference": math.hypot(*(scaled["y_IQ"][i] - reference["y_IQ"][i] for i in range(2))),
        "clock_phase_difference": scaled["Phi_clock"] - reference["Phi_clock"],
        "classification": "EXTERNAL_FREQUENCY_STANDARD_DIRECTION_NOT_INTERIOR_GEOMETRIC_SCALE",
    }


def _feature(M, rho, R, nu_source, quotient, n):
    record = _raw_record(M, rho, R, nu_source, n)
    iq = quotient_representative(record["y_IQ"]) if quotient else record["y_IQ"]
    return iq + [record["Phi_clock"]] + [x for row in record["P_frequency_converted"] for x in row]


def rank_control(M=1.0, rho=4.0, R=12.0, nu_source=0.2, n=80, h=1e-4):
    def jacobian(quotient):
        base = [rho, R, math.log(M)]
        columns = []
        for j in range(3):
            plus = base[:]
            minus = base[:]
            plus[j] += h
            minus[j] -= h
            fp = _feature(math.exp(plus[2]), plus[0], plus[1], nu_source, quotient, n)
            fm = _feature(math.exp(minus[2]), minus[0], minus[1], nu_source, quotient, n)
            columns.append([(a - b) / (2.0 * h) for a, b in zip(fp, fm)])
        return [[columns[j][i] for j in range(3)] for i in range(len(columns[0]))]

    raw = jacobian(False)
    quotient = jacobian(True)
    return {
        "parameters": ["rho", "R", "log_M"],
        "rank_raw_shape_boundary": cp._rank([row[:2] for row in raw]),
        "rank_raw_with_log_M": cp._rank(raw),
        "rank_quotient_shape_boundary": cp._rank([row[:2] for row in quotient]),
        "rank_quotient_with_log_M": cp._rank(quotient),
        "raw_log_M_column_norm": math.sqrt(sum(row[2] ** 2 for row in raw)),
        "quotient_log_M_column_norm": math.sqrt(sum(row[2] ** 2 for row in quotient)),
        "scale_null_direction": [0, 0, 1],
        "global_injectivity": "NOT_ESTABLISHED",
        "statistical_independence": "DEPENDENCE_UNRESOLVED_WITHOUT_JOINT_COVARIANCE",
    }


def build_result(M=1.0, rho=4.0, R=12.0, nu_source=0.2, n=80):
    raw = _raw_record(M, rho, R, nu_source, n)
    return {
        "study": "schwarzschild-scattering-coherent-readout",
        "status": STATUS,
        "gate": GATE,
        "scope": SCOPE,
        "screen_order": ["polar", "in-plane"],
        "parameters": {"M": M, "rho": rho, "R": R, "nu_source": nu_source, "n": n},
        "raw_readout": raw,
        "nuisance_controls": nuisance_controls(raw["Phi_clock"]),
        "quotient_control": quotient_control(raw["Phi_clock"]),
        "zero_window_control": zero_window_control(M, rho, nu_source, n),
        "geometric_scale_control": geometric_scale_control(M, rho, R, nu_source, n=n),
        "external_frequency_standard_control": external_frequency_standard_control(M, rho, R, n=n),
        "rank_control": rank_control(M, rho, R, nu_source, n),
        "source_scope": {
            "keys": ["Schwarzschild2003Translation", "Darwin1959GravityField", "Sachs1961"],
            "not_established": "coherent source dynamics; emission or absorption interaction; polarization-screen coupling; receiver transfer; calibrated noise; joint covariance; ell0; UMCH; evidence; detection",
        },
        "classification": {
            "propagation_geometry": "KNOWN_RESULT_WITHIN_CITED_SCOPE",
            "iq_nuisance_and_rank_audit": "PROJECT_DERIVATION",
            "source_lo_receiver": "TOY_CONTROL_NOT_PHYSICAL_DETECTOR",
            "scale_blindness": "NEGATIVE_RESULT",
            "physical_readout_and_covariance": "OPEN_PROBLEM",
        },
        "UMCH": "UNPROVEN",
        "ell0_identified": False,
        "detection": "NO_POSITIVE_DETECTION_CLAIM",
        "structural_dead_end": "NOT_DECLARED",
        "maximum_interpretation": "CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE",
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
