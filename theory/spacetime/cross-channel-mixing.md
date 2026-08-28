# Cross-channel mixing nuisance quotient

Classification: `TOY_CONTROL_AND_NEGATIVE_RESULT`.

Status: `CROSS_CHANNEL_INJECTIVITY_DESTROYED_BY_FREE_MIXING_GROUP`; `NO_POSITIVE_DETECTION_CLAIM`.

Let latent response be `r(x)=(x,x^2)` for positive `x`. With fixed channel basis, projective ratio `r_2/r_1=x` recovers `x`, so latent map is injective. Observe instead `y=M r(x)`.

If invertible `M` is independently known, inversion preserves latent identifiability. If `M` is unknown, every two positive candidates `x,z` collide under invertible diagonal matrix

`M(x,z)=diag(z/x,(z/x)^2)`,

because `M(x,z)r(x)=r(z)`. Hence even diagonal subgroup of free mixing group destroys injectivity after nuisance quotient; free `GL(2)` is stronger. Common scalar gain alone would preserve projective ratio, showing group choice matters.

Bounded prospective mixing yields a feasible candidate set, not automatic point identification. Channel units, basis, cross-talk/leakage, transport and calibration matrix must be fixed or bounded independently.

Synthetic unequal-homogeneity map is not a physical UMCH mechanism. `ell0` is not derived. Physical channel-native mixing remains open; no core reformulation is triggered.
