#!/usr/bin/env python3
"""Static scalar compact-circle toy control and weak-field tidal Hessian.

This module differentiates the source-scoped Newtonian scalar potential. It is
not a complete gauge-fixed five-dimensional tensor perturbation or evidence.
"""

from __future__ import annotations

import json
import math
import pathlib
import sys

NULL_PROJECTION = "UNIFORM_S1_SOURCE_OR_PROBE_PROJECTS_NONZERO_KK_MODES_NOT_ABSENCE_OF_EXTRA_DIMENSION"


def _validate(r: float, L: float) -> None:
    if not math.isfinite(r) or r <= 0.0:
        raise ValueError("r must be finite and positive away from singular support")
    if not math.isfinite(L) or L <= 0.0:
        raise ValueError("L must be finite and positive")


def circle_mode_weights(source_profile: str, probe_profile: str, n_max: int, delta_y: float, L: float) -> list[float]:
    if L <= 0.0 or n_max < 0:
        raise ValueError("invalid circle scale or mode truncation")
    if source_profile not in {"localized", "uniform"} or probe_profile not in {"localized", "uniform"}:
        raise ValueError("unknown S1 profile")
    weights = [1.0]
    for n in range(1, n_max + 1):
        weights.append(math.cos(n * delta_y / L) if source_profile == probe_profile == "localized" else 0.0)
    return weights


def circle_projection_control(source_profile: str, probe_profile: str, n_max: int, delta_y: float, L: float) -> dict:
    weights = circle_mode_weights(source_profile, probe_profile, n_max, delta_y, L)
    projected = source_profile == "uniform" or probe_profile == "uniform"
    return {
        "source_S1_profile": source_profile,
        "probe_S1_profile": probe_profile,
        "weights": weights,
        "classification": NULL_PROJECTION if projected else "LOCALIZED_SOURCE_PROBE_KK_MODES_RETAINED",
    }


def point_shape_modes(r: float, L: float, delta_y: float = 0.0, n_max: int = 100, source_profile: str = "localized", probe_profile: str = "localized") -> float:
    _validate(r, L)
    weights = circle_mode_weights(source_profile, probe_profile, n_max, delta_y, L)
    total = weights[0]
    for n in range(1, n_max + 1):
        total += 2.0 * weights[n] * math.exp(-n * r / L)
    return total / r


def point_shape_exact(r: float, L: float, delta_y: float = 0.0, source_profile: str = "localized", probe_profile: str = "localized") -> float:
    _validate(r, L)
    if source_profile == "uniform" or probe_profile == "uniform":
        return 1.0 / r
    x = r / L
    theta = delta_y / L
    denominator = math.cosh(x) - math.cos(theta)
    if denominator == 0.0:
        raise ValueError("singular coincident point")
    return math.sinh(x) / denominator / r


def _radial_derivatives(r: float, L: float, delta_y: float, source_profile: str, probe_profile: str) -> tuple[float, float, float]:
    """Return shape f, f', f'' for potential Phi=-A*f."""
    _validate(r, L)
    if source_profile == "uniform" or probe_profile == "uniform":
        return 1.0 / r, -1.0 / (r * r), 2.0 / (r**3)
    x = r / L
    c = math.cos(delta_y / L)
    sh = math.sinh(x)
    ch = math.cosh(x)
    d = ch - c
    h = sh / d
    hx = (1.0 - c * ch) / (d * d)
    hxx = sh * (c * c + c * ch - 2.0) / (d**3)
    f = h / r
    fp = hx / (L * r) - h / (r * r)
    fpp = hxx / (L * L * r) - 2.0 * hx / (L * r * r) + 2.0 * h / (r**3)
    return f, fp, fpp


def _unit(direction: tuple[float, float, float]) -> list[float]:
    norm = math.sqrt(sum(value * value for value in direction))
    if norm == 0.0 or not math.isfinite(norm):
        raise ValueError("direction must be finite and nonzero")
    return [value / norm for value in direction]


def point_response(r: float, L: float, direction: tuple[float, float, float] = (1.0, 0.0, 0.0), delta_y: float = 0.0, source_profile: str = "localized", probe_profile: str = "localized", amplitude: float = 1.0) -> dict:
    _validate(r, L)
    if not math.isfinite(amplitude):
        raise ValueError("amplitude must be finite")
    f, fp, fpp = _radial_derivatives(r, L, delta_y, source_profile, probe_profile)
    # Phi=-A*f, so radial Hessian eigenvalues are -A*f'' and -A*f'/r.
    parallel = -amplitude * fpp
    perpendicular = -amplitude * fp / r
    nhat = _unit(direction)
    matrix = []
    for i in range(3):
        row = []
        for j in range(3):
            delta = 1.0 if i == j else 0.0
            row.append(perpendicular * delta + (parallel - perpendicular) * nhat[i] * nhat[j])
        matrix.append(row)
    reconstructed_parallel = sum(nhat[i] * matrix[i][j] * nhat[j] for i in range(3) for j in range(3))
    trace = sum(matrix[i][i] for i in range(3))
    reconstructed_perpendicular = (trace - reconstructed_parallel) / 2.0
    return {
        "primary_object": "FULL_SPATIAL_TIDAL_HESSIAN",
        "T_matrix": matrix,
        "T_parallel": parallel,
        "T_perpendicular": perpendicular,
        "Phi_auxiliary": -amplitude * f,
        "grad_Phi_radial_auxiliary": -amplitude * fp,
        "source_S1_profile": source_profile,
        "probe_S1_profile": probe_profile,
        "source_probe_relative_S1_position": delta_y,
        "L": L,
        "reconstruction_residual": max(abs(parallel - reconstructed_parallel), abs(perpendicular - reconstructed_perpendicular)),
        "interpretation": "PROJECT_WEAK_FIELD_NEWTONIAN_HESSIAN_NOT_COMPLETE_5D_TENSOR_OR_EVIDENCE",
    }


def asymptotic_control(r: float, L: float) -> dict:
    _validate(r, L)
    exact = point_shape_exact(r, L)
    zero_mode = 1.0 / r
    long_residual = abs(exact - zero_mode) / abs(zero_mode)
    # Same-circle exact shape tends to 2L/r^2.
    short_scaled = exact * r * r / (2.0 * L)
    return {
        "long_distance_relative_residual": long_residual,
        "short_distance_scaled_residual": abs(short_scaled - 1.0),
    }


def convergence_control(r: float, L: float, delta_y: float = 0.0, tolerance: float = 1e-10, max_modes: int = 100000) -> dict:
    _validate(r, L)
    if tolerance <= 0.0 or max_modes < 1:
        raise ValueError("invalid convergence request")
    exact = point_shape_exact(r, L, delta_y)
    total = 1.0
    residual = math.inf
    for n in range(1, max_modes + 1):
        total += 2.0 * math.cos(n * delta_y / L) * math.exp(-n * r / L)
        approximate = total / r
        residual = abs(approximate - exact)
        if residual < tolerance:
            return {"converged": True, "n_used": n, "residual": residual, "exact": exact, "mode_sum": approximate}
    return {"converged": False, "n_used": max_modes, "residual": residual, "exact": exact, "mode_sum": total / r}


def matrix_residual(left: list[list[float]], right: list[list[float]]) -> float:
    return max(abs(left[i][j] - right[i][j]) for i in range(3) for j in range(3))


def source_profile_control(profile: str, size: float) -> dict:
    if not math.isfinite(size) or size <= 0.0:
        raise ValueError("source size must be finite and positive")
    if profile == "uniform_sphere":
        density = 3.0 / (4.0 * math.pi * size**3)
        normalization = density * 4.0 * math.pi * size**3 / 3.0
        return {"profile": profile, "size": size, "normalization": normalization, "width_convention": "COMPACT_SUPPORT_RADIUS_R_S"}
    if profile == "gaussian":
        density0 = 1.0 / ((2.0 * math.pi) ** 1.5 * size**3)
        normalization = density0 * (2.0 * math.pi) ** 1.5 * size**3
        return {"profile": profile, "size": size, "normalization": normalization, "width_convention": "ONE_DIMENSIONAL_COMPONENT_STANDARD_DEVIATION_SIGMA"}
    raise ValueError("unknown three-dimensional source profile")


def _density(profile: str, size: float, radius: float) -> float:
    if profile == "uniform_sphere":
        return 3.0 / (4.0 * math.pi * size**3) if radius <= size else 0.0
    if profile == "gaussian":
        return math.exp(-0.5 * (radius / size) ** 2) / ((2.0 * math.pi) ** 1.5 * size**3)
    raise ValueError("unknown source profile")


def _finite_components(r: float, L: float, profile: str, size: float, source_S1_profile: str, probe_S1_profile: str, n_radial: int, n_mu: int) -> tuple[float, float]:
    radial_max = size if profile == "uniform_sphere" else 7.0 * size
    dr = radial_max / n_radial
    dmu = 2.0 / n_mu
    parallel = 0.0
    trace = 0.0
    for a in range(n_radial):
        source_radius = (a + 0.5) * dr
        shell_weight = 2.0 * math.pi * source_radius**2 * _density(profile, size, source_radius) * dr * dmu
        for b in range(n_mu):
            mu = -1.0 + (b + 0.5) * dmu
            distance2 = r * r + source_radius**2 - 2.0 * r * source_radius * mu
            distance = math.sqrt(distance2)
            if distance < 1e-12:
                continue
            local = point_response(distance, L, source_profile=source_S1_profile, probe_profile=probe_S1_profile)
            cosine = (r - source_radius * mu) / distance
            local_parallel = local["T_perpendicular"] + (local["T_parallel"] - local["T_perpendicular"]) * cosine**2
            local_trace = local["T_parallel"] + 2.0 * local["T_perpendicular"]
            parallel += shell_weight * local_parallel
            trace += shell_weight * local_trace
    return parallel, (trace - parallel) / 2.0


def finite_source_response(r: float, L: float, source_profile_3d: str, source_size: float,
                           source_S1_profile: str = "localized", probe_S1_profile: str = "localized") -> dict:
    _validate(r, L)
    source_profile_control(source_profile_3d, source_size)
    if source_profile_3d == "uniform_sphere" and r <= source_size:
        raise ValueError("baseline compact-source control requires exterior observation")
    coarse = _finite_components(r, L, source_profile_3d, source_size, source_S1_profile, probe_S1_profile, 32, 40)
    fine = _finite_components(r, L, source_profile_3d, source_size, source_S1_profile, probe_S1_profile, 64, 80)
    residual = max(abs(fine[i] - coarse[i]) for i in range(2))
    parallel, perpendicular = fine
    matrix = [[parallel, 0.0, 0.0], [0.0, perpendicular, 0.0], [0.0, 0.0, perpendicular]]
    projection = circle_projection_control(source_S1_profile, probe_S1_profile, 8, 0.0, L)
    return {
        "primary_object": "FULL_SPATIAL_TIDAL_HESSIAN",
        "T_matrix": matrix,
        "T_parallel": parallel,
        "T_perpendicular": perpendicular,
        "source_3d_profile": source_profile_3d,
        "source_size": source_size,
        "source_S1_profile": source_S1_profile,
        "probe_S1_profile": probe_S1_profile,
        "circle_projection": projection,
        "quadrature_certificate": {"converged": residual < 3e-4, "residual": residual, "coarse_grid": [32, 40], "fine_grid": [64, 80]},
        "classification": "SOURCE_PROFILE_AND_WINDOW_SHAPE_ARE_PREPARATION_NUISANCES_NOT_INTRINSIC_GEOMETRY",
    }


def radial_shell_window(r_center: float, width: float, L: float, n: int = 80) -> dict:
    _validate(r_center, L)
    if width <= 0.0 or n < 2 or r_center - width / 2.0 <= 0.0:
        raise ValueError("radial shell must exclude singular support")
    dr = width / n
    parallel = perpendicular = 0.0
    for index in range(n):
        radius = r_center - width / 2.0 + (index + 0.5) * dr
        local = point_response(radius, L)
        parallel += local["T_parallel"] / n
        perpendicular += local["T_perpendicular"] / n
    return {
        "T_window_matrix": [[parallel, 0.0, 0.0], [0.0, perpendicular, 0.0], [0.0, 0.0, perpendicular]],
        "window_family": "radial_shell",
        "window_geometry": {"r_center": r_center, "width": width},
        "kernel_normalization": 1.0,
        "transport_convention": "FLAT_BACKGROUND_RADIAL_EIGENFRAME",
    }


def _rotation_z(angle: float) -> list[list[float]]:
    c, s = math.cos(angle), math.sin(angle)
    return [[c, -s, 0.0], [s, c, 0.0], [0.0, 0.0, 1.0]]


def _matmul(left: list[list[float]], right: list[list[float]]) -> list[list[float]]:
    return [[sum(left[i][k] * right[k][j] for k in range(3)) for j in range(3)] for i in range(3)]


def rotate_matrix_z(matrix: list[list[float]], angle: float) -> list[list[float]]:
    rotation = _rotation_z(angle)
    transpose = [[rotation[j][i] for j in range(3)] for i in range(3)]
    return _matmul(_matmul(rotation, matrix), transpose)


def oriented_box_window(center: tuple[float, float, float], dimensions: tuple[float, float, float], L: float,
                        angle: float = 0.0, n_per_axis: int = 5) -> dict:
    if any(value <= 0.0 for value in dimensions) or n_per_axis < 2:
        raise ValueError("box dimensions and quadrature must be positive")
    center_radius = math.sqrt(sum(value * value for value in center))
    _validate(center_radius, L)
    half_diagonal = 0.5 * math.sqrt(sum(value * value for value in dimensions))
    if center_radius <= half_diagonal:
        raise ValueError("oriented region intersects singular support")
    rotation = _rotation_z(angle)
    total = [[0.0] * 3 for _ in range(3)]
    count = n_per_axis**3
    for i in range(n_per_axis):
        for j in range(n_per_axis):
            for k in range(n_per_axis):
                local = [
                    ((i + 0.5) / n_per_axis - 0.5) * dimensions[0],
                    ((j + 0.5) / n_per_axis - 0.5) * dimensions[1],
                    ((k + 0.5) / n_per_axis - 0.5) * dimensions[2],
                ]
                offset = [sum(rotation[a][b] * local[b] for b in range(3)) for a in range(3)]
                point = [center[a] + offset[a] for a in range(3)]
                radius = math.sqrt(sum(value * value for value in point))
                matrix = point_response(radius, L, direction=tuple(point))["T_matrix"]
                for a in range(3):
                    for b in range(3):
                        total[a][b] += matrix[a][b] / count
    return {
        "T_window_matrix": total,
        "window_family": "oriented_box",
        "window_geometry": {"center": list(center), "dimensions": list(dimensions)},
        "window_orientation": angle,
        "kernel_normalization": 1.0,
        "transport_convention": "FLAT_BACKGROUND_CARTESIAN_IDENTITY",
    }


def _scaled_matrix(matrix: list[list[float]], factor: float) -> list[list[float]]:
    return [[factor * matrix[i][j] for j in range(3)] for i in range(3)]


def geometric_scale_control(scale: float, r: float, L: float, source_size: float, window_width: float) -> dict:
    if scale <= 0.0:
        raise ValueError("scale must be positive")
    base = point_response(r, L)["T_matrix"]
    scaled = point_response(scale * r, scale * L)["T_matrix"]
    # Fixed dimensionless coupling-amplitude convention: Hessian scales as length^-3.
    point_residual = matrix_residual(base, _scaled_matrix(scaled, scale**3))
    shell = radial_shell_window(r, window_width, L)["T_window_matrix"]
    scaled_shell = radial_shell_window(scale * r, scale * window_width, scale * L)["T_window_matrix"]
    shell_residual = matrix_residual(shell, _scaled_matrix(scaled_shell, scale**3))
    return {
        "dimensionless_point_matrix_residual": point_residual,
        "dimensionless_shell_matrix_residual": shell_residual,
        "source_size_ratio": source_size / L,
        "classification": "JOINT_5D_GEOMETRIC_DILATION_NOT_INTERIOR_ABSOLUTE_SCALE",
    }


def _dimensionless_features(log_L: float, source_ratio: float, window_ratio: float) -> list[float]:
    L = math.exp(log_L)
    radius = 2.0 * L
    point = point_response(radius, L)
    shell = radial_shell_window(radius, window_ratio * L, L)
    pscale = L**3
    return [
        point["T_parallel"] * pscale,
        point["T_perpendicular"] * pscale,
        shell["T_window_matrix"][0][0] * pscale,
        shell["T_window_matrix"][1][1] * pscale,
        source_ratio,
    ]


def rank_control(r_over_L: float = 2.0, source_size_over_L: float = 0.25, window_width_over_L: float = 0.3) -> dict:
    if abs(r_over_L - 2.0) > 1e-12:
        raise ValueError("bounded rank baseline currently preregisters r_over_L=2")
    base = [0.0, source_size_over_L, window_width_over_L]
    step = 1e-5
    columns = []
    for index in range(3):
        plus = base[:]
        minus = base[:]
        plus[index] += step
        minus[index] -= step
        fplus = _dimensionless_features(*plus)
        fminus = _dimensionless_features(*minus)
        columns.append([(fplus[j] - fminus[j]) / (2.0 * step) for j in range(len(fplus))])
    norms = [math.sqrt(sum(value * value for value in column)) for column in columns]
    # Source-ratio and window-ratio columns are linearly independent in this declared feature map.
    rank = sum(norm > 1e-8 for norm in norms)
    return {
        "parameters": ["log_L", "source_size_over_L", "window_width_over_L"],
        "log_L_column_norm": norms[0],
        "column_norms": norms,
        "rank": rank,
        "scale_null_direction": [1.0, 0.0, 0.0],
        "classification": "L_NOT_IDENTIFIABLE_WITHOUT_SOURCE_PROBE_AND_WINDOW_CALIBRATION",
    }


def identifiability_gate() -> dict:
    return {
        "L_identified": False,
        "ell0_identified": False,
        "L_equals_ell0": "NOT_DERIVED",
        "extra_dimension_detected": False,
        "dependence": "DEPENDENCE_UNRESOLVED_WITHOUT_JOINT_COVARIANCE",
        "physical_gate": "NONLINEAR_5D_DYNAMICS_RADION_STABILIZATION_MATTER_LOCALIZATION_SOURCE_PROBE_PREPARATION_ABSOLUTE_COUPLING_CLOCK_RECEIVER_CALIBRATED_NOISE_JOINT_COVARIANCE_DATA_AND_ELL0_LAW_NOT_DERIVED",
    }


def stable(value):
    if isinstance(value, float):
        if abs(value) < 1e-7:
            return 0.0
        return float(format(value, ".8g"))
    if isinstance(value, list):
        return [stable(item) for item in value]
    if isinstance(value, dict):
        return {key: stable(value[key]) for key in sorted(value)}
    return value


def build_result() -> dict:
    L = 1.0
    point = point_response(r=2.0, L=L)
    source_controls = []
    for profile, size in (("uniform_sphere", 0.25), ("gaussian", 0.25)):
        for circle in ("localized", "uniform"):
            source_controls.append(finite_source_response(2.0, L, profile, size, circle, "localized"))
    status = {
        "HIGHER_DIMENSIONAL_GRAVITY_CORE": "REFORMULATION_CANDIDATE_UNRATIFIED",
        "MODEL": "LINEARIZED_5D_COMPACT_KK_TOY_CONTROL",
        "UMCH": "UNPROVEN_SECONDARY_CANDIDATE",
        "L_identified": False,
        "ell0_identified": False,
        "L_equals_ell0": "NOT_DERIVED",
        "extra_dimension_detected": False,
        "structural_dead_end": "NOT_DECLARED",
        "Detection": "NO_POSITIVE_DETECTION_CLAIM",
        "Maximum_interpretation": "MODEL_LEVEL_DIMENSIONLESS_KK_SHAPE_DERIVED_NOT_EVIDENCE",
    }
    return {
        "status": status,
        "baseline": {"L": L, "r": 2.0, "source_size": 0.25, "shell_width": 0.3},
        "point_localized_localized": point,
        "projection_controls": [
            circle_projection_control(source, probe, 8, 0.0, L)
            for source, probe in (("localized", "localized"), ("localized", "uniform"), ("uniform", "localized"), ("uniform", "uniform"))
        ],
        "source_controls": source_controls,
        "window_controls": {
            "radial_shell": radial_shell_window(2.0, 0.3, L),
            "oriented_box": oriented_box_window((2.0, 0.0, 0.0), (0.4, 0.2, 0.1), L, angle=0.3, n_per_axis=5),
        },
        "asymptotic_controls": {"long": asymptotic_control(20.0, L), "short": asymptotic_control(0.01, L)},
        "convergence": convergence_control(0.2, L, tolerance=1e-9),
        "scale_control": geometric_scale_control(2.5, 1.8, 0.9, 0.2, 0.3),
        "rank_control": rank_control(),
        "identifiability_gate": identifiability_gate(),
        "result": "LOCALIZED_SOURCE_PROBE_KK_TOWER_ADDS_DIMENSIONLESS_FINITE_WINDOW_TIDAL_SHAPE_BUT_UNIFORM_PROFILE_PROJECTION_SOURCE_WINDOW_DEGENERACY_AND_JOINT_5D_DILATION_PREVENT_ABSOLUTE_SCALE_OR_ELL0_IDENTIFICATION",
    }


def render(result: dict) -> str:
    return json.dumps(stable(result), indent=2, sort_keys=True) + "\n"


def main(argv: list[str] | None = None) -> int:
    args = sys.argv[1:] if argv is None else argv
    target = pathlib.Path(__file__).with_name("kaluza-klein-linearized-tidal-results.json")
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
