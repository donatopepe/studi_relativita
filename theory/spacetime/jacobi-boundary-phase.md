# Jacobi boundary-phase caustic

Classification: `PROJECT_DERIVATION_AND_NEGATIVE_RESULT`.

Status: `JACOBI_CAUSTIC_BOUNDARY_PHASE_MOVABLE_NOT_ELL0`; `NO_POSITIVE_DETECTION_CLAIM`.

For constant positive `lambda`, general scalar solution is

`d(s)=d0 cos(sqrt(lambda)s)+(v0/sqrt(lambda)) sin(sqrt(lambda)s)`.

Vertex boundary data `d0=0,v0=1` give first positive zero `pi/sqrt(lambda)`. With general nontrivial `(d0,v0)`, phase changes zero location. For any target strictly inside first half-period, choosing

`v0=-sqrt(lambda)d0 cot(sqrt(lambda)s_target)`

places first positive zero at target. Common scaling of both boundary values leaves zeros unchanged; phase ratio controls location. Zero initial data gives trivial unusable channel.

Therefore curvature eigenvalue alone does not fix caustic under unrestricted source boundary data. Vertex/source contract, affine normalization, screen convention and observer condition must be fixed independently before calling zero geometric landmark. Even then it measures focusing geometry, not `ell0`, absent from ODE.

This is exact algebra for constant scalar ODE only. Varying matrix optics remain open; no core reformulation is triggered.
