# Linearized compact Kaluza–Klein reformulation implementation plan

> Direct execution in current session. User explicitly forbids subagents, so mandatory plan recon and later review are performed directly and labeled `DIRECT_RECON_NO_SUBAGENT` / `DIRECT_REVIEW_NO_SUBAGENT`; neither is independent review.

**Goal:** Build a canonical-source-scoped, counterexample-first toy control for static linearized gravity on `R^(1,3) x S^1`, with finite-window tidal matrices for localized/uniform source–probe profiles, point/sphere/Gaussian sources, and explicit scale-identifiability failures; then record the higher-dimensional route as `REFORMULATION_CANDIDATE_UNRATIFIED` without merging it.

**Architecture:** Keep one deterministic standard-library Python study under `studies/spacetime/`. Separate circle-mode overlaps, radial Green-function/source form factors, pointwise Hessian, finite-window integration, convergence, limits, scaling, and rank controls. Preserve raw matrices and preparation labels in JSON. Add source, numerical, report, and reformulation-ledger tests before each production/documentation wave.

**Tooling:** Python 3 standard library, `unittest`, deterministic JSON/Markdown, existing DOCX extraction/inventory tools, Git/GitHub CI. No SciPy/SymPy dependency. Numeric rendering uses `.8g`; canonicalize to `0.0` only when `abs(value)<1e-7`.

**Worktree:** `/home/public/studi_relativita/.worktrees/kaluza-klein-linearized-reformulation`

**Branch:** `research/kaluza-klein-linearized-reformulation`

**Approved spec:** `doc/specs/2026-08-30-kaluza-klein-linearized-reformulation.md`

**Merge policy:** Open a PR labeled/statused `REFORMULATION_CANDIDATE_UNRATIFIED`; do not auto-merge. Stop durable autonomous loop if recreated. Request human scientific ratification with exact pushed SHA and CI URLs.

## Direct recon map

`DIRECT_RECON_NO_SUBAGENT` because user forbids subagents.

Patterns to follow:

- study module and deterministic artifact: `studies/spacetime/kottler_null_scattering_jacobi.py`, `studies/spacetime/kottler-null-scattering-jacobi-results.json`;
- numerical/source/report tests: `tests/test_kottler_null_scattering_jacobi.py`, `tests/test_kottler_null_scattering_sources.py`, `tests/test_kottler_null_scattering_reports.py`;
- bilingual theory/audit artifacts: `theory/spacetime/kottler-null-scattering-jacobi.md`, `audit/kottler-null-scattering-jacobi-report-{en,it}.md`;
- canonical metadata: `references/library.bib`, `references/verification-log.md`;
- public authority/history: `README.md`, `README.en.md`, `docs/roadmap.md`, `papers/umch/{en,it}/main.tex`;
- ledgers: `audit/unified-claims.csv`, `audit/unified-assumptions.csv`, `audit/unified-equations.csv`, plus relevant `audit/spacetime-claims.csv` and `audit/equations/equations.csv` only where a new stable row is required;
- CI entrypoint: `python3 -m unittest discover -s tests -v`, `python3 tools/extract_docx.py --check`, `python3 tools/inventory_source.py --check`, `python3 studies/free-fall-identifiability/analysis.py --check`, `git diff --check`;
- focused test form: `python3 -m unittest tests/test_<module>.py -v` is unreliable because `tests` is not guaranteed to be an import package; use `python3 -m unittest discover -s tests -p 'test_<module>.py' -v`;
- no Makefile, repo formatter, or linter is present; syntax-check touched Python with `python3 -m py_compile <files>` and use `git diff --check` repo-wide;
- GitHub `latex` job is authoritative when local TeX is unavailable.

## Task 1 — Freeze ratified spec and create reformulation ledger RED

**Files**

- Modify: `doc/specs/2026-08-30-kaluza-klein-linearized-reformulation.md`
- Create: `tests/test_kaluza_klein_reformulation_ledger.py`

1. Add tests requiring exact global statuses in spec and later authority files:

```text
HIGHER_DIMENSIONAL_GRAVITY_CORE=REFORMULATION_CANDIDATE_UNRATIFIED
MODEL=LINEARIZED_5D_COMPACT_KK_TOY_CONTROL
UMCH=UNPROVEN_SECONDARY_CANDIDATE
L_identified=false
ell0_identified=false
L_equals_ell0=NOT_DERIVED
extra_dimension_detected=false
structural_dead_end=NOT_DECLARED
NO_POSITIVE_DETECTION_CLAIM
MODEL_LEVEL_DIMENSIONLESS_KK_SHAPE_DERIVED_NOT_EVIDENCE
```

2. Require preservation tokens for existing primary object, `F_0`, pointwise negative results, `ELL0_STRUCTURALLY_NON_IDENTIFIABLE_UNDER_CURRENT_FAMILIES`, `PROJECTIVE_SCALE_NON_IDENTIFIABLE_IN_CURRENT_EXACT_CONTROLS`, RN/Kottler negative controls, and `HISTORICAL_WORLDLINE_FORMULATION` / `SUPERSEDED_AS_CORE`.
3. Require explicit change-ledger categories: frozen old core, retained results, changed authority, deferred routes, unresolved physical dependencies, and no structural-dead-end declaration.
4. Run focused test. Expected RED: public authority and ledger files do not yet contain candidate statuses.
5. Commit only ratified spec and RED test:

```bash
git add doc/specs/2026-08-30-kaluza-klein-linearized-reformulation.md tests/test_kaluza_klein_reformulation_ledger.py
git commit -m "docs: ratify linearized Kaluza-Klein reformulation spec"
```

## Task 2 — Verify canonical source contract before numerical authority

**Files**

- Create: `tests/test_kaluza_klein_linearized_sources.py`
- Modify: `references/library.bib`
- Modify: `references/verification-log.md`
- Possibly modify spec if exact sourced conventions require clarification: `doc/specs/2026-08-30-kaluza-klein-linearized-reformulation.md`

1. Research canonical publisher/arXiv/institutional sources for:
   - linearized gravity and mode decomposition on a compact circle;
   - exact static Green function/mode sum for one periodic spatial dimension;
   - long-distance four-dimensional and short-distance five-dimensional laws;
   - normalized source/probe Fourier overlaps;
   - relation between higher- and lower-dimensional Newton constants;
   - tensor/vector/scalar and gauge scope relevant to interpreting a Newtonian Hessian.
2. Inspect exact equations/pages/sections. Do not use search summaries as authority. Prefer primary papers or standard canonical reviews with stable DOI/arXiv metadata.
3. Write source tests requiring exact BibTeX keys, DOI/arXiv/publisher metadata, inspected scope, normalization convention, and exclusions. Required exclusions include:

```text
finite-window
source preparation
probe preparation
identifiability
receiver
covariance
ell0
UMCH
detection
```

4. Run focused source tests. Preserve RED before bibliography/log edits.
5. Add only verified entries and a narrow verification-log section for each source. If exact normalization, coupling, or tensor interpretation remains ambiguous, stop implementation, record gate in Hermes, and request human scientific review.
6. Re-run source tests GREEN and commit:

```bash
git add tests/test_kaluza_klein_linearized_sources.py references/library.bib references/verification-log.md doc/specs/2026-08-30-kaluza-klein-linearized-reformulation.md
git commit -m "docs: verify compact Kaluza-Klein source scope"
```

## Task 3 — Define circle-profile and Green-function contracts RED

**Files**

- Create: `tests/test_kaluza_klein_linearized_tidal.py`

1. Write tests importing missing `studies/spacetime/kaluza_klein_linearized_tidal.py`; preserve actual missing-module RED.
2. Test normalized Fourier overlaps for:
   - localized source/localized probe at declared relative circle angle;
   - localized/uniform;
   - uniform/localized;
   - uniform/uniform.
3. Require every case containing a uniform profile to return exact zero nonzero-mode weights within deterministic tolerance and classification:

```text
UNIFORM_S1_SOURCE_OR_PROBE_PROJECTS_NONZERO_KK_MODES_NOT_ABSENCE_OF_EXTRA_DIMENSION
```

4. Test point-source mode sum against sourced closed form or an independently computed high-precision reference at long-, transition-, and short-distance points.
5. Test four-dimensional long-distance and, only if source-verified, five-dimensional short-distance asymptotics.
6. Test increasing mode truncation and require explicit convergence record; no fixed truncation may silently become authority.
7. Commit RED tests:

```bash
git add tests/test_kaluza_klein_linearized_tidal.py
git commit -m "test: define compact-circle mode and Green-function contract"
```

## Task 4 — Implement circle modes and point-source tidal matrix GREEN

**Files**

- Create: `studies/spacetime/kaluza_klein_linearized_tidal.py`

1. Implement input validation for `L>0`, regular observation radius, normalized profiles, finite values, and declared relative `S^1` position.
2. Implement source/probe Fourier overlaps from integrals or exact profile coefficients; do not hard-code expected projection labels without computing weights.
3. Implement sourced static point potential shape as exact closed form when verified, plus explicit finite mode sum for convergence cross-check.
4. Derive radial first and second derivatives from exact expressions or deterministic stable formulas. Build full Hessian:

```python
T = T_perp * (I - rhat_rhat) + T_parallel * rhat_rhat
```

5. Return raw matrix, eigen-components, potential/gradient auxiliaries, coupling convention, mode data, convergence certificate, and preparation labels.
6. Keep amplitude/coupling separate from dimensionless shape; never identify either with `ell0`.
7. Run focused tests GREEN, syntax-check module, and commit:

```bash
python3 -m unittest discover -s tests -p 'test_kaluza_klein_linearized_tidal.py' -v
python3 -m py_compile studies/spacetime/kaluza_klein_linearized_tidal.py
git add studies/spacetime/kaluza_klein_linearized_tidal.py
git commit -m "feat: derive compact-circle point tidal response"
```

## Task 5 — Add finite sphere and Gaussian source RED/GREEN

**Files**

- Modify: `tests/test_kaluza_klein_linearized_tidal.py`
- Modify: `studies/spacetime/kaluza_klein_linearized_tidal.py`

1. Add RED tests for normalized fixed-total-mass point, uniform-sphere, and Gaussian profiles under both localized and uniform circle profiles.
2. Specify Gaussian width convention in tests and returned record.
3. Test exterior finite-source response against independent radial convolution or sourced Yukawa form factors, not a copied production helper.
4. Test `R_s->0` and `sigma->0` convergence to point source away from singular support.
5. Test suppression/shape changes across several `R_s/L` and `sigma/L` values.
6. Require source labels and classification:

```text
SOURCE_PROFILE_AND_WINDOW_SHAPE_ARE_PREPARATION_NUISANCES_NOT_INTRINSIC_GEOMETRY
```

7. Implement deterministic radial integration/form factors with endpoint-safe quadrature and an error/refinement certificate. Avoid adding SciPy/SymPy.
8. Run focused tests GREEN and commit:

```bash
git add tests/test_kaluza_klein_linearized_tidal.py studies/spacetime/kaluza_klein_linearized_tidal.py
git commit -m "feat: compare finite compact and Gaussian KK sources"
```

## Task 6 — Define and implement finite windows test-first

**Files**

- Modify: `tests/test_kaluza_klein_linearized_tidal.py`
- Modify: `studies/spacetime/kaluza_klein_linearized_tidal.py`

1. Add RED tests for radial-shell window:
   - normalized weight;
   - finite `Delta r`;
   - explicit boundary exclusion from singular support;
   - `Delta r->0` pointwise limit;
   - agreement between analytic/reference quadrature and production result.
2. Add RED tests for oriented 3D region:
   - declared box or ellipsoid shape, dimensions, center, orientation matrix, and normalized kernel;
   - matrix symmetry;
   - rotational covariance under paired rotation of geometry and basis;
   - anisotropic-window orientation response;
   - zero-window pointwise limit.
3. Add RED comparison between:
   - average of local Hessian;
   - Hessian of averaged potential where meaningfully defined;
   - source convolution followed by differentiation.
   Record equality only when numerically and analytically justified.
4. Implement deterministic tensor transport on the flat product baseline, explicit quadrature refinement, matrix accumulation, and complete window metadata.
5. Keep raw matrix primary. No norm-only success criterion.
6. Run focused tests GREEN and commit:

```bash
git add tests/test_kaluza_klein_linearized_tidal.py studies/spacetime/kaluza_klein_linearized_tidal.py
git commit -m "feat: add finite-window Kaluza-Klein tidal operators"
```

## Task 7 — Add counterexamples, scaling, and identifiability RED/GREEN

**Files**

- Modify: `tests/test_kaluza_klein_linearized_tidal.py`
- Modify: `studies/spacetime/kaluza_klein_linearized_tidal.py`

1. Add tests for exact/controlled uniform-profile null projection in all source–probe combinations.
2. Add long-distance 4D recovery and sourced short-distance control.
3. Derive dimensional scaling for potential, gradient, Hessian, window measure, coupling, and source normalization. Test joint dilation of every geometric length, including `L`, `r`, source size, and window dimensions.
4. Build preregistered dimensionless feature vector from raw matrix invariants/eigenvalue ratios at fixed dimensionless protocol coordinates.
5. Compute finite-difference sensitivity/rank for at least:
   - `log_L` and source-size ratio;
   - `log_L` and window-size ratio;
   - source and probe preparation directions where continuously parameterized profiles are explicitly introduced;
   - overall geometric dilation direction.
6. Report null directions rather than converting local numerical rank into global or physical identifiability.
7. Require classifications:

```text
JOINT_5D_GEOMETRIC_DILATION_NOT_INTERIOR_ABSOLUTE_SCALE
L_NOT_IDENTIFIABLE_WITHOUT_SOURCE_PROBE_AND_WINDOW_CALIBRATION
```

8. Require physical gate:

```text
NONLINEAR_5D_DYNAMICS_RADION_STABILIZATION_MATTER_LOCALIZATION_SOURCE_PROBE_PREPARATION_ABSOLUTE_COUPLING_CLOCK_RECEIVER_CALIBRATED_NOISE_JOINT_COVARIANCE_DATA_AND_ELL0_LAW_NOT_DERIVED
```

9. Implement controls, run focused tests GREEN, and commit:

```bash
git add tests/test_kaluza_klein_linearized_tidal.py studies/spacetime/kaluza_klein_linearized_tidal.py
git commit -m "feat: audit KK projection and scale identifiability"
```

## Task 8 — Generate deterministic artifact RED/GREEN

**Files**

- Modify: `tests/test_kaluza_klein_linearized_tidal.py`
- Create: `studies/spacetime/kaluza-klein-linearized-tidal-results.json`
- Modify: `studies/spacetime/kaluza_klein_linearized_tidal.py`

1. Add tests for complete structured record, stable sorting, `.8g` rendering, and near-zero canonicalization threshold.
2. Preregister modest baseline values only as numerical toy inputs, never physical estimates. Include all source classes, profile combinations, both window families, convergence data, limits, scale controls, rank/null directions, classifications, exclusions, and global statuses.
3. Add `build_result()`, stable conversion, rendering, `main()`, and `--check` behavior consistent with repository deterministic studies.
4. Generate artifact twice and compare byte-for-byte:

```bash
python3 studies/spacetime/kaluza_klein_linearized_tidal.py
cp studies/spacetime/kaluza-klein-linearized-tidal-results.json /tmp/kk-results.json
python3 studies/spacetime/kaluza_klein_linearized_tidal.py
cmp /tmp/kk-results.json studies/spacetime/kaluza-klein-linearized-tidal-results.json
```

5. Run focused tests GREEN and commit:

```bash
git add tests/test_kaluza_klein_linearized_tidal.py studies/spacetime/kaluza_klein_linearized_tidal.py studies/spacetime/kaluza-klein-linearized-tidal-results.json
git commit -m "feat: record deterministic linearized KK controls"
```

## Task 9 — Add bilingual scientific reports and theory test-first

**Files**

- Create: `tests/test_kaluza_klein_linearized_reports.py`
- Create: `audit/kaluza-klein-linearized-report-en.md`
- Create: `audit/kaluza-klein-linearized-report-it.md`
- Create: `theory/spacetime/kaluza-klein-linearized-tidal.md`

1. Write RED report tests requiring identical EN/IT:
   - equations and conventions;
   - source/probe/window labels;
   - artifact baseline values;
   - primary result and all negative classifications;
   - source scopes;
   - global statuses;
   - `DIRECT_REVIEW_NO_SUBAGENT` and no independent-review claim.
2. Require theory note to distinguish:
   - known sourced KK results;
   - project finite-window derivation;
   - toy controls;
   - negative identifiability results;
   - unresolved physical model;
   - hypothesis/reformulation candidate.
3. Write reports semantically aligned, without translating stable identifiers. Explain in both languages that matrix shape in a model is not evidence for an extra dimension.
4. Re-run report tests GREEN and commit:

```bash
git add tests/test_kaluza_klein_linearized_reports.py audit/kaluza-klein-linearized-report-en.md audit/kaluza-klein-linearized-report-it.md theory/spacetime/kaluza-klein-linearized-tidal.md
git commit -m "docs: report linearized Kaluza-Klein negative scale gate"
```

## Task 10 — Freeze old core and write complete candidate change ledger

**Files**

- Create: `audit/kaluza-klein-reformulation-change-ledger.md`
- Modify: `README.md`
- Modify: `README.en.md`
- Modify: `docs/roadmap.md`
- Modify: `papers/umch/it/main.tex`
- Modify: `papers/umch/en/main.tex`
- Modify: `audit/unified-claims.csv`
- Modify: `audit/unified-assumptions.csv`
- Modify: `audit/unified-equations.csv`
- Modify only if required by existing schema/tests: `audit/spacetime-claims.csv`, `audit/equations/equations.csv`, `audit/README.md`
- Modify: `tests/test_kaluza_klein_reformulation_ledger.py`

1. Expand RED ledger tests to require bilingual/public-authority alignment and exact preservation of old statuses.
2. Create complete ledger with:
   - old primary core and ratification provenance;
   - every retained negative result category;
   - authority files changed and exact semantic change;
   - why no old result is deleted;
   - new candidate assumptions/dependencies;
   - source and model scope;
   - unresolved gauge/coupling/source/probe/window/detector/covariance/data/`ell0` gates;
   - deferred Kerr and full nonlinear 5D routes;
   - rollback path if human rejects reformulation;
   - explicit `structural_dead_end=NOT_DECLARED` rationale.
3. Update README/roadmap/papers conservatively: old operator core becomes frozen prior primary formulation, while higher-dimensional gravity is explicitly only a ratified-for-engineering, unratified-as-scientific-core candidate.
4. Preserve `R_op`, raw channel records, scalar projections, `F_0`, all no-go and exact-control conclusions, and history.
5. Add stable ledger rows using existing CSV schemas. Do not invent data-result or evidence classifications. Use `HYPOTHESIS`, `TOY_CONTROL`, `PROJECT_DERIVATION`, `NEGATIVE_RESULT`, and `OPEN_PROBLEM` as appropriate.
6. Keep EN/IT equations, labels, claim IDs, values, citations, and limitations aligned.
7. Run ledger, paper, public-doc, unified-claim/equation/assumption tests. Commit:

```bash
python3 -m unittest discover -s tests -p 'test_kaluza_klein_reformulation_ledger.py' -v
python3 -m unittest discover -s tests -p 'test_*paper*.py' -v
python3 -m unittest discover -s tests -p 'test_*public*.py' -v
git add audit README.md README.en.md docs/roadmap.md papers/umch tests/test_kaluza_klein_reformulation_ledger.py
git commit -m "docs: record unratified higher-dimensional core candidate"
```

## Task 11 — Direct closure review and conformance fix wave

**Files**

- Modify only files required by verified findings.

1. Record `DIRECT_REVIEW_NO_SUBAGENT`; do not call it independent review.
2. Review every spec requirement against files/tests/artifact using a traceability table.
3. Attack strongest counterexamples again:
   - uniform projection;
   - long/short limits;
   - mode and quadrature convergence;
   - finite-source point limits;
   - zero-window limit;
   - orientation covariance;
   - source/window degeneracy;
   - joint dilation and rank loss;
   - imported coupling/size calibration;
   - `L != ell0` and no-evidence language.
4. Compare all numeric report values to JSON mechanically.
5. Run citation-key and verification-log scope checks.
6. Fix only demonstrated conformance defects test-first. Commit each bounded fix or one small review-fix commit.

## Task 12 — Full verification

Run fresh commands from worktree root and preserve exact outputs:

```bash
python3 -m py_compile studies/spacetime/kaluza_klein_linearized_tidal.py \
  tests/test_kaluza_klein_linearized_tidal.py \
  tests/test_kaluza_klein_linearized_sources.py \
  tests/test_kaluza_klein_linearized_reports.py \
  tests/test_kaluza_klein_reformulation_ledger.py
python3 -m unittest discover -s tests -p 'test_kaluza_klein*.py' -v
python3 -m unittest discover -s tests -v
python3 studies/spacetime/kaluza_klein_linearized_tidal.py --check
python3 tools/extract_docx.py --check
python3 tools/inventory_source.py --check
python3 studies/free-fall-identifiability/analysis.py --check
git diff --check
git status --short
```

If local LaTeX exists, compile both unified papers. Otherwise state that local LaTeX is unavailable and require green GitHub `latex` job before presenting the ratification PR as verified.

Do not claim passing from stale output. Any failure triggers systematic debugging and a new full-suite run.

## Task 13 — Commit, push, PR, CI, Hermes, and stop

**Files**

- Create concurrent note: `/home/public/HermesVault/Inbox/<timestamp>-umch-kaluza-klein-reformulation-candidate.md`

1. Confirm branch contains only intended commits and worktree is clean.
2. Push exact branch SHA:

```bash
git push -u origin research/kaluza-klein-linearized-reformulation
```

3. Open PR to `main` titled clearly as unratified reformulation candidate. PR body must include:
   - exact status `REFORMULATION_CANDIDATE_UNRATIFIED`;
   - complete change-ledger link;
   - source scope;
   - RED/GREEN and full-suite evidence;
   - direct-review limitation;
   - `L_identified=false`, `ell0_identified=false`, `extra_dimension_detected=false`;
   - no structural dead end and no detection;
   - explicit `DO NOT MERGE WITHOUT HUMAN SCIENTIFIC RATIFICATION`.
4. Wait for both `tests` and `latex` GitHub jobs to pass on exact pushed SHA. Do not merge even when green.
5. Write Hermes Inbox note with worktree, branch, SHA, PR URL, CI URLs, tests, classifications, open gates, and ratification request. No secrets.
6. Cancel any active durable autonomous loop because a reformulation PR now awaits human ratification.
7. Leave branch/worktree clean and intact for review. Report exact gate to user.

## Completion boundary

Plan is complete only when PR is open and green, Hermes is updated, any autonomous loop is stopped, and human ratification is explicitly requested. Scientific implementation is not merged and neither UMCH nor the higher-dimensional candidate is reported as evidence-supported.
