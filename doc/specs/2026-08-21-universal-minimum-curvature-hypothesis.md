# Universal Minimum Curvature Hypothesis Research Program

## Status

Approved design specification for the initial repository and research program.

- Project title (Italian): **Ipotesi della Curvatura Minima Universale**
- Project title (English): **Universal Minimum Curvature Hypothesis**
- Working acronym: **UMCH**
- Author: **Pepe Donato**
- Affiliation: **Independent Researcher**
- Contact: **donato.pepe.it@gmail.com**
- Text license: **Creative Commons Attribution 4.0 International (CC BY 4.0)**
- Primary languages: **Italian and English, maintained as equivalent versions**

## Problem statement

The source document, `Dimostrazione e Prove Relatività Einstein.docx`, proposes that no physically relevant motion or configuration is exactly rectilinear and that a universal nonzero lower curvature bound may exist. It combines claims about relativistic kinematics, Abraham–Lorentz–Dirac radiation reaction, Kaluza–Klein theory, quantum electrodynamics, gravity, decoherence, horizons, and cosmology. It is currently a sequence of AI-assisted drafts rather than a coherent scientific paper: derivations are incomplete, references are sparse, numerical results are not reproducibly supported, and conjectures are sometimes phrased as established results.

The project will convert that source into a transparent, bilingual, falsifiable research program. The source document is historical input to be audited, not evidence and not an already validated manuscript.

## Scientific objective

The minimum successful scientific outcome is a mathematically coherent model with at least one quantitative, falsifiable prediction. A rigorous negative result is also a valid outcome: the audit may show that the hypothesis is inconsistent, observationally excluded, physically empty, or viable only in a restricted sector.

The project must never suppress negative evidence or change acceptance criteria to preserve the hypothesis.

## Central hypothesis

The core hypothesis is that there may exist a universal fundamental constant

\[
\kappa_0>0, \qquad [\kappa_0]=L^{-1}, \qquad \ell_0=\kappa_0^{-1},
\]

associated with a nonzero lower bound on physically relevant curvature.

In the theoretical core, \(\kappa_0\) is a free parameter constrained by experiment. Exploratory modules may investigate whether it can be derived from combinations of \(c,\hbar,G,\Lambda\), other established constants, or a cosmological scale. Such identifications remain conjectures unless supported by a physical derivation and independent predictions; dimensional analysis alone is insufficient.

The hypothesis is intended to apply, ultimately, to massive matter, massless particles, fields, and vacuum. These sectors do not share a single naive definition of curvature. The same universal scale \(\kappa_0\) may appear through distinct covariant observables. Validity in one sector does not establish validity in another.

For timelike curves, the initial candidate observable is

\[
a^\mu=u^\nu\nabla_\nu u^\mu,
\qquad
\kappa(\tau)=\frac{\sqrt{a^\mu a_\mu}}{c^2}.
\]

This vanishes on ideal geodesic motion. Consequently, imposing \(\kappa\geq\kappa_0>0\) may conflict with free fall, local equivalence, conservation laws, or Lorentz symmetry unless a consistent new dynamics is supplied. That tension is a primary research question, not an issue to conceal.

Null curves require affine-parameter and null-frame methods rather than proper acceleration. Fields require local observables or structures on configuration space. Vacuum requires geometric or quantum-state observables rather than an ordinary trajectory. Each extension must be formulated and tested separately.

## Scientific principles

All promoted results must satisfy the applicable requirements below:

1. Definitions are covariant and independent of arbitrary coordinates and parametrizations.
2. Equations are mathematically and dimensionally consistent.
3. Assumptions, definitions, derivations, numerical findings, conjectures, evidence, and open questions are visibly distinguished.
4. Compatibility or tension with special relativity, general relativity, quantum field theory, and established conservation laws is explicit.
5. Standard theories are recovered in a well-defined \(\kappa_0\to0\) limit wherever the model claims to deform those theories.
6. At least one new observable consequence is quantitative and falsifiable.
7. Existing measurements are used first to derive upper bounds; no positive detection is presumed.
8. Primary literature or authoritative reviews support claims about established physics.
9. AI output is never treated as a scientific source.
10. “Unification,” “proof,” and similar language is used only when justified by complete derivations and evidence.
11. Contradictions and negative results remain part of the public record.

## Scope

The maximum research scope is retained, but work proceeds through dependency-ordered modules:

1. differential-geometric foundations;
2. classical relativistic dynamics;
3. radiation reaction, including Abraham–Lorentz–Dirac and Landau–Lifshitz comparisons;
4. quantum fields and QED;
5. gravitation, semiclassical backreaction, and decoherence;
6. cosmology;
7. experimental bounds and falsification;
8. synthesis of only those results that survive audit and testing.

### Out of scope for the initial milestone

- Claiming a complete theory of everything or validated unification.
- Claiming experimental detection of \(\kappa_0\).
- Publishing AI-generated citations without source verification.
- Treating the source `.docx` as a proof.
- Completing all seven scientific papers before the foundational audit.
- Equating spacetime curvature, trajectory curvature, field-space curvature, and vacuum structure without separate definitions.

## Chosen architecture

The project uses a modular, claim-driven architecture rather than one monolithic paper or disconnected papers. A foundational paper defines the shared assumptions and geometry. Specialist papers consume only explicit, reviewed claims. A synthesis paper is deferred until dependencies have survived audit.

This architecture ensures that an error in a speculative QED or cosmology module does not automatically invalidate a narrower geometric result, while preventing downstream work from silently relying on rejected premises.

## Repository design

The intended structure is:

```text
README.md
README.en.md
LICENSE
CITATION.cff
CONTRIBUTING.md
CODE_OF_CONDUCT.md

archive/
  original/
    Dimostrazione e Prove Relatività Einstein.docx
  extracted/
    document-it.md
  provenance.md

audit/
  claims.csv
  equations/
  references/
  dimensional-analysis/
  contradiction-log.md
  audit-report-it.md
  audit-report-en.md

papers/
  foundation/
    it/
    en/
  classical-dynamics/
  radiation-reaction/
  quantum-fields/
  gravitation/
  cosmology/
  synthesis/

theory/
  definitions.md
  assumptions.md
  notation.md
  limiting-cases.md
  open-problems.md

tests/
  symbolic/
  numerical/
  dimensional/
  regression/

data/
  raw/
  processed/
  metadata/

references/
  library.bib
  verification-log.md

docs/
  overview-it.md
  overview-en.md
  glossary-it.md
  glossary-en.md
  roadmap.md
  falsification.md
```

The exact set of empty directories need not be committed. Directories are created when their first owned artifact is introduced. Generated PDFs, temporary files, and large datasets are excluded unless publication or reproducibility requires them.

`README.md` and `README.en.md` serve a scientifically literate general audience. Papers and appendices target physicists and mathematicians and retain full formalism. Neither README substitutes explanatory prose for a derivation.

## Source preservation and provenance

The original `.docx` remains byte-for-byte preserved under `archive/original/` and retains its Git history through a move. An extracted Markdown representation receives stable paragraph identifiers. Extraction must preserve headings, equations as recoverably as the format permits, hyperlinks, and source order. The extraction is not silently corrected; normalized or corrected versions are separate and traceable.

`archive/provenance.md` records:

- source filename and checksum;
- repository commit that introduced it;
- extraction method and software version;
- known limitations of equation extraction;
- the AI-assisted origin apparent in the document;
- the distinction between historical source, audit record, and accepted scientific text.

## Claim-driven audit

Every substantive source statement is atomized. Claims receive stable IDs such as `UMCH-CLM-0001`, equations `UMCH-EQ-0001`, and references `UMCH-REF-0001`.

The claim registry records at least:

- stable ID;
- original text and location;
- normalized Italian text;
- English translation;
- physical sector;
- claim type;
- prerequisites;
- linked equation and reference IDs;
- dimensional-check result;
- evidence level;
- review status;
- reviewer or verification method;
- decision and rationale.

Claim types include `DEFINITION`, `ASSUMPTION`, `DERIVATION`, `PREDICTION`, `NUMERICAL_RESULT`, `COMPARISON`, `CONJECTURE`, and `CONCLUSION`.

Review statuses are:

- `UNREVIEWED`
- `SUPPORTED`
- `SUPPORTED_WITH_CONDITIONS`
- `CORRECTABLE`
- `UNPROVEN`
- `CONTRADICTED`
- `OUT_OF_SCOPE`

No `UNREVIEWED` or `UNPROVEN` claim may appear as an established result in a paper. Previous formulations and status changes remain traceable.

## Audit workflow

The audit proceeds in this order:

1. inventory headings, paragraphs, equations, links, tables, and alleged numerical results;
2. perform loss-aware extraction and normalization;
3. classify atomic claims and dependencies;
4. check notation, signs, indices, parametrizations, boundary conditions, and omitted steps;
5. check dimensions in declared unit conventions;
6. test covariance, causality, conservation, stability, symmetries, equivalence principles, and limiting behavior;
7. locate and verify primary sources, DOI or arXiv identifiers, and exact support for each cited proposition;
8. reproduce symbolic derivations and numerical results with scripts or notebooks;
9. actively seek counterexamples and compare with precision experiments;
10. decide whether each claim is retained, corrected, demoted to conjecture, separated, or rejected.

Dependency order is foundational geometry, ALD/classical dynamics, Kaluza–Klein claims, QED, decoherence and gravity, horizons, and cosmology. Downstream work pauses when a load-bearing premise is contradicted.

## Falsification framework

The research program treats any of the following as a possible basis for rejecting all or part of UMCH:

1. no covariant, parametrization-independent observable can express the proposed bound;
2. unavoidable instability, acausality, ghosts, or other unphysical degrees of freedom;
3. conflict with observational tests of Lorentz invariance or equivalence principles;
4. failure to recover established theories as \(\kappa_0\to0\);
5. exclusion of every \(\kappa_0>0\) interval by existing observations;
6. mutually inconsistent predictions between sectoral formulations;
7. exact equivalence to a known theory with no new observable content.

Initial empirical work seeks upper bounds using, where applicable, atom interferometry, free-fall tests, clocks, orbital dynamics, accelerators, synchrotron radiation, photon propagation, and cosmological observations. Each candidate constraint must identify its observable, dataset or cited result, model assumptions, likelihood or inequality, units, systematic limitations, and reproducible calculation.

## Publication series

The intended bilingual series is:

1. **Paper I — Foundations:** covariant definitions, axiomatic structure, relations among curvature notions, symmetries, and the \(\kappa_0\to0\) limit.
2. **Paper II — Classical Dynamics:** candidate action, equations of motion, conservation, stability, and equivalence principles.
3. **Paper III — Radiation Reaction:** Abraham–Lorentz–Dirac behavior, runaway and preacceleration, and comparison with Landau–Lifshitz.
4. **Paper IV — Quantum Fields:** QFT/QED compatibility, Lorentz invariance, unitarity, and renormalization.
5. **Paper V — Gravitation:** backreaction, semiclassical limits, decoherence, and Diósi–Penrose comparison.
6. **Paper VI — Cosmology:** consequences for expansion, perturbations, and observables.
7. **Paper VII — Synthesis:** only claims that survive the preceding audit and tests.

Italian and English versions use aligned equation, figure, table, claim, and reference numbering. Every paper includes definitions, relation to literature, derivations, predictions, test protocols, limitations, and attempted falsifications.

## Reproducibility and quality controls

Automation will be introduced incrementally to check:

- LaTeX compilation and unresolved references;
- BibTeX integrity;
- Markdown structure and links;
- units and dimensional consistency;
- symbolic identities and limiting cases;
- numerical outputs with declared tolerances;
- claim-to-source links;
- bilingual structural alignment;
- software and data manifests;
- reproducible PDF builds.

A result is not called reproduced unless the recorded command runs from a documented environment and generates an output matching declared tolerances. Simulated or placeholder output is labeled as such.

## Initial milestone and acceptance criteria

The initial milestone is complete when the repository contains:

1. bilingual README files explaining purpose, hypothesis, status, cautions, structure, and contribution process;
2. CC BY 4.0 license and citation metadata for Pepe Donato;
3. the original document preserved with provenance and checksum;
4. a faithful, stable-ID extraction of the source;
5. a complete inventory of source claims and equations, even where review remains pending;
6. a verified starter bibliography with no fabricated entries;
7. a completed audit of the foundational geometric claims;
8. a bilingual Paper I draft that promotes only supported claims and labels conjectures;
9. at least one reproducible preliminary experimental upper-bound analysis for \(\kappa_0\), or a documented proof that no bound can yet be derived from the selected observable;
10. an explicit open-problems and contradiction log;
11. automated checks for the artifacts actually present;
12. documented AI-assistance policy and human scientific responsibility.

The milestone does not require favorable evidence. A finding that the central timelike formulation is inconsistent, redundant, or experimentally excluded satisfies the audit goal when rigorously demonstrated and documented.

## Documentation impact

- Feature/user-facing docs introduced: bilingual READMEs, bilingual overviews and glossaries, roadmap, falsification guide, contribution guide, provenance record.
- Materially amended existing docs: none; the repository currently has no documentation.
- Derived or memory docs invalidated: none.

## Attribution and AI disclosure

Scientific authorship is attributed to Pepe Donato. AI systems are tools for extraction, drafting, code assistance, translation, and hypothesis checking; they are not scientific sources or coauthors. The repository must disclose material AI assistance and require human verification of equations, citations, computations, translations, and conclusions. Responsibility for publication remains with the named author.
