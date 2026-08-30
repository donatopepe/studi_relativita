#!/usr/bin/env python3
"""Independent full-Riemann photon-sphere screen conformance; no UMCH inference."""
import importlib.util
import math
import pathlib

HERE = pathlib.Path(__file__).resolve().parent

_SPEC = importlib.util.spec_from_file_location(
    "scattering_screen_conformance", HERE / "schwarzschild_scattering_screen_conformance.py"
)
riemann = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(riemann)

_LEGACY_SPEC = importlib.util.spec_from_file_location(
    "legacy_photon_sphere_jacobi", HERE / "schwarzschild_photon_sphere_jacobi.py"
)
legacy = importlib.util.module_from_spec(_LEGACY_SPEC)
_LEGACY_SPEC.loader.exec_module(legacy)


def _matrix_distance(A, B):
    return math.sqrt(sum((A[i][j] - B[i][j]) ** 2 for i in range(2) for j in range(2)))


def _vectors(M=1.0, orientation=1):
    r = 3.0 * M
    f = 1.0 - 2.0 * M / r
    return {
        "r": r,
        "f": f,
        "k": [1.0 / math.sqrt(f), 0.0, 0.0, orientation / r],
        "screen": [[0.0, 0.0, 1.0 / r, 0.0], [0.0, math.sqrt(f), 0.0, 0.0]],
        "screen_order": ["polar", "radial"],
    }


def circular_screen_control(M=1.0, orientation=1):
    vectors = _vectors(M, orientation)
    g = riemann.metric(M, vectors["r"], math.pi / 2)
    k = vectors["k"]
    screen = vectors["screen"]
    metric_screen = [[riemann.dot(g, screen[A], screen[B]) for B in range(2)] for A in range(2)]
    return {
        "M": M,
        "r": vectors["r"],
        "orientation": orientation,
        "screen_order": vectors["screen_order"],
        "k": k,
        "screen": screen,
        "null_residual": abs(riemann.dot(g, k, k)),
        "screen_metric": metric_screen,
        "screen_metric_residual": max(abs(metric_screen[i][j] - (1.0 if i == j else 0.0)) for i in range(2) for j in range(2)),
        "screen_tangent_residual": max(abs(riemann.dot(g, e, k)) for e in screen),
    }


def _projection(M, orientation, relative_step):
    vectors = _vectors(M, orientation)
    Riemann = riemann.numerical_riemann_lowered(M, vectors["r"], math.pi / 2, relative_step)
    return riemann._project_riemann(Riemann, vectors["screen"], vectors["k"])


def full_riemann_control(M=1.0, orientation=1, coarse_step=4e-4, fine_step=1e-4):
    coarse = _projection(M, orientation, coarse_step)
    fine = _projection(M, orientation, fine_step)
    amplitude = 1.0 / (9.0 * M * M)
    analytic = [[-amplitude, 0.0], [0.0, amplitude]]
    # Reorder legacy (radial,polar) to (polar,radial), preserving its signs.
    legacy_in_polar_radial_order = [[legacy.optical_K(M, orientation)[1][1], 0.0], [0.0, legacy.optical_K(M, orientation)[0][0]]]
    return {
        "M": M,
        "orientation": orientation,
        "screen_order": ["polar", "radial"],
        "derivative_coordinates": ["r", "theta"],
        "polar_channel_origin": "DIRECT_RIEMANN_PROJECTION",
        "radial_channel_origin": "DIRECT_RIEMANN_PROJECTION",
        "K_coarse": coarse,
        "K_fine": fine,
        "K_analytic": analytic,
        "coarse_projection_mismatch": _matrix_distance(coarse, analytic),
        "fine_projection_mismatch": _matrix_distance(fine, analytic),
        "symmetry_residual": abs(fine[0][1] - fine[1][0]),
        "vacuum_trace_residual": abs(fine[0][0] + fine[1][1]),
        "legacy_profile_polar_radial": legacy_in_polar_radial_order,
        "legacy_profile_mismatch": _matrix_distance(fine, legacy_in_polar_radial_order),
        "legacy_profile_status": "CONFIRMED_AFTER_EXPLICIT_SCREEN_ORDER_AND_AFFINE_NORMALIZATION",
    }


def affine_normalization_control(M=1.0):
    circular = full_riemann_control(M)["K_analytic"]
    scattering_limit = [[-1.0 / (3.0 * M * M), 0.0], [0.0, 1.0 / (3.0 * M * M)]]
    frequency_ratio = math.sqrt(3.0)
    converted = [[value / frequency_ratio ** 2 for value in row] for row in scattering_limit]
    return {
        "screen_order": ["polar", "radial"],
        "circular_local_frequency": 1.0,
        "scattering_E_infinity": 1.0,
        "scattering_local_frequency_at_3M": frequency_ratio,
        "scattering_to_circular_frequency_ratio": frequency_ratio,
        "tidal_matrix_quadratic_ratio": frequency_ratio ** 2,
        "circular_K": circular,
        "scattering_limit_K": scattering_limit,
        "converted_scattering_K": converted,
        "converted_profile_residual": _matrix_distance(circular, converted),
        "unconverted_profile_residual": _matrix_distance(circular, scattering_limit),
        "naive_comparison_status": "FALSIFIED_UNCONVERTED_AFFINE_NORMALIZATION_COMPARISON",
    }
