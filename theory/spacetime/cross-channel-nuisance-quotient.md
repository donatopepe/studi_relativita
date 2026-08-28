# Cross-channel calibration nuisance quotient

Classification: `PROJECT_DERIVATION_AND_NEGATIVE_RESULT`.

Status: `CROSS_CHANNEL_IDENTIFIABILITY_REQUIRES_CALIBRATION_QUOTIENT`; `NO_POSITIVE_DETECTION_CLAIM`.

For positive toy channels `r_i=A c_i x^{p_i}`, observed as `y_i=g_i r_i`, common gain (`g_1=g_2`) and amplitude cancel from ratio. If `c_i`, exponents, and gain ratio are independently fixed, `p_1!=p_2` permits algebraic recovery of `x`.

With free independent gains, observed ratio is

`y_1/y_2=(g_1/g_2)(c_1/c_2)x^{p_1-p_2}`.

For every positive candidate `x'`, choose a positive `g_1/g_2` reproducing same record. Thus `X_STRUCTURALLY_NON_IDENTIFIABLE_FREE_GAIN_RATIO`. Bounded prospective gain ratio gives set identification (an interval), not point identification. Equal exponents give `X_NON_IDENTIFIABLE_EQUAL_EXPONENTS` even with known calibration.

Therefore projective normalization removes only common scalar nuisance, not channel-wise calibration group. A physical UMCH inference needs channel-native calibration, fixed cross-channel transport/units, shape derivation and bounded nuisance quotient before data. Synthetic exponents do not supply these.

No core reformulation is triggered; physical channel derivation, transport and boundary routes remain open.
