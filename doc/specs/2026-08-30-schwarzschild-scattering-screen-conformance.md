# Schwarzschild scattering screen/Riemann conformance gate

## Status and bounded question

This conservative follow-up audits the full finite-boundary Schwarzschild null-scattering Jacobi control merged in PR #94. It does not change the ratified UMCH object or hypothesis. UMCH remains `UNPROVEN`; `ell0_identified=false`; detection remains `NO_POSITIVE_DETECTION_CLAIM`.

Question: is the declared polar-plus-in-plane screen genuinely Levi-Civita parallel along the equatorial scattering ray, at least modulo null-gauge equivalence, and does an independent coordinate finite-difference reconstruction of the four-dimensional Schwarzschild Riemann tensor reproduce or falsify the currently implemented analytic optical profile? The preregistered target before running the reconstruction was

\[
 \mathcal K_{\rm old}=\operatorname{diag}(+1,-1)\frac{Mb^2}{r^5}.
\]

The test may falsify its sign, screen ordering or normalization; no generated result may be absorbed by changing tolerances. Sign convention remains `X''=K X`.

Classifications:

- Schwarzschild metric, Levi-Civita connection, null geodesics and geodesic deviation: `KNOWN_RESULT` within canonical source scope;
- coordinate screen conversion, covariant finite-difference derivative, null-gauge quotient, numerical Christoffel/Riemann reconstruction and convergence audit: `PROJECT_DERIVATION`;
- finite endpoint, static tetrad, `E_infinity=1`, selected screen handedness and numerical step schedule: `TOY_CONTROL` / project anchors;
- nonzero quotient transport drift, failed convergence, polar-sector mismatch or profile normalization mismatch: `NEGATIVE_RESULT` against the current project implementation;
- physical screen preparation, emitter/absorber tetrads, detector readout, covariance and any `ell0` law: `OPEN_PROBLEM`.

No cited source establishes this project protocol, detector calibration, covariance, `ell0`, UMCH, evidence or detection.

## Alternatives and selected design

1. **Trust the analytic screen label and hard-code zero residual.** Rejected: declaration is not a transport proof.
2. **Integrate a second transported screen as the primary basis.** Valid but risks changing the already audited phase-map trivialization before testing whether the existing basis is equivalent modulo null gauge.
3. **Audit the existing basis covariantly, quotient only the allowed null gauge, and independently reconstruct Riemann.** Selected. This is the smallest counterexample-first conformance test and preserves raw objects.

If the quotient residual is not convergent to zero, option 2 becomes required in a separate correction. No tolerance failure may be relabelled as calibration freedom.

## Domain, path and conventions

Reuse the preregistered domain and path:

- `M>0`, `R>rho>3`;
- `beta=b/M=rho/sqrt(1-2/rho)`;
- finite incoming branch, one turning point, finite outgoing branch;
- future null ray, equatorial plane, orientation `+/-1`;
- `E_infinity=-k_t=1` project normalization.

Use Schwarzschild coordinates `(t,r,theta,phi)`, signature `(-,+,+,+)`, and

\[
 ds^2=-fdt^2+f^{-1}dr^2+r^2d\theta^2+r^2\sin^2\theta d\phi^2,
 \qquad f=1-2M/r.
\]

The local static-tetrad direction is `(n_r,0,n_phi)`, with `n_r^2+n_phi^2=1`. Coordinate vectors are

\[
 k^\mu=(f^{-1},n_r,0,b/r^2),\quad
 e_1^\mu=(0,0,r^{-1},0),\quad
 e_2^\mu=(0,-n_\phi\sqrt f,0,n_r/r).
\]

Preserve orientation and branch labels. Turning-point derivatives use symmetric path neighbours; endpoints use one-sided differences and are reported separately.

## Screen transport audit

For each retained interior sample compute

\[
 q_A^\mu=\frac{de_A^\mu}{d\lambda}
 +\Gamma^\mu{}_{\alpha\beta}k^\alpha e_A^\beta.
\]

Construct an auxiliary null vector from the static observer and spatial ray direction,

\[
 l^{(a)}=\frac{\sqrt f}{2}(1,-n_r,0,-n_\phi),
 \qquad k\cdot l=-1.
\]

For a transported screen equivalence class, `q_A` may equal `alpha_A k`. Determine `alpha_A=-l_mu q_A^mu`, retain both raw `q_A` and quotient residual

\[
 q_{A,\perp}^\mu=q_A^\mu-\alpha_A k^\mu.
\]

Record:

- raw covariant-derivative norm;
- fitted null-gauge coefficient;
- quotient residual norm;
- screen-rotation entries `e_B dot q_A`;
- orthonormality and `k dot e_A` residuals;
- endpoint one-sided residuals separately;
- coarse/fine convergence ratios.

The full derivative need not vanish when a null-gauge representative changes. Only the explicitly recorded quotient residual supports `PARALLEL_SCREEN_MODULO_NULL_GAUGE`. A mathematical quotient remains distinct from physical endpoint calibration.

## Independent Riemann reconstruction

Implement a generic Schwarzschild metric evaluator at `(r,theta)`. Reconstruct Christoffel symbols from centered finite differences of the metric in both `r` and `theta`; do not use the equatorial-only connection helper for the polar sector. Reconstruct

\[
 R^\rho{}_{\sigma\mu\nu}
 =\partial_\mu\Gamma^\rho{}_{\nu\sigma}
 -\partial_\nu\Gamma^\rho{}_{\mu\sigma}
 +\Gamma^\rho{}_{\mu\eta}\Gamma^\eta{}_{\nu\sigma}
 -\Gamma^\rho{}_{\nu\eta}\Gamma^\eta{}_{\mu\sigma}
\]

with a second centered finite-difference layer, lower the first index with the metric, and project the full tensor:

\[
 K^{FD}_{AB}=-R_{\mu\nu\rho\sigma}e_A^\mu k^\nu e_B^\rho k^\sigma.
\]

Use at least endpoint-adjacent, intermediate and turning checkpoints on both orientations. Run two or more dimensionless step sizes. Record full `2x2` matrices, symmetry, trace, analytic mismatch and observed convergence. The acceptance threshold must be fixed in tests before implementation and must not be inferred from generated values.

## Tests and falsifiers

Tests are preregistered to require:

1. metric signature and null/screen orthogonality at incoming, turning and outgoing samples;
2. polar screen raw transport near zero and in-plane raw derivative either near zero or explicitly null-gauge only;
3. quotient transport and screen-rotation residuals decrease under step refinement and pass fixed bounds;
4. finite-difference Riemann projection includes `theta` derivatives, is symmetric and trace-free within fixed bounds, and converges to the analytic full matrix;
5. both orientations agree in the projected profile while retaining orientation in raw path/screen labels;
6. `rho -> 3+` independently evaluates the photon-sphere anchor rather than assuming the old `M^2 K_11 -> 1/9` value;
7. deterministic artifact rerendering is byte-identical;
8. all prior Jacobi, scale, caustic, endpoint-action and rank tests remain green.

Failure states:

- `SCREEN_NOT_PARALLEL_EVEN_MODULO_NULL_GAUGE`;
- `POLAR_RIEMANN_PROJECTION_NOT_INDEPENDENTLY_REPRODUCED`;
- `FINITE_DIFFERENCE_CONVERGENCE_NOT_ESTABLISHED`;
- `CURRENT_JACOBI_PROFILE_CONFORMANCE_FAILED`.

No bounded failure is evidence for UMCH.

## Outputs and interpretation ceiling

Produce a deterministic JSON artifact, theory note, bilingual EN/IT audits, source-scope log and roadmap entry. Preserve raw derivative vectors and full finite-difference `K` matrices; scalar maxima are diagnostics only.

Passing state if the old profile survives:

`SCHWARZSCHILD_SCATTERING_SCREEN_IS_LEVI_CIVITA_PARALLEL_MODULO_EXPLICIT_NULL_GAUGE_AND_INDEPENDENT_FOUR_DIMENSIONAL_RIEMANN_RECONSTRUCTION_CONFIRMS_OPTICAL_PROFILE_NOT_ELL0`.

Correction state if the raw reconstruction falsifies the old profile but a bounded replacement passes convergence and all phase-map controls:

`SCHWARZSCHILD_SCATTERING_SCREEN_IS_PARALLEL_MODULO_NULL_GAUGE_BUT_FULL_RIEMANN_RECONSTRUCTION_FALSIFIES_PRIOR_OPTICAL_PROFILE_AND_REQUIRES_CORRECTED_PHASE_MAP_NOT_ELL0`.

Only fixed tests decide between them. Interpretation ceiling remains `CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE`.

Open gate remains:

`PHYSICAL_SCATTERING_SOURCE_PROFILE_EMITTER_ABSORBER_TETRADS_ABSOLUTE_FREQUENCY_STANDARD_SCREEN_PREPARATION_CAUSTIC_CONTINUATION_VECTOR_READOUT_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED`.

This audit does not satisfy structural-dead-end criteria: detector-derived calibration/readout and more physical exact controls remain open routes. No reformulation is triggered.
