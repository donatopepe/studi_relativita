# Cross-channel mixing nuisance gate

## Question

Can a multidimensional response identify scale when calibration mixes channels, not merely rescales each channel?

## Toy control

Let latent response be `r(x)=(x,x^2)` for `x>0`, injective when channel basis is fixed. Observation is `y=M r(x)` with unknown invertible `2x2` calibration/transport mixing matrix.

For any positive candidates `x` and `z`, construct invertible diagonal `M=diag(z/x,z^2/x^2)` so `M r(x)=r(z)`. More generally a free `GL(2)` nuisance acts transitively on nonzero vectors. Thus injectivity before quotient does not imply injectivity after quotient.

## Gates

- Known fixed invertible mixing can be inverted and preserves latent identifiability.
- Unknown common scalar gain leaves projective direction and permits recovery from ratio `r2/r1=x` in this toy.
- Unknown diagonal gains already destroy recovery; free `GL(2)` is stronger.
- Bounded matrix nuisance yields a feasible candidate set, not automatic point identification.
- Physical cross-channel units, basis, transport and leakage matrix must be fixed independently.
- Synthetic `r=(x,x^2)` is not a UMCH mechanism; `ell0` is not derived.

## Decision

Status `CROSS_CHANNEL_INJECTIVITY_DESTROYED_BY_FREE_MIXING_GROUP`. No reformulation: physical calibration/transport derivation remains open. `UNPROVEN`; `NO_POSITIVE_DETECTION_CLAIM`.
