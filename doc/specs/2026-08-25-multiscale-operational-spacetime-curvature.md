# Multiscale Operational Spacetime Curvature Hypothesis

## Status

Ratified restart specification. Supersedes the worldline-curvature formulation as UMCH core while preserving its audit history.

- Italian title: **Ipotesi Multiscala della Curvatura Operativa dello Spaziotempo**
- English title: **Multiscale Operational Spacetime Curvature Hypothesis**
- Acronym retained: **UMCH**
- Author: Pepe Donato, Independent Researcher
- Core status: `UNPROVEN`

## Correction of physical interpretation

A freely falling body may follow a timelike geodesic,

\[
a^\mu=u^\nu\nabla_\nu u^\mu=0,
\qquad \kappa_{\rm wl}=0,
\]

while spacetime is intrinsically curved. No reaction force is required at a minimum worldline curvature because the restarted hypothesis does not impose one. Physical curvature is probed through finite-region relative effects: geodesic deviation, holonomy, clocks, null bundles, and congruences.

Previous Candidate A/B results remain valid only for their fixed historical worldline models and are marked `HISTORICAL_WORLDLINE_FORMULATION` / `SUPERSEDED_AS_CORE`.

## Global statement

The realized spacetime of our universe is not globally isometric to Minkowski spacetime:

\[
(\mathcal M,g_{\rm real})\not\cong(\mathbb R^4,\eta).
\]

This statement alone is not novel. Minkowski remains a valid mathematical solution and null model.

## Multiscale operational hypothesis

Introduce universal length `ℓ₀>0`, with historical notation `κ₀=ℓ₀^{-1}` retained only as a scale. For causally admissible physical regions `Ω` of characteristic scale `ℓ≥ℓ₀`, resolved physical frame `u_phys`, and preregistered experiment family, define dimensionless response vector

\[
\mathbf R(\Omega,\ell;g,u_{\rm phys})=
(R_{\rm tidal},R_{\rm mag},R_{\rm hol},R_{\rm clock},R_{\rm null},R_{\rm cong}).
\]

Preregister two norms:

\[
\mathfrak C_\infty=\|\mathbf R\|_\infty,
\qquad
\mathfrak C_2=\|\mathbf R\|_2.
\]

A quantitative model must select norm before data analysis and test

\[
\mathfrak C_q(\Omega,\ell)
\ge F_j(\ell/\ell_0;\theta_j)>0,
\qquad q\in\{2,\infty\}.
\]

Raw response vector remains public. No switching norm after results.

## Domain

- Applies to realized spacetime of our universe, not every mathematical spacetime.
- Regions are causally testable at least in principle, geometrically regular, and support contained test protocols.
- Scale domain is `ℓ≥ℓ₀`; no operational claim below `ℓ₀`.
- Technology available today does not define admissibility.
- Frame-unresolved regions cannot confirm hypothesis.

## Physical frame hierarchy

1. Use unique future timelike regular eigenvector of `T^μ_ν` when it exists.
2. In vacuum/degenerate sectors, use covariantly specified continuation of cosmological mean/CMB frame.
3. If no unique continuation exists, classify `FRAME_UNRESOLVED`.

This is a property of realized cosmological state; local-law Lorentz violation must be derived, not assumed.

## Response components

Candidate normalized definitions:

\[
R_{\rm tidal}=\ell^2\langle E_{\mu\nu}E^{\mu\nu}\rangle_\Omega^{1/2},
\quad E_{\mu\nu}=R_{\mu\alpha\nu\beta}u^\alpha u^\beta,
\]

\[
R_{\rm mag}=\ell^2\langle B_{\mu\nu}B^{\mu\nu}\rangle_\Omega^{1/2},
\quad B_{\mu\nu}={}^\star R_{\mu\alpha\nu\beta}u^\alpha u^\beta,
\]

plus preregistered finite-loop holonomy, differential-clock, null-bundle, and congruence responses. Each requires exact normalization, sampling, subtraction, and uncertainty protocol before data use.

## Threshold families

Always compare null model `F₀(x)=0` against preregistered positive families:

\[
F_P(x)=Ax^{-p},\quad A>0,p>0,
\]

\[
F_E(x)=Ae^{-q(x-1)},\quad A>0,q>0,
\]

\[
F_{PE}(x)=A_\infty+A_1x^{-p},
\quad A_\infty\ge0,A_1>0,p>0.
\]

No post-data family invention or favorable-family selection.

## Exact baseline cases

1. **Minkowski:** all operational responses must be zero; null mathematical control.
2. **FLRW:** cosmological Ricci/expansion responses; frame naturally defined by cosmological fluid where regular.
3. **Schwarzschild vacuum:** Ricci zero but Weyl/tidal response nonzero; cosmological frame continuation issue explicit.
4. **VSI gravitational wave:** polynomial scalar invariants may vanish while observer-dependent tidal/magnetic/holonomy responses are nonzero.
5. **Nearly flat limit:** response vector may tend continuously to zero mathematically.

These cases test definitions; they do not establish positive lower bound in real universe.

## Falsification and states

Positive hypothesis is contradicted if an admissible realized region and `ℓ≥ℓ₀` has exactly zero preregistered response vector, or if data force all positive threshold families to null boundary under preregistered inference.

States:

- `SUPPORTED_WITHIN_DATA_RANGE`
- `UPPER_BOUND_ONLY`
- `NON_IDENTIFIABLE`
- `FRAME_UNRESOLVED`
- `CONTRADICTED`
- `UNREVIEWED`

Noise or failure to resolve zero is not positive evidence.

## Repository reorganization

Create new spacetime core under:

```text
theory/spacetime/
papers/spacetime-foundations/{it,en}/
studies/spacetime/
audit/spacetime-claims.csv
audit/spacetime-foundation-report-{it,en}.md
archive/worldline-program/README.md
```

Existing files retain paths/history but receive historical/superseded banners where they present worldline formulation as core. README files are rewritten around spacetime hypothesis.

## New sequence

1. Spacetime foundations and operational definitions.
2. Exact cases and nearly flat limits.
3. Observables/data and identifiability.
4. QFT/quantum gravity only after operational identifiability.

ALD/worldline Paper III is not resumed from superseded pointwise premise.

## Initial milestone acceptance criteria

1. Rewrite bilingual README and scientific roadmap.
2. Mark historical worldline core without deleting results.
3. Implement theory documents for regions, frame, responses, thresholds, limits, open problems.
4. Add deterministic exact-case calculations for Minkowski, FLRW, Schwarzschild, and one VSI-wave example with source provenance.
5. Preserve dimensionless response normalization and frame statuses.
6. Produce bilingual audit and new Paper I.
7. Include null threshold model and all preregistered positive families.
8. Report identifiability, not positive detection.
9. Full tests/checks and bilingual LaTeX CI pass.
10. PR requires human review before merge.

## Out of scope

Claiming the cosmologically realized positive floor is measured; selecting `ℓ₀`; modifying Einstein equations; erasing historical no-go; using current technology as definition; proceeding to ALD/QED/cosmology phenomenology before exact-case definitions and identifiability.
