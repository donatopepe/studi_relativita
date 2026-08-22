#!/usr/bin/env python3
"""Check weighted RMS and exhibit non-equivalence to a pointwise bound."""

from __future__ import annotations

import argparse
import json
import math
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
DEFAULT_INPUT = HERE / "coarse-grained-cases.json"
DEFAULT_OUTPUT = HERE / "coarse-grained-results.json"


def weighted_rms(values: list[float], weights: list[float]) -> float:
    if len(values) != len(weights) or not values:
        raise ValueError("Values and weights must be nonempty and aligned")
    if any(weight < 0 for weight in weights):
        raise ValueError("Weights must be nonnegative")
    total = sum(weights)
    if total <= 0:
        raise ValueError("Weight sum must be positive")
    return math.sqrt(sum(weight * value * value for value, weight in zip(values, weights)) / total)


def evaluate(data: dict) -> dict:
    if data["hypothesis_class"] != "ALTERNATIVE_HYPOTHESIS":
        raise ValueError("Coarse-grained proposal must remain separate")
    kappa0 = float(data["kappa0"])
    cases = []
    for case in data["cases"]:
        values = [float(value) for value in case["kappa"]]
        rms = weighted_rms(values, [float(weight) for weight in case["weights"]])
        cases.append({
            **case,
            "rms": rms,
            "rms_bound_satisfied": rms >= kappa0,
            "pointwise_bound_satisfied": all(value >= kappa0 for value in values),
            "contains_zero_curvature": any(value == 0 for value in values),
        })
    counterexamples = [case["name"] for case in cases if case["rms_bound_satisfied"] and not case["pointwise_bound_satisfied"]]
    return {
        "study_id": data["study_id"],
        "hypothesis_class": data["hypothesis_class"],
        "observable_dimension": data["observable_dimension"],
        "cases": cases,
        "counterexamples": counterexamples,
        "equivalence_to_pointwise_umch": "NOT_EQUIVALENT" if counterexamples else "NOT_DETERMINED",
        "identifiability": "NON_IDENTIFIABLE",
        "warning": "Algebraic counterexample establishes non-equivalence only; no dynamics or experimental estimator is supplied.",
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
            print(f"Coarse-grained result differs: {args.output}", file=sys.stderr)
            return 1
        print("Coarse-grained non-equivalence result is current.")
        return 0
    args.output.write_text(expected, encoding="utf-8")
    print(f"Wrote {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
