# Kerr shared-calibration robustness

## Status

`RATIFIED_FOR_IMPLEMENTATION_PLANNING`

This bounded follow-up separates physically plausible common calibration from the prior branch-dependent counterexample. Bounds remain toy assumptions, not measured priors.

## MVP-first gate

**Objective:** determine whether plus/minus Kerr Gaussian receiver models retain positive information separation for one common bounded calibration, while proving that unbounded common attenuation/noise can erase separation asymptotically.

**Metric and threshold:** exactly `8/8` controls.

**Cases/order:** common-map injectivity, bounded-domain validity, deterministic minimum, refinement, boundary location, asymptotic attenuation, asymptotic noise, basis/scale/nonclaims.

**MVP domain:** common diagonal gain `(g1,g2)` with each in `[0.5,1.5]`; common isotropic noise sigma in `[0.1,1.0]`; tensor-product grids `5^3`, `9^3`, `17^3`. Signal covariances are fixed outputs from prior source/analyzer gate.

For common invertible `G=diag(g1,g2)` and same finite noise `n`,

```text
C_+-C_-=G*(Gamma_+-Gamma_-)*G^T
```

so exact covariance collision is impossible when `Gamma_+ != Gamma_-`. Information may nevertheless tend to zero when common gains tend to zero or noise tends to infinity.

## Eight controls

1. Algebraic common-map difference identity and finite noncollision.
2. Domain rejects nonpositive/nonfinite gains/noise and out-of-bound values in bounded scan.
3. Coarse/fine/refined deterministic minimum symmetric KL remains positive; refined anchor recorded.
4. Refinement sequence is stable and nonincreasing within `2e-10`.
5. Minimum occurs at expected least-informative boundary `(0.5,0.5,1.0)` and agrees with direct evaluation.
6. Common attenuation sequence `g={0.5,0.1,0.01}` at noise 1 decreases toward zero.
7. Common noise sequence `n={1,10,100}` at gain 1 decreases toward zero; attenuation/noise dual values agree where signal-to-noise ratio matches.
8. Common-basis covariance, geometric scale null, and all scientific nonclaims remain.

## Scenarios

J23–J30, categories `robustness`, `calibration`, `asymptotic`, `scale`; total becomes `30/30`.

## Expected result

```text
KERR_BRANCH_COVARIANCES_REMAIN_INFORMATION_DISTINCT_UNDER_COMMON_BOUNDED_INVERTIBLE_CALIBRATION_BUT_COMMON_ATTENUATION_OR_UNBOUNDED_NOISE_DRIVES_SEPARATION_TO_ZERO_AND_ABSOLUTE_SCALE_REMAINS_BLIND_NOT_ELL0
```

Physical gate:

```text
PHYSICAL_KERR_CALIBRATION_BOUNDS_PRIORS_HARDWARE_NOISE_SPECTRUM_SYSTEMATICS_SAMPLING_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED
```

```text
UMCH=UNPROVEN_SECONDARY_CANDIDATE
L_identified=false
ell0_identified=false
L_equals_ell0=NOT_DERIVED
extra_dimension_detected=false
structural_dead_end=NOT_DECLARED
NO_POSITIVE_DETECTION_CLAIM
```

No evidence or detection claim.
