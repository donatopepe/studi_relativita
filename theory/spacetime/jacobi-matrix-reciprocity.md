# Exact matrix Jacobi profile-reversal reciprocity

Classification: `EXACT_MATRIX_JACOBI_CONTROL_AND_NEGATIVE_RESULT`.

Status: `JACOBI_MATRIX_PROFILE_REVERSAL_TRANSPOSE_RECIPROCITY_SINGULAR_VALUES_BLIND_NOT_ELL0`; `NO_POSITIVE_DETECTION_CLAIM`.

For piecewise-constant symmetric optical matrices, exact segment maps solve the matrix Jacobi equation. Reversing full ordered profile reverses segment sequence while retaining each segment's length and screen matrix.

Test-first computation initially expected three rotated anisotropic segments to break two-segment transpose reciprocity. It did not. For tested two-, three-, and four-segment profiles,

`B_reverse = B_forward^T`,

where `B` is vertex Jacobi block mapping initial screen velocity to observer displacement. This is consistent with reciprocity for self-adjoint second-order evolution. Consequently vertex determinant, Frobenius norm and singular values remain profile-reversal blind even with fixed Euclidean screen metric. Full phase-space characteristic polynomial is also reversal-blind in tested profiles, while raw full maps and generally raw vertex blocks can differ.

Aligned profiles reduce to independent scalar modes and give identical, not merely transposed, vertex blocks. Rotated anisotropic profiles can expose reversal only through oriented entries or antisymmetric part, requiring source/observer screen frames, orientation and transport fixed consistently. Scalar magnification or shear-strength summaries cannot recover reversal.

This exact finite-product result does not derive a spacetime observable or `ell0`; it identifies a null space in candidate Jacobi scalarizations. It is not a proof for every smooth matrix profile, though it motivates an analytic reciprocity derivation. Exact spacetime optical tidal profiles and covariant screen transport remain open. No structural dead end or reformulation.
