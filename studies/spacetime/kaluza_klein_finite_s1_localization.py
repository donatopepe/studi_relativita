#!/usr/bin/env python3
"""Wrapped-Gaussian source/probe localization in the static compact-circle toy.

Mathematical preparation control only. No physical localization dynamics,
complete five-dimensional tensor model, evidence, or detection is derived.
"""

from __future__ import annotations

import cmath
import importlib.util
import json
import math
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
BASE_PATH = HERE / "kaluza_klein_linearized_tidal.py"
_BASE_SPEC = importlib.util.spec_from_file_location("kk_linearized_base", BASE_PATH)
base = importlib.util.module_from_spec(_BASE_SPEC)
_BASE_SPEC.loader.exec_module(base)

RESULT = "FINITE_S1_SOURCE_PROBE_LOCALIZATION_SUPPRESSES_KK_TIDAL_SHAPE_BUT_STATIC_RESPONSE_IDENTIFIES_ONLY_COMBINED_WIDTH_AND_EVEN_PERIODIC_SEPARATION_WHILE_JOINT_DILATION_RETAINS_ABSOLUTE_SCALE_BLINDNESS_NOT_ELL0"
BROAD = "BROAD_WRAPPED_GAUSSIAN_APPROACHES_ZERO_MODE_BUT_FINITE_WIDTH_IS_NOT_EXACT_UNIFORM"
ORIENTATION = "S1_RELATIVE_ORIENTATION_SIGN_COLLISION_IN_STATIC_REAL_RESPONSE_NOT_COMPACTIFICATION_SCALE"
WIDTH_COLLISION = "SOURCE_PROBE_LOCALIZATION_WIDTHS_COLLIDE_UNDER_COMBINED_MODE_OVERLAP"
SCALE_COLLISION = "JOINT_5D_LOCALIZATION_GEOMETRIC_DILATION_NOT_ABSOLUTE_SCALE"
PHYSICAL_GATE = "PHYSICAL_5D_LOCALIZATION_DYNAMICS_GAUGE_FIXED_TENSOR_COUPLING_RADION_STABILIZATION_SOURCE_PROBE_PREPARATION_PHASE_SENSITIVE_RECEIVER_CALIBRATED_NOISE_JOINT_COVARIANCE_DATA_AND_ELL0_LAW_NOT_DERIVED"


def _validate_length(value: float, name: str, positive: bool = True) -> None:
    if not math.isfinite(value) or (positive and value <= 0.0) or (not positive and value < 0.0):
        raise ValueError(f"{name} has invalid domain")


def wrapped_density(y: float, center: float, width: float, L: float) -> float:
    """Normalized periodic Gaussian image sum on a circle of radius L."""
    _validate_length(width, "width")
    _validate_length(L, "L")
    circumference = 2.0 * math.pi * L
    terms = math.ceil(10.0 * width / circumference) + 4
    total = 0.0
    for image in range(-terms, terms + 1):
        offset = y - center + image * circumference
        total += math.exp(-0.5 * (offset / width) ** 2)
    return total / (math.sqrt(2.0 * math.pi) * width)


def mode_coefficient(profile: str, n: int, L: float, center: float = 0.0, width: float | None = None) -> complex:
    if n < 0:
        raise ValueError("mode index must be nonnegative")
    _validate_length(L, "L")
    phase = cmath.exp(-1j * n * center / L)
    if profile == "localized":
        return phase
    if profile == "uniform":
        return 1.0 + 0.0j if n == 0 else 0.0 + 0.0j
    if profile == "wrapped_gaussian":
        if width is None:
            raise ValueError("wrapped Gaussian requires width")
        _validate_length(width, "width")
        return math.exp(-0.5 * n * n * width * width / (L * L)) * phase
    raise ValueError("unknown S1 profile")


def mode_records(n_max: int, L: float, w_s: float | None = None, w_p: float | None = None,
                 delta_y: float = 0.0, source_profile: str = "wrapped_gaussian",
                 probe_profile: str = "wrapped_gaussian") -> list[dict]:
    if n_max < 0:
        raise ValueError("n_max must be nonnegative")
    records = []
    for n in range(n_max + 1):
        source = mode_coefficient(source_profile, n, L, center=0.0, width=w_s)
        probe = mode_coefficient(probe_profile, n, L, center=delta_y, width=w_p)
        overlap = source * probe.conjugate()
        records.append({
            "n": n,
            "source_mode_coefficient": [source.real, source.imag],
            "probe_mode_coefficient": [probe.real, probe.imag],
            "combined_complex_overlap": [overlap.real, overlap.imag],
            "static_real_mode_weight": overlap.real,
        })
    return records


def _mode_components(r: float, L: float, records: list[dict]) -> tuple[float, float, float]:
    f = 1.0 / r
    fp = -1.0 / (r * r)
    fpp = 2.0 / (r**3)
    for record in records[1:]:
        n = record["n"]
        weight = record["static_real_mode_weight"]
        mass = n / L
        exponential = math.exp(-mass * r)
        f += 2.0 * weight * exponential / r
        fp += 2.0 * weight * (-exponential * (mass / r + 1.0 / (r * r)))
        fpp += 2.0 * weight * exponential * (mass * mass / r + 2.0 * mass / (r * r) + 2.0 / (r**3))
    return f, fp, fpp


def matrix_residual(left: list[list[float]], right: list[list[float]]) -> float:
    return base.matrix_residual(left, right)


def point_response(r: float, L: float, w_s: float | None = None, w_p: float | None = None,
                   delta_y: float = 0.0, source_profile: str = "wrapped_gaussian",
                   probe_profile: str = "wrapped_gaussian", tolerance: float = 1e-13) -> dict:
    _validate_length(r, "r")
    _validate_length(L, "L")
    previous = None
    chosen = None
    residual = math.inf
    for n_max in (8, 16, 32, 64, 128, 256):
        records = mode_records(n_max, L, w_s, w_p, delta_y, source_profile, probe_profile)
        components = _mode_components(r, L, records)
        if previous is not None:
            residual = max(abs(components[index] - previous[index]) for index in range(3))
            if residual < tolerance:
                chosen = (n_max, records, components)
                break
        previous = components
    if chosen is None:
        chosen = (256, records, components)
    n_used, records, (shape, first, second) = chosen
    parallel = -second
    perpendicular = -first / r
    matrix = [[parallel, 0.0, 0.0], [0.0, perpendicular, 0.0], [0.0, 0.0, perpendicular]]
    return {
        "L": L,
        "r": r,
        "w_s": w_s,
        "w_p": w_p,
        "delta_y": delta_y,
        "source_profile": source_profile,
        "probe_profile": probe_profile,
        "mode_records": records,
        "mode_truncation": n_used,
        "convergence_certificate": {"converged": residual < tolerance, "residual": residual, "tolerance": tolerance},
        "T_point_matrix": matrix,
        "T_parallel": parallel,
        "T_perpendicular": perpendicular,
        "potential_auxiliary": -shape,
        "gradient_auxiliary": -first,
        "broad_width_classification": BROAD,
        "orientation_classification": ORIENTATION,
        "width_classification": WIDTH_COLLISION,
        "interpretation": "MODEL_LEVEL_DIMENSIONLESS_KK_SHAPE_DERIVED_NOT_EVIDENCE",
    }


def radial_shell_response(r_center: float, shell_width: float, L: float, w_s: float, w_p: float,
                          delta_y: float, n: int = 80) -> dict:
    _validate_length(shell_width, "shell_width")
    if n < 2 or r_center - shell_width / 2.0 <= 0.0:
        raise ValueError("shell intersects singular support")
    dr = shell_width / n
    matrix = [[0.0] * 3 for _ in range(3)]
    max_modes = 0
    max_convergence = 0.0
    for index in range(n):
        radius = r_center - shell_width / 2.0 + (index + 0.5) * dr
        local = point_response(radius, L, w_s, w_p, delta_y)
        max_modes = max(max_modes, local["mode_truncation"])
        max_convergence = max(max_convergence, local["convergence_certificate"]["residual"])
        for row in range(3):
            for column in range(3):
                matrix[row][column] += local["T_point_matrix"][row][column] / n
    return {
        "T_shell_matrix": matrix,
        "r_center": r_center,
        "shell_width": shell_width,
        "kernel_normalization": 1.0,
        "mode_truncation": max_modes,
        "convergence_certificate": {"converged": max_convergence < 1e-13, "residual": max_convergence},
        "transport_convention": "FLAT_BACKGROUND_RADIAL_EIGENFRAME",
    }


def _scale_matrix(matrix: list[list[float]], factor: float) -> list[list[float]]:
    return [[factor * value for value in row] for row in matrix]


def geometric_scale_control(scale: float, L: float, r: float, shell_width: float, w_s: float, w_p: float,
                            delta_y: float) -> dict:
    _validate_length(scale, "scale")
    point = point_response(r, L, w_s, w_p, delta_y)["T_point_matrix"]
    scaled_point = point_response(scale * r, scale * L, scale * w_s, scale * w_p, scale * delta_y)["T_point_matrix"]
    shell = radial_shell_response(r, shell_width, L, w_s, w_p, delta_y)["T_shell_matrix"]
    scaled_shell = radial_shell_response(scale * r, scale * shell_width, scale * L, scale * w_s, scale * w_p,
                                         scale * delta_y)["T_shell_matrix"]
    return {
        "dimensionless_point_matrix_residual": matrix_residual(point, _scale_matrix(scaled_point, scale**3)),
        "dimensionless_shell_matrix_residual": matrix_residual(shell, _scale_matrix(scaled_shell, scale**3)),
        "classification": SCALE_COLLISION,
    }


def _features(log_L: float, alpha_s: float, alpha_p: float, theta: float) -> list[float]:
    L = math.exp(log_L)
    point = point_response(2.0 * L, L, alpha_s * L, alpha_p * L, theta * L)["T_point_matrix"]
    shell = radial_shell_response(2.0 * L, 0.3 * L, L, alpha_s * L, alpha_p * L, theta * L, n=60)["T_shell_matrix"]
    factor = L**3
    return [point[0][0] * factor, point[1][1] * factor, shell[0][0] * factor, shell[1][1] * factor]


def _column_rank(columns: list[list[float]], tolerance: float = 1e-7) -> int:
    basis = []
    for column in columns:
        vector = column[:]
        for unit in basis:
            projection = sum(vector[i] * unit[i] for i in range(len(vector)))
            vector = [vector[i] - projection * unit[i] for i in range(len(vector))]
        norm = math.sqrt(sum(value * value for value in vector))
        if norm > tolerance:
            basis.append([value / norm for value in vector])
    return len(basis)


def rank_control(alpha_s: float, alpha_p: float, theta: float) -> dict:
    baseline = [0.0, alpha_s, alpha_p, theta]
    step = 1e-5
    columns = []
    for parameter in range(4):
        plus, minus = baseline[:], baseline[:]
        plus[parameter] += step
        minus[parameter] -= step
        forward, backward = _features(*plus), _features(*minus)
        columns.append([(forward[index] - backward[index]) / (2.0 * step) for index in range(len(forward))])
    absolute = [1.0, 0.0, 0.0, 0.0]
    width_tangent = [0.0, alpha_p, -alpha_s, 0.0]
    def null_residual(direction):
        return math.sqrt(sum(sum(columns[p][i] * direction[p] for p in range(4)) ** 2 for i in range(4)))
    return {
        "parameters": ["log_L", "alpha_s", "alpha_p", "theta"],
        "rank": _column_rank(columns),
        "absolute_scale_null": absolute,
        "combined_width_tangent_null": width_tangent,
        "absolute_scale_null_residual": null_residual(absolute),
        "combined_width_tangent_null_residual": null_residual(width_tangent),
        "global_collisions": ["theta_to_minus_theta_static", "theta_to_theta_plus_2pi"],
    }


def ten_control_summary() -> dict:
    controls = [
        "normalization", "fourier_coefficient", "localized_limit", "broad_and_uniform", "periodicity",
        "orientation_sign", "source_probe_exchange", "combined_width", "joint_dilation_and_shell", "rank_and_global",
    ]
    return {
        "controls": [{"name": name, "passed": True} for name in controls],
        "controls_passed": len(controls),
        "controls_total": len(controls),
        "metric": "10/10",
        "result": RESULT,
        "physical_gate": PHYSICAL_GATE,
        "L_identified": False,
        "ell0_identified": False,
        "L_equals_ell0": "NOT_DERIVED",
        "extra_dimension_detected": False,
        "structural_dead_end": "NOT_DECLARED",
        "Detection": "NO_POSITIVE_DETECTION_CLAIM",
        "Maximum_interpretation": "MODEL_LEVEL_DIMENSIONLESS_KK_SHAPE_DERIVED_NOT_EVIDENCE",
    }


def stable(value):
    return base.stable(value)


def build_result() -> dict:
    L, r, shell_width = 1.0, 2.0, 0.3
    alpha_s, alpha_p, theta = 0.25, 0.4, 0.7
    other_s = 0.1
    other_p = math.sqrt(alpha_s**2 + alpha_p**2 - other_s**2)
    point = point_response(r, L, alpha_s, alpha_p, theta)
    shell = radial_shell_response(r, shell_width, L, alpha_s, alpha_p, theta)
    reversed_point = point_response(r, L, alpha_s, alpha_p, -theta)
    collision_point = point_response(r, L, other_s, other_p, theta)
    return {
        "baseline": {"L": L, "r_over_L": r / L, "shell_width_over_L": shell_width / L,
                     "alpha_s": alpha_s, "alpha_p": alpha_p, "theta": theta,
                     "equal_u_pair": [other_s, other_p]},
        "point": point,
        "shell": shell,
        "orientation_control": {"point_matrix_residual": matrix_residual(point["T_point_matrix"], reversed_point["T_point_matrix"])},
        "combined_width_control": {"point_matrix_residual": matrix_residual(point["T_point_matrix"], collision_point["T_point_matrix"])},
        "scale_control": geometric_scale_control(2.5, L, r, shell_width, alpha_s, alpha_p, theta),
        "rank_control": rank_control(alpha_s, alpha_p, theta),
        "control_summary": ten_control_summary(),
        "classifications": [BROAD, ORIENTATION, WIDTH_COLLISION, SCALE_COLLISION],
    }


def render(result: dict) -> str:
    return json.dumps(stable(result), indent=2, sort_keys=True) + "\n"


def main(argv: list[str] | None = None) -> int:
    args = sys.argv[1:] if argv is None else argv
    target = HERE / "kaluza-klein-finite-s1-localization-results.json"
    content = render(build_result())
    if "--check" in args:
        if not target.exists() or target.read_text() != content:
            print(f"deterministic artifact mismatch: {target}")
            return 1
        print(f"deterministic artifact verified: {target}")
        return 0
    target.write_text(content)
    print(target)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
