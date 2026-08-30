# Schwarzschild null-scattering scale gate implementation plan

> Execute directly without subagents. Follow TDD RED-GREEN-REFACTOR. UMCH stays `UNPROVEN`; no detection claim.

**Goal:** Build deterministic finite-boundary nonradial Schwarzschild null-scattering and open-transport control that separates turning/boundary shape directions from geometric scale.

**Architecture:** New pure-Python study reuses matrix/connection helpers from `schwarzschild_mixed_levi_civita_holonomy.py`. It integrates a regularized symmetric scattering path, transports a 4D basis along ordered samples, converts to endpoint static tetrads, then audits orientation, endpoint actions, scale symmetry, local rank and bounded collisions. JSON is generated from one `build_result()` entry point and checked byte-for-byte.

**Runtime:** Python 3 standard library, `unittest`; no NumPy/pytest dependency.

## Task 1: RED scientific contracts

**Create:**
- `tests/test_schwarzschild_null_scattering_scale_gate.py`

Write failing tests for:
- invalid domains and `beta(rho)` turning relation;
- regularized incoming/outgoing path, monotonic future time, matched turning point;
- null/energy/angular-momentum residuals;
- raw `T_coord`, `T_tet`, metric compatibility and reverse inverse;
- boundary and orientation controls;
- endpoint action/reconstruction;
- scale invariance and `Delta t` scaling;
- Jacobian rank with null `log M` direction;
- bounded collision result and exact status/gate/nonclaims.

Run:

```bash
python3 -m unittest tests.test_schwarzschild_null_scattering_scale_gate
```

Expected: import failure because study module does not exist. Commit RED tests.

## Task 2: GREEN path and transport core

**Create:**
- `studies/spacetime/schwarzschild_null_scattering_scale_gate.py`

Implement minimally:
- matrix helpers or bounded reuse of existing helpers;
- `turning_beta`, domain validation and regularized quadrature/path samples;
- branch tangent and residual controls;
- RK4 transport over path samples;
- endpoint tetrad conversion and reverse integration;
- `raw_control`, `boundary_control`, `orientation_control`, `endpoint_control`, `scale_control`, `rank_control`, `collision_control`;
- `build_result`, deterministic JSON formatting and CLI `--check`.

Run focused scientific tests until green. Commit implementation and generated artifact separately if useful.

## Task 3: RED/GREEN artifact and authority contracts

**Create:**
- `tests/test_schwarzschild_null_scattering_scale_gate_sources.py`
- `tests/test_schwarzschild_null_scattering_scale_gate_reports.py`
- `studies/spacetime/schwarzschild-null-scattering-scale-gate-results.json`
- `theory/spacetime/schwarzschild-null-scattering-scale-gate.md`
- `audit/schwarzschild-null-scattering-scale-gate-report-en.md`
- `audit/schwarzschild-null-scattering-scale-gate-report-it.md`

**Modify:**
- `references/verification-log.md`
- `docs/roadmap.md`

First add failing tests requiring:
- byte-identical artifact regeneration;
- exact status/scope/gate/classification parity;
- EN/IT equations, values, limits and nonclaims;
- source keys and bounded source scope;
- roadmap status and no evidence language.

Then generate artifact and write aligned reports/theory. Do not claim source support for project integrations, endpoint protocol, detector, covariance, `ell0`, UMCH or detection. Commit docs.

## Task 4: Focused and full verification

Run:

```bash
python3 -m unittest \
  tests.test_schwarzschild_null_scattering_scale_gate \
  tests.test_schwarzschild_null_scattering_scale_gate_sources \
  tests.test_schwarzschild_null_scattering_scale_gate_reports
python3 studies/spacetime/schwarzschild_null_scattering_scale_gate.py --check
python3 -m unittest \
  tests.test_schwarzschild_photon_orbit_holonomy \
  tests.test_schwarzschild_photon_sphere_jacobi \
  tests.test_schwarzschild_photon_arc_cross_map \
  tests.test_schwarzschild_photon_arc_freefall_endpoints \
  tests.test_schwarzschild_null_scattering_scale_gate
python3 -m unittest
python3 tools/extract_docx.py --check
python3 tools/inventory_source.py --check
python3 studies/free-fall-identifiability/analysis.py --check
git diff --check
```

Record test counts, runtime, residuals and direct-review exception in both reports. If `pdflatex` absent, record exact failure and require green GitHub `latex` before merge.

## Task 5: Ship conservatively

- Directly review spec-to-code/test/report conformance; no subagent.
- Push exact SHA.
- Open PR stating toy/project/negative/open-problem classifications and no `ell0`/detection.
- Wait for all PR CI jobs; inspect `tests` and `latex`.
- Auto-merge only if change remains conservative, unambiguous and fully green.
- Sync `main`, remove worktree/branch, prune.
- Write timestamped Hermes Inbox note with PR, merge SHA, CI URLs, results, gates and next route.
- Keep loop `16588751` active: structural dead end cannot pass because generic Sachs/Jacobi scattering and detector-derived readout remain open.
