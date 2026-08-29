# Exact matrix Jacobi rotated-segment gate

Classification: `EXACT_MATRIX_JACOBI_CONTROL_AND_NEGATIVE_RESULT`.

Status: `JACOBI_EXACT_MATRIX_SPECTRUM_AND_VERTEX_SINGULAR_VALUES_ORDER_BLIND_BLOCK_TRANSPOSE_SENSITIVE_NOT_ELL0`; `NO_POSITIVE_DETECTION_CLAIM`.

For symmetric positive optical matrix `K=Q diag(lambda_i)Q^T`, exact segment propagator is

`P(K,L)=[[C,S],[-KS,C]]`,

with spectral matrix functions `C=cos(sqrt(K)L)` and `S=sin(sqrt(K)L)/sqrt(K)`. Propagator is symplectic.

For two segments with rotated eigenframes, `P2P1` and `P1P2` are similar, so full phase-space characteristic polynomial is order-blind. Their vertex Jacobi blocks generally differ. Test-first algebra reveals stronger reciprocity than expected: reversed vertex block is transpose of forward block. Hence determinant, Frobenius norm and singular values coincide exactly. Only oriented block entries or antisymmetric part retain reversal information after source/observer screen frames and transport are fixed.

Aligned eigenframes or isotropic segment make vertex blocks identical. Thus rotated matrix profiles break raw block equality but not orthogonal left-right invariants. A scalar magnification/shear-strength channel based on singular values remains order-blind.

This is exact piecewise-constant matrix optics, not smooth Sachs integration in exact spacetime. Screen metric, orientation, boundary, affine normalization and transport remain required. Optical order is geometric; `ell0` is absent. Smooth connection-derived profiles remain open, so no structural dead end or reformulation is triggered.
