#!/usr/bin/env python3
"""Multipath limit and preregistered Paper III gate decision for Candidate B."""

from __future__ import annotations

import argparse
import json
import math
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
DEFAULT_INPUT = HERE / "barrier-gate-cases.json"
DEFAULT_OUTPUT = HERE / "barrier-gate-results.json"


def physical_root(epsilon):
    epsilon = float(epsilon)
    if epsilon <= 0:
        raise ValueError("epsilon must be positive")
    return 1 + epsilon + math.sqrt(epsilon * epsilon + epsilon)


def ell(z, epsilon):
    return -1 + float(epsilon) / (float(z) - 1)


def limit_path(name, epsilon, ratio=2.0):
    epsilon = float(epsilon)
    if name == "fixed-curvature":
        return {"name": name, "classification": "FREE_LAGRANGIAN_DENSITY_POINTWISE", "barrier_limit": 0.0, "domain": "eventually inside"}
    if name == "stationary-root":
        z = physical_root(epsilon)
        return {"name": name, "classification": "CURVATURE_COLLAPSES_BUT_BARRIER_REMAINS_FINITE", "barrier_limit": epsilon / (z - 1), "z": z}
    if name == "boundary-layer":
        ratio = float(ratio)
        if ratio <= 1:
            raise ValueError("ratio must exceed one")
        return {"name": name, "classification": "FINITE_PATH_DEPENDENT_BARRIER", "barrier_limit": epsilon / (ratio - 1), "z": ratio}
    if name == "geodesic":
        return {"name": name, "classification": "OUTSIDE_DOMAIN_FOR_ALL_POSITIVE_KAPPA0", "barrier_limit": None, "z": 0.0}
    raise ValueError(name)


def stationary_limit(epsilon, kappa0):
    z = physical_root(epsilon)
    kappa_star = float(kappa0) * z
    return {"z_star": z, "kappa_star": kappa_star, "growth_rate": kappa_star, "classification": "TIMESCALE_DIVERGES_AS_KAPPA0_TO_ZERO"}


def evaluate(data):
    checks = data["required_checks"]
    failed = [key for key, value in checks.items() if value.startswith("FAIL")]
    unresolved = [key for key, value in checks.items() if value == "UNRESOLVED"]
    return {
        "study_id": data["study_id"],
        "epsilon": data["epsilon"],
        "paths": [limit_path(name, data["epsilon"]) for name in ["fixed-curvature", "stationary-root", "boundary-layer", "geodesic"]],
        "stationary_scaling": [stationary_limit(data["epsilon"], value) for value in data["kappa0_samples"]],
        "required_checks": checks,
        "failed_required_checks": failed,
        "unresolved_required_checks": unresolved,
        "candidate_b_state": "CONTRADICTED_UNDER_ASSUMPTIONS",
        "paper_iii_gate": "BLOCKED",
        "full_phase_space_instability_proven": False,
        "bounded_energy_resolved": False,
        "decision_basis": "Fixed barrier fails reduced planar local-stability gate, full standard-solution-space limit, and observable mapping under preregistered criteria.",
        "warning": "Conditional rejection applies to fixed barrier in flat timelike pointwise model; it is not a proof against all UMCH formulations.",
    }


def render(data):
    return json.dumps(evaluate(data), indent=2, sort_keys=True) + "\n"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=pathlib.Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=pathlib.Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    expected = render(json.loads(args.input.read_text(encoding="utf-8")))
    if args.check:
        if not args.output.exists() or args.output.read_text(encoding="utf-8") != expected:
            print(f"Gate result differs: {args.output}", file=sys.stderr)
            return 1
        print("Barrier gate decision is current.")
        return 0
    args.output.write_text(expected, encoding="utf-8")
    print(f"Wrote {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
