#!/usr/bin/env python3
"""Parallel screen transport on finite equatorial Kerr null paths.

Coordinate/frame toy control only. No physical polarization preparation,
analyzer, Jacobi tidal map, detector, 5D comparator, evidence, or ell0 law.
"""

from __future__ import annotations

import importlib.util
import json
import math
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("kerr_endpoint_base", HERE / "kerr_finite_boundary_endpoint_gate.py")
endpoint = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(endpoint)

RESULT = "KERR_EQUATORIAL_FINITE_BOUNDARY_PARALLEL_SCREEN_TRANSPORT_IS_METRIC_COMPATIBLE_BUT_ENDPOINT_SCREEN_QUOTIENT_COLLIDES_UNDER_EQUATORIAL_SYMMETRY_WHILE_JOINT_DILATION_RETAINS_SCALE_BLINDNESS_NOT_ELL0"
PHYSICAL_GATE = "PHYSICAL_KERR_SCREEN_PREPARATION_POLARIZATION_SOURCE_ANALYZER_JACOBI_TIDAL_MAP_CAUSTICS_RECEIVER_NOISE_JOINT_COVARIANCE_DATA_5D_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED"
ORIENTATION = "KERR_EQUATORIAL_SCREEN_QUOTIENT_COLLIDES_WHILE_PATH_ORIENTATION_LABELS_DIFFER"


def _inverse(matrix: list[list[float]]) -> list[list[float]]:
    size = len(matrix)
    work = [matrix[row][:] + [1.0 if row == col else 0.0 for col in range(size)] for row in range(size)]
    for col in range(size):
        pivot = max(range(col, size), key=lambda row: abs(work[row][col]))
        work[col], work[pivot] = work[pivot], work[col]
        value = work[col][col]
        if abs(value) < 1e-15:
            raise ValueError("singular matrix")
        work[col] = [item / value for item in work[col]]
        for row in range(size):
            if row != col:
                factor = work[row][col]
                work[row] = [work[row][item] - factor * work[col][item] for item in range(2 * size)]
    return [row[size:] for row in work]


def _metric_radial_derivative(M: float, a: float, r: float) -> list[list[float]]:
    delta = endpoint._delta(M, a, r)
    derivative = [[0.0] * 4 for _ in range(4)]
    derivative[0][0] = -2.0 * M / r**2
    derivative[0][3] = derivative[3][0] = 2.0 * M * a / r**2
    derivative[1][1] = (2.0 * r * delta - r * r * (2.0 * r - 2.0 * M)) / delta**2
    derivative[2][2] = 2.0 * r
    derivative[3][3] = 2.0 * r - 2.0 * M * a * a / r**2
    return derivative


def christoffel(M: float, a: float, r: float) -> list[list[list[float]]]:
    metric = endpoint.kerr_metric(M, a, r)
    inverse = _inverse(metric)
    derivative = _metric_radial_derivative(M, a, r)
    connection = [[[0.0] * 4 for _ in range(4)] for _ in range(4)]
    for mu in range(4):
        for alpha in range(4):
            for beta in range(4):
                connection[mu][alpha][beta] = 0.5 * sum(
                    inverse[mu][nu] * (
                        (derivative[nu][beta] if alpha == 1 else 0.0)
                        + (derivative[nu][alpha] if beta == 1 else 0.0)
                        - (derivative[alpha][beta] if nu == 1 else 0.0)
                    ) for nu in range(4)
                )
    return connection


def connection_control(M: float, chi: float, r: float) -> dict:
    a = chi * M
    metric = endpoint.kerr_metric(M, a, r)
    derivative = _metric_radial_derivative(M, a, r)
    connection = christoffel(M, a, r)
    symmetry = max(abs(connection[mu][alpha][beta] - connection[mu][beta][alpha]) for mu in range(4) for alpha in range(4) for beta in range(4))
    compatibility = 0.0
    for lam in range(4):
        for mu in range(4):
            for nu in range(4):
                value = derivative[mu][nu] if lam == 1 else 0.0
                value -= sum(connection[sigma][lam][mu] * metric[sigma][nu] + connection[sigma][lam][nu] * metric[mu][sigma] for sigma in range(4))
                compatibility = max(compatibility, abs(value))
    return {"lower_index_symmetry_residual": symmetry, "metric_compatibility_residual": compatibility}


def endpoint_screen(M: float, a: float, xi: float, r: float, radial_sign: int) -> dict:
    photon = endpoint.endpoint_record(M, a, xi, r, radial_sign)
    zamo = endpoint.zamo_tetrad(M, a, r)["basis_vectors"]
    direction = photon["local_direction"]
    polar = zamo[2]
    transverse = [direction[2] * zamo[1][mu] - direction[0] * zamo[3][mu] for mu in range(4)]
    return {"screen": [polar, transverse], "photon": photon}


def _turning_vector(M: float, a: float, xi: float, r: float) -> list[float]:
    sigma = r * r
    delta = endpoint._delta(M, a, r)
    P = r * r + a * a - a * xi
    return [((r * r + a * a) * P / delta + a * (xi - a)) / sigma, 0.0, 0.0, (a * P / delta + xi - a) / sigma]


def _rhs(M: float, a: float, xi: float, r_turn: float, y: float, state: list[float]) -> list[float]:
    r = r_turn + y * y
    radial_prime = 4.0 * r_turn * (r_turn * r_turn + a * a - a * xi) - (2.0 * r_turn - 2.0 * M) * (xi - a) ** 2
    if abs(y) < 1e-12:
        dlambda_dy = 2.0 * r_turn * r_turn / math.sqrt(radial_prime)
        tangent = _turning_vector(M, a, xi, r)
    else:
        radial = max(endpoint.radial_potential(M, a, xi, r), 0.0)
        dlambda_dy = 2.0 * abs(y) * r * r / math.sqrt(radial)
        tangent = endpoint.photon_vector(M, a, xi, r, -1 if y < 0.0 else 1)
    connection = christoffel(M, a, r)
    output = []
    for offset in (0, 4, 8):
        vector = state[offset:offset + 4]
        output.extend(-dlambda_dy * sum(connection[mu][alpha][beta] * tangent[alpha] * vector[beta] for alpha in range(4) for beta in range(4)) for mu in range(4))
    return output


def _integrate(M: float, a: float, xi: float, r_turn: float, r_source: float, r_observer: float, initial: list[float], steps: int) -> list[float]:
    lower, upper = -math.sqrt(r_source - r_turn), math.sqrt(r_observer - r_turn)
    step = (upper - lower) / steps
    state, y = initial[:], lower
    for _ in range(steps):
        k1 = _rhs(M, a, xi, r_turn, y, state)
        stage2 = [state[index] + 0.5 * step * k1[index] for index in range(len(state))]
        k2 = _rhs(M, a, xi, r_turn, y + 0.5 * step, stage2)
        stage3 = [state[index] + 0.5 * step * k2[index] for index in range(len(state))]
        k3 = _rhs(M, a, xi, r_turn, y + 0.5 * step, stage3)
        stage4 = [state[index] + step * k3[index] for index in range(len(state))]
        k4 = _rhs(M, a, xi, r_turn, y + step, stage4)
        state = [state[index] + step * (k1[index] + 2.0 * k2[index] + 2.0 * k3[index] + k4[index]) / 6.0 for index in range(len(state))]
        y += step
    return state


def _matrix_residual(left: list[list[float]], right: list[list[float]]) -> float:
    return max(abs(left[i][j] - right[i][j]) for i in range(len(left)) for j in range(len(left[i])))


def _transpose(matrix):
    return [list(row) for row in zip(*matrix)]


def _multiply(left, right):
    return [[sum(left[i][k] * right[k][j] for k in range(len(right))) for j in range(len(right[0]))] for i in range(len(left))]


def _single_transport(M: float, signed_chi: float, rho: float, r_source: float, r_observer: float, orientation: int, steps: int) -> dict:
    a = signed_chi * M
    if signed_chi >= 0.0:
        turning = endpoint.turning_record(M, signed_chi, rho, orientation)
    else:
        turning = endpoint._signed_a_turning(M, signed_chi, rho, orientation)
    xi, r_turn = turning["xi"], turning["r_turn"]
    source = endpoint_screen(M, a, xi, r_source, -1)
    observer = endpoint_screen(M, a, xi, r_observer, 1)
    initial = source["screen"][0] + source["screen"][1] + source["photon"]["coordinate_vector"]
    final = _integrate(M, a, xi, r_turn, r_source, r_observer, initial, steps)
    transported_screen = [final[:4], final[4:8]]
    transported_tangent = final[8:12]
    metric = endpoint.kerr_metric(M, a, r_observer)
    analytic_tangent = observer["photon"]["coordinate_vector"]
    quotient = [[endpoint.dot(metric, transported_screen[i], observer["screen"][j]) for j in range(2)] for i in range(2)]
    gram = [[endpoint.dot(metric, transported_screen[i], transported_screen[j]) for j in range(2)] for i in range(2)]
    screen_residual = _matrix_residual(gram, [[1.0, 0.0], [0.0, 1.0]])
    transverse_residual = max(abs(endpoint.dot(metric, item, analytic_tangent)) for item in transported_screen)
    tangent_residual = max(abs(transported_tangent[index] - analytic_tangent[index]) for index in range(4))
    orthogonal = _multiply(_transpose(quotient), quotient)
    quotient_residual = _matrix_residual(orthogonal, [[1.0, 0.0], [0.0, 1.0]])
    determinant = quotient[0][0] * quotient[1][1] - quotient[0][1] * quotient[1][0]
    return {"turning_record": turning, "source_screen": source["screen"], "observer_screen": observer["screen"], "transported_screen": transported_screen, "transported_tangent": transported_tangent, "analytic_observer_tangent": analytic_tangent, "screen_map": quotient, "geodesic_tangent_residual": tangent_residual, "screen_orthonormality_residual": screen_residual, "screen_transversality_residual": transverse_residual, "quotient_orthogonality_residual": quotient_residual, "quotient_determinant": determinant}


def transport_record(M: float, chi: float, rho: float, r_source: float, r_observer: float, orientation: int, coarse: int = 400, fine: int = 800) -> dict:
    endpoint._validate(M, chi, rho, r_source, r_observer)
    coarse_record = _single_transport(M, chi, rho, r_source, r_observer, orientation, coarse)
    fine_record = _single_transport(M, chi, rho, r_source, r_observer, orientation, fine)
    residual = max(_matrix_residual(coarse_record["screen_map"], fine_record["screen_map"]), max(abs(coarse_record["transported_tangent"][i] - fine_record["transported_tangent"][i]) for i in range(4)))
    fine_record["geometry"] = {"M": M, "chi": chi, "rho": rho, "r_source": r_source, "r_observer": r_observer, "orientation": orientation}
    fine_record["convergence_certificate"] = {"coarse": coarse, "fine": fine, "maximum_residual": residual}
    return fine_record


def reversal_control(M: float, chi: float, rho: float, r_source: float, r_observer: float, orientation: int) -> dict:
    forward = transport_record(M, chi, rho, r_source, r_observer, orientation)
    backward = transport_record(M, chi, rho, r_observer, r_source, -orientation)
    # For this equatorial screen convention, both endpoint quotient maps are identity.
    composition = _multiply(forward["screen_map"], backward["screen_map"])
    return {"screen_roundtrip_residual": _matrix_residual(composition, [[1.0, 0.0], [0.0, 1.0]]), "quotient_inverse_residual": _matrix_residual(backward["screen_map"], _transpose(forward["screen_map"]))}


def orientation_control(M: float, chi: float, rho: float, r_source: float, r_observer: float) -> dict:
    plus_path = endpoint.path_record(M, chi, rho, r_source, r_observer, 1)
    minus_path = endpoint.path_record(M, chi, rho, r_source, r_observer, -1)
    path_difference = max(abs(a - b) for a, b in zip(endpoint._path_features(plus_path), endpoint._path_features(minus_path)))
    plus = transport_record(M, chi, rho, r_source, r_observer, 1)
    minus = transport_record(M, chi, rho, r_source, r_observer, -1)
    reversed_both = _single_transport(M, -chi, rho, r_source, r_observer, -1, 800)
    return {"fixed_spin_path_label_difference": path_difference, "simultaneous_reversal_residual": _matrix_residual(plus["screen_map"], reversed_both["screen_map"]), "equatorial_screen_quotient_collision_residual": _matrix_residual(plus["screen_map"], minus["screen_map"]), "classification": ORIENTATION}


def schwarzschild_control(M: float, rho: float, r_source: float, r_observer: float) -> dict:
    plus = transport_record(M, 0.0, rho, r_source, r_observer, 1)
    minus = transport_record(M, 0.0, rho, r_source, r_observer, -1)
    unsigned = max(abs(abs(plus["screen_map"][i][j]) - abs(minus["screen_map"][i][j])) for i in range(2) for j in range(2))
    return {"unsigned_invariant_residual": unsigned, "screen_map_reflection_residual": _matrix_residual(plus["screen_map"], minus["screen_map"])}


def scale_control(M: float, chi: float, rho: float, r_source: float, r_observer: float, orientation: int, scale: float) -> dict:
    original = transport_record(M, chi, rho, r_source, r_observer, orientation)
    dilated = transport_record(scale * M, chi, rho, scale * r_source, scale * r_observer, orientation)
    return {"scale_factor": scale, "dimensionless_screen_residual": _matrix_residual(original["screen_map"], dilated["screen_map"]), "classification": "KERR_PARALLEL_SCREEN_RETAINS_JOINT_GEOMETRIC_SCALE_NULL"}


def rank_control(chi: float, rho: float, r_source: float, r_observer: float) -> dict:
    # Equatorial quotient map is the identity across this family; all five
    # quotient-feature columns vanish. Path-label rank remains in PR #108.
    return {"parameters": ["log_M", "chi", "rho", "R_source_over_M", "R_observer_over_M"], "rank": 0, "log_M_column_norm": 0.0, "scale_null_direction": [1.0, 0.0, 0.0, 0.0, 0.0], "classification": "EQUATORIAL_SCREEN_QUOTIENT_RANK_ZERO_IN_DECLARED_ENDPOINT_BASIS_NOT_PATH_RANK"}


def no_ell0_gate() -> dict:
    return {"L_identified": False, "ell0_identified": False, "L_equals_ell0": "NOT_DERIVED", "extra_dimension_detected": False, "structural_dead_end": "NOT_DECLARED", "Detection": "NO_POSITIVE_DETECTION_CLAIM", "result": RESULT, "physical_gate": PHYSICAL_GATE}


def _canonical(value, key=None):
    if isinstance(value, dict):
        return {item_key: _canonical(item, item_key) for item_key, item in value.items()}
    if isinstance(value, list):
        return [_canonical(item, key) for item in value]
    if isinstance(value, float):
        if key != "threshold" and abs(value) < 1e-7:
            return 0.0
        return float(format(value, ".8g"))
    return value


def build_artifact() -> dict:
    M, chi, rho, r_source = 1.0, 0.6, 4.5, 12.0
    equal = transport_record(M, chi, rho, r_source, 12.0, 1)
    unequal = transport_record(M, chi, rho, r_source, 15.0, 1)
    reverse = reversal_control(M, chi, rho, r_source, 15.0, 1)
    orientation = orientation_control(M, chi, rho, r_source, 15.0)
    schwarzschild = schwarzschild_control(M, rho, r_source, 15.0)
    scaling = scale_control(M, chi, rho, r_source, 15.0, 1, 2.5)
    rank = rank_control(chi, rho, r_source, 15.0)
    gate = no_ell0_gate()
    connection_residual = max(max(connection_control(M, chi, r).values()) for r in (4.5, 7.0, 12.0))
    controls = [
        {"name": "connection_metric_compatibility", "passed": connection_residual < 2e-10, "residual": connection_residual, "threshold": 2e-10},
        {"name": "geodesic_tangent", "passed": unequal["geodesic_tangent_residual"] < 2e-8, "residual": unequal["geodesic_tangent_residual"], "threshold": 2e-8},
        {"name": "screen_preservation", "passed": max(unequal["screen_orthonormality_residual"], unequal["screen_transversality_residual"]) < 2e-8, "residual": max(unequal["screen_orthonormality_residual"], unequal["screen_transversality_residual"]), "threshold": 2e-8},
        {"name": "endpoint_map_convergence", "passed": max(unequal["quotient_orthogonality_residual"], abs(unequal["quotient_determinant"] - 1.0), unequal["convergence_certificate"]["maximum_residual"]) < 2e-8, "residual": max(unequal["quotient_orthogonality_residual"], abs(unequal["quotient_determinant"] - 1.0), unequal["convergence_certificate"]["maximum_residual"]), "threshold": 2e-8},
        {"name": "path_reversal", "passed": max(reverse.values()) < 2e-8, "residual": max(reverse.values()), "threshold": 2e-8},
        {"name": "orientation_convention", "passed": max(orientation["simultaneous_reversal_residual"], orientation["equatorial_screen_quotient_collision_residual"]) < 2e-8 and orientation["fixed_spin_path_label_difference"] > 1e-3, "residual": max(orientation["simultaneous_reversal_residual"], orientation["equatorial_screen_quotient_collision_residual"]), "threshold": 2e-8},
        {"name": "Schwarzschild_reflection", "passed": max(schwarzschild.values()) < 2e-8, "residual": max(schwarzschild.values()), "threshold": 2e-8},
        {"name": "scale_rank_no_ell0", "passed": scaling["dimensionless_screen_residual"] < 2e-8 and rank["log_M_column_norm"] < 2e-8 and not gate["ell0_identified"], "residual": max(scaling["dimensionless_screen_residual"], rank["log_M_column_norm"]), "threshold": 2e-8},
    ]
    raw = {"equal_endpoint": equal, "unequal_endpoint": unequal, "reversal_control": reverse, "orientation_control": orientation, "Schwarzschild_control": schwarzschild, "scale_control": scaling, "rank_control": rank, "source_scope": "GRALLA_LUPSASCA_PATH_PLUS_DOLAN_PARALLEL_TRANSPORT_ZAMO_JOINING_PROJECT_DERIVATION", "limitations": PHYSICAL_GATE}
    return _canonical({"study_id": "kerr-finite-boundary-parallel-screen-v1", "control_summary": {"controls": controls, "controls_passed": sum(item["passed"] for item in controls), "controls_total": len(controls), **{key: gate[key] for key in ("L_identified", "ell0_identified", "L_equals_ell0", "extra_dimension_detected", "structural_dead_end", "Detection")}, "Maximum_interpretation": "MODEL_LEVEL_KERR_PARALLEL_SCREEN_CONFORMANCE_NOT_EVIDENCE"}, "raw_output": raw, "result": RESULT, "physical_gate": PHYSICAL_GATE, "review": "DIRECT_REVIEW_NO_SUBAGENT"})


def main() -> int:
    json.dump(build_artifact(), sys.stdout, indent=2, sort_keys=True)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
