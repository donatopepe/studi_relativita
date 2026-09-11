# Kerr composite common-calibration profile gate

Previous same-point common calibration and composite profiling answer different questions. One shared physical nuisance point leaves positive same-point separation. Conservative composite testing uses separately profiled candidate values for each branch from same allowed calibration model.

For diagonal signal covariance, output intervals establish bounded set disjointness analytically. Second channel has positive gap:

```text
analytic_channel_gap=8.9423947
```

Finite pair grids provide only a witness, not proof:

```text
profile_grids=[3,5,9]
profile_min_KL=0.2019263
plus_anchor=[1.0,1.5,1.0]
minus_anchor=[1.5,0.5,0.775]
```

Relaxed positive gains restore exact collision:

```text
relaxed_minus_gains=[0.44907953,0.23594622]
collision_residual=8.8817842e-16
```

Thus bounded separation depends entirely on toy nuisance bounds. It does not identify hardware calibration, absolute geometric scale, or `ell0`.

All `8/8` controls and `38/38` scenarios pass.

```text
KERR_COMPOSITE_BRANCH_SETS_ARE_DISJOINT_UNDER_TOY_BOUNDED_PROFILED_COMMON_CALIBRATION_BUT_RELAXED_POSITIVE_GAINS_COLLIDE_EXACTLY_AND_ABSOLUTE_SCALE_REMAINS_BLIND_NOT_ELL0
MODEL_LEVEL_BOUNDED_COMPOSITE_CALIBRATION_PROFILE_NOT_EVIDENCE
PHYSICAL_KERR_SHARED_CALIBRATION_MODEL_BOUNDS_PRIORS_HARDWARE_NOISE_SPECTRUM_SYSTEMATICS_SAMPLING_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED
```
