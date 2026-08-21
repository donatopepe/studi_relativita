#!/usr/bin/env python3
"""Evaluate whether declared evidence identifies an upper bound on kappa_0."""

from __future__ import annotations

import argparse
import json
import pathlib
import sys


HERE = pathlib.Path(__file__).resolve().parent
DEFAULT_INPUT = HERE / "inputs.json"
DEFAULT_OUTPUT = HERE / "results.json"


def evaluate(data: dict) -> dict:
    required = {"study_id", "observable", "mapping", "sources"}
    missing = sorted(required - set(data))
    if missing:
        raise ValueError(f"Missing input fields: {missing}")
    if not data["sources"]:
        raise ValueError("At least one source is required")

    base = {
        "study_id": data["study_id"],
        "observable": data["observable"],
        "mapping": data["mapping"],
        "confidence_level": data.get("confidence_level"),
        "positive_detection": False,
        "sources": data["sources"],
    }
    if data["mapping"] == "direct_timelike_curvature":
        if data.get("observable_unit") != "m s^-2":
            raise ValueError("Direct mapping requires acceleration in m s^-2")
        value = float(data["observable_value"])
        c = float(data["speed_of_light_m_s"])
        if value < 0 or c <= 0:
            raise ValueError("Acceleration must be nonnegative and c positive")
        return {
            **base,
            "status": "BOUND_DERIVABLE_UNDER_DECLARED_MAPPING",
            "kappa0_upper_bound_value": value / (c * c),
            "kappa0_upper_bound_unit": "m^-1",
            "blocking_reason": None,
            "formula": "kappa0 <= a_upper/c^2",
        }
    if data["mapping"] == "none_derived":
        return {
            **base,
            "status": "NO_BOUND_DERIVABLE",
            "kappa0_upper_bound_value": None,
            "kappa0_upper_bound_unit": "m^-1",
            "blocking_reason": "No derived mapping connects the cited free-fall observables to the proper acceleration a entering kappa=a/c^2 under a consistent UMCH dynamics.",
            "formula": "kappa=a/c^2 (kinematic definition only)",
        }
    raise ValueError(f"Unknown mapping: {data['mapping']}")


def rendered(data: dict) -> str:
    return json.dumps(evaluate(data), ensure_ascii=False, indent=2, sort_keys=True) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=pathlib.Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=pathlib.Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    expected = rendered(json.loads(args.input.read_text(encoding="utf-8")))
    if args.check:
        if not args.output.exists() or args.output.read_text(encoding="utf-8") != expected:
            print(f"Result differs: {args.output}", file=sys.stderr)
            return 1
        print("Experimental identifiability result is current.")
        return 0
    args.output.write_text(expected, encoding="utf-8")
    print(f"Wrote {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
