# Candidate A — Hard pointwise constraint

Scientific status: `UNPROVEN`  
Hypothesis class: `POINTWISE_UMCH`

## Domain

Regular timelike worldlines for which proper worldline curvature `κ` is defined. At `κ=0` the scalar can be defined from acceleration, but the Frenet normal is not fixed. For fixed `κ₀>0`, geodesic data are infeasible by construction.

## Candidate functional and sign convention

Use the schematic constrained functional

\[
S_A[x,\lambda]=S_0[x]+\int ds\,\lambda(s)g(s),
\qquad g=\kappa_0-\kappa\le0,
\]

In compact Unicode notation: `g=κ₀-κ≤0`, `λ≥0`, `λg=0`. With algebraic KKT convention

\[
\lambda\ge0,\qquad g\le0,\qquad \lambda g=0.
\]

Choice of extremization sign and boundary terms must be reconciled with the complete varied action. Current checker verifies only this declared algebra.

## Analysis level

- `KINEMATIC`: `κ≥κ₀` defines feasible curves.
- `CONSTRAINT`: only algebraic KKT feasibility/complementarity is checked.
- `CONJECTURAL`: worldline Euler--Lagrange and canonical structure.
- `NO_GO_CONDITIONAL`: geodesic initial data with `κ=0` are excluded for every fixed `κ₀>0`.

## FEASIBILITY branches

- Interior: `κ>κ₀`, hence `g<0`; complementarity requires `λ=0`.
- Boundary: `κ=κ₀`; `λ≥0` may be active.
- Infeasible: `κ<κ₀`, independent of multiplier choice.

These are pointwise algebraic statements, not equations of motion.

## ACTIVE-SET issue

Evolution may encounter `κ=κ₀`, where multiplier activation can change differential equations or regularity. This candidate does not derive matching/jump conditions, uniqueness, or continuous dependence. Therefore well-posed active-set evolution remains `INCOMPLETE`.

## Variation, boundary terms, and differential order

Worldline `κ` contains second derivatives of embedding in proper-time gauge. Varying an integral linear in `κ` generally produces derivatives of variations and requires explicit endpoint data and boundary terms. Reparametrization invariance makes naive derivative counting insufficient for physical degrees of freedom.

No Dirac first-/second-class constraint classification is claimed. Literature supplies methods, not this candidate's completed analysis.

## Initial data and equivalence tension

For `κ₀>0`, data corresponding to ideal geodesic motion (`κ=0`) are outside feasible set. Thus standard freely falling initial data are not approached at fixed positive `κ₀`. This is a direct conditional conflict with pointwise geodesic free fall, unless the theory changes the observable or physical meaning of free fall.

## Standard limit

At exactly `κ₀=0`, geodesic `κ=0` is feasible and active with `λ=0` in the preregistered algebraic case. This shows set-level inclusion only. It does not derive convergence of solutions, multiplier forces, observables, or initial-value problems as `κ₀→0`.

## Observable

None derived. A feasible-set restriction does not map to measured residual acceleration without complete dynamics.

## Reproducible check

`studies/classical-dynamics/hard_constraint_check.py` classifies preregistered interior, active, infeasible, and zero-limit cases. Passing it does not derive stability, conservation, causality, or equations.

## Decision

State remains `INCOMPLETE`. Conditional result: pointwise hard constraint excludes geodesic initial data for fixed `κ₀>0`; only exact zero-limit algebra recovers their feasibility. A viable theory needs covariant nonsmooth variation, active-set evolution, constraint analysis, and observational mapping.
