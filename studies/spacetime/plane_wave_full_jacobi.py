#!/usr/bin/env python3
"""Full Jacobi phase-space quotient controls in one exact plane wave."""
import argparse
import importlib.util
import json
import math
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
OUTPUT = HERE / "plane-wave-full-jacobi-results.json"
_spec = importlib.util.spec_from_file_location("plane_wave_cross_channel_local", HERE / "plane_wave_cross_channel.py")
base = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(base)


def transpose(a):
    return [list(row) for row in zip(*a)]


def subtract(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def norm(a):
    return math.sqrt(sum(value * value for row in a for value in row))


def inverse2(a):
    determinant = a[0][0] * a[1][1] - a[0][1] * a[1][0]
    return [[a[1][1] / determinant, -a[0][1] / determinant], [-a[1][0] / determinant, a[0][0] / determinant]]


def assemble(a, b, c, d):
    return [a[0] + b[0], a[1] + b[1], c[0] + d[0], c[1] + d[1]]


def split(p):
    return (
        [p[0][:2], p[1][:2]],
        [p[0][2:], p[1][2:]],
        [p[2][:2], p[3][:2]],
        [p[2][2:], p[3][2:]],
    )


def propagate_pair(kfun, length, d0, v0, n):
    d, v = d0, v0
    step = length / n
    u = -length / 2.0
    for _ in range(n):
        d, v = base.rk4_pair(u, d, v, step, kfun)
        u += step
    return d, v


def full_blocks(kfun=base.base_k, length=1.1, n=6000):
    a, c = propagate_pair(kfun, length, base.eye(), base.zero(), n)
    b, d = propagate_pair(kfun, length, base.zero(), base.eye(), n)
    return {"A": a, "B": b, "C": c, "D": d}


def full_map(kfun=base.base_k, length=1.1, n=6000):
    blocks = full_blocks(kfun, length, n)
    return assemble(blocks["A"], blocks["B"], blocks["C"], blocks["D"])


def symplectic_control(n=6000):
    p = full_map(n=n)
    zero, identity = base.zero(), base.eye()
    omega = assemble(zero, identity, base.scale(identity, -1.0), zero)
    residual = subtract(base.mm(base.mm(transpose(p), omega), p), omega)
    return {"symplectic_residual": norm(residual)}


def endpoint_swap_involution(p):
    identity, zero = base.eye(), base.zero()
    exchange = assemble(zero, identity, identity, zero)
    return base.mm(base.mm(exchange, transpose(p)), exchange)


def reversal_control(n=6000):
    forward = full_blocks(n=n)
    reverse = full_blocks(lambda u: base.base_k(-u), n=n)
    return {
        "a_to_dt_residual": norm(subtract(reverse["A"], transpose(forward["D"]))),
        "b_to_bt_residual": norm(subtract(reverse["B"], transpose(forward["B"]))),
        "c_to_ct_residual": norm(subtract(reverse["C"], transpose(forward["C"]))),
        "d_to_at_residual": norm(subtract(reverse["D"], transpose(forward["A"]))),
    }


def symmetric_eigenvalues(a):
    trace = a[0][0] + a[1][1]
    disc = math.sqrt(max(0.0, (a[0][0] - a[1][1]) ** 2 + 4.0 * ((a[0][1] + a[1][0]) / 2.0) ** 2))
    return sorted(((trace - disc) / 2.0, (trace + disc) / 2.0))


def endpoint_optical_spectra(blocks):
    binv = inverse2(blocks["B"])
    source = base.mm(binv, blocks["A"])
    observer = base.mm(blocks["D"], binv)
    return symmetric_eigenvalues(source), symmetric_eigenvalues(observer)


def vector_residual(left, right):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(left, right)))


def endpoint_optical_control(n=6000):
    forward = full_blocks(n=n)
    reverse = full_blocks(lambda u: base.base_k(-u), n=n)
    fs, fo = endpoint_optical_spectra(forward)
    rs, ro = endpoint_optical_spectra(reverse)
    return {
        "forward_source_spectrum": fs,
        "forward_observer_spectrum": fo,
        "reverse_source_spectrum": rs,
        "reverse_observer_spectrum": ro,
        "forward_endpoint_spectrum_difference": vector_residual(fs, fo),
        "reversal_source_to_forward_observer_residual": vector_residual(rs, fo),
        "reversal_observer_to_forward_source_residual": vector_residual(ro, fs),
    }


def endpoint_swap_quotient_control(n=6000):
    forward = full_map(n=n)
    reverse = full_map(lambda u: base.base_k(-u), n=n)
    return {"quotient_reversal_residual": norm(subtract(reverse, endpoint_swap_involution(forward)))}


def dimensionless_map(blocks, length):
    return assemble(blocks["A"], base.scale(blocks["B"], 1.0 / length), base.scale(blocks["C"], length), blocks["D"])


def affine_rescaling_control(length=0.8, scale_factor=1.3, n=6000):
    first = full_blocks(base.base_k, length, n)
    second_length = scale_factor * length
    second_profile = lambda u: base.scale(base.base_k(u / scale_factor), 1.0 / scale_factor**2)
    second = full_blocks(second_profile, second_length, n)
    return {
        "dimensionless_full_map_residual": norm(subtract(dimensionless_map(first, length), dimensionless_map(second, second_length)))
    }


def ell0_gate(symbols):
    if "ell0" in symbols:
        return "ELL0_DEPENDENCE_REQUIRES_REVIEW"
    return "FULL_JACOBI_LABELLED_ENDPOINT_ORIENTATION_CONDITIONAL_AFFINE_SCALE_NOT_ELL0"


def build_artifact():
    return {
        "artifact": "plane-wave-full-jacobi-quotient",
        "classification": "EXACT_SPACETIME_CROSS_CHANNEL_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT",
        "status": "EXACT_PLANE_WAVE_FULL_JACOBI_LABELLED_ENDPOINT_ORDER_CONDITIONAL_SWAP_AND_AFFINE_SCALE_NONIDENTIFIABLE_NOT_ELL0",
        "raw_forward_blocks": full_blocks(),
        "symplectic": symplectic_control(),
        "reversal": reversal_control(),
        "endpoint_optical": endpoint_optical_control(),
        "endpoint_swap_quotient": endpoint_swap_quotient_control(),
        "affine_rescaling": affine_rescaling_control(),
        "ell0_gate": ell0_gate(["L", "K", "A", "B", "C", "D", "endpoint_labels"]),
        "open_gate": "PHYSICAL_ENDPOINT_LABELS_AND_CALIBRATION_NOT_DERIVED",
        "source_scope": "Exact vacuum Brinkmann plane waves and curvature-driven geodesic deviation only; full-map protocol, boundary labels, quotient, detector observability, UMCH, ell0, and detection are not source-established.",
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
