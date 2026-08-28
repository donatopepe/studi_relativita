# Cross-channel calibration nuisance quotient

## Question

Does an unequal-exponent channel ratio remain scale-identifying when calibration nuisance is admitted?

## Model

For positive channels `r_i(x)=A c_i x^p_i`, compare nuisance groups:

- common gain `g`: observed channels `g r_i`; ratio cancels `A,g` and can recover `x` if `c_i,p_i` are independently fixed and `p_1!=p_2`;
- independent gains `g_i`: ratio contains unknown `g_1/g_2`; for every candidate `x'` a positive gain ratio reproduces same observation;
- bounded gain ratio: yields only an interval for `x`, not point identification;
- equal exponents: ratio independent of `x` even with known calibration.

This is an exact algebraic project derivation/toy control. It does not derive physical exponents, coefficients, gains, or UMCH channels.

## Decision

Status `CROSS_CHANNEL_IDENTIFIABILITY_REQUIRES_CALIBRATION_QUOTIENT`. Cross-channel multidimensionality identifies scale only after nuisance group is prospectively constrained. Under independent free gains, `x` and hence `ell0` are structurally non-identifiable. No reformulation: transport/boundary and physical channel derivation remain open. `UNPROVEN`; `NO_POSITIVE_DETECTION_CLAIM`.
