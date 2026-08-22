# Candidate B — Canonical specialization

Scientific status: `UNPROVEN`. Fixed barrier unchanged.

## Source scope

Generic first-curvature formulas are imported from Capovilla–Guven–Rojas (`hep-th/0111014`) and identified as `CGR2002-E19` through `CGR2002-E31`. Barrier satisfies generic assumption `L_{κκ}>0` throughout `κ>κ₀`, so it is outside excluded linear/degenerated case.

## Highest momentum — CGR2002-E19

In source notation,

\[
P=\frac{L_\kappa}{\sqrt{-\gamma}}\eta_1.
\]

Thus primary identity `P·Xdot=0` follows geometrically. In proper gauge, coefficient is negative but finite inside domain.

## Conserved momentum — CGR2002-E24

\[
p=(L_\kappa\kappa-L)X'-(L_\kappa)'\eta_1+L_\kappa\kappa_2\eta_2.
\]

Code specializes all three coefficients. Translation invariance gives conservation only on valid equations and boundary assumptions.

## Hessian and Legendre map — CGR2002-E26/E27

Barrier has nonzero radial/transverse normal factors and only tangent null direction in generic source Hessian. Curvature Legendre map is invertible with momentum range negative. This permits source canonical construction; it does not remove reparametrization constraints.

## Hamiltonian — CGR2002-E28/E29

\[
\mathcal H_c=p\cdot\dot X+\sqrt{-\gamma}V,
\qquad V=L_\kappa\kappa-L.
\]

Specialized potential is exact. Canonical Hamiltonian is itself constrained to vanish after consistency; it is not a positive physical energy function.

## Constraint chain — CGR2002-E25/E30/E31

Source generic first-curvature sector states:

1. primary `P·Xdot=0`;
2. consistency gives secondary `H_c=0`;
3. no further constraints;
4. two first-class constraints associated with reparametrization structure;
5. source physical phase-space degree count `2N`.

These claims are source-derived for generic `L(κ)` and apply because `L_{κκ}≠0`; they are not independently re-derived from Poisson brackets here.

## Stability boundary

Two first-class constraints do not prove bounded reduced Hamiltonian. Local planar exponential mode previously derived may be physical or interact with other constrained directions; current specialization cannot decide complete phase-space stability. It does not prove bounded energy, ghost absence/presence, causality, or observability.

## Decision contribution

Canonical existence and constraint closure remove one incompleteness: B has a sourced generic constrained Hamiltonian formulation. Gate remains blocked by reduced stability, standard-limit convergence, and observable mapping.
