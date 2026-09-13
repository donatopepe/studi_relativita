# Kerr count-dependent rho phase window

For full-window latent-lag support, solve at each count

```text
rho_low(N): unrestricted-lag risk=0.05
rho_high(N): uniform-lag risk=0.05.
```

At iid rho zero, N=53 is already unsafe (`uniform=0.0500676203`, `unrestricted=0.0502699814`); N=54 is first safe count (`0.0491228897`, `0.0493214912`). Finite windows:

```text
N        =[54,64,87,128,256]
rho_low  =[0.084265333564,0.309816339325,0.499243438917,0.649991897137,0.814628675425]
rho_high =[0.095873875058,0.313101631950,0.501157235677,0.651271982688,0.815322224235]
width    =[0.011608541494,0.003285292625,0.001913796761,0.001280085551,0.000693548809]
```

Both boundaries move upward with count; sensitivity width contracts strictly. Larger sample count tolerates larger rho before gate failure, but narrow transition does not identify physical correlation or prescribe sample size. All `8/8` controls and `158/158` scenarios pass.

```text
KERR_LATENT_LAG_LAW_RHO_SENSITIVITY_WINDOW_MOVES_UPWARD_AND_NARROWS_WITH_TOY_SAMPLE_COUNT_WHILE_N53_IS_UNSAFE_ALREADY_AT_IID_NOT_ELL0
MODEL_LEVEL_COUNT_DEPENDENT_RHO_PHASE_NOT_EVIDENCE
PHYSICAL_KERR_SAMPLE_COUNT_AR1_RHO_LAG_LAW_RADIUS_SUPPORT_WINDOW_INDEPENDENCE_SYNCHRONY_COMMON_NOISE_MODEL_STATIONARITY_CONDITIONAL_GAUSSIANITY_CALIBRATION_MATCHING_HARDWARE_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED
```
