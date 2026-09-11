# Kerr composite common-calibration profile audit

```text
ell0_identified=false
NO_POSITIVE_DETECTION_CLAIM
MODEL_LEVEL_BOUNDED_COMPOSITE_CALIBRATION_PROFILE_NOT_EVIDENCE
DIRECT_REVIEW_NO_SUBAGENT
```

Controls `8/8`; scenario battery `38/38`.

```text
analytic_channel_gap=8.9423947
profile_grids=[3,5,9]
profile_min_KL=0.2019263
plus_anchor=[1.0,1.5,1.0]
minus_anchor=[1.5,0.5,0.775]
relaxed_minus_gains=[0.44907953,0.23594622]
collision_residual=8.8817842e-16
```

```text
KERR_COMPOSITE_BRANCH_SETS_ARE_DISJOINT_UNDER_TOY_BOUNDED_PROFILED_COMMON_CALIBRATION_BUT_RELAXED_POSITIVE_GAINS_COLLIDE_EXACTLY_AND_ABSOLUTE_SCALE_REMAINS_BLIND_NOT_ELL0
PHYSICAL_KERR_SHARED_CALIBRATION_MODEL_BOUNDS_PRIORS_HARDWARE_NOISE_SPECTRUM_SYSTEMATICS_SAMPLING_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED
```

Analytic interval gap proves disjoint bounded covariance sets; finite KL grid is supporting witness only. Relaxed positive gains collide exactly. Toy bounds are not measured calibration priors or evidence.
