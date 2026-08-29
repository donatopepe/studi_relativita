#!/usr/bin/env python3
"""Joint endpoint-frame quotient controls for one exact plane-wave profile."""

import argparse
import importlib.util
import json
import math
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
OUTPUT = HERE / "plane-wave-joint-quotient-results.json"
CROSS_CHANNEL_PROGRAM = HERE / "plane_wave_cross_channel.py"


def load_cross_channel():
    spec = importlib.util.spec_from_file_location("plane_wave_cross_channel", CROSS_CHANNEL_PROGRAM)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


BASE = load_cross_channel()


def transpose(matrix):
    return [list(row) for row in zip(*matrix)]


def matrix_difference(left, right):
    return BASE.add(left, right, -1.0)


def symmetric_eigenvalues(matrix):
    trace = matrix[0][0] + matrix[1][1]
    discriminant = math.sqrt(
        max(0.0, (matrix[0][0] - matrix[1][1]) ** 2 + 4.0 * matrix[0][1] ** 2)
    )
    return sorted(((trace - discriminant) / 2.0, (trace + discriminant) / 2.0))


def singular_values(matrix):
    gram = BASE.mm(transpose(matrix), matrix)
    return [math.sqrt(max(0.0, value)) for value in symmetric_eigenvalues(gram)]


def vector_residual(left, right):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(left, right)))


def determinant(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def reversal_control(n=6000):
    length = 1.1
    reverse_profile = lambda u: BASE.base_k(-u)
    window_forward, jacobi_forward = BASE.channels(length, BASE.base_k, n)
    window_reverse, jacobi_reverse = BASE.channels(length, reverse_profile, n)
    return {
        "affine_length": length,
        "window_reversal_residual": BASE.norm(matrix_difference(window_forward, window_reverse)),
        "jacobi_transpose_residual": BASE.norm(
            matrix_difference(jacobi_reverse, transpose(jacobi_forward))
        ),
        "raw_jacobi_reversal_residual": BASE.norm(
            matrix_difference(jacobi_forward, jacobi_reverse)
        ),
        "window_eigenvalue_residual": vector_residual(
            symmetric_eigenvalues(window_forward), symmetric_eigenvalues(window_reverse)
        ),
        "jacobi_singular_value_residual": vector_residual(
            singular_values(jacobi_forward), singular_values(jacobi_reverse)
        ),
        "jacobi_determinant_residual": abs(
            determinant(jacobi_forward) - determinant(jacobi_reverse)
        ),
        "jacobi_frobenius_residual": abs(
            BASE.norm(jacobi_forward) - BASE.norm(jacobi_reverse)
        ),
    }


def affine_rescaling_control(length_one=0.8, length_two=1.3, n=6000):
    factor = length_two / length_one
    rescaled_profile = lambda u: BASE.scale(BASE.base_k(u / factor), 1.0 / factor**2)
    window_one, jacobi_one = BASE.channels(length_one, BASE.base_k, n)
    window_two, jacobi_two = BASE.channels(length_two, rescaled_profile, n)
    dimensionless_window_one = BASE.scale(window_one, length_one)
    dimensionless_window_two = BASE.scale(window_two, length_two)
    dimensionless_jacobi_one = BASE.scale(jacobi_one, 1.0 / length_one)
    dimensionless_jacobi_two = BASE.scale(jacobi_two, 1.0 / length_two)
    return {
        "length_one": length_one,
        "length_two": length_two,
        "rescaling_factor": factor,
        "dimensionless_window_spectrum_residual": vector_residual(
            symmetric_eigenvalues(dimensionless_window_one),
            symmetric_eigenvalues(dimensionless_window_two),
        ),
        "dimensionless_jacobi_singular_value_residual": vector_residual(
            singular_values(dimensionless_jacobi_one),
            singular_values(dimensionless_jacobi_two),
        ),
    }


def ell0_gate(symbols):
    if "ell0" in symbols:
        return "ELL0_REQUIRES_INDEPENDENT_PHYSICAL_LAW"
    return "JOINT_QUOTIENT_PROFILE_ORDER_AND_ABSOLUTE_SCALE_NOT_ELL0"


def evaluate():
    return {
        "study_id": "exact-plane-wave-joint-quotient-v1",
        "geometry": "SAME_EXACT_VACUUM_PLANE_WAVE_PROFILE_CENTERED_AFFINE_INTERVAL_PARALLEL_SCREEN",
        "reversal_control": reversal_control(),
        "affine_rescaling_control": affine_rescaling_control(),
        "quotient": "EIGENVALUES_OF_SYMMETRIC_W_AND_SINGULAR_VALUES_DETERMINANT_FROBENIUS_OF_B",
        "quotient_gate": "RAW_JACOBI_ORDER_DIFFERENCE_REMOVED_BY_INDEPENDENT_ENDPOINT_FRAME_QUOTIENT",
        "ell0_gate": ell0_gate(["L", "K", "W", "B", "endpoint_frames", "affine_scale"]),
        "status": "EXACT_PLANE_WAVE_JOINT_QUOTIENT_REVERSAL_AND_AFFINE_SCALE_NONIDENTIFIABLE_NOT_ELL0",
        "classification": "EXACT_SPACETIME_CROSS_CHANNEL_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT",
        "open_route": "COMMON_ENDPOINT_ANCHOR_REMAINS_OPEN",
        "conclusion": "NO_POSITIVE_DETECTION_CLAIM",
        "limitation": "Minimal individual endpoint-frame quotient only; no physical common anchor, detector calibration, universal-scale law, data, or mechanism.",
    }


def render():
    return json.dumps(evaluate(), indent=2, sort_keys=True) + "\n"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    content = render()
    if args.check:
        if not OUTPUT.exists() or OUTPUT.read_text() != content:
            print("Plane-wave joint quotient artifact differs", file=sys.stderr)
            return 1
        print("Plane-wave joint quotient artifact is current.")
        return 0
    OUTPUT.write_text(content)
    print(f"Wrote {OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
