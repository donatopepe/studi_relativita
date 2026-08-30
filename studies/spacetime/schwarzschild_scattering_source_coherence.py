#!/usr/bin/env python3
"""Bounded Gaussian first-order source coherence for Schwarzschild scattering.

Project derivation, toy source control and negative scale-identifiability audit.
No microscopic emitter, detector, noise model, covariance or ell0 law is derived.
"""
import argparse
import importlib.util
import json
import math
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / "schwarzschild-scattering-source-coherence-results.json"
STATUS = "SCHWARZSCHILD_GAUSSIAN_SOURCE_COHERENCE_ADDS_VISIBILITY_SHAPE_BUT_FIXED_DIMENSIONLESS_COHERENCE_RETAINS_GEOMETRIC_SCALE_BLINDNESS_NOT_ELL0"
GATE = "PHYSICAL_SOURCE_SPECTRUM_COHERENCE_DYNAMICS_EMISSION_ABSORPTION_POLARIZATION_SCREEN_COUPLING_RECEIVER_TRANSFER_CALIBRATED_NOISE_JOINT_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED"
SCOPE = "FOUR_DIMENSIONAL_SCHWARZSCHILD_EQUATORIAL_FUTURE_NULL_FINITE_SCATTERING_EQUAL_RADIUS_STATIC_ENDPOINT_GAUSSIAN_FIRST_ORDER_SOURCE_COHERENCE_TOY_FULL_SCREEN_PHASE_MAP_NO_PHYSICAL_SOURCE_OR_DETECTOR"


def _load(name, filename):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


cp = _load("source_coherence_clock_phase", "schwarzschild_scattering_clock_phase.py")
cr = _load("source_coherence_readout", "schwarzschild_scattering_coherent_readout.py")


def _maxabs_vector(a, b):
    return max(abs(x - y) for x, y in zip(a, b))


def _maxabs_matrix(a, b):
    return max(abs(a[i][j] - b[i][j]) for i in range(len(a)) for j in range(len(a[0])))


def _identity_residual(matrix):
    return max(abs(matrix[i][j] - (1.0 if i == j else 0.0)) for i in range(4) for j in range(4))


def coherence_readout(delta_tau, phase, tau_c, A_coherence=1.3, phi_source=0.4, gain=0.8, phi_lo=-0.2):
    if tau_c <= 0.0 or A_coherence <= 0.0 or gain <= 0.0:
        raise ValueError("require positive coherence time, source amplitude and receiver gain")
    visibility = math.exp(-0.5 * (delta_tau / tau_c) ** 2)
    amplitude = A_coherence * gain
    relative_phase = phase + phi_source - phi_lo
    return {
        "y_coh": [amplitude * visibility * math.cos(relative_phase), amplitude * visibility * math.sin(relative_phase)],
        "visibility": visibility,
        "amplitude": amplitude,
        "relative_phase": relative_phase,
        "A_coherence": A_coherence,
        "phi_source": phi_source,
        "receiver_gain": gain,
        "phi_LO": phi_lo,
        "tau_c": tau_c,
    }


def quotient_representative(vector):
    norm = math.hypot(*vector)
    if norm == 0.0:
        raise ValueError("coherence I/Q vector must be nonzero")
    return [1.0, 0.0]


def _raw_record(M, rho, R, nu_source, chi_c=None, tau_c=None, n=80):
    if (chi_c is None) == (tau_c is None):
        raise ValueError("provide exactly one of chi_c or tau_c")
    timing = cp.clock_phase(M, rho, R, nu_source, n)
    resolved_tau_c = M * chi_c if tau_c is None else tau_c
    readout = coherence_readout(timing["delta_tau"], timing["phase"], resolved_tau_c)
    return {
        **readout,
        "chi_c": resolved_tau_c / M,
        "Phi_clock": timing["phase"],
        "Delta_tau_R": timing["delta_tau"],
        "Delta_tau_R_over_M": timing["delta_tau_over_M"],
        "P_frequency_converted": cp._converted_map(M, rho, R, nu_source, n),
    }


def nuisance_controls(phase=0.73, delta_tau=2.4, tau_c=3.0):
    base = coherence_readout(delta_tau, phase, tau_c)
    shifted = coherence_readout(delta_tau, phase, tau_c, phi_source=1.1, phi_lo=0.5)
    compensated = coherence_readout(delta_tau, phase, tau_c, A_coherence=2.6, gain=0.4)
    return {
        "common_phase_residual": _maxabs_vector(base["y_coh"], shifted["y_coh"]),
        "source_gain_compensation_residual": _maxabs_vector(base["y_coh"], compensated["y_coh"]),
        "nuisance_parameters": ["log_A_coherence", "phi_source", "log_receiver_gain", "phi_LO"],
        "nuisance_jacobian_rank": 2,
        "phase_null_direction": [0.0, 1.0, 0.0, 1.0],
        "amplitude_null_direction": [1.0, 0.0, -1.0, 0.0],
        "classification": "SOURCE_LO_PHASE_AND_SOURCE_RECEIVER_GAIN_REMAIN_EXACT_TOY_NUISANCES",
    }


def quotient_control():
    q0 = quotient_representative(coherence_readout(2.4, 0.73, 3.0)["y_coh"])
    q1 = quotient_representative(coherence_readout(5.1, -1.2, 8.0, A_coherence=2.2, gain=1.7)["y_coh"])
    return {
        "reference_representative": q0,
        "transformed_representative": q1,
        "representative_residual": _maxabs_vector(q0, q1),
        "classification": "UNRESTRICTED_POSITIVE_GAIN_AND_PHASE_QUOTIENT_REMOVES_COHERENCE_IQ_BUT_NOT_SEPARATELY_RETAINED_VISIBILITY",
    }


def zero_window_control(M=1.0, rho=4.0, nu_source=0.2, chi_c=3.0, n=80):
    epsilon = 1e-15
    record = _raw_record(M, rho, rho + epsilon, nu_source, chi_c=chi_c, n=n)
    return {
        "R_minus_rho": epsilon,
        "visibility": record["visibility"],
        "visibility_difference_from_one": abs(1.0 - record["visibility"]),
        "clock_phase": abs(record["Phi_clock"]),
        "phase_map_identity_residual": _identity_residual(record["P_frequency_converted"]),
        "raw_coherence_iq_norm": math.hypot(*record["y_coh"]),
        "interpretation": "ZERO_WINDOW_RAW_COHERENCE_PHASE_CAN_REMAIN_SOURCE_LO_NUISANCE_NOT_GEOMETRY",
    }


def geometric_scale_control(M=1.0, rho=4.0, R=12.0, nu_source=0.2, chi_c=3.0, factor=1.7, n=80):
    reference = _raw_record(M, rho, R, nu_source, chi_c=chi_c, n=n)
    scaled = _raw_record(factor * M, rho, R, nu_source, chi_c=chi_c, n=n)
    return {
        "scale_factor": factor,
        "chi_c_fixed": chi_c,
        "coherence_iq_residual": _maxabs_vector(reference["y_coh"], scaled["y_coh"]),
        "visibility_residual": abs(reference["visibility"] - scaled["visibility"]),
        "clock_phase_residual": abs(reference["Phi_clock"] - scaled["Phi_clock"]),
        "converted_phase_map_residual": _maxabs_matrix(reference["P_frequency_converted"], scaled["P_frequency_converted"]),
        "classification": "FIXED_DIMENSIONLESS_SOURCE_COHERENCE_RETAINS_SCHWARZSCHILD_DILATION_BLINDNESS",
    }


def external_coherence_standard_control(M=1.0, rho=4.0, R=12.0, nu_source=0.2, tau_c=20.0, factor=1.7, n=80):
    reference = _raw_record(M, rho, R, nu_source, tau_c=tau_c, n=n)
    scaled = _raw_record(factor * M, rho, R, nu_source, tau_c=tau_c, n=n)
    return {
        "scale_factor": factor,
        "tau_c_fixed": tau_c,
        "chi_c_reference": tau_c / M,
        "chi_c_scaled": tau_c / (factor * M),
        "visibility_difference": scaled["visibility"] - reference["visibility"],
        "coherence_iq_difference": math.hypot(*(scaled["y_coh"][i] - reference["y_coh"][i] for i in range(2))),
        "classification": "EXTERNAL_SOURCE_COHERENCE_STANDARD_DIRECTION_NOT_INTERIOR_GEOMETRIC_SCALE",
    }


def _feature(M, rho, R, nu_source, chi_c, quotient, n):
    record = _raw_record(M, rho, R, nu_source, chi_c=chi_c, n=n)
    iq = quotient_representative(record["y_coh"]) if quotient else record["y_coh"]
    return iq + [record["visibility"], record["Phi_clock"]] + [value for row in record["P_frequency_converted"] for value in row]


def rank_control(M=1.0, rho=4.0, R=12.0, nu_source=0.2, chi_c=3.0, n=80, h=1e-4):
    def jacobian(quotient):
        base = [rho, R, math.log(M)]
        columns = []
        for j in range(3):
            plus = base[:]
            minus = base[:]
            plus[j] += h
            minus[j] -= h
            fp = _feature(math.exp(plus[2]), plus[0], plus[1], nu_source, chi_c, quotient, n)
            fm = _feature(math.exp(minus[2]), minus[0], minus[1], nu_source, chi_c, quotient, n)
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
        "scale_null_direction": [0.0, 0.0, 1.0],
        "global_injectivity": "NOT_ESTABLISHED",
        "statistical_independence": "DEPENDENCE_UNRESOLVED_WITHOUT_JOINT_COVARIANCE",
    }


def build_result():
    return {
        "study": "schwarzschild_scattering_source_coherence",
        "status": STATUS,
        "gate": GATE,
        "scope": SCOPE,
        "preregistered_parameters": {"M": 1.0, "rho": 4.0, "R": 12.0, "nu_source": 0.2, "chi_c": 3.0, "screen_order": ["polar", "in-plane"]},
        "record_order": ["y_coh", "visibility", "Phi_clock", "P_frequency_converted"],
        "raw_coherence_record": _raw_record(1.0, 4.0, 12.0, 0.2, chi_c=3.0),
        "nuisance_controls": nuisance_controls(),
        "quotient_control": quotient_control(),
        "zero_window_control": zero_window_control(),
        "geometric_scale_control": geometric_scale_control(),
        "external_coherence_standard_control": external_coherence_standard_control(),
        "rank_control": rank_control(),
        "classifications": {
            "schwarzschild_clock_and_jacobi": "KNOWN_RESULT_WITHIN_CITED_SCOPE",
            "coherence_propagation_and_rank_audit": "PROJECT_DERIVATION",
            "gaussian_stationary_source_and_visibility": "TOY_CONTROL_NOT_PHYSICAL_SOURCE_OR_DETECTOR",
            "scale_blindness": "NEGATIVE_RESULT",
            "physical_source_readout_covariance_and_ell0_law": "OPEN_PROBLEM",
        },
        "UMCH": "UNPROVEN",
        "ell0_identified": False,
        "structural_dead_end": "NOT_DECLARED",
        "detection": "NO_POSITIVE_DETECTION_CLAIM",
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
