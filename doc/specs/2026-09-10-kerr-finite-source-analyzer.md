# Kerr finite Gaussian source covariance and endpoint analyzer

## Status

`RATIFIED_FOR_IMPLEMENTATION_PLANNING`

Human authorized continuation after the Kerr Jacobi gate. This specification selects the smallest source/readout preparation layer that can test whether the orientation-sensitive Jacobi shape survives finite source spread and scalar endpoint projection. It does not define physical emission, hardware, noise, data, or evidence.

## MVP-first gate

**Objective:** determine whether the verified finite-boundary Kerr Jacobi orientation shape survives a declared finite Gaussian phase-space source covariance and endpoint analyzer scan, while exposing preparation/analyzer collisions and retaining the exact absolute-scale null.

**Metric and threshold:** correctness over exactly eight preregistered controls; threshold `8/8`.

**Cases and order:** source covariance domain, covariance propagation, width homogeneity, orientation survival, analyzer extrema, common-basis covariance, analyzer collision, and joint scaling/rank/no-`ell0`.

**MVP:** propagate one diagonal positive Gaussian covariance through the existing dimensionless `4x4` Kerr Jacobi phase map and project its observer position covariance onto ideal real analyzer axes. No source dynamics, polarization interaction, intensity calibration, detector noise, likelihood, data, or 5D Kerr model.

**Escalation condition:** add receiver/noise or physical source dynamics only if all eight controls pass and the named blocker is lack of a calibrated statistical observation model. If analyzer collisions erase branch distinction, preserve the negative result rather than tuning preparation.

## Dimensionless phase-space convention

Use source state

```text
z_bar=(X_1/M,X_2/M,V_1,V_2)
V=dX/dlambda
```

and convert the dimensional Jacobi map `P=[[A,B],[C,D]]` to

```text
P_bar=[[A,B/M],[M*C,D]]
```

so joint geometric dilation leaves `P_bar` invariant after the already verified affine-rate conversion.

The source is a zero-mean Gaussian preparation label with covariance

```text
Sigma_source=diag(alpha_1^2,alpha_2^2,beta_1^2,beta_2^2)
alpha=(0.08,0.12)
beta=(0.015,0.02)
```

where `alpha` and `beta` are dimensionless toy widths, not measured source parameters. Propagate

```text
Sigma_observer=P_bar*Sigma_source*P_bar^T
Gamma_observer=Sigma_observer[0:2,0:2]
```

Raw `Sigma_observer` and `Gamma_observer` remain primary.

## Analyzer convention

For ideal real analyzer axis

```text
a(theta)=(cos(theta),sin(theta))
variance(theta)=a^T*Gamma_observer*a
rms(theta)=sqrt(variance(theta))
```

Use scan angles `theta={0,pi/8,pi/4,3pi/8,pi/2}`. Analyzer is a mathematical projection label, not hardware. Overall source intensity/gain is excluded.

## Eight counterexample-first controls

1. **Source covariance domain.** Covariance is symmetric positive definite, widths finite/positive, and the normalized Gaussian convention is explicit. Reject zero/negative/nonfinite widths.
2. **Covariance propagation.** Direct matrix propagation and independent block formula agree; observer covariance is symmetric positive definite within `2e-10`.
3. **Width homogeneity.** Multiplying every source width by `c=2.5` multiplies observer covariance and analyzer variance by `c^2`, while normalized shape/eigenvalue ratios remain unchanged within `2e-10`. This is preparation amplitude, not geometry.
4. **Orientation survival.** At fixed preparation and analyzer convention, `orientation=+1` and `-1` observer position covariances and analyzer scans differ by more than `1e-3`.
5. **Analyzer extrema.** Analytic minimum/maximum analyzer variances equal eigenvalues of `Gamma_observer`; dense deterministic scan brackets them within `2e-5`.
6. **Common-basis covariance.** A common screen rotation applied to `P_bar`, source covariance, and analyzer preserves scalar variance and covariance eigenvalues within `2e-10`.
7. **Analyzer collision.** Plus/minus analyzer variance intervals overlap. Construct a common target inside the overlap and explicit branch-dependent analyzer angles that give the same scalar variance within `2e-10`, while full `Gamma_observer` matrices remain distinct. Therefore one unknown analyzer scalar is not branch-identifying.
8. **Joint scale/rank/no-`ell0`.** Joint geometric dilation preserves dimensionless covariance and scan. The exact `log_M` feature column is null. Report local rank over preparation/analyzer parameters without calling it physical identifiability; retain all nonclaims.

## Scenario matrix extension

Extend the existing authoritative `studies/spacetime/kerr-jacobi-scenarios.json`:

| ID | category | purpose |
|---|---|---|
| J07 | preparation | source covariance domain |
| J08 | preparation | plus covariance propagation |
| J09 | preparation | minus covariance propagation |
| J10 | preparation | width homogeneity |
| J11 | orientation | orientation survival |
| J12 | analyzer | analyzer extrema |
| J13 | analyzer | basis covariance and scalar collision |
| J14 | scale | dimensionless scaling/rank/nonclaims |

Existing J01–J06 remain unchanged. Runner total must report `14/14`; granular scenario and categories `conformance`, `orientation`, `scale`, `preparation`, and `analyzer` must remain available and fail closed.

## Expected bounded result

If controls pass:

```text
KERR_JACOBI_ORIENTATION_SHAPE_SURVIVES_FIXED_FINITE_GAUSSIAN_SOURCE_AND_ANALYZER_SCAN_BUT_SOURCE_WIDTH_HOMOGENEITY_AND_ANALYZER_COLLISIONS_PREVENT_INDEPENDENT_BRANCH_OR_ABSOLUTE_SCALE_IDENTIFICATION_NOT_ELL0
```

Physical gate:

```text
PHYSICAL_KERR_SOURCE_DYNAMICS_EMISSION_INTENSITY_POLARIZATION_ANALYZER_HARDWARE_RECEIVER_TRANSFER_CALIBRATED_NOISE_LIKELIHOOD_JOINT_COVARIANCE_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED
```

## Stop conditions and nonclaims

Stop or preserve a negative result if covariance loses positivity, propagation disagrees, orientation shape vanishes, basis covariance fails, collision construction fails, scale invariance fails, or any preparation label is promoted to measured physics.

```text
UMCH=UNPROVEN_SECONDARY_CANDIDATE
L_identified=false
ell0_identified=false
L_equals_ell0=NOT_DERIVED
extra_dimension_detected=false
structural_dead_end=NOT_DECLARED
NO_POSITIVE_DETECTION_CLAIM
```
