#!/usr/bin/env python3
"""Canonical endpoint-shear transfer for a non-vertex Sachs graph."""
import argparse
import importlib.util
import json
import math
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
OUTPUT = HERE / "plane-wave-sachs-shear-transfer-results.json"


def load(name, filename):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


shear = load("plane_wave_endpoint_shear_local", "plane_wave_endpoint_shear.py")
twist = load("plane_wave_sachs_twist_boundary_local", "plane_wave_sachs_twist_boundary.py")
full, base, optics = shear.full, shear.base, twist.optics


def add(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def matrix_residual(a, b):
    return full.norm(full.subtract(a, b))


def graph_endpoint(blocks, s0):
    x = add(blocks["A"], base.mm(blocks["B"], s0))
    v = add(blocks["C"], base.mm(blocks["D"], s0))
    optical = optics.optical_matrix(x, v)
    if optical["status"] != "REGULAR":
        return {"status": "CAUSTIC_OR_CONGRUENCE_BLOCK_SINGULAR", "X": x, "V": v}
    return {"status": "REGULAR", "X": x, "V": v, "S": optical["matrix"], **optics.decompose(optical["matrix"])}


def source_h():
    return [[0.18, -0.07], [-0.07, -0.11]]


def observer_h():
    return [[0.16, 0.05], [0.05, -0.04]]


def source_absorption_control(n=6000):
    blocks = full.full_blocks(n=n)
    s0, hs, zero = twist.boundary_matrix(), source_h(), base.zero()
    baseline = graph_endpoint(blocks, s0)
    calibrated = shear.calibrated_blocks(blocks, hs, zero)
    shifted_boundary = add(s0, hs)
    transformed = graph_endpoint(calibrated, shifted_boundary)
    graph_prediction = base.mm(transformed["S"], transformed["X"])
    return {
        "raw_P": full.assemble(blocks["A"], blocks["B"], blocks["C"], blocks["D"]),
        "source_H": hs,
        "boundary_S0": s0,
        "shifted_boundary_S0": shifted_boundary,
        "X_residual": matrix_residual(transformed["X"], baseline["X"]),
        "V_residual": matrix_residual(transformed["V"], baseline["V"]),
        "S_residual": matrix_residual(transformed["S"], baseline["S"]),
        "graph_residual": matrix_residual(transformed["V"], graph_prediction),
    }


def observer_shift_control(n=6000):
    blocks = full.full_blocks(n=n)
    s0, ho, zero = twist.boundary_matrix(), observer_h(), base.zero()
    baseline = graph_endpoint(blocks, s0)
    transformed = graph_endpoint(shear.calibrated_blocks(blocks, zero, ho), s0)
    predicted_v = add(baseline["V"], base.mm(ho, baseline["X"]))
    predicted_s = add(baseline["S"], ho)
    return {
        "observer_H": ho,
        "X_residual": matrix_residual(transformed["X"], baseline["X"]),
        "V_shift_residual": matrix_residual(transformed["V"], predicted_v),
        "S_shift_residual": matrix_residual(transformed["S"], predicted_s),
        "expansion_shift": transformed["expansion"] - baseline["expansion"],
        "shear_norm_shift": transformed["shear_norm"] - baseline["shear_norm"],
        "twist_shift": transformed["twist"] - baseline["twist"],
    }


def uncompensated_source_control(n=6000):
    blocks = full.full_blocks(n=n)
    s0, hs = twist.boundary_matrix(), source_h()
    baseline = graph_endpoint(blocks, s0)
    transformed = graph_endpoint(shear.calibrated_blocks(blocks, hs, base.zero()), s0)
    return {
        "X_difference": matrix_residual(transformed["X"], baseline["X"]),
        "V_difference": matrix_residual(transformed["V"], baseline["V"]),
        "S_difference": matrix_residual(transformed["S"], baseline["S"]),
    }


def dimensionless_transfer(kfun, length, s0, hs, ho, n):
    blocks = full.full_blocks(kfun, length, n)
    endpoint = graph_endpoint(shear.calibrated_blocks(blocks, hs, ho), add(s0, hs))
    return {
        "X": endpoint["X"],
        "LV": base.scale(endpoint["V"], length),
        "LS": base.scale(endpoint["S"], length),
        "LS0": base.scale(s0, length),
        "LHs": base.scale(hs, length),
        "LHo": base.scale(ho, length),
    }


def affine_transfer_control(n=6000, length=1.1, factor=1.43):
    s0, hs, ho = twist.boundary_matrix(), source_h(), observer_h()
    first = dimensionless_transfer(base.base_k, length, s0, hs, ho, n)
    second = dimensionless_transfer(twist.scaled_profile(factor), factor * length, base.scale(s0, 1.0 / factor), base.scale(hs, 1.0 / factor), base.scale(ho, 1.0 / factor), n)
    return {"scale_factor": factor, "residuals": {key: matrix_residual(first[key], second[key]) for key in first}}


def alternate_k(u):
    k = base.base_k(u)
    return [[1.19 * k[0][0], 0.81 * k[0][1]], [0.81 * k[1][0], 1.19 * k[1][1]]]


def profile_sensitivity_control(n=6000):
    s0, hs, ho = twist.boundary_matrix(), source_h(), observer_h()
    first = dimensionless_transfer(base.base_k, 1.1, s0, hs, ho, n)
    second = dimensionless_transfer(alternate_k, 1.1, s0, hs, ho, n)
    return {"raw_difference": math.sqrt(sum(matrix_residual(first[key], second[key]) ** 2 for key in ("X", "LV", "LS"))), "interpretation": "PROFILE_INFORMATIVE_ONLY_AT_FIXED_BOUNDARY_AND_CALIBRATION"}


def caustic_guard_control():
    result = optics.optical_matrix(base.zero(), base.eye())
    return {"status": "CAUSTIC_OR_CONGRUENCE_BLOCK_SINGULAR" if result["status"] != "REGULAR" else "REGULAR"}


def ell0_gate(symbols):
    return "SACHS_SHEAR_TRANSFER_BOUNDARY_AND_AFFINE_NOT_ELL0" if "ell0" not in symbols else "ELL0_SYMBOL_PRESENT_REQUIRES_DERIVATION"


def build_artifact():
    return {
        "classification": "EXACT_SPACETIME_SACHS_CALIBRATION_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT",
        "status": "EXACT_PLANE_WAVE_SACHS_SOURCE_SHEAR_ABSORBED_BY_BOUNDARY_OBSERVER_SHEAR_MOVES_OPTICS_NOT_ELL0",
        "open_gate": "PHYSICAL_SACHS_SOURCE_BOUNDARY_AND_OBSERVER_CALIBRATION_NOT_DERIVED",
        "primary_objects": ["P", "X", "V", "S", "S0", "Hs", "Ho"],
        "source_absorption": source_absorption_control(),
        "observer_shift": observer_shift_control(),
        "uncompensated_source": uncompensated_source_control(),
        "affine_transfer": affine_transfer_control(),
        "profile_sensitivity": profile_sensitivity_control(),
        "caustic_guard": caustic_guard_control(),
        "ell0_gate": ell0_gate(["P", "X", "V", "S", "S0", "Hs", "Ho", "K", "L"]),
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
            print("Plane-wave Sachs shear-transfer artifact is stale.", file=sys.stderr)
            return 1
        print("Plane-wave Sachs shear-transfer artifact is current.")
        return 0
    OUTPUT.write_text(text)
    print(OUTPUT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
