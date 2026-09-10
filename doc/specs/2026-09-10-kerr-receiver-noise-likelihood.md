# Kerr calibrated Gaussian receiver/noise likelihood

## Status

`RATIFIED_FOR_IMPLEMENTATION_PLANNING`

Human authorized continuation after finite source/analyzer closure. This MVP adds one declared statistical receiver layer, not physical hardware or real data.

## MVP-first gate

**Objective:** determine whether plus/minus Kerr observer covariance models are statistically distinguishable under fixed calibrated Gaussian gain/noise, while constructing counterexamples for unknown calibration nuisances and retaining geometric scale blindness.

**Metric and threshold:** exactly `8/8` preregistered controls.

**Cases/order:** receiver covariance, likelihood normalization, directed/symmetric KL, noise monotonicity, expected finite-sample log-likelihood ratio, common-basis covariance, nuisance collision, scale/rank/no-`ell0`.

**MVP:** two-dimensional zero-mean Gaussian receiver record

```text
y=g*A(theta)*x+n
n~N(0,N)
C_branch=g^2*A*Gamma_branch*A^T+N
```

Default fixed calibration: `g=0.8`, `A=I_2`, isotropic `N=sigma_n^2 I`, `sigma_n=0.25`. This uses full two-component receiver covariance, not the prior one-scalar analyzer. No random Monte Carlo is needed: use exact expected log-likelihood ratios.

**Escalation condition:** add sampled data or fitted likelihood only after fixed/noise and nuisance controls pass; otherwise preserve named calibration collision.

## Statistical record

For zero-mean `d=2` Gaussian covariances `C_p,C_q`, use

```text
D_KL(p||q)=0.5*(tr(C_q^-1 C_p)-d+ln(det C_q/det C_p))
J_KL=D_KL(p||q)+D_KL(q||p)
E_p[log p(y)/q(y)]=D_KL(p||q)
```

For `N_samples=25`, expected total log-likelihood ratio is `25*D_KL`.

Canonical sources:

- Kullback and Leibler (1951), *On Information and Sufficiency*, DOI `10.1214/aoms/1177729694`, supports information divergence only.
- NIST/SEMATECH e-Handbook, Sec. 6.5.4.2, supports multivariate normal density/covariance form.
- Gaussian covariance propagation and all Kerr receiver/nuisance constructions remain project derivations.

## Eight controls

1. **Receiver covariance:** symmetry/SPD, positive gain/noise domains, direct and expanded formulas agree below `2e-10`.
2. **Likelihood normalization:** deterministic quadrature for diagonal anchor integrates to one and analytic log-density agrees with direct product below `2e-7`.
3. **KL conformance:** directed KL nonnegative, zero on self, analytic formula agrees with deterministic quadrature below `2e-5`.
4. **Noise monotonicity:** symmetric KL decreases strictly for `sigma_n={0.1,0.25,0.5,1.0,2.0}` under fixed calibration.
5. **Expected finite-sample LLR:** exact `N*D_KL`; plus and minus directed expectations positive; swapping hypotheses changes direction but not symmetric sum.
6. **Common-basis covariance:** rotate signal, analyzer and receiver basis together; KL and covariance eigenvalues invariant below `2e-10`.
7. **Calibration nuisance collision:** with branch-dependent unknown diagonal gains and isotropic noise, construct a shared diagonal target covariance above both branch minima; solve gains/noises yielding exact same `C_target` while underlying `Gamma` differ. Thus unconstrained calibration can erase statistical distinction.
8. **Joint scale/rank/no-`ell0`:** fixed dimensionless receiver covariance/KL invariant under geometric dilation; exact `log_M` null. Receiver calibration is imported, not an interior scale or `ell0`.

## Scenario extension

Add J15–J22:

| ID | category | control |
|---|---|---|
| J15 | receiver | covariance |
| J16 | likelihood | normalization |
| J17 | likelihood | KL conformance |
| J18 | noise | monotonicity |
| J19 | likelihood | finite-sample expected LLR |
| J20 | receiver | common-basis covariance |
| J21 | calibration | nuisance collision |
| J22 | scale | scale/rank/nonclaims |

Total battery becomes `22/22`; granular categories add `receiver`, `likelihood`, `noise`, `calibration`.

## Expected bounded result

```text
KERR_FULL_COVARIANCE_BRANCHES_ARE_DISTINGUISHABLE_UNDER_FIXED_GAUSSIAN_RECEIVER_CALIBRATION_BUT_UNCONSTRAINED_GAIN_NOISE_NUISANCES_CAN_COLLIDE_EXACTLY_AND_GEOMETRIC_SCALE_REMAINS_BLIND_NOT_ELL0
```

Physical gate:

```text
PHYSICAL_KERR_EMISSION_RECEIVER_HARDWARE_CALIBRATION_PRIORS_NOISE_SPECTRUM_SAMPLING_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED
```

## Nonclaims

```text
UMCH=UNPROVEN_SECONDARY_CANDIDATE
L_identified=false
ell0_identified=false
L_equals_ell0=NOT_DERIVED
extra_dimension_detected=false
structural_dead_end=NOT_DECLARED
NO_POSITIVE_DETECTION_CLAIM
```
