# Exact Jacobi two-segment order-versus-spectrum gate

## Goal

Upgrade second-order path-order toy to exact scalar Jacobi propagators and separate conjugacy spectrum from boundary endpoint information.

## Exact construction

For `d''+lambda d=0`, `lambda>0`, segment length `L`, phase-space propagator on `(d,d')` is

`P(lambda,L)=[[cos(wL),sin(wL)/w],[-w sin(wL),cos(wL)]]`, `w=sqrt(lambda)`, with determinant one.

For two distinct segments, forward/reverse maps are `M21=P2 P1` and `M12=P1 P2`. Since each propagator is invertible, `M12=P1 M21 P1^-1`; therefore maps are similar and have identical determinant, trace, eigenvalues and characteristic polynomial. Yet matrices generally differ. With vertex source vector `(0,1)`, observer displacement is `(M)01` and generally changes under reversal.

## Counterexample meaning

- Total conjugacy spectrum cannot identify segment order.
- Boundary endpoint can identify some order information only after source/observer phase-space basis, affine normalization and screen transport are fixed.
- Same unordered local spectra, lengths and total-map eigenvalues can yield different endpoint displacement.
- At special parameters endpoints may collide, so endpoint map is not globally order-injective.
- No ell0 appears; phases measure optical geometry.

## Scope and decision

Classification `EXACT_JACOBI_CONTROL_AND_NEGATIVE_RESULT`; expected status `JACOBI_EXACT_TOTAL_SPECTRUM_ORDER_BLIND_BOUNDARY_ENDPOINT_ORDER_SENSITIVE_NOT_ELL0`. Exact piecewise-constant scalar optical profile, not smooth matrix Sachs system or exact spacetime solution. Structural dead-end criteria fail; varying matrix geometry and physical boundaries remain open. No reformulation.
