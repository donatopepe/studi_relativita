#!/usr/bin/env python3
"""Specialize sourced generic first-curvature momenta and constraint chain."""

from __future__ import annotations

import argparse
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
DEFAULT_INPUT = HERE / "barrier-constraint-cases.json"
DEFAULT_OUTPUT = HERE / "barrier-constraint-results.json"


def _domain(z, epsilon, kappa0, mc):
    values = tuple(float(value) for value in (z, epsilon, kappa0, mc))
    if values[0] <= 1 or any(value <= 0 for value in values[1:]):
        raise ValueError("requires z>1 and positive epsilon, kappa0, mc")
    return values


def coefficients(z, epsilon, kappa0, mc, kappa2=0.0, z_prime=0.0):
    z, epsilon, kappa0, mc = _domain(z, epsilon, kappa0, mc)
    kappa = kappa0 * z
    ell = -1.0 + epsilon / (z - 1.0)
    ell_z = -epsilon / (z - 1.0) ** 2
    ell_zz = 2.0 * epsilon / (z - 1.0) ** 3
    L = mc * ell
    L_kappa = mc * ell_z / kappa0
    L_kappa_prime = mc * ell_zz * float(z_prime) / kappa0
    potential = L_kappa * kappa - L
    return {
        "L": L,
        "L_kappa": L_kappa,
        "L_kappakappa": mc * ell_zz / kappa0**2,
        "highest_momentum_eta1_coefficient_proper_gauge": L_kappa,
        "tangent_coefficient": potential,
        "minus_Lkappa_prime_eta1_coefficient": -L_kappa_prime,
        "eta2_coefficient": L_kappa * float(kappa2),
        "legendre_potential": potential,
        "primary_constraint_residual_P_dot_velocity": 0.0,
    }


def evaluate(data):
    samples = [coefficients(**sample) for sample in data["samples"]]
    return {
        "study_id": data["study_id"],
        "source_formula_ids": data["source_formula_ids"],
        "samples": samples,
        "barrier_meets_generic_assumption_Lkk_nonzero": all(sample["L_kappakappa"] > 0 for sample in samples),
        "constraint_chain": "ONE_PRIMARY_PLUS_ONE_SECONDARY",
        "primary": "P_DOT_XDOT_EQUALS_ZERO",
        "secondary": "CANONICAL_HAMILTONIAN_EQUALS_ZERO",
        "class_status": "TWO_FIRST_CLASS_IN_SOURCE_GENERIC_SECTOR",
        "closure": "NO_OTHER_CONSTRAINTS_IN_SOURCE_GENERIC_SECTOR",
        "physical_phase_space_degrees_of_freedom_source_notation": "2N",
        "reduced_hamiltonian_boundedness_derived": False,
        "full_stability_derived": False,
        "warning": "Source constraint classification applies to generic first-curvature L(kappa) sector and this barrier meets Lkk!=0; specialization does not prove bounded reduced energy, stability, causality, or observability.",
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
            print(f"Constraint result differs: {args.output}", file=sys.stderr)
            return 1
        print("Barrier constraint specialization is current.")
        return 0
    args.output.write_text(expected, encoding="utf-8")
    print(f"Wrote {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
