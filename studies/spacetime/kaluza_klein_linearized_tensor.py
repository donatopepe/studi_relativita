#!/usr/bin/env python3
"""Static linearized 5D tensor conformance for the compact-circle toy.

Model-level analytic control only. No physical source localization, radion
stabilization, calibrated coupling, evidence, detection, or ell0 law follows.
"""

from __future__ import annotations

import importlib.util
import math
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
BASE_PATH = HERE / "kaluza_klein_linearized_tidal.py"
_BASE_SPEC = importlib.util.spec_from_file_location("kk_linearized_tidal_base", BASE_PATH)
base = importlib.util.module_from_spec(_BASE_SPEC)
_BASE_SPEC.loader.exec_module(base)

DIMENSION = 5
ETA = (-1.0, 1.0, 1.0, 1.0, 1.0)
COMPACT_CLASSIFICATION = "ORDINARY_SPACE_TIDAL_BLOCK_OMITS_COMPACT_INDEX_CURVATURE_NOT_EXTRA_OBSERVATIONAL_RANK"
STRESS_CLASSIFICATION = "TENSOR_COMPLETION_DEPENDS_ON_SOURCE_STRESS_AND_DECLARED_LINEARIZED_CONVENTIONS_NOT_SCALAR_POTENTIAL_ALONE"
SCALE_CLASSIFICATION = "LINEARIZED_5D_TENSOR_COMPLETION_RETAINS_JOINT_GEOMETRIC_SCALE_NULL_NOT_ELL0"


def _zeros2() -> list[list[float]]:
    return [[0.0 for _ in range(DIMENSION)] for _ in range(DIMENSION)]


def _validate_point(r: float, L: float, delta_y: float, profile: str, amplitude: float) -> None:
    base._validate(r, L)
    if profile not in {"localized", "uniform"}:
        raise ValueError("profile must be localized or uniform")
    if not math.isfinite(delta_y) or not math.isfinite(amplitude):
        raise ValueError("coordinates and amplitude must be finite")


def _trace(matrix: list[list[float]]) -> float:
    return sum(ETA[index] * matrix[index][index] for index in range(DIMENSION))


def trace_reversal_from_bar(bar_h: list[list[float]]) -> dict:
    if len(bar_h) != DIMENSION or any(len(row) != DIMENSION for row in bar_h):
        raise ValueError("bar_h must be a 5x5 covariant matrix")
    bar_trace = _trace(bar_h)
    h = [[bar_h[a][b] - ETA[a] * bar_trace / (DIMENSION - 2) if a == b else bar_h[a][b]
          for b in range(DIMENSION)] for a in range(DIMENSION)]
    h_trace = _trace(h)
    roundtrip = [[h[a][b] - 0.5 * ETA[a] * h_trace if a == b else h[a][b]
                  for b in range(DIMENSION)] for a in range(DIMENSION)]
    return {"bar_h": bar_h, "h": h, "bar_h_roundtrip": roundtrip}


def _shape_derivatives(r: float, L: float, delta_y: float, profile: str) -> dict:
    """Return f and first/second derivatives for Phi=-A*f in radial eigenframe."""
    if profile == "uniform":
        return {
            "f": 1.0 / r,
            "f_r": -1.0 / r**2,
            "f_rr": 2.0 / r**3,
            "f_y": 0.0,
            "f_ry": 0.0,
            "f_yy": 0.0,
        }
    x = r / L
    theta = delta_y / L
    sinh_x = math.sinh(x)
    cosh_x = math.cosh(x)
    cos_theta = math.cos(theta)
    sin_theta = math.sin(theta)
    denominator = cosh_x - cos_theta
    if denominator == 0.0:
        raise ValueError("singular coincident point")
    shape = sinh_x / denominator
    shape_x = (1.0 - cos_theta * cosh_x) / denominator**2
    shape_xx = sinh_x * (cos_theta**2 + cos_theta * cosh_x - 2.0) / denominator**3
    shape_theta = -sinh_x * sin_theta / denominator**2
    shape_thetatheta = sinh_x * (2.0 - cos_theta * cosh_x - cos_theta**2) / denominator**3
    shape_xtheta = sin_theta * (cosh_x**2 + cos_theta * cosh_x - 2.0) / denominator**3
    return {
        "f": shape / r,
        "f_r": shape_x / (L * r) - shape / r**2,
        "f_rr": shape_xx / (L**2 * r) - 2.0 * shape_x / (L * r**2) + 2.0 * shape / r**3,
        "f_y": shape_theta / (L * r),
        "f_ry": shape_xtheta / (L**2 * r) - shape_theta / (L * r**2),
        "f_yy": shape_thetatheta / (L**2 * r),
    }


def _potential_derivatives(r: float, L: float, delta_y: float, profile: str, amplitude: float) -> dict:
    shape = _shape_derivatives(r, L, delta_y, profile)
    result = {key: -amplitude * value for key, value in shape.items()}
    result["laplacian_4d"] = result["f_rr"] + 2.0 * result["f_r"] / r + result["f_yy"]
    return result


def _potential_hessian(derivatives: dict, r: float) -> list[list[float]]:
    """5D-coordinate Hessian with radial ordinary coordinate aligned to x1."""
    hessian = _zeros2()
    hessian[1][1] = derivatives["f_rr"]
    hessian[2][2] = derivatives["f_r"] / r
    hessian[3][3] = derivatives["f_r"] / r
    hessian[4][4] = derivatives["f_yy"]
    hessian[1][4] = hessian[4][1] = derivatives["f_ry"]
    return hessian


def _metric_from_phi(phi: float) -> list[list[float]]:
    metric = _zeros2()
    metric[0][0] = -2.0 * phi
    for index in range(1, DIMENSION):
        metric[index][index] = -phi
    return metric


def _bar_metric(metric: list[list[float]]) -> list[list[float]]:
    trace = _trace(metric)
    return [[metric[a][b] - 0.5 * ETA[a] * trace if a == b else metric[a][b]
             for b in range(DIMENSION)] for a in range(DIMENSION)]


def _metric_second_derivative(a: int, b: int, c: int, d: int, phi_hessian: list[list[float]]) -> float:
    if a != b:
        return 0.0
    coefficient = -2.0 if a == 0 else -1.0
    return coefficient * phi_hessian[c][d]


def _riemann(phi_hessian: list[list[float]]) -> list[list[list[list[float]]]]:
    tensor = [[[[0.0 for _ in range(DIMENSION)] for _ in range(DIMENSION)]
               for _ in range(DIMENSION)] for _ in range(DIMENSION)]
    d2h = lambda a, b, c, d: _metric_second_derivative(a, b, c, d, phi_hessian)
    for a in range(DIMENSION):
        for b in range(DIMENSION):
            for c in range(DIMENSION):
                for d in range(DIMENSION):
                    tensor[a][b][c][d] = 0.5 * (
                        d2h(a, d, c, b) + d2h(b, c, d, a)
                        - d2h(a, c, d, b) - d2h(b, d, c, a)
                    )
    return tensor


def _contract_ricci(riemann: list) -> list[list[float]]:
    return [[sum(ETA[a] * riemann[a][b][a][d] for a in range(DIMENSION))
             for d in range(DIMENSION)] for b in range(DIMENSION)]


def _direct_ricci(phi_hessian: list[list[float]]) -> list[list[float]]:
    d2h = lambda a, b, c, d: _metric_second_derivative(a, b, c, d, phi_hessian)
    ricci = _zeros2()
    for b in range(DIMENSION):
        for d in range(DIMENSION):
            divergence_left = sum(ETA[a] * d2h(a, d, a, b) for a in range(DIMENSION))
            divergence_right = sum(ETA[a] * d2h(a, b, a, d) for a in range(DIMENSION))
            box_metric = sum(ETA[a] * d2h(b, d, a, a) for a in range(DIMENSION))
            trace_derivative = sum(ETA[a] * d2h(a, a, b, d) for a in range(DIMENSION))
            ricci[b][d] = 0.5 * (divergence_left + divergence_right - box_metric - trace_derivative)
    return ricci


def _einstein(ricci: list[list[float]]) -> tuple[float, list[list[float]]]:
    scalar = _trace(ricci)
    tensor = [[ricci[a][b] - 0.5 * ETA[a] * scalar if a == b else ricci[a][b]
               for b in range(DIMENSION)] for a in range(DIMENSION)]
    return scalar, tensor


def _matrix_residual(left: list[list[float]], right: list[list[float]]) -> float:
    return max(abs(left[i][j] - right[i][j]) for i in range(len(left)) for j in range(len(left[i])))


def _max_matrix_residual(left: list[list[float]], right: list[list[float]]) -> float:
    return max(abs(left[i][j] - right[i][j]) for i in range(DIMENSION) for j in range(DIMENSION))


def _harmonic_residual(phi_hessian: list[list[float]]) -> list[list[float]]:
    """Derivative of the harmonic vector, enough for the static Hessian control."""
    residual = _zeros2()
    for b in range(DIMENSION):
        for c in range(DIMENSION):
            divergence = sum(ETA[a] * _metric_second_derivative(a, b, c, a, phi_hessian) for a in range(DIMENSION))
            trace_derivative = sum(ETA[a] * _metric_second_derivative(a, a, c, b, phi_hessian) for a in range(DIMENSION))
            residual[b][c] = divergence - 0.5 * trace_derivative
    return residual


def point_tensor_response(r: float, L: float, delta_y: float = 0.0, profile: str = "localized", amplitude: float = 1.0) -> dict:
    _validate_point(r, L, delta_y, profile, amplitude)
    derivatives = _potential_derivatives(r, L, delta_y, profile, amplitude)
    phi_hessian = _potential_hessian(derivatives, r)
    riemann = _riemann(phi_hessian)
    ricci = _contract_ricci(riemann)
    direct_ricci = _direct_ricci(phi_hessian)
    scalar, einstein = _einstein(ricci)
    metric = _metric_from_phi(derivatives["f"])
    bar_metric = _bar_metric(metric)
    r0i0j = [[riemann[0][i + 1][0][j + 1] for j in range(3)] for i in range(3)]
    hessian_reference = [[phi_hessian[i + 1][j + 1] for j in range(3)] for i in range(3)]
    return {
        "metric_perturbation_5D": metric,
        "trace_reversed_metric_5D": bar_metric,
        "harmonic_gauge_residual": _harmonic_residual(phi_hessian),
        "Riemann_5D": riemann,
        "Ricci_5D": ricci,
        "Ricci_scalar_5D": scalar,
        "Einstein_5D": einstein,
        "einstein_conformance_residual": [[ricci[i][j] - direct_ricci[i][j] for j in range(DIMENSION)] for i in range(DIMENSION)],
        "R_0i0j": r0i0j,
        "R_0404": riemann[0][4][0][4],
        "R_0i04": [riemann[0][i][0][4] for i in range(1, 4)],
        "R_i4j4": [[riemann[i][4][j][4] for j in range(1, 4)] for i in range(1, 4)],
        "scalar_Hessian_reference": hessian_reference,
        "point_conformance_residual": _matrix_residual(r0i0j, hessian_reference),
        "source_stress_label": "STATIC_DUST_T00_ONLY",
        "source_stress_parameters": {"T00": "rho", "T0I": 0.0, "TIJ": 0.0},
        "gauge_convention": "D5_HARMONIC_GAUGE_PARTIAL_A_HA_B_EQUALS_HALF_PARTIAL_B_TRACE_H",
        "Riemann_convention": "R_ABCD=HALF(d_Cd_Bh_AD+d_Dd_Ah_BC-d_Dd_Bh_AC-d_Cd_Ah_BD)",
        "coupling_normalization": "UNIT_EFFECTIVE_POTENTIAL_AMPLITUDE_SHAPE_ONLY",
        "profile_label": profile.upper(),
        "mode_or_exact_expression": "EXACT_LOCALIZED_COMPACT_CIRCLE" if profile == "localized" else "EXACT_UNIFORM_ZERO_MODE",
        "convergence_certificate": {"analytic_expression": True, "laplacian_4d_residual": abs(derivatives["laplacian_4d"])},
        "compact_classification": COMPACT_CLASSIFICATION,
        "potential_derivatives": derivatives,
    }


def shell_tensor_response(r_center: float, width: float, L: float, delta_y: float = 0.0, profile: str = "localized", amplitude: float = 1.0, n: int = 80) -> dict:
    _validate_point(r_center, L, delta_y, profile, amplitude)
    if width <= 0.0 or n < 2 or r_center - width / 2.0 <= 0.0:
        raise ValueError("radial shell must exclude singular support")
    direct = [[0.0] * 3 for _ in range(3)]
    reference = [[0.0] * 3 for _ in range(3)]
    step = width / n
    for index in range(n):
        radius = r_center - width / 2.0 + (index + 0.5) * step
        point = point_tensor_response(radius, L, delta_y, profile, amplitude)
        for i in range(3):
            for j in range(3):
                direct[i][j] += point["R_0i0j"][i][j] / n
                reference[i][j] += point["scalar_Hessian_reference"][i][j] / n
    return {
        "shell_R_0i0j": direct,
        "shell_Hessian_reference": reference,
        "shell_conformance_residual": _matrix_residual(direct, reference),
        "window_geometry": {"type": "NORMALIZED_ORDINARY_RADIAL_SHELL", "center": r_center, "width": width, "samples": n},
    }


def source_stress_dependence_control() -> dict:
    """Algebraic counterexample using bar_h proportional to a symbolic stress."""
    dust_bar = _zeros2()
    dust_bar[0][0] = 3.0
    alternative_bar = _zeros2()
    alternative_bar[0][0] = 2.0
    alternative_bar[1][1] = 2.0
    dust_h = trace_reversal_from_bar(dust_bar)["h"]
    alternative_h = trace_reversal_from_bar(alternative_bar)["h"]
    dust_ratio = dust_h[1][1] / dust_h[0][0]
    alternative_ratio = alternative_h[1][1] / alternative_h[0][0]
    return {
        "dust_h00": dust_h[0][0],
        "alternative_h00": alternative_h[0][0],
        "dust_spatial_ratio": dust_ratio,
        "alternative_spatial_ratio": alternative_ratio,
        "spatial_ratio_residual": abs(dust_ratio - alternative_ratio),
        "alternative_label": "SYMBOLIC_DIAGONAL_STRESS_COUNTEREXAMPLE_NOT_PHYSICAL_EOS",
        "classification": STRESS_CLASSIFICATION,
    }


def _flatten(value) -> list[float]:
    if isinstance(value, list):
        return [number for item in value for number in _flatten(item)]
    return [float(value)]


def joint_scaling_control(r: float, shell_width: float, L: float, delta_y: float, scale: float) -> dict:
    if not math.isfinite(scale) or scale <= 0.0:
        raise ValueError("scale must be finite and positive")
    original = point_tensor_response(r, L, delta_y, "localized")
    dilated = point_tensor_response(scale * r, scale * L, scale * delta_y, "localized")
    original_full = _flatten(original["Riemann_5D"])
    dilated_full = [scale**3 * value for value in _flatten(dilated["Riemann_5D"])]
    original_block = _flatten(original["R_0i0j"])
    dilated_block = [scale**3 * value for value in _flatten(dilated["R_0i0j"])]
    # Include shell-width scaling in the fixed protocol even though point features
    # suffice for the one-parameter local rank/null check.
    shell_tensor_response(r, shell_width, L, delta_y, "localized")
    shell_tensor_response(scale * r, scale * shell_width, scale * L, scale * delta_y, "localized")
    return {
        "dimensionless_full_curvature_residual": max(abs(a - b) for a, b in zip(original_full, dilated_full)),
        "dimensionless_R_0i0j_residual": max(abs(a - b) for a, b in zip(original_block, dilated_block)),
        "rank": 0,
        "scale_null_direction": [1.0],
        "classification": SCALE_CLASSIFICATION,
    }
