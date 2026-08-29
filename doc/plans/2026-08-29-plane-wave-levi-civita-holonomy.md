# Exact Brinkmann plane-wave Levi-Civita holonomy implementation plan

> Execute directly in isolated worktree. No subagents. TDD required.

**Goal:** Derive and falsification-test genuine four-dimensional Levi-Civita holonomy on explicit Brinkmann coordinate loops, preserving raw matrices and proving bounded spectral/scale non-identifiability without making UMCH claims.

**Architecture:** Add one dependency-free deterministic Python study. Integrate the pulled-back analytic Levi-Civita connection segment by segment with fixed-step RK4, extract/verify null-rotation parameters, run reversal/composition/profile/anchor/scaling/null controls, and serialize JSON. Tests own scientific identities and report parity. Docs classify source facts, project derivations, negative results, and open physical gates.

**Tools:** Python standard library, existing local matrix helpers/patterns, `unittest`, JSON, Markdown, GitHub Actions.

## Task 1: Scientific API tests — RED

**Files:**
- Create `tests/test_plane_wave_levi_civita_holonomy.py`

Write tests requiring:
- analytic connection transport preserves base null Gram matrix and parallel null vector;
- nonzero rectangle gives nonidentity `H_LC` matching extracted `N(b)`;
- distinct amplitudes have all-unit eigenvalue/characteristic data while raw matrices differ;
- reversal gives inverse and `b -> -b`;
- based-loop composition commutes and adds `b`;
- profile collision, null competitor, common-screen covariance, null-boost nuisance, and affine scaling behave as specified;
- generated artifact is deterministic and contains status, gate, scope, raw record, `ell0_identified=false`, `umch_status=UNPROVEN`, `positive_detection_claim=false`, `structural_dead_end=NOT_DECLARED`.

Run:

`python3 -m unittest tests.test_plane_wave_levi_civita_holonomy -v`

Expected RED: module/file absent.

Commit failing tests.

## Task 2: Minimal connection-derived implementation — GREEN

**Files:**
- Create `studies/spacetime/plane_wave_levi_civita_holonomy.py`
- Generate `studies/spacetime/plane-wave-levi-civita-holonomy-results.json`

Implement dependency-free:
- matrix operations, RK4 matrix transport, profile and derivative;
- metric/connection pullback for `(u,v,x1,x2)`;
- explicit rectangle segments and reversed paths;
- `null_rotation(b)`, extraction, characteristic coefficients appropriate to unipotent check;
- controls: `geometry_control`, `spectrum_control`, `reversal_control`, `composition_control`, `profile_control`, `anchor_control`, `affine_control`, `null_control`, `build`;
- CLI `--write` and `--check`.

Keep numerical tolerances at least an order above observed residuals. Do not use spectrum alone as proof of matrix equality.

Run focused tests until GREEN. Commit implementation and artifact.

## Task 3: Bilingual reports and scientific boundary tests

**Files:**
- Create `tests/test_plane_wave_levi_civita_holonomy_reports.py`
- Create `theory/spacetime/plane-wave-levi-civita-holonomy.md`
- Create `audit/plane-wave-levi-civita-holonomy-report-en.md`
- Create `audit/plane-wave-levi-civita-holonomy-report-it.md`

Write report tests first. Require exact shared status/gate/scope tokens, equations, raw record, classifications, source limits, numeric artifact values, no independent-channel claim, no `ell0`, no detection, and `NOT_DECLARED` structural-dead-end state. Run and record RED.

Write aligned English/Italian reports and theory note. State:
- known pp-wave/parallel-null/Abelian-holonomy context only within verified source scope;
- explicit finite-loop result as project derivation;
- unipotent spectral collapse and scaling orbit as negative result;
- causal detector loop, tetrad/null normalization, readout, and `ell0` law as open problems.

Run focused report tests until GREEN. Commit.

## Task 4: Source verification and bounded authority updates

**Files:**
- Modify `references/library.bib`
- Modify `references/verification-log.md`
- Modify only relevant authoritative roadmap/open-problem or bilingual paper sections if exact bounded result adds necessary public state
- Modify claim/equation/assumption ledgers only if existing schema requires entries
- Add/update tests guarding any authority changes

Verify DOI metadata and inspect source text. Record exact supported topic and explicit unsupported project choices. Never attribute project loop formulas or detector implications to sources.

Prefer no paper change if theory/audit plus roadmap already suffice. Any bilingual paper edit must be semantically paired and tested.

Run focused bibliography/alignment tests. Commit.

## Task 5: Full verification

Run fresh:

- `python3 studies/spacetime/plane_wave_levi_civita_holonomy.py --check`
- `python3 studies/spacetime/plane_wave_screen_connection_holonomy.py --check`
- `python3 studies/spacetime/plane_wave_magnus_phase_holonomy.py --check`
- `python3 studies/spacetime/plane_wave_full_jacobi.py --check`
- `python3 -m unittest discover -s tests`
- `python3 tools/extract_docx.py --check`
- `python3 tools/inventory_source.py --check`
- `python3 studies/free-fall-identifiability/analysis.py --check`
- `git diff --check origin/main...HEAD`

If local TeX unavailable, record that and require GitHub LaTeX job green. Review deterministic JSON diff and scientific claims manually against spec.

## Task 6: Ship conservatively

Push branch and open PR with exact status, negative result, source scope, test count, and missing physical gates. Wait for tests and LaTeX CI. Auto-merge only if all green and no ambiguity or contract change. Then sync `main`, rerun core checks, update Hermes memory, and remove worktree/branch.

If source or derivation fails, preserve failure and stop. Do not declare structural dead end from this single exact family.