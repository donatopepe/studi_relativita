# Exact matrix Jacobi rotated-segment gate

## Goal

Move from scalar exact segments to exact two-dimensional optical matrices with rotated eigenframes, while retaining closed-form propagators.

## Construction

For symmetric positive `K=Q diag(lambda1,lambda2) Q^T`, exact phase-space propagator is block spectral function

`P(K,L)=[[C,S],[-K S,C]]`,

where `C=Q diag(cos(sqrt(lambda_i)L)) Q^T` and `S=Q diag(sin(sqrt(lambda_i)L)/sqrt(lambda_i)) Q^T`.

Choose `K1=diag(1,4)` and `K2=Q(theta)diag(2,5)Q(theta)^T`. Reverse two segments. Because products `P2P1` and `P1P2` are similar, full 4x4 spectrum is order-blind. Unlike scalar 2x2 case, vertex Jacobi block `B=M[0:2,2:4]` is expected to change under reversal when eigenframes rotate. Test determinant, singular values, Frobenius norm and matrix difference. Singular values require fixed Euclidean screen metric; determinant is screen-basis invariant under matched orthogonal source/observer frames but not arbitrary independent calibration.

## Counterexamples

- `theta=0` aligned diagonal profiles decouple into scalar modes and vertex block is reversal-blind.
- repeated eigenvalues make rotation irrelevant.
- generic rotation can make full vertex block order-sensitive while total-map spectrum remains blind.
- any observed scale dependence is optical geometry/profile, not ell0.

## Decision

Classification `EXACT_MATRIX_JACOBI_CONTROL_AND_NEGATIVE_RESULT`; expected status `JACOBI_EXACT_MATRIX_TOTAL_SPECTRUM_ORDER_BLIND_VERTEX_BLOCK_ROTATION_SENSITIVE_NOT_ELL0`. Exact piecewise-constant matrix optics, not smooth Sachs spacetime solution. No structural dead end or reformulation.
