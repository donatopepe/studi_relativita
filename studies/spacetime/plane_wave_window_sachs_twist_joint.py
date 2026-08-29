#!/usr/bin/env python3
"""Joint finite-window/non-vertex Sachs controls in an exact plane wave."""
import argparse
import importlib.util
import json
import math
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
OUTPUT = HERE / "plane-wave-window-sachs-twist-joint-results.json"

def load(name, filename):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

window_module = load("plane_wave_joint_common_spectrum_local", "plane_wave_joint_common_spectrum.py")
twist = load("plane_wave_sachs_twist_boundary_local", "plane_wave_sachs_twist_boundary.py")
base, full, optics = twist.base, twist.full, twist.optics


def flatten(matrix):
    return [value for row in matrix for value in row]


def vector_residual(a, b):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


def dimensionless_joint(kfun, length, s0, kernel="top_hat", n=6000):
    propagated = twist.propagate(kfun, length, s0, n)
    return {
        "LW": window_module.dimensionless_window(kfun, length, kernel, n),
        "X": propagated["X"],
        "LV": base.scale(propagated["V"], length),
        "LS": base.scale(propagated["S"], length),
        "LS0": base.scale(s0, length),
        "twist": propagated["twist"],
    }


def joint_flat(record):
    return sum((flatten(record[key]) for key in ("LW", "X", "LV", "LS", "LS0")), [])


def affine_joint_control(kernel="top_hat", n=6000, length=1.1, factor=1.37):
    s0 = twist.boundary_matrix()
    first = dimensionless_joint(base.base_k, length, s0, kernel, n)
    second = dimensionless_joint(twist.scaled_profile(factor), factor * length, base.scale(s0, 1.0 / factor), kernel, n)
    return {
        "kernel": kernel,
        "lengths": [length, factor * length],
        "scale_factor": factor,
        "residuals": {key: optics.norm(full.subtract(first[key], second[key])) for key in ("LW", "X", "LV", "LS", "LS0")},
        "full_joint_residual": vector_residual(joint_flat(first), joint_flat(second)),
    }


def boundary_mobility_control(n=6000):
    length = 1.1
    low = dimensionless_joint(base.base_k, length, twist.boundary_matrix(0.11), "top_hat", n)
    high = dimensionless_joint(base.base_k, length, twist.boundary_matrix(0.31), "top_hat", n)
    sachs_low = sum((flatten(low[key]) for key in ("X", "LV", "LS", "LS0")), [])
    sachs_high = sum((flatten(high[key]) for key in ("X", "LV", "LS", "LS0")), [])
    return {
        "window_residual": optics.norm(full.subtract(low["LW"], high["LW"])),
        "sachs_joint_difference": vector_residual(sachs_low, sachs_high),
        "endpoint_twist_difference": abs(low["twist"] - high["twist"]),
        "profile_difference": 0.0,
    }


def landmark_reparameterization_control(n=6000):
    length, factor = 0.83, 1.61
    result = affine_joint_control("triangular", n, length, factor)
    return {"base_coordinate": length, "scaled_coordinate": factor * length, "scale_factor": factor, "full_joint_residual": result["full_joint_residual"], "interpretation": "JOINT_LANDMARK_COORDINATE_AFFINE_PROFILE_BOUNDARY_MOVABLE_NOT_ELL0"}


def alternate_k(u):
    k = base.base_k(u)
    return [[1.24 * k[0][0], 0.84 * k[0][1]], [0.84 * k[1][0], 1.24 * k[1][1]]]


def profile_sensitivity_control(n=6000):
    length, s0 = 1.1, twist.boundary_matrix()
    first = dimensionless_joint(base.base_k, length, s0, "top_hat", n)
    second = dimensionless_joint(alternate_k, length, s0, "top_hat", n)
    return {
        "window_difference": optics.norm(full.subtract(first["LW"], second["LW"])),
        "sachs_difference": vector_residual(sum((flatten(first[key]) for key in ("X", "LV", "LS")), []), sum((flatten(second[key]) for key in ("X", "LV", "LS")), [])),
        "interpretation": "JOINT_OBJECT_PROFILE_INFORMATIVE_CONDITIONALLY_AT_FIXED_BOUNDARY",
    }


def ell0_gate(symbols):
    return "WINDOW_SACHS_TWIST_JOINT_AFFINE_AND_BOUNDARY_NOT_ELL0" if "ell0" not in symbols else "ELL0_SYMBOL_PRESENT_REQUIRES_DERIVATION"


def build_artifact():
    return {
        "classification": "EXACT_SPACETIME_CROSS_CHANNEL_SACHS_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT",
        "status": "EXACT_PLANE_WAVE_WINDOW_SACHS_TWIST_JOINT_PROFILE_AND_BOUNDARY_CONDITIONAL_AFFINE_ORBIT_NOT_ELL0",
        "open_gate": "PHYSICAL_CAUSAL_WINDOW_ROTATING_BOUNDARY_COMMON_SCREEN_AND_ELL0_LAW_NOT_DERIVED",
        "primary_object": "raw_dimensionless_LW_X_LV_LS_LS0",
        "top_hat_affine_joint": affine_joint_control("top_hat"),
        "triangular_affine_joint": affine_joint_control("triangular"),
        "boundary_mobility": boundary_mobility_control(),
        "landmark_reparameterization": landmark_reparameterization_control(),
        "profile_sensitivity": profile_sensitivity_control(),
        "ell0_gate": ell0_gate(["W", "X", "V", "S", "S0", "K", "L"]),
        "structural_dead_end": False,
        "umch_status": "UNPROVEN",
        "conclusion": "NO_POSITIVE_DETECTION_CLAIM",
    }


def render():
    return json.dumps(build_artifact(), indent=2, sort_keys=True) + "\n"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    text = render()
    if args.check:
        if not OUTPUT.exists() or OUTPUT.read_text() != text:
            print("Plane-wave window/Sachs-twist joint artifact is stale.", file=sys.stderr)
            return 1
        print("Plane-wave window/Sachs-twist joint artifact is current.")
        return 0
    OUTPUT.write_text(text)
    print(OUTPUT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
