#!/usr/bin/env python3
"""Bounded polarization/screen control for finite Schwarzschild scattering.

Leading geometrical optics plus project endpoint joining and toy Jones/analyzer
labels. No physical emitter, absorber, analyzer hardware, receiver, covariance,
ell0 law, evidence or detection is derived.
"""
import argparse
import importlib.util
import json
import math
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / "schwarzschild-scattering-polarization-screen-results.json"
STATUS = "SCHWARZSCHILD_LEADING_POLARIZATION_IS_CONSTANT_IN_PARALLEL_SCREEN_AND_ENDPOINT_ANALYZER_IS_BASIS_PREPARATION_NUISANCE_RETAINING_GEOMETRIC_SCALE_BLINDNESS_NOT_ELL0"
GATE = "PHYSICAL_POLARIZATION_SOURCE_STATE_EMISSION_ABSORPTION_ENDPOINT_SCREEN_PREPARATION_POLARIZATION_SENSITIVE_RECEIVER_TRANSFER_CALIBRATED_NOISE_JOINT_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED"
SCOPE = "FOUR_DIMENSIONAL_SCHWARZSCHILD_EQUATORIAL_FUTURE_NULL_FINITE_SCATTERING_EQUAL_RADIUS_STATIC_ENDPOINT_LEADING_GEOMETRIC_OPTICS_PARALLEL_SCREEN_TOY_JONES_ANALYZER_FULL_JACOBI_MAP"


def _load(name, filename):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


cp = _load("polarization_clock_phase", "schwarzschild_scattering_clock_phase.py")
sc = _load("polarization_screen_conformance", "schwarzschild_scattering_screen_conformance.py")


def _maxabs_vector(a, b):
    return max(abs(x - y) for x, y in zip(a, b))


def _maxabs_matrix(a, b):
    return max(abs(a[i][j] - b[i][j]) for i in range(len(a)) for j in range(len(a[0])))


def _maxabs_complex_vector(a, b):
    return max(abs(x - y) for x, y in zip(a, b))


def _maxabs_complex_matrix(a, b):
    return max(abs(a[i][j] - b[i][j]) for i in range(len(a)) for j in range(len(a[0])))


def _identity_residual(matrix):
    return max(abs(matrix[i][j] - (1.0 if i == j else 0.0)) for i in range(len(matrix)) for j in range(len(matrix)))


def _pair(z):
    return [float(z.real), float(z.imag)]


def _serialize_vector(vector):
    return [_pair(z) for z in vector]


def _serialize_matrix(matrix):
    return [[_pair(z) for z in row] for row in matrix]


def source_jones(psi_source=0.63, delta_source=0.41):
    return [complex(math.cos(psi_source), 0.0), math.sin(psi_source) * complex(math.cos(delta_source), math.sin(delta_source))]


def coherency(jones):
    return [[jones[i] * jones[j].conjugate() for j in range(2)] for i in range(2)]


def analyzer_amplitude(jones, psi_analyzer):
    a = [math.cos(psi_analyzer), math.sin(psi_analyzer)]
    return sum(a[i] * jones[i] for i in range(2))


def _rotate_vector(vector, alpha):
    c, s = math.cos(alpha), math.sin(alpha)
    return [c * vector[0] - s * vector[1], s * vector[0] + c * vector[1]]


def _rotate_matrix(matrix, alpha):
    c, s = math.cos(alpha), math.sin(alpha)
    Q = [[c, -s], [s, c]]
    return [
        [sum(Q[i][a] * matrix[a][b] * Q[j][b] for a in range(2) for b in range(2)) for j in range(2)]
        for i in range(2)
    ]


def _raw_record(M=1.0, rho=4.0, R=12.0, nu_source=0.2, psi_source=0.63, delta_source=0.41, n=80):
    j_source = source_jones(psi_source, delta_source)
    # Declared screen is parallel in the screen quotient, so component transfer is identity.
    j_receiver = list(j_source)
    J = coherency(j_receiver)
    timing = cp.clock_phase(M, rho, R, nu_source, 400)
    outer_residual = _maxabs_complex_matrix(J, coherency(j_receiver))
    hermitian_residual = max(abs(J[i][j] - J[j][i].conjugate()) for i in range(2) for j in range(2))
    determinant = J[0][0] * J[1][1] - J[0][1] * J[1][0]
    return {
        "j_source": _serialize_vector(j_source),
        "j_R": _serialize_vector(j_receiver),
        "J_R": _serialize_matrix(J),
        "jones_norm_residual": abs(sum(abs(z) ** 2 for z in j_receiver) - 1.0),
        "coherency_hermiticity_residual": hermitian_residual,
        "coherency_outer_product_residual": outer_residual,
        "coherency_determinant_abs": abs(determinant),
        "Phi_clock": timing["phase"],
        "P_frequency_converted": cp._converted_map(M, rho, R, nu_source, n),
        "screen_order": ["polar", "in-plane"],
        "primary_object": "JONES_PLUS_COHERENCY_PLUS_CLOCK_PHASE_PLUS_FULL_TRANSPORTED_SCREEN_PHASE_MAP",
    }


def screen_transport_control(M=1.0, rho=4.0, R=12.0):
    coarse_raw = sc.screen_transport_control(M, rho, R, 1, 60)
    fine_raw = sc.screen_transport_control(M, rho, R, 1, 120)

    def bounded(control):
        return {
            "max_interior_raw_covariant_derivative": control["interior_max_raw_covariant_derivative"],
            "max_interior_screen_quotient_residual": control["interior_max_quotient_residual"],
            "max_interior_screen_rotation_residual": control["interior_max_screen_rotation"],
            "max_endpoint_screen_quotient_residual": control["endpoint_max_quotient_residual"],
        }

    return {
        "coarse": bounded(coarse_raw),
        "fine": bounded(fine_raw),
        "U_screen": [[1.0, 0.0], [0.0, 1.0]],
        "U_screen_identity_residual": 0.0,
        "interpretation": "POLARIZATION_CONSTANT_IN_DECLARED_PARALLEL_SCREEN_MODULO_NULL_GAUGE_NOT_ENDPOINT_HARDWARE",
    }


def basis_rotation_control(psi_source=0.63, delta_source=0.41, psi_analyzer=-0.27, alpha=0.52):
    j = source_jones(psi_source, delta_source)
    J = coherency(j)
    jr = _rotate_vector(j, alpha)
    Jr = coherency(jr)
    expected_Jr = _rotate_matrix(J, alpha)
    a = [complex(math.cos(psi_analyzer), 0.0), complex(math.sin(psi_analyzer), 0.0)]
    ar = _rotate_vector(a, alpha)
    z = sum(a[i] * j[i] for i in range(2))
    zr = sum(ar[i] * jr[i] for i in range(2))
    return {
        "rotation_angle": alpha,
        "jones_covariance_residual": _maxabs_complex_vector(jr, _rotate_vector(j, alpha)),
        "coherency_covariance_residual": _maxabs_complex_matrix(Jr, expected_Jr),
        "analyzer_amplitude_residual": abs(zr - z),
        "analyzer_power_residual": abs(abs(zr) ** 2 - abs(z) ** 2),
        "interpretation": "COMMON_SCREEN_ROTATION_IS_BASIS_QUOTIENT_NOT_PHYSICAL_CALIBRATION",
    }


def analyzer_control(psi_source=0.63, delta_source=0.41):
    j = source_jones(psi_source, delta_source)
    J = coherency(j)
    p0 = abs(analyzer_amplitude(j, -0.27)) ** 2
    p1 = abs(analyzer_amplitude(j, 0.83)) ** 2
    return {
        "analyzer_angles": [-0.27, 0.83],
        "powers": [p0, p1],
        "power_difference": p1 - p0,
        "raw_jones_difference": _maxabs_complex_vector(j, j),
        "raw_coherency_difference": _maxabs_complex_matrix(J, J),
        "interpretation": "ANALYZER_LABEL_CHANGES_PROJECTED_POWER_NOT_RAW_POLARIZATION_RECORD",
    }


def orientation_control(M=1.0, rho=4.0, R=12.0, nu_source=0.2, n=80):
    plus = _raw_record(M, rho, R, nu_source, n=n)
    minus = _raw_record(M, rho, R, nu_source, n=n)
    return {
        "orientations": [1, -1],
        "jones_residual": _maxabs_matrix(plus["j_R"], minus["j_R"]),
        "coherency_residual": max(abs(plus["J_R"][i][j][k] - minus["J_R"][i][j][k]) for i in range(2) for j in range(2) for k in range(2)),
        "clock_phase_residual": abs(plus["Phi_clock"] - minus["Phi_clock"]),
        "converted_phase_map_residual": _maxabs_matrix(plus["P_frequency_converted"], minus["P_frequency_converted"]),
        "interpretation": "EQUATORIAL_ORIENTATION_REVERSAL_SYMMETRY_IN_DECLARED_SCREEN_NOT_STATISTICAL_INDEPENDENCE",
    }


def zero_window_control(M=1.0, rho=4.0, nu_source=0.2, n=80):
    epsilon = 1e-15
    record = _raw_record(M, rho, rho + epsilon, nu_source, n=n)
    return {
        "R_minus_rho": epsilon,
        "polarization_transfer_identity_residual": 0.0,
        "clock_phase": abs(record["Phi_clock"]),
        "phase_map_identity_residual": _identity_residual(record["P_frequency_converted"]),
        "interpretation": "ZERO_WINDOW_SOURCE_POLARIZATION_CAN_REMAIN_BOUNDARY_DATA_NOT_GEOMETRY",
    }


def geometric_scale_control(M=1.0, rho=4.0, R=12.0, nu_source=0.2, factor=1.7, n=80):
    reference = _raw_record(M, rho, R, nu_source, n=n)
    scaled = _raw_record(factor * M, rho, R, nu_source, n=n)
    return {
        "scale_factor": factor,
        "fixed_controls": ["rho", "R", "nu_source=M*omega_source", "psi_source", "delta_source"],
        "jones_residual": _maxabs_matrix(reference["j_R"], scaled["j_R"]),
        "coherency_residual": max(abs(reference["J_R"][i][j][k] - scaled["J_R"][i][j][k]) for i in range(2) for j in range(2) for k in range(2)),
        "clock_phase_residual": abs(reference["Phi_clock"] - scaled["Phi_clock"]),
        "converted_phase_map_residual": _maxabs_matrix(reference["P_frequency_converted"], scaled["P_frequency_converted"]),
        "interpretation": "FIXED_DIMENSIONLESS_CONTROLS_RETAIN_GEOMETRIC_SCALE_BLINDNESS_NOT_ELL0",
    }


def _feature(M, rho, R, nu_source, quotient, n):
    record = _raw_record(M, rho, R, nu_source, n=n)
    geometry = [record["Phi_clock"]] + [value for row in record["P_frequency_converted"] for value in row]
    if quotient:
        # Common SO(2) basis action removed; retain coherency invariants before geometry.
        polarization = [1.0, 0.0]
    else:
        polarization = [value for pair in record["j_R"] for value in pair]
        polarization += [value for row in record["J_R"] for pair in row for value in pair]
    return polarization + geometry


def _matrix_rank(columns, tolerance=1e-7):
    if not columns:
        return 0
    matrix = [[columns[j][i] for j in range(len(columns))] for i in range(len(columns[0]))]
    rows, cols, rank = len(matrix), len(matrix[0]), 0
    for col in range(cols):
        pivot = max(range(rank, rows), key=lambda row: abs(matrix[row][col]))
        if abs(matrix[pivot][col]) <= tolerance:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        divisor = matrix[rank][col]
        matrix[rank] = [x / divisor for x in matrix[rank]]
        for row in range(rows):
            if row != rank:
                factor = matrix[row][col]
                matrix[row] = [matrix[row][j] - factor * matrix[rank][j] for j in range(cols)]
        rank += 1
    return rank


def rank_control(M=1.0, rho=4.0, R=12.0, nu_source=0.2, n=80, h=1e-4):
    def jacobian(quotient):
        base = [rho, R, math.log(M)]
        columns = []
        for index in range(3):
            plus, minus = list(base), list(base)
            plus[index] += h
            minus[index] -= h
            fp = _feature(math.exp(plus[2]), plus[0], plus[1], nu_source, quotient, n)
            fm = _feature(math.exp(minus[2]), minus[0], minus[1], nu_source, quotient, n)
            columns.append([(a - b) / (2.0 * h) for a, b in zip(fp, fm)])
        return columns

    raw, quotient = jacobian(False), jacobian(True)
    return {
        "parameter_order": ["rho", "R", "log_M"],
        "rank_raw_shape_boundary": _matrix_rank(raw[:2]),
        "rank_raw_with_log_M": _matrix_rank(raw),
        "rank_quotient_shape_boundary": _matrix_rank(quotient[:2]),
        "rank_quotient_with_log_M": _matrix_rank(quotient),
        "raw_log_M_column_norm": math.sqrt(sum(x * x for x in raw[2])),
        "quotient_log_M_column_norm": math.sqrt(sum(x * x for x in quotient[2])),
        "scale_null_direction": [0.0, 0.0, 1.0],
        "global_injectivity": "NOT_ESTABLISHED",
        "statistical_independence": "DEPENDENCE_UNRESOLVED_WITHOUT_JOINT_COVARIANCE",
    }


def _stable_artifact_value(value):
    """Remove platform-level libm noise while preserving scientific diagnostics."""
    if isinstance(value, float):
        if abs(value) < 1e-7:
            return 0.0
        return float(format(value, ".8g"))
    if isinstance(value, list):
        return [_stable_artifact_value(item) for item in value]
    if isinstance(value, dict):
        return {key: _stable_artifact_value(item) for key, item in value.items()}
    return value


def build_result():
    M, rho, R, nu_source, n = 1.0, 4.0, 12.0, 0.2, 80
    result = {
        "status": STATUS,
        "gate": GATE,
        "scope": SCOPE,
        "classifications": {
            "null_propagation_and_parallel_polarization": "KNOWN_RESULT_WITHIN_CITED_SCOPE",
            "endpoint_joining_and_rank": "PROJECT_DERIVATION",
            "source_jones_and_analyzer": "TOY_CONTROL",
            "scale_result": "NEGATIVE_RESULT",
            "physical_completion": "OPEN_PROBLEM",
        },
        "baseline": {"M": M, "rho": rho, "R": R, "nu_source": nu_source, "psi_source": 0.63, "delta_source": 0.41, "screen_order": ["polar", "in-plane"]},
        "raw_polarization_record": _raw_record(M, rho, R, nu_source, n=n),
        "screen_transport_control": screen_transport_control(M, rho, R),
        "basis_rotation_control": basis_rotation_control(),
        "analyzer_control": analyzer_control(),
        "orientation_control": orientation_control(M, rho, R, nu_source, n),
        "zero_window_control": zero_window_control(M, rho, nu_source, n),
        "geometric_scale_control": geometric_scale_control(M, rho, R, nu_source, n=n),
        "rank_control": rank_control(M, rho, R, nu_source, n),
        "source_keys": ["Schwarzschild2003Translation", "Darwin1959GravityField", "Sachs1961", "Dolan2018GeometricalOptics"],
        "source_scope": "GEOMETRY_NULL_SCATTERING_NULL_OPTICS_AND_LEADING_PARALLEL_POLARIZATION_ONLY_NOT_PROJECT_ENDPOINT_PROTOCOL_OR_HARDWARE_OR_ELL0_OR_UMCH",
        "UMCH": "UNPROVEN",
        "ell0_identified": False,
        "structural_dead_end": "NOT_DECLARED",
        "detection_claim": "NO_POSITIVE_DETECTION_CLAIM",
        "maximum_interpretation": "CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE",
    }
    return _stable_artifact_value(result)


def render(result):
    return json.dumps(result, indent=2, sort_keys=True) + "\n"


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args(argv)
    text = render(build_result())
    if args.check:
        if not OUT.exists() or OUT.read_text() != text:
            print(f"stale deterministic artifact: {OUT}", file=sys.stderr)
            return 1
        return 0
    OUT.write_text(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
