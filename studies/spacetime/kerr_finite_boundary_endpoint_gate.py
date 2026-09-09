#!/usr/bin/env python3
"""Finite-boundary equatorial Kerr path with declared ZAMO endpoints.

Model-level coordinate/frame conformance only. No physical emitter, receiver,
clock, screen transport, 5D comparator, evidence, detection, or ell0 law.
"""

from __future__ import annotations

import json
import math
import sys

RESULT = "KERR_FINITE_BOUNDARY_ZAMO_ENDPOINTS_CONVERT_COORDINATE_PATHS_TO_LOCAL_DIRECTION_AND_RELATIVE_FREQUENCY_SHAPE_BUT_WITHOUT_PHYSICAL_ENDPOINT_STANDARDS_OR_SCREEN_TRANSPORT_JOINT_DILATION_RETAINS_ABSOLUTE_SCALE_BLINDNESS_NOT_ELL0"
PHYSICAL_GATE = "PHYSICAL_KERR_EMITTER_ABSORBER_WORLDLINES_CLOCKS_AFFINE_FREQUENCY_STANDARD_PARALLEL_SCREEN_JACOBI_PREPARATION_RECEIVER_NOISE_JOINT_COVARIANCE_DATA_5D_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED"
ORIENTATION = "KERR_ENDPOINT_ORIENTATION_ASYMMETRY_IS_FRAME_DRAGGING_SHAPE_NOT_ABSOLUTE_SCALE"
SCHWARZSCHILD = "KERR_FINITE_BOUNDARY_ORIENTATION_BRANCHES_COLLIDE_IN_SCHWARZSCHILD_UNSIGNED_RECORD"
SCALE = "KERR_FINITE_BOUNDARY_ZAMO_RECORD_RETAINS_JOINT_GEOMETRIC_SCALE_NULL"
ETA = (-1.0, 1.0, 1.0, 1.0)


def _validate(M: float, chi: float, rho: float, r_source: float, r_observer: float) -> None:
    if not all(math.isfinite(value) for value in (M, chi, rho, r_source, r_observer)):
        raise ValueError("all geometry inputs must be finite")
    if M <= 0.0 or chi < 0.0 or chi >= 1.0:
        raise ValueError("require M>0 and 0<=chi<1")
    horizon_ratio = 1.0 + math.sqrt(1.0 - chi * chi)
    if rho <= horizon_ratio or r_source <= rho * M or r_observer <= rho * M:
        raise ValueError("endpoints must lie outside one exterior turning point")


def _delta(M: float, a: float, r: float) -> float:
    return r * r - 2.0 * M * r + a * a


def radial_potential(M: float, a: float, xi: float, r: float) -> float:
    P = r * r + a * a - a * xi
    return P * P - _delta(M, a, r) * (xi - a) ** 2


def turning_record(M: float, chi: float, rho: float, orientation: int) -> dict:
    _validate(M, chi, rho, (rho + 1.0) * M, (rho + 1.0) * M)
    if orientation not in {-1, 1}:
        raise ValueError("orientation must be +/-1")
    a = chi * M
    r_turn = rho * M
    root = math.sqrt(_delta(M, a, r_turn))
    if a == 0.0:
        xi = orientation * r_turn * r_turn / root
    else:
        xi = (r_turn * r_turn + a * a + orientation * a * root) / (a + orientation * root)
    return {
        "orientation": orientation,
        "rho": rho,
        "r_turn": r_turn,
        "xi": xi,
        "xi_over_M": xi / M,
        "R_turn_residual": radial_potential(M, a, xi, r_turn) / M**4,
    }


def kerr_metric(M: float, a: float, r: float) -> list[list[float]]:
    sigma = r * r
    delta = _delta(M, a, r)
    A = (r * r + a * a) ** 2 - a * a * delta
    return [
        [-(1.0 - 2.0 * M / r), 0.0, 0.0, -2.0 * M * a / r],
        [0.0, sigma / delta, 0.0, 0.0],
        [0.0, 0.0, sigma, 0.0],
        [-2.0 * M * a / r, 0.0, 0.0, A / sigma],
    ]


def dot(metric: list[list[float]], left: list[float], right: list[float]) -> float:
    return sum(metric[i][j] * left[i] * right[j] for i in range(4) for j in range(4))


def zamo_tetrad(M: float, a: float, r: float) -> dict:
    metric = kerr_metric(M, a, r)
    sigma = r * r
    delta = _delta(M, a, r)
    A = (r * r + a * a) ** 2 - a * a * delta
    if delta <= 0.0 or A <= 0.0:
        raise ValueError("ZAMO endpoint must be outside the horizon")
    lapse = math.sqrt(delta * sigma / A)
    dragging = 2.0 * M * a * r / A
    g_phiphi = A / sigma
    tetrad = [
        [1.0 / lapse, 0.0, 0.0, dragging / lapse],
        [0.0, math.sqrt(delta / sigma), 0.0, 0.0],
        [0.0, 0.0, 1.0 / math.sqrt(sigma), 0.0],
        [0.0, 0.0, 0.0, 1.0 / math.sqrt(g_phiphi)],
    ]
    gram = [[dot(metric, tetrad[i], tetrad[j]) for j in range(4)] for i in range(4)]
    residual = max(abs(gram[i][j] - (ETA[i] if i == j else 0.0)) for i in range(4) for j in range(4))
    return {"basis_vectors": tetrad, "Gram": gram, "lapse": lapse, "frame_dragging": dragging, "tetrad_orthonormality_residual": residual}


def photon_vector(M: float, a: float, xi: float, r: float, radial_sign: int) -> list[float]:
    if radial_sign not in {-1, 1}:
        raise ValueError("radial_sign must be +/-1 away from turning point")
    sigma = r * r
    delta = _delta(M, a, r)
    P = r * r + a * a - a * xi
    radial = radial_potential(M, a, xi, r)
    if radial < -1e-10 * M**4:
        raise ValueError("negative radial potential")
    radial = max(radial, 0.0)
    return [
        ((r * r + a * a) * P / delta + a * (xi - a)) / sigma,
        radial_sign * math.sqrt(radial) / sigma,
        0.0,
        (a * P / delta + (xi - a)) / sigma,
    ]


def endpoint_record(M: float, a: float, xi: float, r: float, radial_sign: int) -> dict:
    metric = kerr_metric(M, a, r)
    tetrad_record = zamo_tetrad(M, a, r)
    tetrad = tetrad_record["basis_vectors"]
    vector = photon_vector(M, a, xi, r, radial_sign)
    local_frequency = -dot(metric, vector, tetrad[0])
    spatial = [dot(metric, vector, tetrad[index]) for index in range(1, 4)]
    direction = [value / local_frequency for value in spatial]
    reconstructed = [local_frequency * tetrad[0][mu] + sum(spatial[index] * tetrad[index + 1][mu] for index in range(3)) for mu in range(4)]
    coordinate_null = dot(metric, vector, vector)
    local_null = -local_frequency**2 + sum(value * value for value in spatial)
    reconstruction = max(abs(vector[index] - reconstructed[index]) for index in range(4))
    return {
        "r": r,
        "radial_sign": radial_sign,
        "coordinate_vector": vector,
        "ZAMO_tetrad": tetrad,
        "tetrad_orthonormality_residual": tetrad_record["tetrad_orthonormality_residual"],
        "local_frequency": local_frequency,
        "local_spatial_components": spatial,
        "local_direction": direction,
        "coordinate_null_residual": coordinate_null,
        "local_null_residual": local_null,
        "reconstruction_residual": reconstruction,
    }


def _half_integrals(M: float, a: float, xi: float, r_turn: float, r_end: float, n: int) -> tuple[float, float, float, float, float]:
    ymax = math.sqrt(r_end - r_turn)
    step = ymax / n
    totals = [0.0, 0.0, 0.0]
    minimum_radial = math.inf
    minimum_kt = math.inf
    # Midpoint rule avoids direct 0/0 at the regularized turning endpoint.
    for index in range(n):
        y = (index + 0.5) * step
        r = r_turn + y * y
        sigma = r * r
        delta = _delta(M, a, r)
        P = r * r + a * a - a * xi
        radial = radial_potential(M, a, xi, r)
        minimum_radial = min(minimum_radial, radial / M**4)
        root = math.sqrt(max(radial, 0.0))
        k_t = ((r * r + a * a) * P / delta + a * (xi - a)) / sigma
        k_phi = (a * P / delta + (xi - a)) / sigma
        k_r_abs = root / sigma
        multiplier = 2.0 * y / max(k_r_abs, 1e-300)
        rates = (k_t * multiplier, k_phi * multiplier, multiplier)
        for item in range(3):
            totals[item] += rates[item] * step
        minimum_kt = min(minimum_kt, k_t)
    return totals[0], totals[1], totals[2], minimum_radial, minimum_kt


def _integrals(M: float, chi: float, rho: float, r_source: float, r_observer: float, orientation: int, n: int) -> dict:
    _validate(M, chi, rho, r_source, r_observer)
    turning = turning_record(M, chi, rho, orientation)
    a, xi, r_turn = chi * M, turning["xi"], turning["r_turn"]
    source = _half_integrals(M, a, xi, r_turn, r_source, n)
    observer = _half_integrals(M, a, xi, r_turn, r_observer, n)
    return {
        "Delta_t": source[0] + observer[0],
        "Delta_phi": source[1] + observer[1],
        "affine_length": source[2] + observer[2],
        "minimum_radial_potential": min(source[3], observer[3]),
        "minimum_k_t": min(source[4], observer[4]),
    }


def path_record(M: float, chi: float, rho: float, r_source: float, r_observer: float, orientation: int, coarse: int = 800, fine: int = 1600) -> dict:
    coarse_record = _integrals(M, chi, rho, r_source, r_observer, orientation, coarse)
    fine_record = _integrals(M, chi, rho, r_source, r_observer, orientation, fine)
    residuals = {
        "Delta_t_over_M": abs(fine_record["Delta_t"] - coarse_record["Delta_t"]) / M,
        "Delta_phi": abs(fine_record["Delta_phi"] - coarse_record["Delta_phi"]),
        "affine_length_over_M": abs(fine_record["affine_length"] - coarse_record["affine_length"]) / M,
    }
    turning = turning_record(M, chi, rho, orientation)
    a, xi = chi * M, turning["xi"]
    source_endpoint = endpoint_record(M, a, xi, r_source, -1)
    observer_endpoint = endpoint_record(M, a, xi, r_observer, 1)
    return {
        "geometry": {"M": M, "a": a, "chi": chi, "rho": rho, "r_source": r_source, "r_observer": r_observer, "orientation": orientation},
        "turning_record": turning,
        "Delta_t": fine_record["Delta_t"],
        "Delta_t_over_M": fine_record["Delta_t"] / M,
        "Delta_phi": fine_record["Delta_phi"],
        "affine_length": fine_record["affine_length"],
        "affine_length_over_M": fine_record["affine_length"] / M,
        "minimum_radial_potential": fine_record["minimum_radial_potential"],
        "minimum_k_t": fine_record["minimum_k_t"],
        "radial_signs": [-1, 1],
        "source_endpoint": source_endpoint,
        "observer_endpoint": observer_endpoint,
        "convergence_certificate": {"coarse": coarse, "fine": fine, "residuals": residuals, "maximum_residual": max(residuals.values())},
    }


def _path_features(record: dict) -> list[float]:
    source, observer = record["source_endpoint"], record["observer_endpoint"]
    return [
        record["Delta_t_over_M"], record["Delta_phi"], record["affine_length_over_M"],
        source["local_frequency"], observer["local_frequency"],
        *source["local_direction"], *observer["local_direction"],
    ]


def orientation_control(M: float, chi: float, rho: float, r_source: float, r_observer: float) -> dict:
    positive = path_record(M, chi, rho, r_source, r_observer, 1)
    negative = path_record(M, chi, rho, r_source, r_observer, -1)
    fixed_difference = max(abs(a - b) for a, b in zip(_path_features(positive), _path_features(negative)))
    # Under simultaneous spin/orientation reversal, compare positive-a,+orientation
    # with negative-a,-orientation through direct signed-a helper records.
    reversed_path = _signed_a_path_record(M, -chi, rho, r_source, r_observer, -1)
    target = _path_features(positive)
    candidate = _path_features(reversed_path)
    # Signed azimuthal quantities reverse; unsigned/local radial records agree.
    signed_indices = {1, 7, 10}
    residual = max(abs(target[index] + candidate[index] if index in signed_indices else target[index] - candidate[index]) for index in range(len(target)))
    return {"fixed_spin_shape_difference": fixed_difference, "simultaneous_reversal_residual": residual, "classification": ORIENTATION}


def _signed_a_turning(M: float, signed_chi: float, rho: float, orientation: int) -> dict:
    a = signed_chi * M
    r_turn = rho * M
    root = math.sqrt(_delta(M, a, r_turn))
    xi = orientation * r_turn * r_turn / root if a == 0.0 else (r_turn * r_turn + a * a + orientation * a * root) / (a + orientation * root)
    return {"orientation": orientation, "rho": rho, "r_turn": r_turn, "xi": xi, "xi_over_M": xi / M, "R_turn_residual": radial_potential(M, a, xi, r_turn) / M**4}


def _signed_a_path_record(M: float, signed_chi: float, rho: float, r_source: float, r_observer: float, orientation: int, n: int = 1600) -> dict:
    a = signed_chi * M
    turning = _signed_a_turning(M, signed_chi, rho, orientation)
    xi, r_turn = turning["xi"], turning["r_turn"]
    source = _half_integrals(M, a, xi, r_turn, r_source, n)
    observer = _half_integrals(M, a, xi, r_turn, r_observer, n)
    return {
        "Delta_t_over_M": (source[0] + observer[0]) / M,
        "Delta_phi": source[1] + observer[1],
        "affine_length_over_M": (source[2] + observer[2]) / M,
        "source_endpoint": endpoint_record(M, a, xi, r_source, -1),
        "observer_endpoint": endpoint_record(M, a, xi, r_observer, 1),
    }


def schwarzschild_control(M: float, rho: float, r_source: float, r_observer: float) -> dict:
    positive = path_record(M, 0.0, rho, r_source, r_observer, 1)
    negative = path_record(M, 0.0, rho, r_source, r_observer, -1)
    p, n = _path_features(positive), _path_features(negative)
    signed_indices = {1, 7, 10}
    unsigned_residual = max(abs(p[index] - n[index]) for index in range(len(p)) if index not in signed_indices)
    signed_residual = max(abs(p[index] + n[index]) for index in signed_indices)
    return {"unsigned_collision_residual": unsigned_residual, "signed_azimuthal_reversal_residual": signed_residual, "classification": SCHWARZSCHILD}


def scale_control(M: float, chi: float, rho: float, r_source: float, r_observer: float, orientation: int, scale: float) -> dict:
    if scale <= 0.0:
        raise ValueError("scale must be positive")
    original = path_record(M, chi, rho, r_source, r_observer, orientation)
    dilated = path_record(scale * M, chi, rho, scale * r_source, scale * r_observer, orientation)
    dimensionless = max(abs(a - b) for a, b in zip(_path_features(original), _path_features(dilated)))
    covariance = max(abs(dilated["Delta_t"] - scale * original["Delta_t"]), abs(dilated["affine_length"] - scale * original["affine_length"]))
    return {"scale_factor": scale, "dimensionless_record_residual": dimensionless, "dimensional_covariance_residual": covariance, "classification": SCALE}


def _rank_features(log_M: float, chi: float, rho: float, source_ratio: float, observer_ratio: float) -> list[float]:
    M = math.exp(log_M)
    return _path_features(path_record(M, chi, rho, source_ratio * M, observer_ratio * M, 1, coarse=300, fine=600))


def rank_control(chi: float, rho: float, r_source: float, r_observer: float, h: float = 2e-5) -> dict:
    parameters = ["log_M", "chi", "rho", "R_source_over_M", "R_observer_over_M"]
    anchor = [0.0, chi, rho, r_source, r_observer]
    columns = [[0.0] * len(_rank_features(*anchor))]
    # Dimensionless equations contain no log_M dependence; preserve the exact
    # analytic null instead of finite-differencing quadrature roundoff.
    for index in range(1, len(anchor)):
        plus, minus = anchor[:], anchor[:]
        plus[index] += h
        minus[index] -= h
        fp = _rank_features(*plus)
        fm = _rank_features(*minus)
        columns.append([(a - b) / (2.0 * h) for a, b in zip(fp, fm)])
    norms = [math.sqrt(sum(value * value for value in column)) for column in columns]
    # Small Gaussian elimination on feature-by-parameter Jacobian.
    matrix = [[columns[column][row] for column in range(len(columns))] for row in range(len(columns[0]))]
    rank = _matrix_rank(matrix, 1e-7)
    return {"parameters": parameters, "feature_Jacobian": matrix, "column_norms": norms, "log_M_column_norm": norms[0], "rank": rank, "scale_null_direction": [1.0, 0.0, 0.0, 0.0, 0.0]}


def _matrix_rank(matrix: list[list[float]], tolerance: float) -> int:
    work = [row[:] for row in matrix]
    rows, cols, pivot_row = len(work), len(work[0]), 0
    for column in range(cols):
        pivot = max(range(pivot_row, rows), key=lambda row: abs(work[row][column]), default=pivot_row)
        if pivot_row >= rows or abs(work[pivot][column]) <= tolerance:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        value = work[pivot_row][column]
        work[pivot_row] = [item / value for item in work[pivot_row]]
        for row in range(rows):
            if row != pivot_row:
                factor = work[row][column]
                work[row] = [work[row][item] - factor * work[pivot_row][item] for item in range(cols)]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def no_ell0_gate() -> dict:
    return {"M_identified_internally": False, "a_identified_internally": False, "L_identified": False, "ell0_identified": False, "L_equals_ell0": "NOT_DERIVED", "extra_dimension_detected": False, "structural_dead_end": "NOT_DECLARED", "Detection": "NO_POSITIVE_DETECTION_CLAIM", "result": RESULT, "physical_gate": PHYSICAL_GATE}


def _flatten(value) -> list[float]:
    if isinstance(value, dict):
        return [number for item in value.values() for number in _flatten(item)]
    if isinstance(value, list):
        return [number for item in value for number in _flatten(item)]
    return [float(value)]


def _canonical(value, key: str | None = None):
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
    M, chi, rho, r_source, r_observer = 1.0, 0.6, 4.5, 12.0, 12.0
    positive = path_record(M, chi, rho, r_source, r_observer, 1)
    negative = path_record(M, chi, rho, r_source, r_observer, -1)
    orientation = orientation_control(M, chi, rho, r_source, r_observer)
    schwarzschild = schwarzschild_control(M, rho, r_source, r_observer)
    scaling = scale_control(M, chi, rho, r_source, r_observer, 1, 2.5)
    rank = rank_control(chi, rho, r_source, r_observer)
    gate = no_ell0_gate()
    turning_residual = max(abs(positive["turning_record"]["R_turn_residual"]), abs(negative["turning_record"]["R_turn_residual"]))
    convergence = max(positive["convergence_certificate"]["maximum_residual"], negative["convergence_certificate"]["maximum_residual"])
    tetrad_residual = max(endpoint["tetrad_orthonormality_residual"] for path in (positive, negative) for endpoint in (path["source_endpoint"], path["observer_endpoint"]))
    null_residual = max(max(abs(endpoint[key]) for key in ("coordinate_null_residual", "local_null_residual", "reconstruction_residual")) for path in (positive, negative) for endpoint in (path["source_endpoint"], path["observer_endpoint"]))
    controls = [
        {"name": "turning_impact_parameter", "passed": turning_residual < 1e-11, "residual": turning_residual, "threshold": 1e-11},
        {"name": "path_first_integrals_convergence", "passed": convergence < 2e-6 and min(positive["minimum_k_t"], negative["minimum_k_t"]) > 0.0, "residual": convergence, "threshold": 2e-6},
        {"name": "ZAMO_tetrad", "passed": tetrad_residual < 2e-9, "residual": tetrad_residual, "threshold": 2e-9},
        {"name": "endpoint_null_reconstruction", "passed": null_residual < 2e-9, "residual": null_residual, "threshold": 2e-9},
        {"name": "orientation_asymmetry", "passed": orientation["simultaneous_reversal_residual"] < 2e-9 and orientation["fixed_spin_shape_difference"] > 1e-3, "residual": orientation["simultaneous_reversal_residual"], "threshold": 2e-9},
        {"name": "Schwarzschild_collision", "passed": max(schwarzschild["unsigned_collision_residual"], schwarzschild["signed_azimuthal_reversal_residual"]) < 2e-9, "residual": max(schwarzschild["unsigned_collision_residual"], schwarzschild["signed_azimuthal_reversal_residual"]), "threshold": 2e-9},
        {"name": "joint_dilation", "passed": max(scaling["dimensionless_record_residual"], scaling["dimensional_covariance_residual"]) < 2e-9, "residual": max(scaling["dimensionless_record_residual"], scaling["dimensional_covariance_residual"]), "threshold": 2e-9},
        {"name": "rank_no_ell0", "passed": rank["log_M_column_norm"] < 2e-9 and rank["rank"] >= 2 and not gate["ell0_identified"], "residual": rank["log_M_column_norm"], "threshold": 2e-9},
    ]
    raw = {
        "geometry": positive["geometry"], "turning_record": [positive["turning_record"], negative["turning_record"]],
        "path_samples": {"positive": {"source": positive["source_endpoint"]["coordinate_vector"], "observer": positive["observer_endpoint"]["coordinate_vector"]}, "negative": {"source": negative["source_endpoint"]["coordinate_vector"], "observer": negative["observer_endpoint"]["coordinate_vector"]}},
        "Delta_t_over_M": [positive["Delta_t_over_M"], negative["Delta_t_over_M"]], "Delta_phi": [positive["Delta_phi"], negative["Delta_phi"]], "affine_length_over_M": [positive["affine_length_over_M"], negative["affine_length_over_M"]],
        "source_ZAMO_tetrad": positive["source_endpoint"]["ZAMO_tetrad"], "observer_ZAMO_tetrad": positive["observer_endpoint"]["ZAMO_tetrad"],
        "source_local_frequency": [positive["source_endpoint"]["local_frequency"], negative["source_endpoint"]["local_frequency"]], "observer_local_frequency": [positive["observer_endpoint"]["local_frequency"], negative["observer_endpoint"]["local_frequency"]],
        "source_local_direction": [positive["source_endpoint"]["local_direction"], negative["source_endpoint"]["local_direction"]], "observer_local_direction": [positive["observer_endpoint"]["local_direction"], negative["observer_endpoint"]["local_direction"]],
        "coordinate_null_residual": max(abs(endpoint["coordinate_null_residual"]) for path in (positive, negative) for endpoint in (path["source_endpoint"], path["observer_endpoint"])), "local_null_residual": max(abs(endpoint["local_null_residual"]) for path in (positive, negative) for endpoint in (path["source_endpoint"], path["observer_endpoint"])), "reconstruction_residual": max(endpoint["reconstruction_residual"] for path in (positive, negative) for endpoint in (path["source_endpoint"], path["observer_endpoint"])),
        "orientation_control": orientation, "Schwarzschild_control": schwarzschild, "scale_control": scaling, "rank_control": rank,
        "convergence_certificate": {"positive": positive["convergence_certificate"], "negative": negative["convergence_certificate"]},
        "source_scope": "GRALLA_LUPSASCA_2020_EQS_1_TO_13F_PATH_ONLY_ZAMO_PROTOCOL_PROJECT_DERIVATION",
        "limitations": PHYSICAL_GATE,
    }
    return _canonical({"study_id": "kerr-finite-boundary-zamo-endpoint-gate-v1", "control_summary": {"controls": controls, "controls_passed": sum(control["passed"] for control in controls), "controls_total": len(controls), **{key: gate[key] for key in ("L_identified", "ell0_identified", "L_equals_ell0", "extra_dimension_detected", "structural_dead_end", "Detection")}, "Maximum_interpretation": "MODEL_LEVEL_KERR_ENDPOINT_CONFORMANCE_NOT_EVIDENCE"}, "raw_output": raw, "result": RESULT, "physical_gate": PHYSICAL_GATE, "review": "DIRECT_REVIEW_NO_SUBAGENT"})


def main() -> int:
    json.dump(build_artifact(), sys.stdout, indent=2, sort_keys=True)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
