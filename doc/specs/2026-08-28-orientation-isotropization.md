# Orientation-family isotropization gate

## Question

Can scale-dependent averaging over orientations create spectral evolution or a rank/multiplicity landmark unrelated to `ell0`?

## Toy control

Use anisotropic symmetric operator `A=diag(3,1)` and its 90-degree rotated form `QAQ^T=diag(1,3)`. Weighted orientation average `R(w)=wA+(1-w)QAQ^T` becomes isotropic at `w=1/2`, where eigenvalues cross and multiplicity changes.

This is finite-dimensional orientation averaging, not a derived spacetime window or observation.

## Counterexamples and gates

- If window scale changes orientation weights, projective spectral shape changes without new curvature law.
- Any target positive scale can be assigned isotropy by choosing a nuisance weight profile with `w(ell_target)=1/2`.
- Symmetric full orientation average erases anisotropy and orientation information.
- Rank/multiplicity/crossing events can therefore be protocol landmarks unless orientation measure is fixed independently.
- Conjugacy quotient does not remove mixture effects: average of conjugates is generally not conjugate to original operator.
- `ell0` remains absent.

## Decision

Status `ORIENTATION_WEIGHT_LANDMARK_PROTOCOL_MOVABLE_NOT_ELL0`. No reformulation: physically fixed orientation measures and exact-region transport remain open. `UNPROVEN`; `NO_POSITIVE_DETECTION_CLAIM`.
