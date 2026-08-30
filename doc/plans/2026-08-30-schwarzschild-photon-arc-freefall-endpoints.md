# Schwarzschild photon-arc freefall endpoint implementation plan

> Execute directly without subagents, per binding user instruction. Follow TDD RED-GREEN-REFACTOR and preserve bounded scientific scope.

**Goal:** Determine whether local radial freely falling endpoint frames add an interior geometric scale direction to the exact photon-sphere finite-arc connection/Jacobi cross-map, or only endpoint-preparation nuisance directions.

**Architecture:** Reuse the merged photon-arc module as the immutable static interior control. A new module derives radial geodesic endpoint boosts, applies explicit left/right endpoint actions to connection and phase maps, reconstructs static objects, tests matched-frame composition and computes separately labelled interior and preparation Jacobians. Emit one canonical JSON artifact; theory and EN/IT reports consume exact tokens and numeric outputs.

**Tech stack:** Python standard library, existing matrix helpers/RK4 controls, `unittest`, Markdown, deterministic JSON.

---

## Task 1: Freeze scientific contract in RED tests

**Files:**
- Create `tests/test_schwarzschild_photon_arc_freefall_endpoints.py`
- Create `tests/test_schwarzschild_photon_arc_freefall_endpoints_sources.py`
- Create `tests/test_schwarzschild_photon_arc_freefall_endpoints_reports.py`

1. Add failing tests for radial geodesic normalization/acceleration, endpoint tetrad orthonormality, static limit, raw endpoint action/reconstruction, zero-window comparison, matched and mismatched composition, caustics, endpoint quotient, separate affine/geometric scale controls, fixed-preparation `(alpha,log M)` rank, separately labelled preparation direction, collision/provenance controls and canonical artifact.
2. Add source-scope tests requiring existing canonical keys and bounded verification-log language.
3. Add bilingual report tests requiring exact status/scope/gate and aligned negative-state tokens.
4. Run:

```bash
python3 -m unittest \
  tests.test_schwarzschild_photon_arc_freefall_endpoints \
  tests.test_schwarzschild_photon_arc_freefall_endpoints_sources \
  tests.test_schwarzschild_photon_arc_freefall_endpoints_reports -q
```

Expected: RED because module/artifact/reports are absent.
5. Commit: `test: define photon-arc freefall endpoint controls`.

## Task 2: Implement endpoint-frame module and canonical artifact

**Files:**
- Create `studies/spacetime/schwarzschild_photon_arc_freefall_endpoints.py`
- Create `studies/spacetime/schwarzschild-photon-arc-freefall-endpoints-results.json`

1. Load existing photon-arc and Schwarzschild matrix helpers locally.
2. Implement radial geodesic state and coordinate/tetrad controls with explicit domain checks.
3. Implement connection action `B_o^-1 T B_s`, phase-rate action `D_o^-1 P D_s`, and exact static reconstruction.
4. Implement zero-window, matched/mismatched composition with inserted transition, caustic and quotient controls.
5. Implement affine and geometric scale controls independently.
6. Implement finite-difference Jacobians: fixed preparation versus `(alpha,log M)`, and augmented preparation derivative explicitly labelled nuisance. Do not infer statistical independence.
7. Implement collision and prior full-winding provenance controls.
8. Emit deterministic artifact through normal generation and `--check`.
9. Run focused tests to GREEN and commit: `feat: audit photon-arc freefall endpoint frames`.

## Task 3: Theory, bilingual audit, source log and roadmap

**Files:**
- Create `theory/spacetime/schwarzschild-photon-arc-freefall-endpoints.md`
- Create `audit/schwarzschild-photon-arc-freefall-endpoints-report-en.md`
- Create `audit/schwarzschild-photon-arc-freefall-endpoints-report-it.md`
- Modify `references/verification-log.md`
- Modify `docs/roadmap.md`

1. Explain known/project/toy/negative/open classifications and formulas.
2. Report raw objects before diagnostics; distinguish endpoint comparison from interior transport and from holonomy.
3. Record exact residuals, ranks, scale null, preparation nuisance and caustic behavior from artifact.
4. Bound source claims: existing Schwarzschild/Darwin/Sachs sources provide geometry/framework context only; endpoint protocol and readout are project/open.
5. Keep EN/IT exact semantic parity for labels, tokens, equations, citations, limitations and direct-review exception.
6. Run source/report/focused tests and commit: `docs: report photon-arc freefall endpoint nuisance`.

## Task 4: Direct conformance review and full verification

1. Because the user forbids subagents, record and perform direct closure review against spec, plan, artifact, theory, EN/IT reports and roadmap.
2. Run fresh focused suite and artifact `--check`.
3. Run full local CI equivalents:

```bash
python3 -m unittest discover -s tests -q
python3 tools/extract_docx.py --check
python3 tools/inventory_source.py --check
python3 studies/free-fall-identifiability/analysis.py --check
python3 studies/spacetime/schwarzschild_photon_arc_freefall_endpoints.py --check
git diff --check
```

4. Attempt local LaTeX only if `pdflatex` exists; otherwise record exact unavailability and require CI `latex` pass.
5. Fix only bounded conformance defects test-first; commit any review-only alignment.

## Task 5: PR, CI, conservative merge and Hermes

1. Push `research/schwarzschild-photon-arc-freefall-endpoints` and open PR with exact status/scope/gate, source limits and verification evidence.
2. Require green `tests` and `latex` jobs. Do not merge if ambiguity, scientific overclaim or failure appears.
3. If conservative and green, merge normally, sync `main`, remove worktree/local branch and prune remote.
4. Write timestamped Hermes Inbox note with PR, merge SHA, CI URLs, state/scope/gate, rank and open routes.
5. Keep loop `16588751` active. Do not declare structural dead end: generic scattering and physical detector/readout routes remain open.
