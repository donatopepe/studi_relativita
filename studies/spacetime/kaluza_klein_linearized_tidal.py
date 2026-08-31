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
