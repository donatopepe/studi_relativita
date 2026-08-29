# Cross-channel bounded-gain set identification

Classification: `PROJECT_DERIVATION_AND_NEGATIVE_RESULT`.

Status: `CROSS_CHANNEL_BOUNDED_GAIN_SHARP_SET_IDENTIFICATION_ONLY`; `NO_POSITIVE_DETECTION_CLAIM`.

For positive ratio model

`R=gamma C x^delta`,

with independently fixed `C>0`, unequal homogeneity `delta!=0`, and prospective gain-ratio bounds `gamma in [gamma_min,gamma_max]`, exact feasible interval is obtained by transforming both gain endpoints and sorting:

`X=[min z_i,max z_i]`, where `z_i=(R/(C gamma_i))^(1/delta)`.

For every candidate inside interval, `gamma=R/(C x^delta)` is admissible and reproduces record. Interval is therefore sharp set identification, not point identification. Point recovery occurs only when gain interval collapses, conditional on synthetic model and all other quantities fixed.

For `delta=0`, ratio contains no `x`. It can only test whether `R/C` lies inside gain bounds; inconsistency rejects nuisance/model combination but does not estimate `x`.

Bounds must be prospective and independently calibrated. Post-fit tightening is forbidden. This positive power-ratio toy supplies no physical channel law, bounds, data or `ell0`; no core reformulation is triggered.
