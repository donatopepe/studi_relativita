# Schwarzschild scattering frequency-transfer implementation plan

> Execution is direct in isolated worktree. No subagents. Follow TDD and preserve negative-result history.

**Goal:** test whether static endpoint frequency transfer converts the generic Schwarzschild scattering affine anchor into physical interior scale information, or remains an external clock calibration with exact geometric scale blindness.

**Architecture:** add a small study module importing the corrected PR #95 scattering/Jacobi implementation. Compute static-tetrad redshift, tangent normalization, rescaled optical profile/full phase map, explicit phase-rate similarity, geometric scaling controls and bounded Jacobian. Serialize one deterministic JSON artifact. Add focused scientific, report-parity and source-scope tests; write bilingual audits/theory and update roadmap/verification log.

**No new dependency:** Python standard library and existing project matrix helpers only.

## Task 1 — RED scientific contract

Create `tests/test_schwarzschild_scattering_frequency_transfer.py` before production module. Require:

- endpoint Killing-energy consistency and rejection of inconsistent independent frequencies;
- correct static redshift transfer;
- tangent/profile quadratic scaling;
- exact full-map phase-rate similarity;
- fixed-`nu_s` Schwarzschild scale orbit and scale-null Jacobian;
- explicit external-standard classification when dimensional `omega_s` is held fixed;
- bounded status/gate/global UMCH fields and deterministic artifact check.

Run focused test and witness expected missing-module failure. Commit RED.

## Task 2 — GREEN study and artifact

Create:

- `studies/spacetime/schwarzschild_scattering_frequency_transfer.py`
- `studies/spacetime/schwarzschild-scattering-frequency-transfer-results.json`

Reuse corrected profile and full phase map. Keep screen order and affine conversion explicit. Implement CLI `--check`. Run focused scientific test, artifact check and relevant PR #95/#96 cross-controls. Commit GREEN.

## Task 3 — RED/GREEN reports and source scope

Create report/source tests first, witness missing files or required text, then add:

- `theory/spacetime/schwarzschild-scattering-frequency-transfer.md`
- `audit/schwarzschild-scattering-frequency-transfer-report-en.md`
- `audit/schwarzschild-scattering-frequency-transfer-report-it.md`

Require semantic parity for equations, status, gate, values, classifications and limitations. Reuse only existing canonical Schwarzschild/Darwin/Sachs citations unless a directly needed canonical static-redshift source is verified and narrowly scoped. No source may support detector, covariance, `ell0`, UMCH or detection absent explicit evidence.

## Task 4 — Integration records

Update:

- `docs/roadmap.md`
- `references/verification-log.md`
- preregistration post-run disposition

Preserve PR #94 falsified profile history and PR #96 affine reconciliation. Commit docs.

## Task 5 — Direct review and verification

No closure-review subagent by user instruction. Record `DIRECT_REVIEW_NO_SUBAGENT`. Perform direct spec/diff review, focused suites, full `python3 -m unittest discover -s tests`, all deterministic `--check` commands relevant to changed artifacts, extraction/inventory checks and `git diff --check`. Local LaTeX if available; otherwise require GitHub `latex` green.

Push branch and open PR. Auto-merge only if result is conservative, unambiguous and all PR checks pass. Confirm main CI after merge, clean worktree/branches, and write timestamped Hermes Inbox note. Keep durable loop `16588751` active unless structural-dead-end/reformulation gate is actually met.
