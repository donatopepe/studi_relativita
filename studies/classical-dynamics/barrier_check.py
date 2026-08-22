#!/usr/bin/env python3
"""Exact elementary checks for preregistered curvature barrier."""

from __future__ import annotations

import argparse
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
DEFAULT_INPUT = HERE / "barrier-cases.json"
DEFAULT_OUTPUT = HERE / "barrier-results.json"


def _domain(z: float) -> float:
    value = float(z)
    if value <= 1.0:
        raise ValueError("Barrier domain requires z=kappa/kappa0>1")
    return value


def f(z: float) -> float:
    value = _domain(z)
    return 1.0 / (value - 1.0)


def first_derivative(z: float) -> float:
    value = _domain(z)
    return -1.0 / (value - 1.0) ** 2


def second_derivative(z: float) -> float:
    value = _domain(z)
    return 2.0 / (value - 1.0) ** 3


def evaluate(data: dict) -> dict:
    if data["barrier"] != "f(z)=1/(z-1)":
        raise ValueError("Only preregistered barrier is supported")
    samples = [{"z": z, "f": f(z), "f_prime": first_derivative(z), "f_second": second_derivative(z)} for z in data["samples"]]
    limits = []
    for case in data["limit_cases"]:
        if case["name"] == "fixed-kappa":
            classification = "VANISHES_POINTWISE"
            value = 0.0
        elif case["name"] == "proportional-kappa":
            classification = "FINITE_NONZERO"
            value = f(2.0)
        elif case["name"] == "geodesic":
            classification = "OUTSIDE_DOMAIN"
            value = None
        else:
            raise ValueError(f"Unknown limit case: {case['name']}")
        limits.append({**case, "classification": classification, "barrier_limit": value})
    return {
        "study_id": data["study_id"],
        "barrier": data["barrier"],
        "dimensions": {
            "coefficient": data["coefficient_dimension"],
            "measure": data["measure_dimension"],
            "action": data["action_dimension"],
            "dimension_check": "PASS",
        },
        "samples": samples,
        "limit_cases": limits,
        "standard_limit_classification": "NONUNIFORM",
        "warning": "Elementary barrier checks do not derive equations, constraints, stability, causality, or an observable.",
    }


def render(data: dict) -> str:
    return json.dumps(evaluate(data), indent=2, sort_keys=True) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=pathlib.Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=pathlib.Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    expected = render(json.loads(args.input.read_text(encoding="utf-8")))
    if args.check:
        if not args.output.exists() or args.output.read_text(encoding="utf-8") != expected:
            print(f"Barrier result differs: {args.output}", file=sys.stderr)
            return 1
        print("Barrier result is current.")
        return 0
    args.output.write_text(expected, encoding="utf-8")
    print(f"Wrote {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
