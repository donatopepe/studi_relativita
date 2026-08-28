# Finite holonomy ordering and conjugacy gate

## Question

Can finite-loop segment ordering produce identifiable scale shape beyond leading linearized holonomy?

## Toy control

Use invertible 2x2 segment maps `A(t)=I+tX` and `B(t)=I+tY`. Compare ordered products `AB` and `BA`. This is finite-dimensional matrix algebra, not a derived spacetime connection or exact holonomy.

## Counterexamples and gates

- Noncommuting generators give different raw matrices at order `t^2`.
- For invertible `A`, `BA=A^{-1}(AB)A`; opposite cyclic starting points are conjugate and share trace, determinant and eigenvalues.
- Thus raw matrix order difference can be base-point/frame representation, not conjugacy-invariant shape.
- Singular values are not invariant under arbitrary similarity and require a fixed metric/frame convention.
- Non-cyclic permutations or different paths may carry geometric information, but path family, anchor, transport and quotient must be fixed.
- `ell0` remains absent from toy.

## Decision

Status `FINITE_HOLONOMY_RAW_ORDER_DIFF_CONJUGACY_AMBIGUOUS`. No reformulation: exact connection-derived loops and non-cyclic path families remain open. `UNPROVEN`; `NO_POSITIVE_DETECTION_CLAIM`.
