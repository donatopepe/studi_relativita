# Exact-pattern cross-channel homogeneity gate

## Question

Can ratios between operator-native exact channels recover a scale when both have same area homogeneity?

## Control

For fixed-curvature exact-pattern channels, write normalized nonzero invariants `y_i=g_i c_i ell^2 k_i`. Here `k_i` are independently specified geometric amplitudes and `c_i` channel normalization factors. This is an algebraic specialization of existing fixed-curvature `ell^2` controls, not a new physical cross-channel derivation.

## Counterexamples and gates

- Ratio cancels `ell^2`; known calibration recovers geometry/amplitude ratio, not ell.
- Free channel gain and free geometric amplitude ratio are multiplicatively confounded.
- Even with all gains and amplitudes independently fixed, equal homogeneity leaves scale absent from ratio.
- Zero channel makes ratio undefined.
- Unequal synthetic exponents would restore algebraic scale dependence but are not supplied by these exact controls or UMCH theory.
- `ell0` is absent.

## Decision

Status `EXACT_CROSS_CHANNEL_EQUAL_HOMOGENEITY_SCALE_CANCELS`. No reformulation: physically derived unequal scale dependence, transport and boundary maps remain open. `UNPROVEN`; `NO_POSITIVE_DETECTION_CLAIM`.
