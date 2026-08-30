# Schwarzschild scattering clock-phase implementation plan

**Goal:** Add a deterministic counterexample-first audit of finite static-endpoint elapsed clock phase joined to the corrected full Schwarzschild scattering Jacobi map, testing whether the joint record retains geometric dilation blindness.

**Architecture:** A small standard-library study module reuses the audited scattering and frequency-transfer modules. It independently computes regularized Killing/proper elapsed time and clock phase, composes these with the full converted `4x4` map, runs fixed-dimensionless-frequency and external-frequency controls, and emits a deterministic JSON artifact. Unit tests define the scientific contract before implementation; report/source tests define bilingual authority and bounded citations.

**Constraints:** Direct execution only; no subagent. Preserve raw operator maps. No detector, covariance, `ell0`, UMCH evidence or detection claim. Frequent commits. Baseline command is `python3 -m unittest discover -s tests`.

---

## Task 1: Commit preregistration and define RED scientific contract

**Files:**
- Add: `doc/specs/2026-08-30-schwarzschild-scattering-clock-phase.md`
- Add: `doc/plans/2026-08-30-schwarzschild-scattering-clock-phase.md`
- Add: `tests/test_schwarzschild_scattering_clock_phase.py`

**Steps:**
1. Commit spec, then plan separately to preserve preregistration order.
2. Write tests importing `studies.spacetime.schwarzschild_scattering_clock_phase` and requiring:
   - analytic turning-limit regularity and mesh convergence;
   - positive finite `Delta t/M`, `Delta tau/M`, and `Phi_clock`;
   - clock linearity in `nu_s` and orientation parity;
   - zero-window convergence;
   - fixed-`nu_s` dilation invariance of clock and full converted map;
   - fixed-`omega_s` external-standard change;
   - rank shape/boundary `2`, rank with `log M` `2`, negligible `log M` column, `[0,0,1]` null direction and global injectivity not established;
   - exact status/gate/no-evidence labels;
   - deterministic artifact `--check` behavior.
3. Run `python3 -m unittest tests.test_schwarzschild_scattering_clock_phase`; record expected `ImportError`/missing-module RED.
4. Commit RED tests.

## Task 2: Implement GREEN study and artifact

**Files:**
- Add: `studies/spacetime/schwarzschild_scattering_clock_phase.py`
- Add: `studies/spacetime/schwarzschild-scattering-clock-phase-results.json`

**Steps:**
1. Implement standard-library trapezoidal regularized timing integral with analytic turning endpoint.
2. Implement static proper elapsed time and `Phi_clock=nu_s Delta tau/M`.
3. Reuse frequency-transfer converted full phase map; keep complete matrix in output.
4. Implement orientation, frequency-linearity, zero-window, geometric-dilation, external-standard, and finite-difference rank controls.
5. Implement deterministic renderer and `--check` using the repository artifact pattern.
6. Run focused test; correct only bounded numerical/contract defects until GREEN.
7. Run script to generate artifact, then `--check`.
8. Commit implementation and artifact.

## Task 3: Define RED/GREEN bilingual report and source contracts

**Files:**
- Add: `tests/test_schwarzschild_scattering_clock_phase_reports.py`
- Add: `tests/test_schwarzschild_scattering_clock_phase_sources.py`
- Add: `audit/schwarzschild-scattering-clock-phase-report-en.md`
- Add: `audit/schwarzschild-scattering-clock-phase-report-it.md`
- Add: `theory/spacetime/schwarzschild-scattering-clock-phase.md`

**Steps:**
1. Write report tests requiring aligned status, gate, equations, numerical values, limitations, source IDs, and no-positive-detection language in both languages and theory.
2. Write source tests restricting authority to `Schwarzschild2003Translation`, `Darwin1959GravityField`, `Sachs1961`, and requiring explicit non-support scope.
3. Run new report/source tests and record missing-file RED.
4. Write English and Italian audits with matching semantic content and exact artifact values.
5. Write theory note distinguishing coordinate time, static proper time, declared clock phase, source spectrum, photon phase, absorber action and detector readout.
6. Run report/source tests to GREEN.
7. Commit tests first, then reports/theory.

## Task 4: Integrate bounded negative result and history

**Files:**
- Modify: `docs/roadmap.md`
- Modify: `references/verification-log.md`
- Modify: `doc/specs/2026-08-30-schwarzschild-scattering-clock-phase.md`

**Steps:**
1. Add roadmap entry with negative status, exact open gate, no `ell0`, no detection, and route remaining open.
2. Add verification-log entries only for the existing canonical source scope; do not expand source claims.
3. Append post-run disposition to the spec with exact deterministic diagnostics and any bounded deviations from preregistration.
4. Run relevant public/source/report alignment tests.
5. Commit integration records.

## Task 5: Direct verification, PR, CI and Hermes

**Steps:**
1. Perform direct spec-to-diff review and record `DIRECT_REVIEW_NO_SUBAGENT` because subagents are prohibited.
2. Run focused and cross-control suites, including frequency transfer, null scattering, screen conformance and photon-sphere conformance.
3. Run `python3 -m unittest discover -s tests`.
4. Run all affected studies with `--check`, plus `python3 tools/extract_docx.py --check`, `python3 tools/inventory_source.py --check`, and `git diff --check`.
5. Push branch; open PR with exact negative interpretation and no-evidence labels.
6. Wait for GitHub `tests` and `latex`; auto-merge only if all checks are green and diff remains conservative/non-ambiguous.
7. Update local main, verify post-merge main CI, write timestamped Hermes Inbox note, and consolidate into shared memory only if no concurrent conflict.
8. Remove worktree and local/remote feature branch after confirmed merge.
9. Keep cron loop `16588751` active unless the full structural-dead-end contract unexpectedly passes; this task does not preregister such a declaration.
