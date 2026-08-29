# Cross-channel bounded-gain set-identification gate

## Question

What exact candidate set follows from prospectively bounded gain ratio in unequal-homogeneity two-channel toy?

## Derivation

Observed positive ratio

`R=(g1/g2) C x^delta`,

where `C>0`, `delta=p1-p2 != 0`, and gain ratio `gamma=g1/g2` is independently bounded `gamma in [gamma_min,gamma_max]`, both positive.

For `delta>0`, exact feasible set is

`x in [(R/(C gamma_max))^(1/delta),(R/(C gamma_min))^(1/delta)]`.

For `delta<0`, endpoint order reverses; compute both transformed endpoints and sort. Every interior candidate is attainable with `gamma=R/(C x^delta)`. Bounds therefore give sharp set identification, not point identification, unless gain interval collapses. Equal homogeneity `delta=0` contains no x information; inconsistent observed ratio can reject nuisance bounds but does not estimate x.

## Gates

Bounds must be fixed before response; post-fit tightening is forbidden. Synthetic powers remain nonphysical. `ell0` is absent unless x is independently derived as ell/ell0.

## Decision

Status `CROSS_CHANNEL_BOUNDED_GAIN_SHARP_SET_IDENTIFICATION_ONLY`. No reformulation: physical calibration bounds and channel laws remain open. `UNPROVEN`; `NO_POSITIVE_DETECTION_CLAIM`.
