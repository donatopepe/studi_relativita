# Sphere cross-channel harmonic aliasing gate

## Exact channel map

Let connection-derived phase be `alpha=eta ell^2/r^2`. Consider two independently defined conjugacy-invariant synthetic harmonic channels

`y1=cos(alpha)`, `y2=cos(2 alpha)`.

They obey exact dependence

`y2=2 y1^2-1`.

Thus second channel adds no independent phase information: joint map has rank one and remains even/periodic. On preregistered branch `[0,pi]`, y1 identifies alpha; globally `alpha` has sign and `2pi` aliases. If first channel is spectral-gap magnitude `|cos alpha|`, pair `(abs(cos alpha),cos(2alpha))` is even more redundant because `y2=2 gap^2-1`, with pi-period aliases.

Using sine channel would encode orientation locally, but requires oriented frame/loop convention and still leaves `2pi` winding. It is not derived here as physical independent channel.

## Identifiability

Known eta and r plus branch can recover geometric ell/r. Unknown eta/r^2 remains confounded. No ell0 occurs. More channels do not help if algebraically dependent after nuisance quotient.

## Decision

Classification `PROJECT_DERIVATION_AND_NEGATIVE_RESULT`; status `SPHERE_CROSS_CHANNEL_HARMONIC_ALGEBRAIC_DEPENDENCE_NOT_ELL0`. Exact sphere phase specialization, synthetic channels, no data. Structural dead end not met; no detection or reformulation.
