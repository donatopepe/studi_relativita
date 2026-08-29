# Schwarzschild static-radar holonomy implementation plan

> Execute directly without subagents per binding user instruction. Preserve RED failures, deterministic artifacts and small commits.

**Goal:** Replace an arbitrary Schwarzschild `t-r` coordinate rectangle with an idealized static-observer causal radar boundary and attack endpoint, quotient and absolute-scale identifiability.

**Architecture:** Reuse audited dependency-free Schwarzschild connection/matrix primitives. New module derives tortoise travel time, constructs two future radial-null segments plus observer-worldline closure, transports a test tetrad around the loop, and produces endpoint-collision, quotient, scaling and null controls in sorted JSON.

## Task 1 — Scientific RED

Create `tests/test_schwarzschild_radar_holonomy.py` requiring:

- exact travel-time formula and segment null residuals;
- metric/Lorentz compatibility, nonidentity, reversal and refinement;
- comparison with matched coordinate rectangle;
- fixed `Delta tau/M` endpoint ambiguity/control;
- anchored raw versus characteristic/conjugacy quotient classification;
- exact geometric scaling and flat/shrinking limits;
- complete raw record and nonconfirmatory states.

Run missing-module RED and commit.

## Task 2 — Transport GREEN

Create `studies/spacetime/schwarzschild_radar_holonomy.py` and deterministic result JSON.

- Import/reuse existing matrix, metric, tetrad and segment transport functions.
- Implement `r_star`, radar endpoint/time map and bisection endpoint inversion.
- Parameterize radial null legs with exact endpoint coordinate differences; closure is observer worldline.
- Implement causal, reversal, refinement, matched-rectangle, endpoint-family, quotient, scaling and null controls.
- Generate/check JSON; run focused GREEN; commit.

## Task 3 — Source scope RED/GREEN

Create focused source test. Add DOI-backed canonical source only if current bibliography lacks support for Schwarzschild radial null/tortoise/radar geometry. Record exact supported topic and exclusions: ideal mirror, finite loop, vector readout, `ell0`, UMCH and detection. Run generic bibliography tests; commit.

## Task 4 — Bilingual authority RED/GREEN

Create report contract before reports. Add theory note, English/Italian audits and conservative roadmap update. Align status, scope, gate, equations, values, quotient limits and no-claim labels. Run report/public-doc tests; commit.

## Task 5 — Verify and ship

Run focused and related artifacts, full unittest suite, extraction, inventory, legacy identifiability and diff checks. Push PR. Require duplicate GitHub tests/LaTeX green. Auto-merge only if bounded result remains conservative and unambiguous. Sync main, focused post-merge tests, Hermes Inbox update and cleanup. Keep loop active because structural-dead-end criteria do not pass.
