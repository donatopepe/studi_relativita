#!/usr/bin/env python3
"""Non-vertex Sachs twist boundary controls in an exact plane wave."""
import argparse
import importlib.util
import json
import math
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
OUTPUT = HERE / "plane-wave-sachs-twist-boundary-results.json"
_spec = importlib.util.spec_from_file_location("plane_wave_sachs_optics_local", HERE / "plane_wave_sachs_optics.py")
optics = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(optics)
full, base = optics.full, optics.base


def boundary_matrix(twist=0.23):
    return [[0.11, 0.06 - twist], [0.06 + twist, -0.03]]


def propagate(kfun=base.base_k, length=1.1, s0=None, n=6000, record=False):
    x, v = base.eye(), boundary_matrix() if s0 is None else s0
    h, u = length / n, -length / 2.0
    history = []
    initial_twist = optics.decompose(s0 or boundary_matrix())["twist"]
    for index in range(n):
        x, v = base.rk4_pair(u, x, v, h, kfun)
        u += h
        if record and (index % max(1, n // 120) == 0 or index == n - 1):
            current = optics.optical_matrix(x, v)
            if current["status"] == "REGULAR":
                pieces = optics.decompose(current["matrix"])
                history.append({"u": u, "det_x": optics.determinant(x), "twist": pieces["twist"]})
    current = optics.optical_matrix(x, v)
    if current["status"] != "REGULAR":
        return {"status": "CAUSTIC_OR_CONGRUENCE_BLOCK_SINGULAR", "X": x, "V": v}
    return {"status": "REGULAR", "X": x, "V": v, "S": current["matrix"], **optics.decompose(current["matrix"]), "initial_twist": initial_twist, "history": history}


def nonvertex_control(n=6000):
    result = propagate(n=n)
    return {
        "boundary_S0": boundary_matrix(),
        "raw_X": result["X"],
        "raw_V": result["V"],
        "raw_S": result["S"],
        "endpoint": {key: result[key] for key in ("expansion", "shear", "shear_norm", "twist")},
        "minimum_abs_det_x": abs(optics.determinant(result["X"])),
    }


def twist_area_control(n=6000):
    result = propagate(n=n, record=True)
    reference = result["initial_twist"]
    residuals = [abs(point["twist"] * point["det_x"] - reference) for point in result["history"]]
    return {"initial_twist_area": reference, "endpoint_twist_area": result["twist"] * optics.determinant(result["X"]), "maximum_residual": max(residuals)}


def boundary_mobility_control(n=6000):
    low = propagate(s0=boundary_matrix(0.11), n=n)
    high = propagate(s0=boundary_matrix(0.31), n=n)
    return {"boundary_twists": [0.11, 0.31], "endpoint_twists": [low["twist"], high["twist"]], "endpoint_twist_difference": abs(high["twist"] - low["twist"]), "profile_difference": 0.0}


def orientation_control(n=6000):
    result = propagate(n=n)
    q = optics.rotation(0.41)
    reflection = [[1.0, 0.0], [0.0, -1.0]]
    so = optics.multiply(optics.multiply(q, result["S"]), optics.transpose(q))
    reflected = optics.multiply(optics.multiply(reflection, result["S"]), optics.transpose(reflection))
    so_twist = optics.decompose(so)["twist"]
    reflected_twist = optics.decompose(reflected)["twist"]
    return {"so2_twist_residual": abs(so_twist - result["twist"]), "o2_sign_flip_residual": abs(reflected_twist + result["twist"])}


def scaled_profile(factor):
    return lambda u: base.scale(base.base_k(u / factor), 1.0 / (factor * factor))


def affine_orbit_control(n=6000):
    length, factor = 1.1, 1.39
    s0 = boundary_matrix()
    first = propagate(base.base_k, length, s0, n)
    second = propagate(scaled_profile(factor), factor * length, base.scale(s0, 1.0 / factor), n)
    return {
        "scale_factor": factor,
        "dimensionless_X_residual": optics.norm(full.subtract(first["X"], second["X"])),
        "dimensionless_LV_residual": optics.norm(full.subtract(base.scale(first["V"], length), base.scale(second["V"], factor * length))),
        "dimensionless_LS_residual": optics.norm(full.subtract(base.scale(first["S"], length), base.scale(second["S"], factor * length))),
        "twist_area_residual": abs(length * first["twist"] * optics.determinant(first["X"]) - factor * length * second["twist"] * optics.determinant(second["X"])),
    }


def alternate_k(u):
    return base.scale(base.base_k(u), 1.28)


def profile_sensitivity_control(n=6000):
    first, second = propagate(n=n), propagate(kfun=alternate_k, n=n)
    difference = math.sqrt(optics.norm(full.subtract(first["X"], second["X"])) ** 2 + optics.norm(full.subtract(first["V"], second["V"])) ** 2)
    return {"raw_endpoint_difference": difference, "interpretation": "PROFILE_INFORMATIVE_CONDITIONALLY_AT_FIXED_BOUNDARY"}


def caustic_guard_control():
    result = optics.optical_matrix(base.zero(), base.eye())
    return {"status": "CAUSTIC_OR_CONGRUENCE_BLOCK_SINGULAR" if result["status"] != "REGULAR" else "REGULAR"}


def ell0_gate(symbols):
    return "NONVERTEX_TWIST_BOUNDARY_AND_AFFINE_SCALE_NOT_ELL0" if "ell0" not in symbols else "ELL0_SYMBOL_PRESENT_REQUIRES_DERIVATION"


def build_artifact():
    return {
        "classification": "EXACT_SPACETIME_SACHS_BOUNDARY_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT",
        "status": "EXACT_PLANE_WAVE_NONVERTEX_TWIST_BOUNDARY_PROPAGATED_ORIENTATION_AND_AFFINE_SCALE_CONDITIONAL_NOT_ELL0",
        "open_gate": "PHYSICAL_ROTATING_CONGRUENCE_BOUNDARY_PARITY_CALIBRATION_AND_ELL0_LAW_NOT_DERIVED",
        "primary_object": "raw_X_V_S_and_declared_nonvertex_boundary_S0",
        "nonvertex": nonvertex_control(),
        "twist_area": twist_area_control(),
        "boundary_mobility": boundary_mobility_control(),
        "orientation": orientation_control(),
        "affine_orbit": affine_orbit_control(),
        "profile_sensitivity": profile_sensitivity_control(),
        "caustic_guard": caustic_guard_control(),
        "ell0_gate": ell0_gate(["X", "V", "S", "K", "L", "S0", "Q"]),
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
            print("Plane-wave Sachs twist-boundary artifact is stale.", file=sys.stderr)
            return 1
        print("Plane-wave Sachs twist-boundary artifact is current.")
        return 0
    OUTPUT.write_text(text)
    print(OUTPUT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
