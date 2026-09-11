# Kerr correlated-noise mismatch threshold

## Status

`RATIFIED_FOR_IMPLEMENTATION_PLANNING`

## Model

For branch `o`, diagonal gain `G_o`, known inside-interval reference covariance `R=diag(0.1,10.0)`, signal covariance `Gamma_o`, common full SPD receiver noise `N_o`, and calibration-only differential mismatch `Delta_o`, define

```text
S_o=G_o Gamma_o G_o^T+N_o
B_o=G_o R G_o^T+N_o+Delta_o
D_o=S_o-B_o=G_o(Gamma_o-R)G_o^T-Delta_o.
```

When `Delta_o=0`, arbitrary branch-profiled SPD `N_o` cancels exactly from `D_o`. Since inside reference makes `Gamma_+-R` negative definite and `Gamma_--R` positive definite, the two `D` cones cannot collide for positive invertible gains.

Fixed gain domain: each diagonal gain in `[0.5,1.5]`. Fixed shared-noise anchor per branch:

```text
N=[[0.4,0.12],[0.12,0.7]]
```

which is SPD. Mismatch norm is spectral/operator norm. Collision of branch observables requires equality of full matrices, not merely one branch matrix becoming singular. On diagonal gain domain, exact minimum operator-norm branch-set distance is

```text
tau=max_i 0.5^2*((R_i-Gamma_{+,i})+(Gamma_{-,i}-R_i))
   =0.5^2*max_i(Gamma_{-,i}-Gamma_{+,i}).
```

Use aggregate differential mismatch bound `||Delta_+-Delta_-||_2 <= 0.8*tau`. Remaining branch-set distance is at least `0.2*tau`. At aggregate mismatch exactly equal to full boundary matrix `A_+-A_-`, both observable matrices collide; explicit threshold witness records equality while underlying signal/calibration covariances remain SPD.

## MVP-first gate

**Objective:** prove shared correlated-noise cancellation and quantify exact mismatch threshold that destroys sign-cone separation.

**Metric and threshold:** exactly `8/8` controls.

**Cases/order:** full-noise domain, shared-noise cancellation, sign-cone noncollision, analytic mismatch threshold, bounded residual, threshold collision, basis/scale invariance, nonclaims.

## Eight controls

1. Full `2x2` noise anchor is symmetric positive definite and rejects nonfinite/non-SPD matrices.
2. Signal-minus-calibration difference is independent of arbitrary shared correlated `N_o` within `2e-10` when `Delta_o=0`.
3. Inside-reference branch difference cones have opposite definiteness throughout bounded positive gain domain; no exact collision.
4. Analytic `tau` equals operator norm of minimum-gain full branch-difference matrix within `2e-10` and is positive (`>1`).
5. For aggregate differential mismatch below `0.8*tau`, reverse-triangle/operator-norm bound leaves positive branch-set separation (`>1`).
6. At exact threshold, explicit minimum-gain branch candidates and full differential mismatch yield equal observable matrices within `2e-10`; signal and calibration covariances remain SPD.
7. Orthogonal basis rotation and common geometric scale conversion preserve normalized `tau`, norms and rank null within `2e-10`.
8. Artifact preserves `L_identified=false`, `ell0_identified=false`, `L_equals_ell0=NOT_DERIVED`, no extra-dimension detection and no positive detection claim.

## Scenarios

J63-J70 map one-to-one to controls. New category: `calibration_mismatch`. Existing J01-J62 remain unchanged. Runner remains fail-closed total/scenario/category with JSON.

## Interpretation ceiling

```text
KERR_SHARED_CORRELATED_RECEIVER_NOISE_CANCELS_IN_SIGNAL_MINUS_CALIBRATION_BUT_DIFFERENTIAL_MISMATCH_AT_THE_EXACT_CONE_MARGIN_RESTORES_COLLISION_NOT_ELL0
MODEL_LEVEL_CORRELATED_NOISE_MISMATCH_THRESHOLD_NOT_EVIDENCE
PHYSICAL_KERR_SIGNAL_CALIBRATION_NOISE_MATCHING_DRIFT_HARDWARE_PRIORS_SAMPLING_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED
```

Mismatch bound, gain domain and SPD anchor are toy controls, not measured hardware properties.

```text
UMCH=UNPROVEN_SECONDARY_CANDIDATE
L_identified=false
ell0_identified=false
L_equals_ell0=NOT_DERIVED
extra_dimension_detected=false
structural_dead_end=NOT_DECLARED
NO_POSITIVE_DETECTION_CLAIM
```
