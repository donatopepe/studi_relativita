#!/usr/bin/env python3
"""Common canonical similarity invariants for exact plane-wave Jacobi maps."""
import argparse
import importlib.util
import json
import math
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
OUTPUT = HERE / "plane-wave-common-spectrum-results.json"
_spec = importlib.util.spec_from_file_location("plane_wave_canonical_reduction_local", HERE / "plane_wave_canonical_reduction.py")
canonical = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(canonical)
full = canonical.full
base = full.base


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def determinant(a):
    work = [row[:] for row in a]
    result = 1.0
    for col in range(len(work)):
        pivot = max(range(col, len(work)), key=lambda row: abs(work[row][col]))
        if abs(work[pivot][col]) < 1e-15:
            return 0.0
        if pivot != col:
            work[col], work[pivot] = work[pivot], work[col]
            result *= -1.0
        value = work[col][col]
        result *= value
        for row in range(col + 1, len(work)):
            factor = work[row][col] / value
            for j in range(col + 1, len(work)):
                work[row][j] -= factor * work[col][j]
    return result


def characteristic_coefficients(a):
    a2 = base.mm(a, a)
    a3 = base.mm(a2, a)
    t1, t2, t3 = trace(a), trace(a2), trace(a3)
    return [
        1.0,
        -t1,
        (t1 * t1 - t2) / 2.0,
        -(t1 ** 3 - 3.0 * t1 * t2 + 2.0 * t3) / 6.0,
        determinant(a),
    ]


def vector_residual(a, b):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


def diagonal4(first, second):
    return full.assemble(base.scale(base.eye(), first), base.zero(), base.zero(), base.scale(base.eye(), second))


def symplectic_characteristic_control(n=6000):
    coefficients = characteristic_coefficients(full.full_map(n=n))
    return {
        "coefficients": coefficients,
        "determinant_residual": abs(coefficients[4] - 1.0),
        "palindromic_residual": abs(coefficients[3] - coefficients[1]),
    }


def common_conjugation_control(n=6000):
    p = full.full_map(n=n)
    h = [[0.31, -0.17], [-0.17, -0.08]]
    g = full.assemble(base.eye(), base.zero(), h, base.eye())
    transformed = base.mm(base.mm(g, p), canonical.inverse4(g))
    return {
        "raw_map_difference": full.norm(full.subtract(p, transformed)),
        "characteristic_residual": vector_residual(characteristic_coefficients(p), characteristic_coefficients(transformed)),
        "calibration_symplectic_residual": canonical.symplectic_residual(g),
    }


def reversal_spectrum_control(n=6000):
    forward = full.full_map(n=n)
    reverse = full.full_map(lambda u: base.base_k(-u), n=n)
    return {
        "raw_map_difference": full.norm(full.subtract(forward, reverse)),
        "characteristic_residual": vector_residual(characteristic_coefficients(forward), characteristic_coefficients(reverse)),
    }


def affine_similarity_control(n=6000):
    length, factor = 0.8, 1.3
    first = full.full_map(length=length, n=n)
    scaled_k = lambda u: base.scale(base.base_k(u / factor), 1.0 / factor ** 2)
    second = full.full_map(scaled_k, length * factor, n=n)
    transform = diagonal4(1.0 / math.sqrt(factor), math.sqrt(factor))
    predicted = base.mm(base.mm(canonical.inverse4(transform), first), transform)
    return {
        "similarity_residual": full.norm(full.subtract(second, predicted)),
        "characteristic_residual": vector_residual(characteristic_coefficients(first), characteristic_coefficients(second)),
        "canonical_scaling_residual": canonical.symplectic_residual(transform),
    }


def profile_sensitivity_control(n=6000):
    first, second = canonical.profile_maps(n)
    difference = vector_residual(characteristic_coefficients(first), characteristic_coefficients(second))
    return {
        "first_coefficients": characteristic_coefficients(first),
        "second_coefficients": characteristic_coefficients(second),
        "characteristic_difference": difference,
        "interpretation": "PROFILE_GEOMETRY_CONDITIONAL_NOT_ABSOLUTE_SCALE",
    }


def ell0_gate(symbols):
    return "COMMON_CANONICAL_SPECTRUM_AFFINE_SCALE_NOT_ELL0" if "ell0" not in symbols else "ELL0_REQUIRES_DERIVED_PROFILE_SCALE_LAW"


def build_artifact():
    return {
        "study_id": "plane-wave-common-spectrum-v1",
        "classification": "EXACT_SPACETIME_CROSS_CHANNEL_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT",
        "status": "EXACT_PLANE_WAVE_COMMON_CANONICAL_SPECTRUM_PROFILE_INFORMATIVE_REVERSAL_AND_AFFINE_SCALE_BLIND_NOT_ELL0",
        "open_gate": "PHYSICAL_COMMON_CANONICAL_STANDARD_AND_ELL0_LAW_NOT_DERIVED",
        "symplectic_characteristic": symplectic_characteristic_control(),
        "common_conjugation": common_conjugation_control(),
        "reversal_spectrum": reversal_spectrum_control(),
        "affine_similarity": affine_similarity_control(),
        "profile_sensitivity": profile_sensitivity_control(),
        "ell0_gate": ell0_gate(["P", "K", "L", "G"]),
        "structural_dead_end": False,
        "conclusion": "NO_POSITIVE_DETECTION_CLAIM",
        "limitation": "Common canonical standard and finite-window spectral observable are project contracts; no physical detector calibration, ell0 law, or data are derived.",
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
            print("Plane-wave common-spectrum artifact differs", file=sys.stderr)
            return 1
        print("Plane-wave common-spectrum artifact is current.")
        return 0
    OUTPUT.write_text(text)
    print(f"Wrote {OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
