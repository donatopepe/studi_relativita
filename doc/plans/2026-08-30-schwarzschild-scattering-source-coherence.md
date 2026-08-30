# Schwarzschild bounded source-coherence implementation plan

> Execute directly without subagents. Use TDD, small commits, deterministic artifacts, bilingual parity, and `DIRECT_REVIEW_NO_SUBAGENT`.

**Goal:** Test whether a bounded stationary Gaussian first-order source-coherence envelope adds an interior Schwarzschild/UMCH scale after explicit nuisance and dilation controls.

**Architecture:** Build a new study atop `schwarzschild_scattering_clock_phase.py`, preserving its full `4x4` frequency-converted Jacobi map. Produce raw coherence I/Q plus visibility, nuisance/limit/dilation/external-standard/rank controls, then mirror exact outputs and limitations in bilingual audits and theory docs.

**Tech:** Python standard library, `unittest`, deterministic JSON, Markdown audits.

## Task 1: Define RED scientific contract

**Files:**
- Create `tests/test_schwarzschild_scattering_source_coherence.py`

1. Import nonexistent study module and assert preregistered record, nuisance null directions, zero-window limit, fixed-`chi_c` dilation, fixed-`tau_c` external-standard difference, rank null direction, status/gate, and fresh artifact check.
2. Run `python3 -m unittest tests.test_schwarzschild_scattering_source_coherence`; expect import failure.
3. Commit RED test.

## Task 2: Implement deterministic study

**Files:**
- Create `studies/spacetime/schwarzschild_scattering_source_coherence.py`
- Create `studies/spacetime/schwarzschild-scattering-source-coherence-results.json`

1. Implement Gaussian coherence record with input validation.
2. Implement nuisance, quotient, zero-window, geometric-dilation, fixed-dimensional-coherence, and finite-difference rank controls.
3. Preserve full `P_frequency_converted`; report no joint-covariance independence.
4. Generate artifact and run focused test until GREEN.
5. Commit implementation and artifact.

## Task 3: Define RED report and source-scope contract

**Files:**
- Create `tests/test_schwarzschild_scattering_source_coherence_reports.py`
- Create `tests/test_schwarzschild_scattering_source_coherence_sources.py`

1. Require paired audit files, shared status/gate/equations/numbers, no forbidden evidence claims, theory/roadmap/spec alignment, and bounded citations.
2. Run tests; expect missing-report failure.
3. Commit RED report/source tests.

## Task 4: Write bilingual audit and theory record

**Files:**
- Create `audit/schwarzschild-scattering-source-coherence-report-en.md`
- Create `audit/schwarzschild-scattering-source-coherence-report-it.md`
- Create `theory/spacetime/schwarzschild-scattering-source-coherence.md`
- Modify `docs/roadmap.md`
- Modify `references/verification-log.md`
- Modify spec disposition if needed without changing preregistered controls.

1. Copy deterministic values from JSON, not hand-derived substitutes.
2. Keep English/Italian semantic parity and exact labels/equations/values.
3. State source scope does not establish source model, detector, covariance, `ell0`, UMCH, evidence or detection.
4. Run focused report/source and scientific tests until GREEN.
5. Commit docs.

## Task 5: Verify, review, ship

1. Run focused plus dependent Schwarzschild controls.
2. Run `python3 -m unittest discover -s tests`.
3. Run all touched deterministic `--check` commands, `tools/extract_docx.py --check`, `tools/inventory_source.py --check`, and `git diff --check`.
4. Directly review spec/diff and record `DIRECT_REVIEW_NO_SUBAGENT`.
5. Push branch, open PR, wait for `tests` and `latex` CI.
6. Auto-merge only if conservative, unambiguous, mergeable, and fully green; verify post-merge CI.
7. Update Hermes Inbox, clean worktree and branch. Keep loop `16588751` active unless structural-dead-end criteria pass.
