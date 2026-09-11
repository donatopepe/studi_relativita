# Kerr composite common-calibration profile gate

## Status

`RATIFIED_FOR_IMPLEMENTATION_PLANNING`

## Scientific distinction

Previous common-calibration result compares plus/minus branches at one identical physical calibration `(g1,g2,n)`. Composite-hypothesis profiling instead permits each hypothesis to fit its own nuisance point inside same declared domain:

```text
H_+={diag(g_+) Gamma_+ diag(g_+) + n_+^2 I}
H_-={diag(g_-) Gamma_- diag(g_-) + n_-^2 I}
```

This is not branch-dependent hardware. It is conservative statistical profiling of one unknown calibration under competing hypotheses. Positive same-point KL does not prove disjoint composite sets.

## MVP-first gate

**Objective:** decide whether `H_+` and `H_-` overlap on bounded toy domain, and preserve an exact collision when bounds are relaxed.

**Metric and threshold:** exactly `8/8` controls.

**Cases/order:** analytic covariance-set overlap, domain validation, bounded profile separation, deterministic refinement, boundary witness, exact relaxed-domain collision, basis/scale invariance, nonclaims.

**Fixed domain:** branch-profiled diagonal gains `g1,g2 in [0.5,1.5]`; branch-profiled isotropic noise sigma `n in [0.1,1.0]`. Input signal covariances remain fixed prior outputs. Deterministic pair-grid sizes are preregistered before implementation. Bounds are toy controls, not hardware priors.

For diagonal `Gamma_o=diag(a_o,b_o)`, exact collision at noises `n_+,n_-` requires, independently for `i=1,2`, intersection of

```text
[a_+*0.5^2+n_+^2, a_+*1.5^2+n_+^2]
[a_-*0.5^2+n_-^2, a_-*1.5^2+n_-^2]
```

(and analogous `b` intervals). Bounded disjointness must be established analytically, not inferred from a finite scan. Pair profiling uses symmetric Gaussian KL only as a bounded numerical witness.

## Eight controls

1. Analytic interval-overlap evaluator is exact for diagonal covariances and identifies bounded set disjointness.
2. Domain rejects nonfinite, nonpositive and out-of-bound profiled nuisances.
3. Bounded composite profile minimum has preregistered positive lower gate.
4. Deterministic refinement does not increase the sampled minimum and records convergence/boundary caveat.
5. Best bounded witness lies on declared least-separation boundary and direct KL agrees.
6. Relaxing gain bounds yields one explicit exact positive-gain covariance collision with residual below `2e-10`.
7. Simultaneous orthogonal basis change and geometric scale conversion preserve profile KL/rank null within `2e-10`.
8. Artifact preserves `L_identified=false`, `ell0_identified=false`, `L_equals_ell0=NOT_DERIVED`, no extra-dimension detection and no positive detection claim.

## Scenarios

J31-J38 map one-to-one to controls above. New category: `profiling`. Existing J01-J30 remain unchanged. Runner must fail closed in total, per-scenario and per-category modes and emit JSON.

## Interpretation ceiling

```text
MODEL_LEVEL_BOUNDED_COMPOSITE_CALIBRATION_PROFILE_NOT_EVIDENCE
```

No claim of measured calibration bounds, identifiability of absolute scale or `ell0`, Kerr-versus-5D discrimination, extra-dimension detection, or UMCH confirmation.

```text
UMCH=UNPROVEN_SECONDARY_CANDIDATE
L_identified=false
ell0_identified=false
L_equals_ell0=NOT_DERIVED
extra_dimension_detected=false
structural_dead_end=NOT_DECLARED
NO_POSITIVE_DETECTION_CLAIM
```

## Source scope

Uses only already verified Gaussian covariance/KL identities and existing Kerr source covariance outputs. No new external empirical claim or citation is introduced.
