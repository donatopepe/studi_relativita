# Null Jacobi spectrum and caustic gate

Classification: `PROJECT_DERIVATION_AND_NEGATIVE_RESULT`.

Status: `JACOBI_CAUSTIC_GEOMETRIC_LANDMARK_NOT_ELL0`; `NO_POSITIVE_DETECTION_CLAIM`.

For constant diagonal optical-tidal eigenvalue `lambda_i`, solve declared screen ODE

`d_i'' + lambda_i d_i = 0`, with `d_i(0)=0`, `d_i'(0)=1`.

Positive `lambda_i` yields `d_i=sin(sqrt(lambda_i)s)/sqrt(lambda_i)` and first conjugate point `s_c=pi/sqrt(lambda_i)`. Zero gives `d_i=s`; negative gives hyperbolic defocusing and no positive zero in this control.

Caustic position is a genuine geometric focusing landmark after affine normalization, source/observer boundary data and screen convention are fixed. Before that, `s -> alpha s`, `lambda -> lambda/alpha^2` preserves phase and gives `AFFINE_OPTICAL_SCALE_DEGENERACY`. After normalization, measured caustic identifies `1/sqrt(lambda_i)`, not `ell0`: no UMCH-scale variable occurs in ODE.

Degenerate spectra lose anisotropy. General varying optical tidal matrices, path ordering, multiple imaging, parity calibration, caustic crossing noise and nuisance quotient remain open. Sachs (1961), DOI `10.1098/rspa.1961.0202`, supports canonical null-radiation context only; it does not establish this project normalization, UMCH, a floor, or `ell0`.

No core reformulation is triggered.
