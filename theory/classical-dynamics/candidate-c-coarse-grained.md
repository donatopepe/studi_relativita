# Candidate C — Coarse-grained curvature bound

Scientific status: `UNPROVEN`  
Hypothesis class: `ALTERNATIVE_HYPOTHESIS`

## Domain and candidate observable

For a timelike worldline, choose an invariant proper time window and nonnegative normalized kernel `w(τ)`:

\[
\kappa_{\mathrm{RMS}}=
\left[\frac{\int_{\Delta\tau}d\tau\,w(\tau)\kappa(\tau)^2}
{\int_{\Delta\tau}d\tau\,w(\tau)}\right]^{1/2},
\qquad
\kappa_{\mathrm{RMS}}\ge\kappa_0.
\]

The scalar retains dimension `L⁻¹`. Proper time makes parameter choice invariant for timelike curves, but selecting window, kernel, endpoints, and detector response adds physical structure.

## Analysis level

- `KINEMATIC`: weighted RMS definition and dimensions.
- `SYMBOLIC`: finite-sequence counterexample proving non-equivalence.
- `CONJECTURAL`: continuum dynamics, covariant kernel selection, estimator, and universality.

## NOT_EQUIVALENT to pointwise UMCH

A preregistered example uses equal weights, `κ₀=1`, and samples `[0,2]`. Then

\[
\kappa_{\mathrm{RMS}}=\sqrt{2}>1,
\]

while instantaneous `κ=0` occurs and pointwise `κ≥κ₀` fails. Therefore RMS bound does not imply pointwise bound. Conversely, pointwise bound with nonnegative weights implies RMS bound, so relation is one-way, not equivalence.

Candidate C cannot rescue A or B. It changes hypothesis and requires separate ratification before becoming a research program.

## Window and kernel requirements

A viable definition must specify:

- invariant proper time duration or physical scale;
- nonnegative normalized kernel and support;
- endpoint/finite-record treatment;
- whether window is detector-, state-, mass-, or environment-dependent;
- transformation and sampling rules;
- uncertainty and calibration model.

Without these, different windows can classify same trajectory differently.

## Dynamics and initial data

Condition supplies no action or evolution equation. A finite past/future window can be nonlocal and may require history or future data. Causal implementation is not established.

## Standard limit

For finite RMS, `κ₀→0` makes inequality nonrestrictive. This does not recover standard dynamics because no dynamics was defined.

## Observable and identifiability

Possible observable is RMS proper acceleration divided by `c²`, evaluated through calibrated response. No experiment-to-parameter mapping, window-selection law, or noise model exists. Current state is `NON_IDENTIFIABLE`.

## Reproducible check

`studies/classical-dynamics/coarse_grained_check.py` computes weighted RMS and preserves an explicit counterexample with instantaneous κ=0. It proves `NOT_EQUIVALENT` only; it does not validate physical averaging.

## Decision

State: `NON_IDENTIFIABLE`. Candidate remains `ALTERNATIVE_HYPOTHESIS`, not pointwise UMCH. Proceeding requires separate ratification, operational kernel, dynamics, causal interpretation, and data model.
