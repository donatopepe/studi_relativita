# Exact finite-product Jacobi reversal involution

Classification: `PROJECT_DERIVATION_AND_EXACT_MATRIX_CONTROL`.

Status: `JACOBI_FINITE_SYMMETRIC_PROFILE_REVERSAL_EXACT_BLOCK_TRANSPOSE_RECIPROCITY_NOT_ELL0`; `NO_POSITIVE_DETECTION_CLAIM`.

Let an exact symmetric optical segment act on displacement/velocity phase space. Define block-exchange matrix

`E=[[0,I],[I,0]]`

and anti-involution

`R(P)=E P^T E`.

Each segment `P(K,L)=[[C,S],[-KS,C]]` with symmetric `K` and commuting symmetric spectral functions is fixed by `R`. Also

`R(XY)=R(Y)R(X)`.

Therefore, for any finite ordered product of such segments, propagator of completely reversed profile is exactly `R(P_forward)`. If

`P_forward=[[A,B],[C,D]]`,

then

`P_reverse=[[D^T,B^T],[C^T,A^T]]`.

In particular vertex Jacobi block obeys `B_reverse=B_forward^T`. This proves, within finite-product scope, numerical reciprocity pattern previously tested for two, three and four segments. Vertex singular values, determinant and Frobenius norm are reversal-blind. Oriented antisymmetric scalar `(B12-B21)/2` changes sign in fixed endpoint frames and can retain direction only after endpoint screen orientation and transport are fixed.

This derivation does not claim smooth covariant Sachs reciprocity or physical observability in an exact spacetime. It excludes finite symmetric segment count as route to reversal information through SVD-based scalarizations. It does not introduce `ell0`; optical profile order remains geometric. Smooth connection-derived profiles, screen transport and cross-channel laws remain open, so no structural dead end or reformulation follows.
