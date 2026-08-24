#!/usr/bin/env python3
"""Specialize sourced generic L(kappa) canonical expressions to fixed barrier."""

from __future__ import annotations

import argparse
import json
import math
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
DEFAULT_INPUT = HERE / "barrier-canonical-cases.json"
DEFAULT_OUTPUT = HERE / "barrier-canonical-results.json"


def _domain(z: float, epsilon: float) -> tuple[float, float]:
    z, epsilon = float(z), float(epsilon)
    if z <= 1 or epsilon <= 0:
        raise ValueError("Requires z>1 and epsilon>0")
    return z, epsilon


def ell(z: float, epsilon: float) -> float:
    z, epsilon = _domain(z, epsilon)
    return -1.0 + epsilon / (z - 1.0)


def ell_z(z: float, epsilon: float) -> float:
    z, epsilon = _domain(z, epsilon)
    return -epsilon / (z - 1.0) ** 2


def ell_zz(z: float, epsilon: float) -> float:
    z, epsilon = _domain(z, epsilon)
    return 2.0 * epsilon / (z - 1.0) ** 3


def inverse_momentum(p: float, epsilon: float) -> float:
    p, epsilon = float(p), float(epsilon)
    if p >= 0 or epsilon <= 0:
        raise ValueError("Dimensionless momentum ell_z has range (-infinity,0)")
    return 1.0 + math.sqrt(-epsilon / p)


def legendre_potential(z: float, epsilon: float) -> float:
    return z * ell_z(z, epsilon) - ell(z, epsilon)


def hessian_factors(z: float, epsilon: float) -> dict:
    z, epsilon = _domain(z, epsilon)
    # CGR2002-E26, omitting common nonzero metric/gauge scale factors.
    radial = z * ell_zz(z, epsilon)
    transverse = ell_z(z, epsilon)
    return {
        "radial": radial,
        "transverse_normal": transverse,
        "tangent": 0.0,
        "classification": "ONE_TANGENT_NULL_DIRECTION" if radial != 0 and transverse != 0 else "ADDITIONAL_DEGENERACY",
    }


def evaluate(data: dict) -> dict:
    epsilon = float(data["epsilon"])
    samples = []
    for z in data["samples"]:
        samples.append({
            "z": z,
            "ell": ell(z, epsilon),
            "ell_z": ell_z(z, epsilon),
            "ell_zz": ell_zz(z, epsilon),
            "legendre_potential": legendre_potential(z, epsilon),
            "hessian": hessian_factors(z, epsilon),
        })
    return {
        "study_id": data["study_id"],
        "epsilon": epsilon,
        "source_formula_ids": data["source_formula_ids"],
        "conventions": data["conventions"],
        "samples": samples,
        "legendre_sector": "GENERIC_LKK_NONZERO",
        "momentum_range": "(-infinity,0)",
        "warning": "This specialization does not prove reduced Hamiltonian boundedness, stability, or causality; it only establishes generic Hessian factors and curvature Legendre invertibility.",
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
            print(f"Canonical specialization differs: {args.output}", file=sys.stderr)
            return 1
        print("Barrier canonical specialization is current.")
        return 0
    args.output.write_text(expected, encoding="utf-8")
    print(f"Wrote {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
