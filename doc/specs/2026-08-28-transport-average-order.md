# Transport versus averaging order gate

## Question

Does finite-window operator average depend on whether local tensors are transported to a common frame before averaging?

## Toy control

Take one anisotropic physical operator represented in two local frames: `A=diag(3,1)` and `B=QAQ^T=diag(1,3)`. Naive coordinate average `(A+B)/2=2I` is isotropic. Transport `B` back by `Q^T` before averaging gives `A`. Thus averaging and frame alignment do not commute.

This is finite-dimensional frame algebra, not covariant spacetime integration.

## Counterexamples and gates

- Raw coordinate averaging can manufacture isotropization and multiplicity change from one unchanged physical operator.
- Pointwise conjugacy invariants averaged first retain local spectrum but discard relative orientation/connection information.
- Transport-then-average needs common anchor, path family and uniqueness certificate; path dependence can change result.
- Average-then-quotient and quotient-then-average are different operations.
- Any spectral landmark from their difference is protocol/frame dependent unless order is fixed prospectively.
- `ell0` remains absent.

## Decision

Status `TRANSPORT_AND_WINDOW_AVERAGING_ORDER_NONCOMMUTATIVE`. No reformulation: covariant exact-region transport integrals remain open. `UNPROVEN`; `NO_POSITIVE_DETECTION_CLAIM`.
