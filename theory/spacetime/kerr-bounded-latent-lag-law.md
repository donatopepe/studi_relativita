# Kerr bounded latent-lag law robustness

Profile unknown latent lag probabilities on symmetric support under density-ratio box around uniform:

```text
u/kappa <= p_d <= kappa*u
sum_d p_d=1
beta(p)=sum_d p_d beta_d.
```

Because risk decreases linearly with `beta(p)`, exact worst/best extrema follow finite LP: put baseline lower mass everywhere, then allocate remaining mass toward smallest/largest `beta_d` until upper bounds bind.

At fixed `rho=0.5`, fractions `[0,0.25,0.5,1.0]`:

```text
kappa_2_worst_counts=[87,87,87,87]
kappa_2_best_counts=[87,87,87,87]
kappa_4_worst_counts=[87,87,87,88]
kappa_4_best_counts=[87,87,87,87]
```

For kappa 4 and N=64, worst risks increase from `0.067498804` at zero support to `0.067950561` at full-window support; best full-window risk is `0.067612376`. Envelope widens monotonically with kappa. Distributional uncertainty can erase latent-mixture one-count benefit only at wide box/full support; `N=64` remains unsafe throughout.

All `8/8` controls and `134/134` scenarios pass. Density-ratio bounds, support, lag law, conditional Gaussianity, AR(1), shared-noise identity and timing are unmeasured toy assumptions.

```text
KERR_LATENT_LAG_LAW_DENSITY_RATIO_BOUNDS_GIVE_EXACT_RISK_ENVELOPES_BUT_KAPPA_4_CAN_RESTORE_THE_INDEPENDENT_AR1_COUNT_GATE_NOT_ELL0
MODEL_LEVEL_BOUNDED_LATENT_LAG_LAW_ROBUSTNESS_NOT_EVIDENCE
PHYSICAL_KERR_LATENT_LAG_LAW_BOUNDS_WINDOW_INDEPENDENCE_SYNCHRONY_COMMON_NOISE_MODEL_AR1_STATIONARITY_CONDITIONAL_GAUSSIANITY_CALIBRATION_MATCHING_HARDWARE_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED
```
