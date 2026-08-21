#!/usr/bin/env python3
"""Check algebraic KKT feasibility; does not derive dynamics."""

from __future__ import annotations

import argparse
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
DEFAULT_INPUT = HERE / "hard-constraint-cases.json"
DEFAULT_OUTPUT = HERE / "hard-constraint-results.json"
TOLERANCE = 1e-12


def classify(case: dict) -> dict:
    kappa = float(case["kappa"])
    kappa0 = float(case["kappa0"])
    multiplier = float(case["lambda"])
    g = kappa0 - kappa
    residual = multiplier * g
    dual_feasible = multiplier >= -TOLERANCE
    primal_feasible = g <= TOLERANCE
    complementary = abs(residual) <= TOLERANCE
    if not (dual_feasible and primal_feasible and complementary):
        classification = "INFEASIBLE"
    elif abs(g) <= TOLERANCE:
        classification = "FEASIBLE_ACTIVE"
    else:
        classification = "FEASIBLE_INACTIVE"
    return {
        **case,
        "g": g,
        "complementarity_residual": residual,
        "classification": classification,
        "analysis_level": "KINEMATIC_KKT_ALGEBRA",
    }


def evaluate(data: dict) -> dict:
    if data.get("sign_convention") != "g=kappa0-kappa<=0":
        raise ValueError("Unsupported sign convention")
    return {
        "study_id": data["study_id"],
        "scope": data["scope"],
        "warning": "Passing KKT algebra does not derive an action, equations, stability, or well-posed evolution.",
        "cases": [classify(case) for case in data["cases"]],
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
            print(f"Hard-constraint result differs: {args.output}", file=sys.stderr)
            return 1
        print("Hard-constraint algebra result is current.")
        return 0
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(expected, encoding="utf-8")
    print(f"Wrote {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
