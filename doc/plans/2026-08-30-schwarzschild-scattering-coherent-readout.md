# Schwarzschild coherent endpoint-readout implementation plan

> Execute directly without subagents. Follow TDD: observe each new contract fail before production work.

**Goal:** Add deterministic counterexample-first audit showing that ideal coherent endpoint I/Q readout is controlled by source phase, LO phase and gain nuisances and does not unlock Schwarzschild geometric scale or `ell0`.

**Architecture:** Reuse audited clock-phase and corrected scattering-Jacobi modules. New study constructs raw scalar-carrier I/Q, nuisance controls, quotient representative, zero-window/dilation/external-standard controls and local-rank diagnostics while retaining `R_readout=(y_IQ,Phi_clock,P_frequency_converted)`. New JSON artifact and bilingual reports expose exact status, gate, scope and source limitations.

**Tech stack:** Python standard library, `unittest`, deterministic JSON/Markdown, existing repository check scripts and GitHub Actions.

---

### Task 1: RED scientific readout contract

**Files:**
- Create: `tests/test_schwarzschild_scattering_coherent_readout.py`

1. Write tests requiring module API, raw I/Q norm, exact source/LO common-phase invariance, source/gain compensation, quotient collapse, nuisance Jacobian null directions, zero-window behavior, fixed-`nu_s` dilation, fixed-`omega_s` external-standard classification, retained full map, rank status and global authority labels.
2. Run:
   ```bash
   python3 -m unittest tests.test_schwarzschild_scattering_coherent_readout
   ```
   Expected: import failure because module does not exist.
3. Commit RED test.

### Task 2: GREEN study and deterministic artifact

**Files:**
- Create: `studies/spacetime/schwarzschild_scattering_coherent_readout.py`
- Create: `studies/spacetime/schwarzschild-scattering-coherent-readout-results.json`

1. Implement minimal functions for I/Q, nuisance actions, canonical quotient, nuisance Jacobian/null controls, zero-window, geometric dilation, external frequency, local rank, `build_result`, `render`, `main`.
2. Reuse clock-phase and frequency-transfer conversion; do not duplicate or scalarize Jacobi map.
3. Run focused test to GREEN.
4. Generate artifact and verify `--check`.
5. Commit implementation and artifact.

### Task 3: RED/GREEN bilingual reports and source scope

**Files:**
- Create: `tests/test_schwarzschild_scattering_coherent_readout_reports.py`
- Create: `tests/test_schwarzschild_scattering_coherent_readout_sources.py`
- Create: `audit/schwarzschild-scattering-coherent-readout-report-en.md`
- Create: `audit/schwarzschild-scattering-coherent-readout-report-it.md`
- Create: `theory/spacetime/schwarzschild-scattering-coherent-readout.md`

1. Write report/source tests first; require EN/IT status, gate, equations, diagnostics, authority, classification and exact source limitations.
2. Observe missing-report RED failure.
3. Write semantically aligned reports and theory note.
4. Use only existing verified canonical source keys whose scope is needed; do not claim they derive receiver hardware, coherence dynamics, covariance, `ell0` or UMCH.
5. Run report/source tests to GREEN and commit.

### Task 4: Integration records and history

**Files:**
- Modify: `docs/roadmap.md`
- Modify: `references/verification-log.md`
- Modify: `doc/specs/2026-08-30-schwarzschild-scattering-coherent-readout.md`

1. Record bounded negative result, open physical gates, source scope and post-run disposition.
2. Preserve prior clock/frequency results and all global authority labels.
3. Run related clock/frequency/Jacobi/conformance suites and commit.

### Task 5: Direct review, full verification, PR/CI/Hermes

1. Directly review spec-to-diff conformance; record `DIRECT_REVIEW_NO_SUBAGENT` because subagents are forbidden.
2. Run focused/cross-control tests, then:
   ```bash
   python3 -m unittest discover -s tests
   python3 studies/spacetime/schwarzschild_scattering_coherent_readout.py --check
   python3 tools/extract_docx.py --check
   python3 tools/inventory_source.py --check
   git diff --check
   git status --short
   ```
3. Push branch; open PR. Auto-merge only if change remains conservative/unambiguous and PR `tests` and `latex` are green.
4. Confirm post-merge main CI green before cleanup.
5. Write timestamped Hermes Inbox note; remove worktree and local/remote branch after merge.
6. Keep loop `16588751` active because structural-dead-end criteria are not met.
