# Jacobi endpoint-frame quotient

Classification: `PROJECT_DERIVATION_AND_NEGATIVE_RESULT`.

Status: `JACOBI_TRANSPOSE_REVERSAL_NONIDENTIFIABLE_UNDER_INDEPENDENT_ENDPOINT_FRAME_QUOTIENT`; `NO_POSITIVE_DETECTION_CLAIM`.

A vertex Jacobi block maps source-screen data to observer-screen data. Independent oriented orthonormal endpoint-frame changes act by

`B -> Q_o B Q_s^T`, with `Q_o,Q_s in SO(2)`.

This is a left-right action, not simultaneous conjugation. For every real `2x2` block `B`, let

`phi = atan2(B21-B12, B11+B22)`.

Direct multiplication gives

`B^T = R(-phi) B R(phi)^T`.

Therefore `B` and reversal block `B^T` lie in the same independent endpoint `SO(2) x SO(2)` orbit, including rank-deficient cases. Their singular values and determinant coincide, as expected. Raw oriented scalar `(B12-B21)/2` changes sign under transpose, but also changes under endpoint-frame rotations and is not quotient-invariant.

A common anchored rotation `Q_o=Q_s` is a smaller conjugation action and does not generically identify `B` with `B^T`. Retaining oriented reversal information therefore requires a physical certificate linking source and observer screens: anchor, handedness, transport path, boundary convention and calibration fixed prospectively. Merely choosing matching coordinates is insufficient.

This exact algebraic control does not derive screen transport from a four-dimensional spacetime connection. It does not claim detector observability or identify `ell0`; reversal order remains geometric. Smooth connection-derived profiles and physically anchored endpoint frames remain open, so no structural dead end or reformulation follows.
