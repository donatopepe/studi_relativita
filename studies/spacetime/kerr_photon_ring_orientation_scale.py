#!/usr/bin/env python3
"""Exact equatorial Kerr photon-ring orientation and scale toy control.

Boyer-Lindquist orbit records are mathematical coordinate controls, not a
transported screen, detector clock, evidence, detection, or ell0 measurement.
"""

from __future__ import annotations

import json
import math
import sys

RESULT = "KERR_FRAME_DRAGGING_ADDS_PROGRADE_RETROGRADE_DIMENSIONLESS_ORBIT_SHAPE_BUT_JOINT_MA_DILATION_RETAINS_ABSOLUTE_SCALE_BLINDNESS_NOT_ELL0"
PHYSICAL_GATE = "PHYSICAL_KERR_SOURCE_ABSORBER_ENDPOINT_TETRAD_SCREEN_TRANSPORT_AFFINE_FREQUENCY_CLOCK_RECEIVER_NOISE_JOINT_COVARIANCE_DATA_AND_ELL0_LAW_NOT_DERIVED"
SCHWARZSCHILD_COLLISION = "KERR_PROGRADE_RETROGRADE_BRANCHES_COLLIDE_IN_SCHWARZSCHILD_LIMIT"
CONVENTION_COLLISION = "SIMULTANEOUS_SPIN_ORIENTATION_REVERSAL_IS_CONVENTION_COLLISION_NOT_ELL0"
DILATION = "JOINT_MA_GEOMETRIC_DILATION_NOT_INTERIOR_SCALE"


def _validate(M: float, chi: float) -> None:
    if not math.isfinite(M) or M <= 0.0:
        raise ValueError("M must be finite and positive")
    if not math.isfinite(chi) or chi < 0.0 or chi >= 1.0:
        raise ValueError("chi must be finite and subextremal in [0,1)")


def photon_radius_ratio(chi: float, branch: str) -> float:
    _validate(1.0, chi)
    if branch not in {"prograde", "retrograde"}:
        raise ValueError("branch must be prograde or retrograde")
    argument = -chi if branch == "prograde" else chi
    return 2.0 * (1.0 + math.cos((2.0 / 3.0) * math.acos(argument)))


def impact_parameter_ratio(chi: float, branch: str, x_ph: float | None = None) -> float:
    if branch not in {"prograde", "retrograde"}:
        raise ValueError("branch must be prograde or retrograde")
    x = photon_radius_ratio(chi, branch) if x_ph is None else x_ph
    orientation = 1.0 if branch == "prograde" else -1.0
    if chi == 0.0:
        return orientation * 3.0 * math.sqrt(3.0)
    return (x * x * (x - 3.0) + chi * chi * (x + 1.0)) / (chi * (1.0 - x))


def radial_potential(r: float, M: float, a: float, xi: float) -> float:
    delta = r * r - 2.0 * M * r + a * a
    return (r * r + a * a - a * xi) ** 2 - delta * (xi - a) ** 2


def radial_potential_prime(r: float, M: float, a: float, xi: float) -> float:
    first = r * r + a * a - a * xi
    delta_prime = 2.0 * r - 2.0 * M
    return 4.0 * r * first - delta_prime * (xi - a) ** 2


def _equatorial_metric(M: float, a: float, r: float) -> tuple[float, float, float]:
    g_tt = -(1.0 - 2.0 * M / r)
    g_tphi = -2.0 * M * a / r
    g_phiphi = r * r + a * a + 2.0 * M * a * a / r
    return g_tt, g_tphi, g_phiphi


def orbit_record(M: float, chi: float, branch: str) -> dict:
    _validate(M, chi)
    x = photon_radius_ratio(chi, branch)
    orientation = 1.0 if branch == "prograde" else -1.0
    a = chi * M
    r = x * M
    xi_ratio = impact_parameter_ratio(chi, branch, x)
    xi = xi_ratio * M
    omega_M = orientation / (x ** 1.5 + orientation * chi)
    omega = omega_M / M
    period_over_M = 2.0 * math.pi / abs(omega_M)
    g_tt, g_tphi, g_phiphi = _equatorial_metric(M, a, r)
    null_residual = g_tt + 2.0 * g_tphi * omega + g_phiphi * omega * omega
    scale = M**4
    return {
        "branch": branch,
        "relative_orientation": int(orientation),
        "azimuthal_orientation": int(orientation),
        "chi": chi,
        "x_ph": x,
        "r_ph": r,
        "xi_over_M": xi_ratio,
        "Omega_phi_M": omega_M,
        "Omega_phi": omega,
        "Delta_t_per_2pi_over_M": period_over_M,
        "Delta_t_per_2pi": period_over_M * M,
        "R_residual": radial_potential(r, M, a, xi) / scale,
        "R_prime_residual": radial_potential_prime(r, M, a, xi) / M**3,
        "null_angular_rate_residual": null_residual,
        "timing_classification": "BOYER_LINDQUIST_COORDINATE_PERIOD_NOT_PHYSICAL_CLOCK",
        "collision_classification": SCHWARZSCHILD_COLLISION if chi == 0.0 else "KERR_BRANCHES_DISTINCT_AT_NONZERO_SPIN",
    }


def signed_convention_record(M: float, chi: float, spin_sign: int, azimuthal_orientation: int) -> dict:
    _validate(M, chi)
    if spin_sign not in {-1, 1} or azimuthal_orientation not in {-1, 1}:
        raise ValueError("spin_sign and azimuthal_orientation must be +/-1")
    relative = spin_sign * azimuthal_orientation
    branch = "prograde" if relative == 1 else "retrograde"
    orbit = orbit_record(M, chi, branch)
    signed_omega_M = azimuthal_orientation * abs(orbit["Omega_phi_M"])
    return {
        "spin_sign": spin_sign,
        "azimuthal_orientation": azimuthal_orientation,
        "relative_orientation": relative,
        "branch": branch,
        "x_ph": orbit["x_ph"],
        "Omega_phi_M": signed_omega_M,
        "unsigned_period_over_M": 2.0 * math.pi / abs(signed_omega_M),
        "classification": CONVENTION_COLLISION,
    }


def _dimensionless_features(M: float, chi: float) -> list[float]:
    pro = orbit_record(M, chi, "prograde")
    retro = orbit_record(M, chi, "retrograde")
    return [
        pro["x_ph"], retro["x_ph"], pro["xi_over_M"], retro["xi_over_M"],
        pro["Omega_phi_M"], retro["Omega_phi_M"],
        pro["Delta_t_per_2pi_over_M"], retro["Delta_t_per_2pi_over_M"],
    ]


def joint_dilation_control(M: float, chi: float, scale: float) -> dict:
    _validate(M, chi)
    if not math.isfinite(scale) or scale <= 0.0:
        raise ValueError("scale must be finite and positive")
    base_features = _dimensionless_features(M, chi)
    scaled_features = _dimensionless_features(scale * M, chi)
    dimensionless_residual = max(abs(a - b) for a, b in zip(base_features, scaled_features))
    covariance_residual = 0.0
    scale_orbit = []
    for branch in ("prograde", "retrograde"):
        original = orbit_record(M, chi, branch)
        dilated = orbit_record(scale * M, chi, branch)
        branch_residual = max(
            abs(dilated["r_ph"] - scale * original["r_ph"]),
            abs(dilated["Delta_t_per_2pi"] - scale * original["Delta_t_per_2pi"]),
            abs(dilated["Omega_phi"] - original["Omega_phi"] / scale),
        )
        covariance_residual = max(covariance_residual, branch_residual)
        scale_orbit.append({"branch": branch, "r_ratio": dilated["r_ph"] / original["r_ph"], "period_ratio": dilated["Delta_t_per_2pi"] / original["Delta_t_per_2pi"]})
    return {
        "scale_factor": scale,
        "dimensionless_residual": dimensionless_residual,
        "dimensional_covariance_residual": covariance_residual,
        "scale_orbit": scale_orbit,
        "classification": DILATION,
    }


def rank_control(chi: float = 0.6, h: float = 1e-5) -> dict:
    if chi - h <= 0.0 or chi + h >= 1.0:
        raise ValueError("chi rank anchor must be interior")
    log_M = 0.0
    features = lambda lm, spin: _dimensionless_features(math.exp(lm), spin)
    plus_M, minus_M = features(log_M + h, chi), features(log_M - h, chi)
    plus_chi, minus_chi = features(log_M, chi + h), features(log_M, chi - h)
    log_column = [(a - b) / (2.0 * h) for a, b in zip(plus_M, minus_M)]
    chi_column = [(a - b) / (2.0 * h) for a, b in zip(plus_chi, minus_chi)]
    log_norm = math.sqrt(sum(value * value for value in log_column))
    chi_norm = math.sqrt(sum(value * value for value in chi_column))
    return {
        "parameters": ["log_M", "chi"],
        "feature_Jacobian": [[log_column[index], chi_column[index]] for index in range(len(log_column))],
        "log_M_column_norm": log_norm,
        "chi_column_norm": chi_norm,
        "rank": int(log_norm > 1e-10) + int(chi_norm > 1e-10),
        "scale_null_direction": [1.0, 0.0],
        "classification": "DIMENSIONLESS_KERR_ORBIT_MAP_HAS_SPIN_SHAPE_RANK_AND_EXACT_SCALE_NULL",
    }


def no_ell0_gate() -> dict:
    return {
        "M_identified_internally": False,
        "a_identified_internally": False,
        "L_identified": False,
        "ell0_identified": False,
        "L_equals_ell0": "NOT_DERIVED",
        "extra_dimension_detected": False,
        "structural_dead_end": "NOT_DECLARED",
        "Detection": "NO_POSITIVE_DETECTION_CLAIM",
        "result": RESULT,
        "physical_gate": PHYSICAL_GATE,
    }


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
    chis = [0.0, 0.2, 0.6, 0.9, 0.99]
    records = [{"chi": chi, "branches": [orbit_record(1.0, chi, branch) for branch in ("prograde", "retrograde")]} for chi in chis]
    radial_residual = max(max(abs(branch[key]) for item in records for branch in item["branches"]) for key in ("R_residual", "R_prime_residual", "null_angular_rate_residual"))
    minimum_order_gap = min(item["branches"][1]["x_ph"] - item["branches"][0]["x_ph"] for item in records if item["chi"] > 0.0)
    schwarzschild_residual = max(abs(records[0]["branches"][index]["x_ph"] - 3.0) for index in (0, 1))
    signed_forward = signed_convention_record(1.0, 0.6, 1, 1)
    signed_reversed = signed_convention_record(1.0, 0.6, -1, -1)
    convention_residual = max(abs(signed_forward["x_ph"] - signed_reversed["x_ph"]), abs(signed_forward["unsigned_period_over_M"] - signed_reversed["unsigned_period_over_M"]), abs(signed_forward["Omega_phi_M"] + signed_reversed["Omega_phi_M"]))
    dilation = joint_dilation_control(1.3, 0.6, 2.5)
    rank = rank_control(0.6)
    gate = no_ell0_gate()
    controls = [
        {"name": "radius_formula_range", "passed": all(1.0 <= item["branches"][0]["x_ph"] <= 3.0 <= item["branches"][1]["x_ph"] <= 4.0 for item in records), "residual": 0.0, "threshold": 1e-12},
        {"name": "branch_ordering", "passed": minimum_order_gap > 1e-8, "residual": minimum_order_gap, "threshold": 1e-8, "threshold_kind": "minimum_gap"},
        {"name": "Schwarzschild_collision", "passed": schwarzschild_residual < 1e-12, "residual": schwarzschild_residual, "threshold": 1e-12},
        {"name": "radial_potential_conformance", "passed": radial_residual < 1e-10, "residual": radial_residual, "threshold": 1e-10},
        {"name": "signed_convention_collision", "passed": convention_residual < 1e-10, "residual": convention_residual, "threshold": 1e-10},
        {"name": "joint_geometric_dilation", "passed": max(dilation["dimensionless_residual"], dilation["dimensional_covariance_residual"]) < 1e-10, "residual": max(dilation["dimensionless_residual"], dilation["dimensional_covariance_residual"]), "threshold": 1e-10},
        {"name": "rank_scale_null", "passed": rank["rank"] == 1 and rank["log_M_column_norm"] < 1e-10 and rank["chi_column_norm"] > 1e-3, "residual": rank["log_M_column_norm"], "threshold": 1e-10},
        {"name": "no_ell0_identification", "passed": not gate["ell0_identified"] and gate["L_equals_ell0"] == "NOT_DERIVED", "residual": 0.0, "threshold": 1.0, "threshold_kind": "boolean_gate"},
    ]
    return _canonical({
        "study_id": "kerr-equatorial-photon-ring-orientation-scale-v1",
        "baseline": {"M": 1.0, "chi_samples": chis, "rank_anchor_chi": 0.6, "scale_factor": 2.5},
        "branch_records": records,
        "signed_convention_control": {"forward": signed_forward, "simultaneous_reversal": signed_reversed, "residual": convention_residual, "classification": CONVENTION_COLLISION},
        "joint_dilation_control": dilation,
        "rank_control": rank,
        "control_summary": {"controls": controls, "controls_passed": sum(control["passed"] for control in controls), "controls_total": len(controls), **{key: gate[key] for key in ("L_identified", "ell0_identified", "L_equals_ell0", "extra_dimension_detected", "structural_dead_end", "Detection")}, "Maximum_interpretation": "MODEL_LEVEL_KERR_ORBIT_CONFORMANCE_NOT_EVIDENCE"},
        "result": RESULT,
        "physical_gate": PHYSICAL_GATE,
        "review": "DIRECT_REVIEW_NO_SUBAGENT",
    })


def main() -> int:
    json.dump(build_artifact(), sys.stdout, indent=2, sort_keys=True)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
