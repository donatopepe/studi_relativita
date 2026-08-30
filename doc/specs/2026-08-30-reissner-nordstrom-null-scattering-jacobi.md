# Reissner–Nordström finite-boundary null-scattering Jacobi control

## Status and bounded question

This increment extends the ratified operator-valued route to a second exact spherical geometry. It does not reformulate UMCH. Required state remains:

```text
UMCH=UNPROVEN
ell0_identified=false
structural_dead_end=NOT_DECLARED
NO_POSITIVE_DETECTION_CLAIM
CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE
```

Question: for an exterior equatorial neutral null ray in asymptotically flat Reissner–Nordström geometry, with finite equal-radius endpoints, one turning point, a declared screen and unit Killing-energy project normalization, does charge-dependent Ricci/Weyl optical structure add an identifiable absolute-scale direction, or only dimensionless shape through `epsilon=Q/M`?

Classifications:

- RN metric, neutral-null closest-approach/impact relation and general Sachs/Jacobi framework: `KNOWN_RESULT` in cited scope;
- regularized finite path, direct four-dimensional Riemann projection, full `4x4` Jacobi phase map and numerical audits: `PROJECT_DERIVATION`;
- finite endpoints, screen order, unit Killing energy and source boundary matrices: `TOY_CONTROL` / project anchors;
- charge-sign collision and absolute-scale blindness: `NEGATIVE_RESULT` if tests pass;
- physical charge-source realization, emitter, absorber, endpoint screen preparation, calibrated receiver/covariance and geometry–`ell0` law: `OPEN_PROBLEM`.

No source establishes this project protocol, readout, covariance, `ell0`, UMCH or detection.

## Alternatives

1. **Deflection angle only:** rejected as primary because it scalarizes away screen and phase-space structure.
2. **Weak-field lens equation:** rejected because asymptotic observer/source assumptions hide finite-boundary protocol choices.
3. **Full direct-curvature Jacobi map:** selected. It preserves screen matrix, path ordering, boundary conditions and caustic-safe phase map.

## Frozen geometry and path

Use geometrized units and

\[
 ds^2=-f(r)dt^2+f(r)^{-1}dr^2+r^2(d\theta^2+\sin^2\theta\,d\phi^2),
 \qquad f(r)=1-\frac{2M}{r}+\frac{Q^2}{r^2}.
\]

Set

\[
 \epsilon=Q/M,\quad \rho=r_{\min}/M,\quad R=r_{\rm end}/M,
 \quad \beta=b/M=\frac{\rho}{\sqrt{f(M\rho)}}.
\]

Domain: `M>0`, `0<=abs(epsilon)<=1`, `R>rho>rho_ph(epsilon)`, where

\[
 \rho_{\rm ph}=\frac{3+\sqrt{9-8\epsilon^2}}2.
\]

The radial first integral at unit Killing energy is

\[
 (dr/d\lambda)^2=1-\frac{b^2 f(r)}{r^2}.
\]

Regularize each half with `r/M=rho+y^2`. Keep incoming, turning and outgoing labels explicit.

## Primary optical object

Declare screen order `(polar,in-plane)` and reconstruct

\[
 \mathcal K_{AB}=-R_{\mu\nu\rho\sigma}e_A^\mu k^\nu e_B^\rho k^\sigma
\]

directly from the four-dimensional metric, including both Ricci and Weyl content. Integrate

\[
 \frac{d}{d\lambda}\binom X V=
 \begin{pmatrix}0&I\\-\mathcal K&0\end{pmatrix}\binom X V,
 \qquad P(\lambda_s)=I_4.
\]

`P=[[A,B],[C,D]]` is primary through caustics. `S=DB^{-1}` is emitted only when `B` is invertible. Preserve raw `K`, its trace and trace-free part; do not treat them as independent observations.

## Counterexample-first contract

Tests must precede implementation and require:

1. zero-window identity;
2. `epsilon=0` agreement with Schwarzschild path/profile/full map within declared numerical tolerances;
3. exact charge-sign degeneracy under `epsilon -> -epsilon` because metric depends on `Q^2`;
4. orientation reversal as a scoped screen similarity, not new evidence;
5. symplecticity, reversal/inverse and turning composition of full phase map;
6. direct Riemann symmetries and screen orthonormality;
7. geometric dilation `(M,Q,r,b,lambda)->s(M,Q,r,b,lambda)` at fixed `(epsilon,rho,R)` leaves frequency-converted dimensionless record unchanged;
8. finite-difference rank audit includes an `log_M` null direction after retaining `epsilon` as a shape coordinate;
9. `Q`, `epsilon`, photon radius, turning radius, impact parameter and charge-sign collision are not `ell0`.

## Preregistered interpretation

Passing result may be reported only as:

```text
REISSNER_NORDSTROM_CHARGE_ADDS_DIMENSIONLESS_RICCI_WEYL_OPTICAL_SHAPE_BUT_Q_SQUARED_DEGENERACY_AND_JOINT_MQ_DILATION_RETAIN_ABSOLUTE_SCALE_BLINDNESS_NOT_ELL0
```

Gate:

```text
PHYSICAL_CHARGE_SOURCE_EMITTER_ABSORBER_ENDPOINT_SCREEN_PREPARATION_ABSOLUTE_FREQUENCY_RECEIVER_TRANSFER_CALIBRATED_NOISE_JOINT_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED
```

A pass does not establish channel independence or structural-dead-end criteria. `structural_dead_end=NOT_DECLARED` remains because physical source/receiver derivations and other exact geometries remain open.

## Sources and scope

- `EiroaRomeroTorres2002`: RN metric, horizon/photon sphere, closest-approach integral and impact parameter in asymptotically flat RN lensing. It does not supply this finite-boundary screen/Jacobi protocol.
- `Sachs1961`: general null optical-scalar framework, not this RN numerical construction.
- `SchneiderEhlersFalco1992`: general lensing/Jacobi background, not UMCH or project calibration.
