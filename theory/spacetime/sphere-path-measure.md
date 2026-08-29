# Sphere path-measure circular-moment gate

Classification: `KNOWN_RESULT_PLUS_PROJECT_DERIVATION_AND_NEGATIVE_RESULT`.

Status: `SPHERE_PATH_MEASURE_SECOND_CIRCULAR_MOMENT_ONLY_NOT_ELL0`; `NO_POSITIVE_DETECTION_CLAIM`.

On constant-curvature two-sphere, let normalized path family induce holonomy-angle measure `mu`. For anchor operator `D=diag(lambda1,lambda2)`, average

`M_mu=int Q(alpha) D Q(alpha)^T dmu(alpha)`

depends only on complex second circular moment

`m2=int exp(i2alpha)dmu(alpha)`.

Its eigenvalues are

`(lambda1+lambda2)/2 +- |lambda1-lambda2||m2|/2`.

After anchor frame is fixed, full matrix depends only on complex `m2`; spectrum depends only on `|m2|`. Distinct measures with same `m2` give identical matrices. Measures with same magnitude but different phase give conjugate/ispectral matrices. Higher circular moments and path-distribution detail lie in statistic's null space. Many measures satisfy `m2=0` and create isotropy; a deterministic path has `|m2|=1` and preserves anisotropy.

Using Gauss--Bonnet `alpha=K A` modulo orientation/winding translates this to path-area measures. Source and scope are recorded in `references/verification-log.md` under `Peskin2026Gauss`; source does not establish UMCH.

Exact two-sphere algebra only, not four-dimensional spacetime or physical path measure. `ell0` is absent; no core reformulation is triggered.
