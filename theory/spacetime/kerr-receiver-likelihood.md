# Kerr calibrated Gaussian receiver likelihood

## Bounded receiver

The finite-source observer covariance is passed through a declared two-component Gaussian receiver,

```text
y=g*A*x+n
n~N(0,N)
C_receiver=g^2*A*Gamma*A^T+N
```

with fixed toy calibration `g=0.8`, `A=I_2`, and isotropic `sigma_n=0.25`. Kullback–Leibler information uses

```text
D_KL(p||q)=0.5*(tr(C_q^-1 C_p)-2+ln(det(C_q)/det(C_p)))
```

for zero-mean Gaussian models. `KullbackLeibler1951` supports information divergence; `NISTMultivariateNormal` supports multivariate-normal density/covariance. Closed formulas, quadrature checks, receiver calibration and Kerr interpretation are project derivations.

## Fixed-calibration result

```text
C_plus_diag=[0.087505447,2.8994414]
C_minus_diag=[0.18649042,51.021903]
KL_plus_minus=1.0752327
KL_minus_plus=7.0519599
symmetric_KL=8.1271925
expected_LLR_25=[26.880816,176.299]
```

Under fixed calibration, both directed divergences and expected likelihood ratios are positive. Increasing isotropic noise monotonically lowers symmetric KL.

## Calibration nuisance collision counterexample

Unconstrained branch-dependent diagonal gains plus positive isotropic noise map both distinct signal covariances to

```text
calibration_target=[1.0,100.0]
collision_residual=0.0
```

Thus fixed calibration distinguishes branches, while unknown calibration nuisance can collide exactly. Common-basis covariance and joint geometric scale controls pass.

All scientific controls pass `8/8`; complete scenario battery passes `22/22`.

```text
KERR_FULL_COVARIANCE_BRANCHES_ARE_DISTINGUISHABLE_UNDER_FIXED_GAUSSIAN_RECEIVER_CALIBRATION_BUT_UNCONSTRAINED_GAIN_NOISE_NUISANCES_CAN_COLLIDE_EXACTLY_AND_GEOMETRIC_SCALE_REMAINS_BLIND_NOT_ELL0
MODEL_LEVEL_KERR_RECEIVER_LIKELIHOOD_NOT_EVIDENCE
PHYSICAL_KERR_EMISSION_RECEIVER_HARDWARE_CALIBRATION_PRIORS_NOISE_SPECTRUM_SAMPLING_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED
```

No sampled data, physical receiver, calibration prior, noise spectrum, 5D Kerr comparator or `ell0` law is derived.
