# Candidate A — Fixed normalized hard-constraint dynamics

Core status: `UNPROVEN`.

## Fixed action

\[
g=1-\kappa/\kappa_0\le0,\qquad
S=S_0+mc\int ds\,\lambda g,
\quad \lambda\ge0,\quad \lambda g=0.
\]

`λ` is dimensionless. KKT algebra does not define evolution.

## Smooth inactive interval

When `κ>κ₀`, complementarity forces `λ=0`; effective action is free particle. Classification: `INACTIVE_FREE_BRANCH`. But a free solution is geodesic `κ=0`, outside feasible set for positive `κ₀`; therefore generic inactive free evolution does not remain feasible without transition/constraint forces. This is a structural tension, not global theorem.

## ACTIVE_BOUNDARY_BRANCH — Smooth active interval

When `κ=κ₀`, multiplier may be positive. For prescribed smooth λ,

\[
L/(mc)=-1+\lambda-(\lambda/\kappa_0)\kappa.
\]

At fixed λ this is linear in curvature: `LINEAR_CURVATURE_DEGENERATE_SECTOR`, with `L_{κκ}=0`. If λ varies, sourced general formulas involve λ derivatives. Constraint equation simultaneously fixes κ. Complete coupled variation in x and λ is not derived by substituting after variation.

## Transitions

Switching inactive→active can generate jumps in λ or derivatives. Since E42 contains second derivatives of `L_κ∝λ`, jumps produce distributional terms. Classification: `DISTRIBUTIONAL_MATCHING_REQUIRED`. No covariant matching rule, impulse law, or admissible regularity class is derived; global dynamics is not derived.

## Initial data and well-posedness

Ideal geodesic data are KKT infeasible for every positive κ₀. Smooth active data require κ=κ₀ plus additional multiplier/derivative compatibility not yet specified. Global existence, uniqueness, continuous dependence, and preservation of feasible set are not derived.

## Limit

At κ₀=0 normalized expression is undefined. Taking κ₀→0 changes coefficients `λ/κ₀`; recovery needs multiplier scaling and solution convergence, not only feasible-set convergence. This remains unresolved.

## Observable

No data→κ₀ mapping exists. Constraint reaction multiplier is not an observable without coupling and measurement protocol.

## Decision status

Currently `INCOMPLETE`. Evidence derives only `SMOOTH_BRANCHES_ONLY`; global dynamics not derived. Fixed candidate will fail gate if transition/well-posedness and standard-limit requirements remain absent.
