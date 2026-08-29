#!/usr/bin/env python3
"""Connection-derived Sachs optical controls in an exact plane wave."""
import argparse
import importlib.util
import json
import math
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
OUTPUT = HERE / "plane-wave-sachs-optics-results.json"
_spec = importlib.util.spec_from_file_location("plane_wave_full_jacobi_local", HERE / "plane_wave_full_jacobi.py")
full = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(full)
base = full.base


def add(a, b):
    return [[a[i][j] + b[i][j] for j in range(2)] for i in range(2)]


def multiply(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def transpose(a):
    return full.transpose(a)


def norm(a):
    return full.norm(a)


def determinant(a):
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def optical_matrix(b, d, tolerance=1e-12):
    if abs(determinant(b)) <= tolerance:
        return {"status": "CAUSTIC_OR_VERTEX_BLOCK_SINGULAR"}
    return {"status": "REGULAR", "matrix": multiply(d, full.inverse2(b))}


def decompose(s):
    expansion = 0.5 * (s[0][0] + s[1][1])
    twist = 0.5 * (s[1][0] - s[0][1])
    symmetric = [[s[0][0], 0.5 * (s[0][1] + s[1][0])], [0.5 * (s[0][1] + s[1][0]), s[1][1]]]
    shear = [[symmetric[0][0] - expansion, symmetric[0][1]], [symmetric[1][0], symmetric[1][1] - expansion]]
    return {"expansion": expansion, "shear": shear, "shear_norm": norm(shear), "twist": twist}


def endpoint(length=1.1, kfun=base.base_k, n=6000):
    blocks = full.full_blocks(kfun, length, n)
    optical = optical_matrix(blocks["B"], blocks["D"])
    if optical["status"] != "REGULAR":
        return {"blocks": blocks, **optical}
    return {"blocks": blocks, **optical, **decompose(optical["matrix"])}


def optical_decomposition_control(n=6000):
    result = endpoint(n=n)
    return {
        "matrix": result["matrix"],
        "expansion": result["expansion"],
        "shear": result["shear"],
        "shear_norm": result["shear_norm"],
        "twist": result["twist"],
        "minimum_abs_det_b": abs(determinant(result["blocks"]["B"])),
    }


def riccati_control(n=5000):
    length = 1.1
    start = -length / 2.0
    step = length / n
    b, d = base.zero(), base.eye()
    previous = None
    u = start
    residual = math.inf
    for index in range(n):
        b, d = base.rk4_pair(u, b, d, step, base.base_k)
        u += step
        current = optical_matrix(b, d)
        if previous is not None and index == n - 1:
            derivative = base.scale(full.subtract(current["matrix"], previous), 1.0 / step)
            midpoint_s = base.scale(add(current["matrix"], previous), 0.5)
            rhs = base.scale(add(base.base_k(u - step / 2.0), multiply(midpoint_s, midpoint_s)), -1.0)
            residual = norm(full.subtract(derivative, rhs))
        previous = current["matrix"]
    return {"residual": residual, "equation": "S_prime=-K-S_squared"}


def rotation(angle=0.47):
    return [[math.cos(angle), -math.sin(angle)], [math.sin(angle), math.cos(angle)]]


def rotation_control(n=6000):
    result = endpoint(n=n)
    q = rotation()
    rotated_blocks = {key: multiply(multiply(q, value), transpose(q)) for key, value in result["blocks"].items()}
    rotated = optical_matrix(rotated_blocks["B"], rotated_blocks["D"])["matrix"]
    expected = multiply(multiply(q, result["matrix"]), transpose(q))
    pieces = decompose(rotated)
    return {
        "matrix_action_residual": norm(full.subtract(rotated, expected)),
        "expansion_residual": abs(pieces["expansion"] - result["expansion"]),
        "shear_norm_residual": abs(pieces["shear_norm"] - result["shear_norm"]),
        "twist_residual": abs(pieces["twist"] - result["twist"]),
    }


def calibration_mobility_control(n=6000):
    result = endpoint(n=n)
    h = [[0.16, 0.07], [0.07, -0.04]]
    b = result["blocks"]["B"]
    d_prime = add(result["blocks"]["D"], multiply(h, b))
    shifted = optical_matrix(b, d_prime)["matrix"]
    expected = add(result["matrix"], h)
    pieces = decompose(shifted)
    return {
        "H_observer": h,
        "additive_action_residual": norm(full.subtract(shifted, expected)),
        "expansion_shift": abs(pieces["expansion"] - result["expansion"]),
        "shear_norm_shift": abs(pieces["shear_norm"] - result["shear_norm"]),
        "twist_shift": abs(pieces["twist"] - result["twist"]),
    }


def caustic_guard_control():
    return optical_matrix(base.zero(), base.eye())


def reversal_exchange_control(n=6000):
    blocks = endpoint(n=n)["blocks"]
    source_labelled = transpose(multiply(full.inverse2(blocks["B"]), blocks["A"]))
    reversed_blocks = full.full_blocks(lambda u: base.base_k(-u), n=n)
    reversed_observer = optical_matrix(reversed_blocks["B"], reversed_blocks["D"])["matrix"]
    return {"source_observer_exchange_residual": norm(full.subtract(source_labelled, reversed_observer))}


def scaled_profile(scale_factor):
    return lambda u: base.scale(base.base_k(u / scale_factor), 1.0 / (scale_factor * scale_factor))


def affine_scaling_control(n=6000):
    length, factor = 1.1, 1.43
    first = endpoint(length, base.base_k, n)
    second = endpoint(factor * length, scaled_profile(factor), n)
    dimensionless_first = base.scale(first["matrix"], length)
    dimensionless_second = base.scale(second["matrix"], factor * length)
    first_pieces, second_pieces = decompose(dimensionless_first), decompose(dimensionless_second)
    scalar_residual = math.sqrt(
        (first_pieces["expansion"] - second_pieces["expansion"]) ** 2
        + (first_pieces["shear_norm"] - second_pieces["shear_norm"]) ** 2
        + (first_pieces["twist"] - second_pieces["twist"]) ** 2
    )
    return {
        "scale_factor": factor,
        "dimensionless_matrix_residual": norm(full.subtract(dimensionless_first, dimensionless_second)),
        "dimensionless_scalar_residual": scalar_residual,
    }


def ell0_gate(symbols):
    return "SACHS_CALIBRATION_AND_AFFINE_SCALE_NOT_ELL0" if "ell0" not in symbols else "ELL0_SYMBOL_PRESENT_REQUIRES_DERIVATION"


def build_artifact():
    return {
        "classification": "EXACT_SPACETIME_SACHS_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT",
        "status": "EXACT_PLANE_WAVE_SACHS_EXPANSION_SHEAR_CALIBRATION_MOVABLE_TWIST_ZERO_AFFINE_SCALE_BLIND_NOT_ELL0",
        "open_gate": "PHYSICAL_SACHS_ENDPOINT_CALIBRATION_TWIST_SOURCE_AND_ELL0_LAW_NOT_DERIVED",
        "primary_object": "raw_B_D_and_connection_derived_S_equals_D_times_B_inverse",
        "optical_decomposition": optical_decomposition_control(),
        "riccati": riccati_control(),
        "rotation": rotation_control(),
        "calibration_mobility": calibration_mobility_control(),
        "caustic_guard": caustic_guard_control(),
        "reversal_exchange": reversal_exchange_control(),
        "affine_scaling": affine_scaling_control(),
        "ell0_gate": ell0_gate(["B", "D", "S", "K", "L", "H", "Q"]),
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
            print("Plane-wave Sachs-optics artifact is stale.", file=sys.stderr)
            return 1
        print("Plane-wave Sachs-optics artifact is current.")
        return 0
    OUTPUT.write_text(text)
    print(OUTPUT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
