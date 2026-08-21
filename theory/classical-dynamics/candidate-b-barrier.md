# Candidate B — Pointwise curvature barrier

Scientific status: `UNPROVEN`  
Hypothesis class: `POINTWISE_UMCH`

## Domain

Regular timelike worldlines with `κ>κ₀`. Candidate is divergent at `κ=κ₀` and outside real finite domain for `κ≤κ₀`. Thus every ideal geodesic is excluded for fixed `κ₀>0`.

## Preregistered functional

Choose one representative, without post-result tuning: `f(z)=1/(z-1)` with coefficient `εmc`.

\[
S_B[x]=-mc\int ds+\epsilon mc\int ds\,f(z),
\qquad z=\frac{\kappa}{\kappa_0}>1,
\qquad f(z)=\frac{1}{z-1}.
\]

`ε` is dimensionless, `[mc]=M L T⁻¹`, `[ds]=L` (`LENGTH`); therefore each term has action dimension `[S]=M L² T⁻¹`. `f` and `z` are dimensionless. This checks dimensions, not physical correctness.

## Analysis level

- `SYMBOLIC`: exact elementary properties of `f` and selected limits.
- `VARIATIONAL`: derivative-order statement under nondegenerate local embedding variation.
- `CONJECTURAL`: constraint algebra, physical degrees of freedom, stability, causality, and observables.

## Exact barrier behavior

For `z>1`,

\[
f'(z)=-\frac{1}{(z-1)^2}<0,
\qquad
f''(z)=\frac{2}{(z-1)^3}>0.
\]

It diverges as `z→1⁺` and vanishes as `z→∞`. Code reproduces sample values and rejects points outside domain.

## Differential order and boundary data

In proper-time gauge, `κ` depends on second derivatives of worldline embedding. For nonlinear `f(κ/κ₀)` with nonzero second derivative, a generic nondegenerate Euler--Lagrange expression in embedding variables can contain up to fourth derivatives. This is derivative counting, not completed covariant equations.

Varying requires boundary conditions for position and appropriate first-derivative data, or compensating boundary terms. Reparametrization invariance makes action degenerate and generates constraints, so raw fourth-order counting does not equal a count of physical modes.

No Ostrogradsky instability conclusion is made. The constraint analysis remains incomplete; consequently there is no stability conclusion, no ghost count, and no bounded-energy claim.

## Standard limit `κ₀→0`

With fixed `ε`:

1. Fixed `κ=K>0`: `z→∞`, so barrier contribution density vanishes pointwise.
2. Boundary-layer path `κ=rκ₀`, fixed `r>1`: `f(r)` remains finite and nonzero.
3. Geodesic `κ=0`: outside domain for every `κ₀>0`.

Therefore limit is `NONUNIFORM`. Pointwise vanishing on fixed positive-curvature curves does not show convergence to the full standard solution space or initial-value problem.

## Constraints, conservation, causality

Geometric action is reparametrization invariant, but complete primary/secondary constraints have not been derived for this exact barrier. Poincaré symmetry suggests conserved charges in flat spacetime once valid equations/boundary terms exist; their explicit form is absent. Causal and well-posed evolution is not established.

## Observable

None derived. Barrier excludes a region of curve space but supplies no experiment-to-`κ₀` mapping without solved dynamics and initial data.

## Reproducible check

`studies/classical-dynamics/barrier_check.py` verifies domain, monotonicity/convexity samples, dimensions, and three preregistered limit paths. It does not derive dynamics or validate UMCH.

## Decision

State remains `INCOMPLETE`. Exact barrier and dimensions are well specified, but nonuniform standard limit, excluded geodesics, missing constrained Hamiltonian analysis, and missing observable block viability claims.
