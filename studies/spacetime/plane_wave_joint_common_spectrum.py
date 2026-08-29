#!/usr/bin/env python3
"""Joint finite-window/full-map affine scale orbit in an exact plane wave."""
import argparse
import importlib.util
import json
import math
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
OUTPUT = HERE / "plane-wave-joint-common-spectrum-results.json"
_spec = importlib.util.spec_from_file_location("plane_wave_common_spectrum_local", HERE / "plane_wave_common_spectrum.py")
spectrum = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(spectrum)
canonical, full, base = spectrum.canonical, spectrum.full, spectrum.base


def matrix_difference(a, b):
    return full.norm(full.subtract(a, b))


def kernel_weight(x, length, kernel):
    if kernel == "top_hat":
        return 1.0
    if kernel == "triangular":
        return max(0.0, 1.0 - 2.0 * abs(x) / length)
    raise ValueError(kernel)


def window(kfun, length, kernel="top_hat", n=5000):
    step = length / n
    out = base.zero()
    for index in range(n + 1):
        x = -length / 2.0 + index * step
        endpoint = 0.5 if index in (0, n) else 1.0
        out = base.add(out, base.scale(kfun(x), endpoint * kernel_weight(x, length, kernel) * step))
    return out


def scaled_profile(kfun, factor):
    return lambda u: base.scale(kfun(u / factor), 1.0 / factor ** 2)


def dimensionless_window(kfun, length, kernel, n):
    return base.scale(window(kfun, length, kernel, n), length)


def joint_vector(kfun, length, kernel, n):
    w = dimensionless_window(kfun, length, kernel, n)
    coefficients = spectrum.characteristic_coefficients(full.full_map(kfun, length, n))
    return [value for row in w for value in row] + coefficients


def joint_scale_orbit_control(kernel="top_hat", n=5000, length=0.9, factor=1.37):
    first = full.full_map(base.base_k, length, n)
    dilated = scaled_profile(base.base_k, factor)
    second = full.full_map(dilated, factor * length, n)
    transform = spectrum.diagonal4(1.0 / math.sqrt(factor), math.sqrt(factor))
    predicted = base.mm(base.mm(canonical.inverse4(transform), first), transform)
    first_window = dimensionless_window(base.base_k, length, kernel, n)
    second_window = dimensionless_window(dilated, factor * length, kernel, n)
    return {
        "kernel": kernel,
        "lengths": [length, factor * length],
        "scale_factor": factor,
        "dimensionless_windows": [first_window, second_window],
        "dimensionless_window_residual": matrix_difference(first_window, second_window),
        "characteristic_residual": spectrum.vector_residual(spectrum.characteristic_coefficients(first), spectrum.characteristic_coefficients(second)),
        "canonical_similarity_residual": matrix_difference(second, predicted),
        "canonical_scaling_residual": canonical.symplectic_residual(transform),
    }


def block_scaling_control(n=5000, length=0.9, factor=1.37):
    first = full.full_blocks(base.base_k, length, n)
    second = full.full_blocks(scaled_profile(base.base_k, factor), factor * length, n)
    return {
        "scale_factor": factor,
        "residuals": {
            "A": matrix_difference(second["A"], first["A"]),
            "B": matrix_difference(second["B"], base.scale(first["B"], factor)),
            "C": matrix_difference(second["C"], base.scale(first["C"], 1.0 / factor)),
            "D": matrix_difference(second["D"], first["D"]),
        },
    }


def profile_sensitivity_control(n=5000, length=0.9):
    first_window = dimensionless_window(base.base_k, length, "top_hat", n)
    second_window = dimensionless_window(canonical.second_k, length, "top_hat", n)
    first_map = full.full_map(base.base_k, length, n)
    second_map = full.full_map(canonical.second_k, length, n)
    return {
        "window_difference": matrix_difference(first_window, second_window),
        "characteristic_difference": spectrum.vector_residual(spectrum.characteristic_coefficients(first_map), spectrum.characteristic_coefficients(second_map)),
        "interpretation": "JOINT_OBJECT_PROFILE_INFORMATIVE_CONDITIONALLY",
    }


def landmark_reparameterization_control(n=5000, coordinate=0.83, factor=1.61):
    dilated = scaled_profile(base.base_k, factor)
    first = joint_vector(base.base_k, coordinate, "triangular", n)
    second = joint_vector(dilated, factor * coordinate, "triangular", n)
    return {
        "base_coordinate": coordinate,
        "scaled_coordinate": factor * coordinate,
        "scale_factor": factor,
        "joint_residual": spectrum.vector_residual(first, second),
        "interpretation": "JOINT_LANDMARK_COORDINATE_PROFILE_SCALE_MOVABLE_NOT_ELL0",
    }


def ell0_gate(symbols):
    return "JOINT_AFFINE_PROFILE_ORBIT_NOT_ELL0" if "ell0" not in symbols else "ELL0_REQUIRES_DERIVED_PROFILE_SCALE_LAW"


def build_artifact():
    return {
        "study_id": "plane-wave-joint-common-spectrum-v1",
        "classification": "EXACT_SPACETIME_CROSS_CHANNEL_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT",
        "status": "EXACT_PLANE_WAVE_WINDOW_FULL_MAP_COMMON_SPECTRUM_JOINT_AFFINE_ORBIT_NOT_ELL0",
        "open_gate": "PHYSICAL_PROFILE_SCALE_LAW_CAUSAL_WINDOW_AND_COMMON_STANDARD_NOT_DERIVED",
        "top_hat_orbit": joint_scale_orbit_control("top_hat"),
        "triangular_orbit": joint_scale_orbit_control("triangular"),
        "block_scaling": block_scaling_control(),
        "profile_sensitivity": profile_sensitivity_control(),
        "landmark_reparameterization": landmark_reparameterization_control(),
        "ell0_gate": ell0_gate(["W", "P", "K", "L", "G", "w"]),
        "source_scope": "Coley-McNutt-Milson 2012 supports exact vacuum plane waves and geodesic deviation, not this window, kernel, calibration group, profile-scale nuisance, UMCH, ell0, or detection.",
        "structural_dead_end": False,
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
            print("Plane-wave joint common-spectrum artifact differs", file=sys.stderr)
            return 1
        print("Plane-wave joint common-spectrum artifact is current.")
        return 0
    OUTPUT.write_text(text)
    print(f"Wrote {OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
