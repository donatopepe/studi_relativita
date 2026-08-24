# Paper II-B — Canonical Analysis of the Fixed Curvature Barrier

## Status

Approved follow-up chosen to resolve the Paper III gate as far as the fixed Candidate B permits. The analysis may reject, restrict, or retain Candidate B; it must not force viability.

## Fixed model

In flat `D`-dimensional Minkowski spacetime, use the first-curvature action

\[
S=\int ds\,L(\kappa),\qquad
L(\kappa)=mc\left[-1+\frac{\epsilon}{\kappa/\kappa_0-1}\right],
\qquad \kappa>\kappa_0>0,\quad \epsilon>0.
\]

No alternate barrier or parameter scaling may replace this model after results.

## Objective

Apply published Frenet–Serret variational and Hamiltonian formulas for general `L(κ)` to this fixed barrier, then determine what follows exactly about:

1. derivatives and Hessian rank;
2. Euler–Lagrange equations in curvature variables;
3. canonical momenta and constraints;
4. Poincaré charges;
5. constant-curvature solutions;
6. standard-limit behavior;
7. stability/energy claims that are or are not justified;
8. whether Paper III gate can open.

## Evidence boundary

Published general formulas may be specialized algebraically if their assumptions match. Every imported formula must cite the exact source/equation or passage. Symbolic code checks specialization and identities but is not an independent proof of the underlying formalism.

No full Dirac classification, reduced Hamiltonian, or stability theorem may be claimed unless actually derived. If evidence only establishes one primary constraint and a secondary Hamiltonian constraint for generic `L(κ)`, report exactly that scope.

## Required derivations

### Lagrangian derivatives

Compute `L_κ`, `L_κκ`, domains, signs, and Legendre map invertibility. Check the normal Hessian eigenvalues using published general first-curvature Hessian.

### Equations of motion

Specialize the published equations

\[
(L_\kappa)^2\kappa_2=\text{constant},
\]

\[
L_\kappa''+(L-L_\kappa\kappa)\kappa-L_\kappa\kappa_2^2=0,
\]

and state dimensional/sign conventions. Analyze planar constant-curvature candidates without assuming they exist.

### Canonical structure

Specialize published momenta and Legendre potential. Record primary/secondary constraints and first-class statements only where supported by source and regularity conditions. Check whether the barrier lies in a generic nondegenerate `L_{κκ}\neq0` sector.

### Stability and gate decision

Distinguish:

- existence of a stationary constant-curvature solution;
- local curvature-mode linearization in reduced planar equation;
- full constrained phase-space stability;
- bounded physical energy.

The first two do not prove the latter two. Paper III opens only if full load-bearing dynamics, stability, standard limit, and observable mapping pass. Otherwise state remains blocked/deferred with exact unresolved items.

## Artifacts

- verified source passages and expanded reference log;
- `theory/classical-dynamics/candidate-b-canonical.md`;
- deterministic symbolic specialization under `studies/classical-dynamics/`;
- bilingual audit report addendum;
- bilingual Paper II-B appendix or standalone draft;
- tests and CI compilation.

## Acceptance criteria

1. All formulas have source/equation provenance.
2. Symbolic derivatives and specializations reproduce exactly.
3. Constraint claims state assumptions and class evidence.
4. Constant-curvature equation and linearization are explicit.
5. No local mode result is promoted to full stability.
6. `κ₀→0` is tested along multiple paths.
7. Candidate receives a justified state.
8. Paper III gate receives an explicit `OPEN`, `BLOCKED`, or `DEFERRED` decision.
9. Italian/English artifacts align.
10. Full tests/checks and LaTeX CI pass.

## Out of scope

Curved spacetime, external fields, ALD, quantization, Candidate A, Candidate C, experimental fitting, and changing the fixed barrier.
