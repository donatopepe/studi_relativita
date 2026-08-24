#!/usr/bin/env python3
"""Planar constant-curvature roots and reduced local linearization."""

from __future__ import annotations

import argparse
import json
import math
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
DEFAULT_INPUT = HERE / "barrier-stationary-cases.json"
DEFAULT_OUTPUT = HERE / "barrier-stationary-results.json"


def _epsilon(value: float) -> float:
    value = float(value)
    if value <= 0:
        raise ValueError("epsilon must be positive")
    return value


def ell(z: float, epsilon: float) -> float:
    return -1.0 + _epsilon(epsilon) / (float(z) - 1.0)


def ell_z(z: float, epsilon: float) -> float:
    return -_epsilon(epsilon) / (float(z) - 1.0) ** 2


def stationary_equation(z: float, epsilon: float) -> float:
    z = float(z)
    return z * (ell(z, epsilon) - z * ell_z(z, epsilon))


def constant_curvature_roots(epsilon: float) -> dict:
    epsilon = _epsilon(epsilon)
    radical = math.sqrt(epsilon * epsilon + epsilon)
    roots = [1.0 + epsilon - radical, 1.0 + epsilon + radical]
    return {
        "physical": [root for root in roots if root > 1.0],
        "discarded": [root for root in roots if root <= 1.0],
    }


def physical_root(epsilon: float) -> float:
    return constant_curvature_roots(epsilon)["physical"][0]


def planar_linearization(z: float, kappa0: float) -> dict:
    z, kappa0 = float(z), float(kappa0)
    if z <= 1 or kappa0 <= 0:
        raise ValueError("requires z>1 and kappa0>0")
    omega_squared = (kappa0 * z) ** 2
    return {
        "equation": "DELTA_Z_DOUBLE_PRIME_MINUS_OMEGA2_DELTA_Z_EQUALS_ZERO",
        "omega_squared": omega_squared,
        "growth_rate_per_length": math.sqrt(omega_squared),
        "classification": "LOCALLY_HYPERBOLIC_REDUCED_PLANAR_MODE",
        "full_phase_space_stability_claim": False,
    }


def evaluate(data: dict) -> dict:
    kappa0 = float(data["kappa0"])
    cases = []
    for epsilon in data["epsilon_values"]:
        roots = constant_curvature_roots(epsilon)
        z = roots["physical"][0]
        cases.append({
            "epsilon": epsilon,
            "roots": roots,
            "physical_z": z,
            "stationary_residual": stationary_equation(z, epsilon),
            "kappa_star": kappa0 * z,
            "local_reduced_mode": planar_linearization(z, kappa0),
        })
    return {
        "study_id": data["study_id"],
        "scope": data["scope"],
        "source_formula_ids": data["source_formula_ids"],
        "assumptions": data["assumptions"],
        "cases": cases,
        "derivation_summary": "At planar constant curvature, E46 gives ell-z*ell_z=0. Linearization gives delta_z''-(kappa0*z_star)^2 delta_z=0.",
        "warning": "This reduced result does not establish full constrained stability, energy unboundedness, or nonlinear fate; it only identifies local planar exponential modes.",
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
            print(f"Stationary result differs: {args.output}", file=sys.stderr)
            return 1
        print("Barrier stationary-sector result is current.")
        return 0
    args.output.write_text(expected, encoding="utf-8")
    print(f"Wrote {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
