# ell0 structural identifiability gate

## Question

Can `ell0` be separated from threshold amplitudes using the preregistered families and scale-response observations, before any real-data claim?

## Algebraic result

For `ell` observed directly and `x=ell/ell0`:

- `F_P=A(ell/ell0)^(-p)=(A ell0^p) ell^(-p)`. Data identify only `B=A ell0^p`; `A` and `ell0` are structurally non-identifiable without independent amplitude calibration.
- `F_E=A exp[-q(ell/ell0-1)]=(A e^q) exp[-(q/ell0)ell]`. With both `q` and `ell0` free, data identify combinations `B=A e^q` and `r=q/ell0`; `q` and `ell0` are structurally non-identifiable without independent shape calibration.
- `F_PE=A_inf+A_1(ell/ell0)^(-p)=A_inf+(A_1 ell0^p)ell^(-p)`. `A_1` and `ell0` are structurally non-identifiable; `A_inf` does not cure this.
- `F_0=0` contains no `ell0`.

## Gate

Current preregistered family union cannot identify `ell0` when family amplitudes/shape parameters remain free. Resolved frame, fixed norm, uncertainty model, multiple scales, and replication are necessary but cannot remove these exact reparameterization symmetries.

`ell0` may become identifiable in principle only after external, preregistered calibration fixes enough amplitude/shape information and family selection is independently justified. No such calibration exists in the project.

## Status

`ELL0_STRUCTURALLY_NON_IDENTIFIABLE_UNDER_CURRENT_FAMILIES`; core `UNPROVEN`; `NO_POSITIVE_DETECTION_CLAIM`. This is a scoped negative identifiability result, not disproof of all possible UMCH formulations.
