# Sphere connection-derived transport-mixture gate

## Exact geometry

On a unit sphere with Gaussian curvature `K=1`, parallel transport around smooth simple loop enclosing oriented area `A` has angular discrepancy `alpha=A` modulo `2pi` (Gauss--Bonnet, with sign set by orientation). For radius `r`, `K=1/r^2` and `alpha=K A`.

Transport anisotropic tangent operator `D=diag(lambda1,lambda2)` along two admissible paths whose closed difference encloses area A. At anchor, two representatives differ by rotation `Q(alpha)`. Equal mixture

`M=(D+Q D Q^T)/2`

has exact eigenvalues

`(lambda1+lambda2)/2 +- |lambda1-lambda2| |cos alpha|/2`.

Thus connection-derived path holonomy changes mixture spectrum, reaching isotropy at `alpha=pi/2 mod pi`, despite identical local operator spectrum. Spectral shape is even and pi-periodic: signed area/orientation and multiple enclosed areas alias. Landmark is path-area geometry and moves with loop family; `ell0` is absent.

## Classification and scope

`KNOWN_RESULT` only for Gauss--Bonnet relation, supported by Peskin 2026 Courant note. Mixture formula is `PROJECT_DERIVATION_AND_NEGATIVE_RESULT`. Exact two-dimensional sphere tangent geometry; not four-dimensional spacetime, data or UMCH law.

## Decision

Status `SPHERE_HOLONOMY_MIXTURE_SPECTRAL_SHAPE_PATH_AREA_NOT_ELL0`. No structural dead end because exact spacetime bitensors and physically fixed paths remain open. `UNPROVEN`; `NO_POSITIVE_DETECTION_CLAIM`.
