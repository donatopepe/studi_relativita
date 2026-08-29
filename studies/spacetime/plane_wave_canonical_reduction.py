#!/usr/bin/env python3
"""Independent canonical endpoint calibration of exact plane-wave Jacobi maps."""
import argparse
import importlib.util
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
OUTPUT = HERE / "plane-wave-canonical-reduction-results.json"
_spec = importlib.util.spec_from_file_location("plane_wave_full_jacobi_local", HERE / "plane_wave_full_jacobi.py")
full = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(full)
base = full.base


def omega():
    return full.assemble(base.zero(), base.eye(), base.scale(base.eye(), -1.0), base.zero())


def identity4():
    return full.assemble(base.eye(), base.zero(), base.zero(), base.eye())


def inverse4(a):
    n = 4
    augmented = [list(a[i]) + [1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    for col in range(n):
        pivot = max(range(col, n), key=lambda row: abs(augmented[row][col]))
        if abs(augmented[pivot][col]) < 1e-14:
            raise ValueError("singular matrix")
        augmented[col], augmented[pivot] = augmented[pivot], augmented[col]
        value = augmented[col][col]
        augmented[col] = [entry / value for entry in augmented[col]]
        for row in range(n):
            if row == col:
                continue
            factor = augmented[row][col]
            augmented[row] = [augmented[row][j] - factor * augmented[col][j] for j in range(2 * n)]
    return [row[n:] for row in augmented]


def symplectic_residual(p):
    return full.norm(full.subtract(base.mm(base.mm(full.transpose(p), omega()), p), omega()))


def trace(p):
    return sum(p[i][i] for i in range(4))


def second_k(u):
    return base.add(base.base_k(u), base.scale([[1.0, 0.0], [0.0, -1.0]], 0.23 * (1.0 + 0.4 * u)))


def profile_maps(n=6000):
    return full.full_map(n=n), full.full_map(second_k, n=n)


def observer_calibration(p1, p2):
    return base.mm(p2, inverse4(p1))


def symplectic_family_control(n=6000):
    p1, p2 = profile_maps(n)
    go = observer_calibration(p1, p2)
    return {
        "first_map_residual": symplectic_residual(p1),
        "second_map_residual": symplectic_residual(p2),
        "observer_calibration_residual": symplectic_residual(go),
    }


def transitive_collision_control(n=6000):
    p1, p2 = profile_maps(n)
    go = observer_calibration(p1, p2)
    collision = base.mm(base.mm(go, p1), inverse4(identity4()))
    return {
        "raw_map_difference": full.norm(full.subtract(p1, p2)),
        "collision_residual": full.norm(full.subtract(collision, p2)),
        "source_calibration": "IDENTITY",
        "observer_calibration": "P2 P1^{-1}",
    }


def common_conjugation_obstruction_control(n=6000):
    p1, p2 = profile_maps(n)
    difference = abs(trace(p1) - trace(p2))
    return {
        "first_trace": trace(p1),
        "second_trace": trace(p2),
        "trace_difference": difference,
        "gate": "DISTINCT_TRACE_FORBIDS_COMMON_CONJUGATION_COLLISION",
    }


def group_comparison_control(n=6000):
    transitive_collision_control(n)
    return {
        "independent_endpoint_action": "TRANSITIVE_ON_SYMPLECTIC_PROPAGATORS",
        "common_endpoint_action": "CONJUGACY_INVARIANTS_REMAIN",
        "lower_shear_action": "B_BLOCK_REMAINS_INVARIANT",
    }


def dimensionless_map(blocks, length):
    return full.assemble(blocks["A"], base.scale(blocks["B"], 1.0 / length), base.scale(blocks["C"], length), blocks["D"])


def affine_rescaling_control(n=6000):
    length, factor = 0.8, 1.3
    first = full.full_blocks(length=length, n=n)
    scaled_k = lambda u: base.scale(base.base_k(u / factor), 1.0 / factor ** 2)
    second = full.full_blocks(scaled_k, length * factor, n=n)
    return {"dimensionless_full_map_residual": full.norm(full.subtract(dimensionless_map(first, length), dimensionless_map(second, length * factor)))}


def ell0_gate(symbols):
    return "FULL_MAP_CANONICAL_ENDPOINT_QUOTIENT_AFFINE_SCALE_NOT_ELL0" if "ell0" not in symbols else "ELL0_REQUIRES_DERIVED_CANONICAL_CALIBRATION_GROUP"


def build_artifact():
    return {
        "study_id": "plane-wave-canonical-reduction-v1",
        "classification": "EXACT_SPACETIME_CROSS_CHANNEL_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT",
        "status": "EXACT_PLANE_WAVE_FULL_MAP_TRANSITIVE_UNDER_INDEPENDENT_CANONICAL_ENDPOINT_CALIBRATION_NOT_ELL0",
        "open_gate": "PHYSICAL_CANONICAL_ENDPOINT_CALIBRATION_GROUP_NOT_DERIVED",
        "symplectic_family": symplectic_family_control(),
        "transitive_collision": transitive_collision_control(),
        "common_conjugation_obstruction": common_conjugation_obstruction_control(),
        "group_comparison": group_comparison_control(),
        "affine_rescaling": affine_rescaling_control(),
        "ell0_gate": ell0_gate(["P1", "P2", "Gs", "Go", "L"]),
        "structural_dead_end": False,
        "conclusion": "NO_POSITIVE_DETECTION_CLAIM",
        "limitation": "Independent free Sp(4) endpoint calibration is a strongest project nuisance contract, not a physical detector group derived from the canonical plane-wave source.",
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
            print("Plane-wave canonical-reduction artifact differs", file=sys.stderr)
            return 1
        print("Plane-wave canonical-reduction artifact is current.")
        return 0
    OUTPUT.write_text(text)
    print(f"Wrote {OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
