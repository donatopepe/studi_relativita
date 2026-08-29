# Sphere connection-derived transport mixture

Classification: `KNOWN_RESULT_PLUS_PROJECT_DERIVATION_AND_NEGATIVE_RESULT`.

Status: `SPHERE_HOLONOMY_MIXTURE_SPECTRAL_SHAPE_PATH_AREA_NOT_ELL0`; `NO_POSITIVE_DETECTION_CLAIM`.

On constant-curvature two-sphere, Gauss--Bonnet relates parallel-transport angular discrepancy around smooth simple loop to integrated Gaussian curvature, modulo `2pi` and orientation sign. For constant `K`, write `alpha=K A`.

Transport `D=diag(lambda1,lambda2)` along two paths whose closed difference encloses area `A`. At anchor, representatives differ by `Q(alpha)`. Equal mixture

`M=(D+Q D Q^T)/2`

has eigenvalues

`(lambda1+lambda2)/2 +- |lambda1-lambda2||cos alpha|/2`.

Thus connection-derived path holonomy changes mixture spectrum and makes it isotropic at `alpha=pi/2 mod pi`, although local operator spectra are identical. Mixture spectrum is even and `pi`-periodic, aliasing orientation and multiple path areas. Landmark depends on chosen path family and enclosed area, not `ell0`.

Known relation source: Charles S. Peskin, *Parallel Transport and Gaussian Curvature*, Courant Institute note, January 2026, https://math.nyu.edu/~peskin/gauss.pdf. It supports local Gauss--Bonnet/parallel-transport relation, not UMCH.

This is exact two-sphere tangent geometry with equal two-path mixture, not four-dimensional spacetime or data. Physical path measures and exact spacetime bitensors remain open; no core reformulation is triggered.
