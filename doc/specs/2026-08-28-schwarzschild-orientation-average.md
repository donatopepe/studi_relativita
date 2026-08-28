# Schwarzschild-pattern covariant orientation-average gate

## Question

What finite-region spectral shape follows when radial Schwarzschild tidal pattern is averaged over a rotationally symmetric orientation cap after transport to a common Euclidean tangent space?

## Exact angular control

Use normalized pattern `E(n)=I-3nn^T`, equivalent to Schwarzschild principal spectrum `(-2,1,1)` with radial unit vector `n`. Average over spherical cap `0<=theta<=Theta`, uniform solid-angle measure around z-axis. Symmetry gives diagonal average with

`<cos^2 theta>=(1+c+c^2)/3`, `c=cos Theta`,

so

`Ebar=diag((c+c^2)/2,(c+c^2)/2,-c-c^2)`.

For caps below hemisphere (`c>0`) this lies on ray `diag(1/2,1/2,-1)`. Above hemisphere (`-1<c<0`) coefficient changes sign, giving opposite signed ray; hemisphere and full sphere are zeros (`c=0` or `c=-1`). Thus cap size preserves eigenvalue multiplicity and axial pattern but can create a zero/sign reversal from orientation-domain measure alone.

## Scope/gates

This is exact sphere integration of Schwarzschild algebraic tidal pattern after assumed common-space alignment. It is not parallel transport in Schwarzschild spacetime and ignores radial amplitude variation. It supplies counterexample: rotational orientation family preserves axial spectral shape within each sign sector, while domain expansion alone creates a zero and signed-ray reversal at hemisphere. Such landmark is an orientation-domain effect, not `ell0`.

## Decision

Status `SCHWARZSCHILD_CAP_AVERAGE_SIGN_REVERSAL_ORIENTATION_DOMAIN_NOT_ELL0`. No reformulation: covariant spacetime transport with radial variation remains open. `UNPROVEN`; `NO_POSITIVE_DETECTION_CLAIM`.
