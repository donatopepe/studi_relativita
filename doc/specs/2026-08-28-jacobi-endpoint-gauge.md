# Jacobi endpoint-frame quotient gate

## Goal

Determine whether oriented antisymmetric vertex-block reversal signal survives physically allowed independent orthonormal choices at source and observer screens.

## Designs

1. Study simultaneous conjugation only: insufficient because a Jacobi map has distinct source and observer spaces.
2. Study independent endpoint rotations `B -> Q_o B Q_s^T` (selected), test orbit invariants and whether transpose/reversal lies in same orbit.
3. Add general nonorthogonal calibration: deferred; it would enlarge nuisance group and cannot restore identifiability lost under orthogonal subgroup.

## Construction

For real `2x2` vertex map `B`, source and observer orthonormal frame changes act by

`B' = Q_o B Q_s^T`, `Q_o,Q_s in SO(2)`.

Full `O(2)xO(2)` orbit is classified by singular values. Under orientation-preserving `SO(2)xSO(2)`, determinant sign is additionally fixed. Since `B^T` has same singular values and determinant, preregister test constructs proper rotations mapping generic `B` to `B^T` when determinant is nonzero, using oriented SVD/polar decomposition or deterministic angle search.

Tests:

- raw antisymmetric scalar changes sign under transpose;
- raw scalar changes under endpoint rotations and is not gauge invariant;
- singular values and determinant remain invariant;
- generic forward block and transpose are in same independent-endpoint `SO(2)xSO(2)` orbit;
- restricting to common anchored frame `Q_o=Q_s` may retain antisymmetric sign, but that restriction requires physical transport certificate;
- rank-deficient and degenerate singular-value cases have enlarged stabilizers;
- `ell0` absent.

## Interpretation

If transpose is endpoint-gauge equivalent, oriented reversal signal from previous exact control is not identifiable unless source/observer frames are physically linked by preregistered transport, orientation and anchor. This is a quotient result, not a statement that raw map lacks information.

Classification `PROJECT_DERIVATION_AND_NEGATIVE_RESULT`. No exact spacetime transport law, data or UMCH mechanism. Smooth profiles and physically linked endpoint frames remain open; no structural dead end.
