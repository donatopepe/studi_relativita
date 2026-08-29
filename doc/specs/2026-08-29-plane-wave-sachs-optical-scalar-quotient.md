# Exact plane-wave Sachs optical-scalar calibration quotient

## Objective

Extend full Jacobi map into explicit Sachs optical matrix along exact vacuum plane-wave null propagation:

\[
\mathcal S(u)=D(u)B(u)^{-1},
\]

where `B,D` are vertex displacement/derivative blocks. Decompose

\[
\mathcal S=\theta I+\Sigma+\omega J,
\]

with expansion `theta=tr(S)/2`, symmetric trace-free shear `Sigma`, and twist coefficient from antisymmetric part. Test what survives endpoint screen rotations, canonical lower shear calibration, profile reversal, affine/profile scaling, and caustics.

Classification: `EXACT_SPACETIME_SACHS_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT`.

## Alternatives

1. **Only endpoint eigenvalues:** already shown calibration-dependent and omits twist/shear decomposition.
2. **Integrate abstract Sachs scalars:** risks losing connection-derived boundary and full-map provenance.
3. **Selected:** derive `S=DB^{-1}` directly from exact full Jacobi propagation and calculate scalar/tensor pieces before quotient.

## Counterexample-first contract

- Require invertible `B`; otherwise return `CAUSTIC_OR_VERTEX_BLOCK_SINGULAR` and do not interpret optical scalars.
- Under common oriented screen rotation `Q in SO(2)`, `S -> QSQ^T`: expansion and twist coefficient remain invariant, shear components rotate while shear norm is invariant.
- Under observer lower canonical shear `S(H_o)`, optical matrix transforms additively:
  \[
  \mathcal S' = \mathcal S+H_o,\qquad H_o=H_o^T.
  \]
  Thus expansion and shear are movable; antisymmetric twist is preserved by this bounded nuisance.
- For the symmetric tidal Jacobi equation with vertex boundary data, the exact optical matrix should remain symmetric away from caustics, so twist is zero within numerical tolerance. A calibration-invariant twist channel then carries no signal in this class.
- Profile reversal exchanges source/observer optical matrices rather than supplying a label-free orientation invariant.
- Under affine/profile scaling, `S_s=S/s`; dimensionless `L S` and its expansion/shear/twist pieces are invariant. Absolute scale remains absent.

## Expected result

Expected status:

`EXACT_PLANE_WAVE_SACHS_EXPANSION_SHEAR_CALIBRATION_MOVABLE_TWIST_ZERO_AFFINE_SCALE_BLIND_NOT_ELL0`.

Open gate:

`PHYSICAL_SACHS_ENDPOINT_CALIBRATION_TWIST_SOURCE_AND_ELL0_LAW_NOT_DERIVED`.

This does not show that twist vanishes in all congruences or spacetimes. Non-vertex boundary data, rotating congruences, nontrivial screen transport, caustic continuation, detector-derived standards, causal windows, and other geometries remain open. Coley–McNutt–Milson supports exact plane waves and curvature-driven geodesic deviation, not selected Sachs detector protocol, calibration nuisance, UMCH, `ell0`, or detection.

UMCH remains `UNPROVEN`; conclusion remains `NO_POSITIVE_DETECTION_CLAIM`. No structural dead end.
