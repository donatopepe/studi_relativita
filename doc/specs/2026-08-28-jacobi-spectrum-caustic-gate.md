# Constant optical-tidal Jacobi spectrum and caustic gate

## Question

Can null Jacobi-map eigenvalues or caustic/parity landmarks identify `ell0`?

## Scoped control

For a diagonal constant optical tidal matrix with eigenvalues `lambda_i`, solve scalar screen equations `d_i'' + lambda_i d_i = 0`, vertex initial data `d_i(0)=0`, `d_i'(0)=1`. Thus `d_i(s)=sin(sqrt(lambda_i)s)/sqrt(lambda_i)` for positive lambda, `s` for zero, and `sinh(sqrt(-lambda_i)s)/sqrt(-lambda_i)` for negative lambda.

This is a deterministic exact solution of the declared constant-coefficient ODE, not a claim about arbitrary GR spacetime or UMCH.

## Counterexamples and gates

- Positive focusing eigenvalue gives first conjugate/caustic affine distance `pi/sqrt(lambda)`.
- Zero/negative eigenvalues have no positive zero in this control.
- Rescaling affine parameter and optical eigenvalue (`s -> alpha s`, `lambda -> lambda/alpha^2`) preserves dimensionless phase unless affine normalization is independently fixed.
- Even with fixed affine normalization, caustic identifies geometric focusing scale `1/sqrt(lambda)`, not `ell0`; `ell0` is absent without a theory link.
- Degenerate isotropic spectra erase anisotropy; screen-basis rotations preserve eigenvalues but calibration/boundary/source data remain required.

## Decision

Status `JACOBI_CAUSTIC_GEOMETRIC_LANDMARK_NOT_ELL0`. No reformulation: cross-channel transport and boundary families remain open. `UNPROVEN`; `NO_POSITIVE_DETECTION_CLAIM`.
