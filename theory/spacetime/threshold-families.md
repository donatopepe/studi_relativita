# Threshold families

Let `x=ℓ/ℓ₀≥1`. Always compare:

- null: `F_0(x)=0`;
- power: `F_P(x)=A x^-p`, `A,p>0`;
- exponential: `F_E(x)=A exp[-q(x-1)]`, `A,q>0`;
- plateau-power: `F_PE(x)=A_inf+A_1 x^-p`, `A_inf≥0`, `A_1,p>0`.

`no post-data` family invention, norm switching, or favorable-model selection. Parameters remain free until constrained. Noise is not evidence of positive floor.

## Structural identifiability of `ell0`

Writing families against observed `ell` exposes exact degeneracies:

- `F_P=(A ell0^p) ell^-p`;
- `F_E=(A exp(q)) exp[-(q/ell0) ell]`;
- `F_PE=A_inf+(A_1 ell0^p) ell^-p`;
- `F_0` has no `ell0`.

Thus current free-parameter families identify only parameter combinations, not `ell0`. External preregistered amplitude calibration is required for power/plateau-power; exponential additionally requires shape calibration. Current project status is `ELL0_STRUCTURALLY_NON_IDENTIFIABLE_UNDER_CURRENT_FAMILIES`. This scoped result does not cover future families or external calibration.
