# Kerr bounded reference-drift robustness

## Status

`RATIFIED_FOR_IMPLEMENTATION_PLANNING`

## MVP-first gate

**Objective:** determine exact branch-independent reference-drift radius that preserves inside-interval collision obstruction and exhibit endpoint/outside failure.

**Metric and threshold:** exactly `8/8` controls.

**Cases/order:** interval containment, maximal symmetric drift, bounded robust obstruction, endpoint loss, outside crossing collision, Fisher margin, scale invariance, nonclaims.

For channel `i`, let branch variances be `a_i<b_i`, nominal reference midpoint

```text
m_i=(a_i+b_i)/2
```

and maximal symmetric open-interval drift radius

```text
d_i=(b_i-a_i)/2.
```

Reference interval `[m_i-delta_i,m_i+delta_i]` blocks positive gain/noise collision iff `delta_i<d_i`. Use conservative preregistered fraction `delta_i=0.8*d_i`. Endpoints `delta_i=d_i` make one branch satisfy `Gamma=R`, causing collision-obstruction and joint-Jacobian determinant to vanish. Outside witness uses `R_i=b_i+0.2*d_i` and an exact positive gain/noise collision.

Fixed values derive only from committed Kerr covariances:

```text
m=[0.1164030185,42.028394255]
d=[0.0773320070,37.5956732701]
delta=[0.0618656056,30.0765386160]
```

## Eight controls

1. Midpoints and maximal radii reconstruct both branch endpoints within `2e-10`.
2. Entire conservative drift box lies strictly inside both branch intervals.
3. Worst-case sign-obstruction margins over drift box remain positive (`>1e-3`).
4. At exact radius endpoint, placement product and one joint Fisher determinant vanish within `2e-10`.
5. Outside reference crossing yields explicit positive gain/noise exact joint collision below `2e-10`.
6. Minimum joint-Jacobian determinant over conservative drift endpoints remains above `1e-8`.
7. Common geometric scale conversion preserves normalized drift fractions and exact-collision residual within `2e-10`.
8. Artifact preserves all scale/`ell0`/extra-dimension/detection nonclaims.

## Scenarios

J55-J62 map one-to-one to controls above. New category: `reference_drift`. Existing J01-J54 remain unchanged. Runner stays fail-closed total/scenario/category with JSON.

## Interpretation ceiling

```text
MODEL_LEVEL_BOUNDED_REFERENCE_DRIFT_ROBUSTNESS_NOT_EVIDENCE
KERR_REFERENCE_COLLISION_OBSTRUCTION_SURVIVES_ONLY_WHILE_REFERENCE_DRIFT_STAYS_STRICTLY_INSIDE_BRANCH_VARIANCE_INTERVAL_AND_FAILS_AT_ENDPOINT_OR_OUTSIDE_NOT_ELL0
PHYSICAL_KERR_CALIBRATOR_DRIFT_BOUND_STABILITY_CROSS_CHANNEL_NOISE_HARDWARE_PRIORS_SAMPLING_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED
```

Drift fraction is toy control, not measured stability. Endpoint/outside failures are authoritative negatives.

```text
UMCH=UNPROVEN_SECONDARY_CANDIDATE
L_identified=false
ell0_identified=false
L_equals_ell0=NOT_DERIVED
extra_dimension_detected=false
structural_dead_end=NOT_DECLARED
NO_POSITIVE_DETECTION_CLAIM
```
