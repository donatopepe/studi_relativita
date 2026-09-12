# Kerr paired-stream common-noise cancellation

For paired signal/calibration streams sharing additive Gaussian receiver noise, cross-Wishart contraction subtracts twice common cross-covariance coefficient:

```text
E||[(Sx-C_S)-(Sy-C_B)]||_F^2
=alpha(N,rho)[q(C_S)+q(C_B)-2q(K)]
q(A)=(tr A)^2+tr(A A^T)
```

At fixed toy `rho=0.5`:

```text
independent_coefficient=923.6933349
paired_coefficient=916.1381349
rms_ratio=0.995901934
rms=[9.6935525,4.8837780,2.4424379]
minimum_count=87
risk_87=0.049670477
risk_86=0.050247654
risk_64=0.067498804
```

Thus exact pairing cancels a real but small sampling term: RMS falls only `0.4098%`, count gate falls from 88 to 87, and `N=64` remains unsafe. Zero shared covariance exactly restores independent-stream gate 88. All `8/8` controls and `102/102` scenarios pass. Pair synchrony, common-noise identity, Gaussianity and shared AR(1) rho are not measured.

```text
KERR_PAIRED_SIGNAL_CALIBRATION_COMMON_NOISE_CANCELS_A_SMALL_SAMPLING_TERM_BUT_DOES_NOT_REMOVE_AR1_SAMPLE_BURDEN_NOT_ELL0
MODEL_LEVEL_PAIRED_COMMON_NOISE_COVARIANCE_GAIN_NOT_EVIDENCE
PHYSICAL_KERR_CROSS_STREAM_SYNCHRONY_COMMON_NOISE_MODEL_AR1_STATIONARITY_GAUSSIANITY_CALIBRATION_MATCHING_HARDWARE_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED
```
