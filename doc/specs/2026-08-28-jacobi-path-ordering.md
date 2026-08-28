# Noncommuting Jacobi path-ordering gate

## Question

Do local optical-tidal spectra determine finite-path Jacobi transport when matrices at different segments do not commute?

## Toy control

Represent each constant segment by first-order screen generator `G(K)=[[0,I],[-K,0]]` and use second-order deterministic propagator `I+hG+h^2 G^2/2`. Compare two paths containing the same symmetric optical-tidal matrices `K_A,K_B` in opposite order.

This is numerical linear-algebra toy, not exact Sachs integration, observation, or UMCH mechanism.

## Counterexamples and gates

- If generators commute, reversing segments gives same propagator in control.
- If they do not commute, same unordered local spectra and same integrated trace can yield different endpoint Jacobi maps.
- Therefore histogram/average of instantaneous eigenvalues is insufficient; ordered matrix history, screen transport and boundary data are required.
- A commutator norm diagnoses possible ordering sensitivity but is not an `ell0` observable.
- Endpoint differences remain geometric/path-dependent; `ell0` is absent unless a derived injective relation is supplied.

## Decision

Status `JACOBI_PATH_ORDER_REQUIRED_LOCAL_SPECTRA_INSUFFICIENT`. No reformulation: exact varying optical matrices and physical boundary maps remain open. `UNPROVEN`; `NO_POSITIVE_DETECTION_CLAIM`.
