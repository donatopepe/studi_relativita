# Linearized five-dimensional tensor conformance

## Classification

- `KNOWN_RESULT`: `Robinson2006Normalization`, equations (1), (2a,b), (4), (5a,b), (6a,b), (7a-c), and (9)-(15), fixes arbitrary-dimensional trace reversal, harmonic gauge, Newtonian limit, and sign convention.
- `KNOWN_RESULT_CONTEXT`: `AtondoRubio2008Linearized5D`, equations (4)-(19), records a linearized metric/connection/Riemann/Ricci/Einstein construction. Its equations (21)-(23) impose a cylinder ansatz and `h_44=0` and must not be imported into this localized compact-circle calculation.
- `PROJECT_DERIVATION`: the existing compact-circle scalar potential is embedded in one static `d=5` dust metric and differentiated analytically into the full linearized curvature record.
- `TOY_CONTROL`: flat `R^(1,3) x S1`, unit effective potential amplitude, static dust, radial ordinary-space eigenframe, localized exact profile or exact uniform zero mode, and one radial shell.
- `NEGATIVE_RESULT`: tensor completion preserves joint scale blindness and depends on the declared source stress. No physical compactification scale or `ell0` is identified.

## Declared metric and curvature

With signature `(-,+,+,+,+)`, only `bar_h_00` sourced, and `Phi=-h_00/2`, the `d=5` inverse trace reversal gives

```text
h_00=-2 Phi
h_11=h_22=h_33=h_44=-Phi
h_0I=h_IJ=0 for I!=J
```

The project computes

```text
R_ABCD=(1/2)(partial_C partial_B h_AD + partial_D partial_A h_BC
             - partial_D partial_B h_AC - partial_C partial_A h_BD)
R_0i0j=partial_i partial_j Phi
```

and contracts the raw tensor independently to Ricci, Ricci scalar, and Einstein tensor. At regular samples the compact-circle potential is harmonic in four spatial dimensions, so Ricci and Einstein residuals vanish while Riemann remains nonzero.

## Compact-index caveat

For a localized profile, `y` derivatives generate `R_0404` and `R_0i04`, while `R_i4j4` contains both compact-coordinate and ordinary-space derivatives. In the exact uniform zero mode, all `y` derivatives and nonzero KK modes vanish, hence `R_0404=R_0i04=0`. But `h_44=-Phi(r)` remains ordinary-space dependent, so `R_i4j4` need not vanish. Index `4` is not synonymous with a nonzero KK mode.

These are coordinate components of one declared linearized model. They are not automatically independent gauge-invariant observables, detector channels, or evidence for an extra dimension.

## Eight-control result

All `8/8` preregistered controls pass: trace reversal; harmonic residual; Ricci/Einstein plus regular vacuum; point/shell Hessian identity; localized compact-index/nonzero-mode separation; exact-uniform zero mode; symbolic source-stress dependence; and joint scaling/rank.

```text
DECLARED_STATIC_5D_DUST_METRIC_RECOVERS_SCALAR_HESSIAN_AS_R0I0J_BUT_ADDS_COMPACT_INDEX_CURVATURE_WHILE_TENSOR_COMPLETION_REMAINS_SOURCE_DEPENDENT_AND_JOINT_DILATION_RETAINS_ABSOLUTE_SCALE_BLINDNESS_NOT_ELL0
MODEL_LEVEL_LINEARIZED_TENSOR_CONFORMANCE_NOT_EVIDENCE
PHYSICAL_5D_SOURCE_STRESS_LOCALIZATION_DYNAMICS_GAUGE_INVARIANT_OBSERVABLE_RADION_STABILIZATION_COUPLING_CALIBRATION_RECEIVER_NOISE_JOINT_COVARIANCE_DATA_AND_ELL0_LAW_NOT_DERIVED
```

Prior scalar response, finite `S1` localization negative result, and null family `F_0` remain unchanged.
