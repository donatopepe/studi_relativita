#!/usr/bin/env python3
"""Endpoint-local canonical shear nuisance for an exact plane-wave Jacobi map."""
import argparse
import importlib.util
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
OUTPUT = HERE / "plane-wave-endpoint-shear-results.json"
_spec = importlib.util.spec_from_file_location("plane_wave_full_jacobi_local", HERE / "plane_wave_full_jacobi.py")
full = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(full)
base = full.base


def identity4():
    return full.assemble(base.eye(), base.zero(), base.zero(), base.eye())


def omega():
    return full.assemble(base.zero(), base.eye(), base.scale(base.eye(), -1.0), base.zero())


def shear(h):
    return full.assemble(base.eye(), base.zero(), h, base.eye())


def shear_inverse(h):
    return shear(base.scale(h, -1.0))


def symplectic_residual(p):
    return full.norm(full.subtract(base.mm(base.mm(full.transpose(p), omega()), p), omega()))


def add(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def calibrated_map(p, hs, ho):
    return base.mm(base.mm(shear(ho), p), shear_inverse(hs))


def calibrated_blocks(blocks, hs, ho):
    a, b, c, d = (blocks[key] for key in ("A", "B", "C", "D"))
    ap = full.subtract(a, base.mm(b, hs))
    bp = b
    dp = add(d, base.mm(ho, b))
    cp = full.subtract(add(c, base.mm(ho, a)), base.mm(dp, hs))
    return {"A": ap, "B": bp, "C": cp, "D": dp}


def optical_matrices(blocks):
    binv = full.inverse2(blocks["B"])
    return base.mm(binv, blocks["A"]), base.mm(blocks["D"], binv)


def eigenvalues(a):
    return full.symmetric_eigenvalues(a)


def vector_residual(a, b):
    return full.vector_residual(a, b)


def gap(values):
    return values[1] - values[0]


def symplectic_shear_control():
    hs = [[0.31, -0.17], [-0.17, -0.08]]
    ho = [[-0.22, 0.13], [0.13, 0.19]]
    return {
        "source_shear_symplectic_residual": symplectic_residual(shear(hs)),
        "observer_shear_symplectic_residual": symplectic_residual(shear(ho)),
        "endpoint_labels": ["source", "observer"],
    }


def block_action_control(n=6000):
    hs = [[0.31, -0.17], [-0.17, -0.08]]
    ho = [[-0.22, 0.13], [0.13, 0.19]]
    blocks = full.full_blocks(n=n)
    direct = full.split(calibrated_map(full.assemble(*(blocks[k] for k in ("A", "B", "C", "D"))), hs, ho))
    direct = dict(zip(("A", "B", "C", "D"), direct))
    formula = calibrated_blocks(blocks, hs, ho)
    result = {f"{key.lower()}_formula_residual": full.norm(full.subtract(direct[key], formula[key])) for key in formula}
    result["b_unchanged_residual"] = full.norm(full.subtract(direct["B"], blocks["B"]))
    result["calibrated_map_symplectic_residual"] = symplectic_residual(calibrated_map(full.full_map(n=n), hs, ho))
    return result


def optical_additive_control(n=6000):
    hs = [[0.31, -0.17], [-0.17, -0.08]]
    ho = [[-0.22, 0.13], [0.13, 0.19]]
    blocks = full.full_blocks(n=n)
    source, observer = optical_matrices(blocks)
    source_p, observer_p = optical_matrices(calibrated_blocks(blocks, hs, ho))
    return {
        "source_additive_residual": full.norm(full.subtract(source_p, full.subtract(source, hs))),
        "observer_additive_residual": full.norm(full.subtract(observer_p, add(observer, ho))),
    }


def spectral_mobility_control(n=6000):
    hs = [[0.31, -0.17], [-0.17, -0.08]]
    ho = [[-0.22, 0.13], [0.13, 0.19]]
    blocks = full.full_blocks(n=n)
    source, observer = optical_matrices(blocks)
    source_p, observer_p = optical_matrices(calibrated_blocks(blocks, hs, ho))
    se, oe, sep, oep = eigenvalues(source), eigenvalues(observer), eigenvalues(source_p), eigenvalues(observer_p)
    return {
        "source_spectrum": se,
        "observer_spectrum": oe,
        "calibrated_source_spectrum": sep,
        "calibrated_observer_spectrum": oep,
        "source_spectrum_shift": vector_residual(se, sep),
        "observer_spectrum_shift": vector_residual(oe, oep),
        "source_gap_shift": abs(gap(sep) - gap(se)),
        "observer_gap_shift": abs(gap(oep) - gap(oe)),
    }


def scalar_shear_control(n=6000):
    hs, ho = base.scale(base.eye(), 0.27), base.scale(base.eye(), -0.34)
    blocks = full.full_blocks(n=n)
    source, observer = optical_matrices(blocks)
    source_p, observer_p = optical_matrices(calibrated_blocks(blocks, hs, ho))
    se, oe, sep, oep = eigenvalues(source), eigenvalues(observer), eigenvalues(source_p), eigenvalues(observer_p)
    return {
        "source_spectrum_shift": vector_residual(se, sep),
        "observer_spectrum_shift": vector_residual(oe, oep),
        "source_gap_residual": abs(gap(sep) - gap(se)),
        "observer_gap_residual": abs(gap(oep) - gap(oe)),
    }


def dimensionless_map(blocks, length):
    return full.assemble(blocks["A"], base.scale(blocks["B"], 1.0 / length), base.scale(blocks["C"], length), blocks["D"])


def affine_rescaling_control(n=6000):
    length, factor = 0.8, 1.3
    hs = [[0.31, -0.17], [-0.17, -0.08]]
    ho = [[-0.22, 0.13], [0.13, 0.19]]
    first = calibrated_blocks(full.full_blocks(length=length, n=n), hs, ho)
    scaled_k = lambda u: base.scale(base.base_k(u / factor), 1.0 / factor ** 2)
    # H mixes displacement into affine derivative and therefore has units 1/L.
    second = calibrated_blocks(
        full.full_blocks(scaled_k, length * factor, n=n),
        base.scale(hs, 1.0 / factor),
        base.scale(ho, 1.0 / factor),
    )
    return {"dimensionless_calibrated_map_residual": full.norm(full.subtract(dimensionless_map(first, length), dimensionless_map(second, length * factor)))}


def ell0_gate(symbols):
    return "LABELLED_ENDPOINT_SHEAR_CALIBRATION_NONIDENTIFIABLE_AFFINE_SCALE_NOT_ELL0" if "ell0" not in symbols else "ELL0_REQUIRES_DERIVED_PHASE_SPACE_CALIBRATION"


def build_artifact():
    return {
        "study_id": "plane-wave-endpoint-shear-v1",
        "classification": "EXACT_SPACETIME_CROSS_CHANNEL_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT",
        "status": "EXACT_PLANE_WAVE_LABELLED_ENDPOINT_OPTICAL_SPECTRA_NONIDENTIFIABLE_UNDER_CANONICAL_SHEAR_CALIBRATION_NOT_ELL0",
        "open_gate": "PHYSICAL_PHASE_SPACE_ENDPOINT_CALIBRATION_NOT_DERIVED",
        "symplectic_shear": symplectic_shear_control(),
        "block_action": block_action_control(),
        "optical_additive_action": optical_additive_control(),
        "spectral_mobility": spectral_mobility_control(),
        "scalar_shear": scalar_shear_control(),
        "affine_rescaling": affine_rescaling_control(),
        "ell0_gate": ell0_gate(["A", "B", "C", "D", "Hs", "Ho", "L"]),
        "structural_dead_end": False,
        "conclusion": "NO_POSITIVE_DETECTION_CLAIM",
        "limitation": "Project canonical-shear nuisance model; physical endpoint derivative/displacement calibration, detector response, transport, leakage, ell0 law, and data are not derived.",
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
            print("Plane-wave endpoint-shear artifact differs", file=sys.stderr)
            return 1
        print("Plane-wave endpoint-shear artifact is current.")
        return 0
    OUTPUT.write_text(text)
    print(f"Wrote {OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
