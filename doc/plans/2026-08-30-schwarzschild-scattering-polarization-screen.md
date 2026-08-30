# Schwarzschild scattering polarization/screen implementation plan

> Execution policy: work directly in the isolated worktree; no subagents (`DIRECT_REVIEW_NO_SUBAGENT`). Follow TDD, deterministic artifacts, bilingual authority and conservative interpretation.

**Goal:** Add a bounded leading-geometric-optics polarization/screen transport control to the finite Schwarzschild scattering record and test whether it introduces an internal geometric scale direction.

**Architecture:** Build one append-only study module on the existing screen-conformance, clock-phase and frequency-converted Jacobi modules. Preserve complex Jones and coherency objects as paired-real JSON records; treat analyzer power as secondary. Generate one deterministic JSON artifact and bilingual audit/theory records, with source-scope tests.

**Tech stack:** Python standard library, existing project numerical modules, `unittest`, deterministic JSON/Markdown, BibTeX.

---

## Task 1: Freeze source and scientific contracts

**Files:**
- Modify: `references/library.bib`
- Modify: `references/verification-log.md`
- Create: `tests/test_schwarzschild_scattering_polarization_screen.py`

1. Add `Dolan2018GeometricalOptics` with verified title, author, journal, year, article number, DOI and arXiv identifier; bound its scope to leading geometrical optics and parallel-propagated polarization.
2. Write failing tests importing `studies.spacetime.schwarzschild_scattering_polarization_screen` and requiring:
   - declared status/result/gate strings;
   - Jones norm, coherency Hermiticity/rank-one consistency;
   - raw versus null-gauge-quotiented screen diagnostics;
   - common-basis-rotation analyzer invariance;
   - analyzer-only dependence with unchanged raw record;
   - orientation and zero-window controls;
   - fixed-dimensionless dilation invariance;
   - raw/quotient rank two with direct `log M` null direction;
   - full `4x4` frequency-converted map preservation.
3. Run `python3 -m unittest tests.test_schwarzschild_scattering_polarization_screen`; expect import failure (RED).
4. Commit: `test: define polarization screen contract`.

## Task 2: Implement the bounded transport/readout audit

**Files:**
- Create: `studies/spacetime/schwarzschild_scattering_polarization_screen.py`
- Create: `studies/spacetime/schwarzschild-scattering-polarization-screen-results.json`

1. Implement small complex/Jones helpers without external dependencies; serialize complex vectors/matrices as `[real,imag]` entries.
2. Reuse existing screen conformance and scattering phase/clock modules rather than duplicating geodesic integration.
3. Implement:
   - `polarization_record` with `U_screen=I_2` in the declared parallel screen, explicitly justified by the quotient transport diagnostic;
   - coherency construction and identity residuals;
   - common rotation and analyzer controls;
   - orientation, zero-window and geometric-scale controls;
   - raw and basis-quotiented finite-difference feature/rank controls over `(rho,R,log M)`;
   - `build_result`, deterministic `render`, CLI `--check`.
4. Keep `j_R`, `J_R`, `Phi_clock` and `P_frequency_converted` separate; no scalar replaces the full map.
5. Run the focused test until GREEN, generate artifact, then run `--check`.
6. Commit: `feat: audit Schwarzschild polarization screen transport`.

## Task 3: Add bilingual reports and source-scope gates test-first

**Files:**
- Create: `tests/test_schwarzschild_scattering_polarization_screen_reports.py`
- Create: `tests/test_schwarzschild_scattering_polarization_screen_sources.py`
- Create: `audit/schwarzschild-scattering-polarization-screen-report-en.md`
- Create: `audit/schwarzschild-scattering-polarization-screen-report-it.md`
- Create: `theory/spacetime/schwarzschild-scattering-polarization-screen.md`

1. Write RED report tests requiring exact semantic parity for result/gate/status, equations, baseline values, tolerances, limitations, source keys and raw/full-map preservation.
2. Write RED source tests allowing only `Schwarzschild2003Translation`, `Darwin1959GravityField`, `Sachs1961`, `Dolan2018GeometricalOptics`; require explicit denials for source/emitter/absorber/analyzer hardware/receiver/covariance/`ell0`/UMCH/detection support.
3. Observe missing-report failures.
4. Write aligned English/Italian audit records and bounded theory note. Distinguish screen-coordinate rotation from physical polarization rotation and label source Jones/analyzer as `TOY_CONTROL`.
5. Run focused report/source tests to GREEN.
6. Commit: `docs: record polarization screen negative result`.

## Task 4: Integrate public research state

**Files:**
- Modify: `docs/roadmap.md`
- Modify: `references/verification-log.md` if final source-scope wording needs alignment

1. Add the result and remaining physical gate without promoting UMCH, `ell0`, or a detection claim.
2. Preserve current source-coherence result/history and all earlier falsifications.
3. Run focused and cross-control suites:

```bash
python3 -m unittest \
  tests.test_schwarzschild_scattering_polarization_screen \
  tests.test_schwarzschild_scattering_polarization_screen_reports \
  tests.test_schwarzschild_scattering_polarization_screen_sources \
  tests.test_schwarzschild_scattering_source_coherence \
  tests.test_schwarzschild_scattering_source_coherence_reports \
  tests.test_schwarzschild_scattering_source_coherence_sources \
  tests.test_schwarzschild_scattering_screen_conformance \
  tests.test_schwarzschild_null_scattering_jacobi
```

4. Commit: `docs: integrate polarization screen gate`.

## Task 5: Verify, review and ship conservatively

1. Run fresh verification after the last edit:

```bash
python3 studies/spacetime/schwarzschild_scattering_polarization_screen.py --check
python3 studies/spacetime/schwarzschild_scattering_source_coherence.py --check
python3 studies/spacetime/schwarzschild_scattering_clock_phase.py --check
python3 studies/spacetime/schwarzschild_scattering_frequency_transfer.py --check
python3 studies/spacetime/schwarzschild_null_scattering_jacobi.py --check
python3 tools/extract_docx.py --check
python3 tools/inventory_source.py --check
python3 -m unittest discover -s tests
git diff --check
```

2. Perform direct diff/scientific/scope review and record `DIRECT_REVIEW_NO_SUBAGENT`; do not claim an independent reviewer.
3. Push branch and open PR. Merge only if mergeable and all `tests` and `latex` jobs are green; otherwise leave open.
4. Verify post-merge main CI, then write a timestamped Hermes Inbox note with commit, PR, test counts, result/gate and unchanged UMCH state.
5. Remove worktree and local/remote branch only after merge and post-merge CI success.
6. Re-evaluate structural-dead-end criteria. Expected disposition: `NOT_DECLARED`; keep durable loop `16588751` active.
