#!/usr/bin/env python3
"""Static scalar compact-circle toy control and weak-field tidal Hessian.

This module differentiates the source-scoped Newtonian scalar potential. It is
not a complete gauge-fixed five-dimensional tensor perturbation or evidence.
"""

from __future__ import annotations

import math

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
