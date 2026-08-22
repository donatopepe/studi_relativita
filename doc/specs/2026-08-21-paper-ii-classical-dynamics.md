# UMCH Paper II — Comparative Classical Dynamics and No-Go Tests

## Status

Ratified design for the second UMCH milestone. This specification does not assert that any candidate dynamics is physically valid.

- Author: Pepe Donato, Independent Researcher
- Languages: Italian and English as equivalent versions
- Scientific status of `κ₀>0`: `UNPROVEN`
- Dependency: Paper I foundational audit

## Problem

Paper I established a conditional timelike definition

\[
\kappa=\frac{\sqrt{a^\mu a_\mu}}{c^2},
\]

and showed that ideal timelike geodesics have `κ=0`. The pointwise hypothesis `κ≥κ₀>0` therefore does not follow from Frenet–Serret kinematics and conflicts with geodesic free fall unless new dynamics or a different observable is supplied.

Paper II must test explicit candidate mechanisms rather than impose a constant-curvature trajectory and call it a solution. A valid candidate must define an action or constrained variational principle, degrees of freedom, equations, constraints, conserved quantities, standard limit, and observable consequences.

## Objective

Compare two pointwise timelike implementations and one explicitly separate reformulation:

1. hard inequality constraint;
2. divergent barrier potential in worldline curvature;
3. RMS/coarse-grained curvature bound, treated only as a different hypothesis.

Primary outcome is a decision matrix and no-go evidence. Rejection of every candidate is a valid milestone result. Paper III and later modules remain blocked unless at least one pointwise candidate survives load-bearing checks.

## Scope

### Candidate A — Hard inequality

Study a reparametrization-invariant constrained functional schematically of the form

\[
S_A[x,\lambda]=S_0[x]+\int ds\,\lambda(s)\,[\kappa_0-\kappa(s)],
\]

with inequality/complementarity conditions chosen explicitly, for example

\[
\lambda\ge0,\quad \kappa-\kappa_0\ge0,\quad
\lambda(\kappa-\kappa_0)=0.
\]

The sign convention must be derived consistently. Audit:

- reparametrization invariance;
- differentiability at `κ=0` and `κ=κ₀`;
- admissible initial data and feasibility;
- constraint classification and multiplier interpretation;
- whether free segments recover standard geodesics;
- discontinuities or nonunique evolution at active-set transitions;
- `κ₀→0` behavior;
- compatibility with equivalence principles.

No trajectory is accepted merely because it was preselected to satisfy the inequality.

### Candidate B — Barrier action

Study

\[
S_B[x]=S_0[x]+\int ds\,V(\kappa/\kappa_0),
\qquad V(z)\to+\infty\;\text{as}\;z\to1^+,
\]

using at least one dimensionally explicit representative. Alternative barriers may be compared, but parameter tuning after results is prohibited.

Audit:

- domain `κ>κ₀` and boundary behavior;
- higher-derivative Euler–Lagrange equations;
- canonical variables and constraints required by reparametrization invariance;
- additional initial data/degrees of freedom;
- boundedness of conserved energy or applicable constrained Hamiltonian criterion;
- linearized stability around simple backgrounds;
- causal/initial-value structure;
- decoupling and `κ₀→0` limit;
- whether the barrier itself predicts an observable rather than only excluding curves.

The Ostrogradsky label must not be applied mechanically: degeneracy and gauge constraints must be analyzed before any instability conclusion.

### Candidate C — Coarse-grained reformulation

Record, but do not merge into the pointwise hypothesis, possibilities such as

\[
\sqrt{\langle\kappa^2\rangle_{\Delta\tau}}\ge\kappa_0.
\]

This allows instantaneous `κ=0` and changes operational content. Paper II may define requirements and potential observables, but it must label this candidate `ALTERNATIVE_HYPOTHESIS`, not a rescue proved equivalent to original UMCH.

## Literature policy

Starter literature will include canonical metadata and verified scope for worldline-curvature actions and constrained Hamiltonian dynamics, including:

- Arreaga, Capovilla, and Guven, *Frenet–Serret dynamics*, DOI `10.1088/0264-9381/18/23/304`;
- Capovilla, Guven, and Rojas, *Hamiltonian Frenet–Serret dynamics*, DOI `10.1088/0264-9381/19/8/315`;
- Nesterenko et al., *Dynamics of relativistic particles with Lagrangians dependent on acceleration*, DOI `10.1063/1.531332`.

These sources establish analysis methods and examples, not a universal minimum curvature. Every new entry requires canonical DOI/arXiv/publisher verification and a statement of what it does not support.

## Analysis levels

Each conclusion must state its level:

- `KINEMATIC`: follows from definitions;
- `VARIATIONAL`: follows from varied action under declared boundary conditions;
- `CONSTRAINT`: follows from a constraint analysis;
- `LINEARIZED`: valid only around named background;
- `NUMERICAL`: reproduced by committed code and inputs;
- `CONJECTURAL`: plausible but not derived;
- `NO_GO_CONDITIONAL`: rejection under explicit assumptions.

No level may be silently promoted.

## Required checks per candidate

1. Covariance and reparametrization behavior.
2. Dimensions and declared constants.
3. Variational boundary terms.
4. Differential order and initial data.
5. Constraint/gauge structure.
6. Conservations and stress-energy interpretation where applicable.
7. Stability and boundedness under declared assumptions.
8. Causality or well-posedness evidence.
9. Equivalence-principle implications.
10. Standard limit `κ₀→0`.
11. At least one operational observable or a documented non-identifiability result.
12. Counterexamples and failure modes.

## Decision states

Each candidate receives one of:

- `VIABLE_WITHIN_TESTED_SCOPE`
- `VIABLE_WITH_CONDITIONS`
- `INCOMPLETE`
- `NON_IDENTIFIABLE`
- `CONTRADICTED_UNDER_ASSUMPTIONS`
- `REJECTED`

`VIABLE` means only survived listed tests; it is not empirical validation.

## Paper and repository artifacts

Create:

```text
papers/classical-dynamics/it/main.tex
papers/classical-dynamics/en/main.tex
papers/classical-dynamics/README.md

theory/classical-dynamics/candidate-a-hard-constraint.md
theory/classical-dynamics/candidate-b-barrier.md
theory/classical-dynamics/candidate-c-coarse-grained.md
theory/classical-dynamics/decision-matrix.csv

audit/classical-dynamics-report-it.md
audit/classical-dynamics-report-en.md
audit/dimensional-analysis/classical-dynamics.md

studies/classical-dynamics/
tests/test_classical_dynamics.py
```

Symbolic/numerical tooling is introduced only for derivations it can verify. Exact expressions and assumptions remain visible; output is deterministic.

## Falsification and stop rules

Candidate A or B fails its current formulation if any load-bearing issue cannot be removed without changing the hypothesis, including:

- no consistent covariant variational formulation;
- empty or observationally unacceptable admissible initial-data set;
- unavoidable ill-posedness or nonphysical modes after constraints are accounted for;
- failure of standard limit;
- conflict with established equivalence/Lorentz tests for all positive parameter space;
- no operational distinction from known dynamics.

If both pointwise candidates fail, Paper II reports conditional no-go and blocks Paper III under the pointwise UMCH program. Candidate C may continue only as separately renamed research hypothesis.

## Acceptance criteria

Milestone is ready for human scientific review when:

1. bibliography metadata/scope for classical-curvature dynamics is verified;
2. A and B have explicit functionals, domains, dimensions, and variation assumptions;
3. differential order and constraint questions are documented without unsupported claims;
4. at least one exact or symbolic consistency check is reproducible for each pointwise candidate;
5. standard-limit tests are explicit;
6. candidate C is visibly separate;
7. decision matrix cites evidence and analysis level;
8. Italian/English reports and Paper II labels/citations align;
9. tests, deterministic checks, and LaTeX CI pass;
10. negative outcomes remain public;
11. no downstream physics claim is promoted from failed premises.

## Out of scope

- Claiming a unique correct action.
- Quantizing candidates.
- ALD regularization.
- QED, graviton, decoherence, horizon, or cosmological conclusions.
- Positive detection or numerical bound without derived observable mapping.
- Treating an upper-acceleration model as evidence for a lower-curvature bound.
