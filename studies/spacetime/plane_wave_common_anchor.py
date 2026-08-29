#!/usr/bin/env python3
"""Common-anchor handedness gate for exact plane-wave window/Jacobi channels."""
import argparse
import importlib.util
import json
import math
import pathlib
import sys

OUTPUT = pathlib.Path(__file__).with_name("plane-wave-common-anchor-results.json")
_CROSS_PATH = pathlib.Path(__file__).with_name("plane_wave_cross_channel.py")
_spec = importlib.util.spec_from_file_location("plane_wave_cross_channel_local", _CROSS_PATH)
cross = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(cross)


def transpose(a):
    return [list(row) for row in zip(*a)]


def rotation(theta):
    return [[math.cos(theta), -math.sin(theta)], [math.sin(theta), math.cos(theta)]]


def common_action(a, q):
    return cross.mm(cross.mm(q, a), transpose(q))


def distance(a, b):
    return cross.norm(cross.add(a, b, -1.0))


def handed_statistic(b):
    """Coefficient of J=[[0,-1],[1,0]] in the antisymmetric part."""
    return 0.5 * (b[1][0] - b[0][1])


def reversal_handedness_control(n=6000):
    length = 1.1
    forward = cross.jacobi(cross.base_k, length, n)
    reverse = cross.jacobi(lambda u: cross.base_k(-u), length, n)
    hf = handed_statistic(forward)
    hr = handed_statistic(reverse)
    return {
        "forward_handed_statistic": hf,
        "reverse_handed_statistic": hr,
        "jacobi_transpose_residual": distance(reverse, transpose(forward)),
        "reversal_sign_residual": abs(hr + hf),
    }


def common_rotation_control(n=6000):
    b = cross.jacobi(cross.base_k, 1.1, n)
    h = handed_statistic(b)
    residuals = [abs(handed_statistic(common_action(b, rotation(t))) - h) for t in (0.17, 0.73, 1.41, 2.62)]
    return {"maximum_rotation_residual": max(residuals)}


def reflection_control(n=6000):
    b = cross.jacobi(cross.base_k, 1.1, n)
    reflection = [[1.0, 0.0], [0.0, -1.0]]
    return {"reflection_sign_residual": abs(handed_statistic(common_action(b, reflection)) + handed_statistic(b))}


def endpoint_equivalence_control(n=6000):
    b = cross.jacobi(cross.base_k, 1.1, n)
    phi = math.atan2(b[1][0] - b[0][1], b[0][0] + b[1][1])
    transformed = cross.mm(cross.mm(rotation(-phi), b), transpose(rotation(phi)))
    return {"transpose_orbit_residual": distance(transformed, transpose(b))}


def affine_rescaling_control(length=0.8, scale_factor=1.3, n=6000):
    b1 = cross.jacobi(cross.base_k, length, n)
    length2 = scale_factor * length
    k2 = lambda u: cross.scale(cross.base_k(u / scale_factor), 1.0 / scale_factor**2)
    b2 = cross.jacobi(k2, length2, n)
    return {
        "dimensionless_handed_1": handed_statistic(b1) / length,
        "dimensionless_handed_2": handed_statistic(b2) / length2,
        "dimensionless_handed_residual": abs(handed_statistic(b1) / length - handed_statistic(b2) / length2),
    }


def ell0_gate(symbols):
    return "ORIENTED_PROFILE_REVERSAL_CONDITIONAL_ABSOLUTE_SCALE_NOT_ELL0" if "ell0" not in symbols else "ELL0_DEPENDENCE_REQUIRES_REVIEW"


def build_artifact():
    return {
        "artifact": "plane-wave-common-anchor-handedness",
        "classification": "EXACT_SPACETIME_CROSS_CHANNEL_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT",
        "status": "EXACT_PLANE_WAVE_COMMON_ORIENTED_ANCHOR_RECOVERS_REVERSAL_SIGN_CONDITIONALLY_NOT_ELL0",
        "reversal": reversal_handedness_control(),
        "common_so2": common_rotation_control(),
        "common_o2_reflection": reflection_control(),
        "independent_endpoints": endpoint_equivalence_control(),
        "affine_rescaling": affine_rescaling_control(),
        "ell0_gate": ell0_gate(["L", "K", "B", "common_anchor", "handedness"]),
        "open_gate": "PHYSICAL_ORIENTED_ENDPOINT_ANCHOR_NOT_DERIVED",
        "source_scope": "Exact Brinkmann plane-wave and curvature-driven geodesic deviation only; common anchor, window, boundary, detector observability, UMCH, ell0, and detection are not source-established.",
        "structural_dead_end": False,
        "conclusion": "NO_POSITIVE_DETECTION_CLAIM",
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    text = json.dumps(build_artifact(), indent=2, sort_keys=True) + "\n"
    if args.check:
        if not OUTPUT.exists() or OUTPUT.read_text() != text:
            print("artifact missing or stale", file=sys.stderr)
            return 1
        return 0
    OUTPUT.write_text(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
