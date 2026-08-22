# Comparative classical-dynamics audit — English

## UMCH-P2-0001 — Scope

This audit compares three proposals without validating `κ₀>0`, which remains `UNPROVEN`. Curvature-action sources provide methods, not evidence for UMCH. Allowed levels are `KINEMATIC`, `SYMBOLIC`, algebraic `CONSTRAINT`, derivative-count `VARIATIONAL`, and `CONJECTURAL` for underived parts.

## UMCH-P2-0002 — Candidate A — `INCOMPLETE`

Hard constraint: `g=κ₀-κ≤0`, `λ≥0`, `λg=0`. A preregistered KKT check classifies interior, active, infeasible, and zero-limit cases. For every `κ₀>0`, `κ=0` is infeasible; at `κ₀=0` only algebraic admissibility returns. Complete covariant variation, boundary terms, active-set evolution, Dirac classification, stability, causality, and observable remain missing.

## UMCH-P2-0003 — Candidate B — `INCOMPLETE`

Fixed barrier: `f(z)=1/(z-1)`, `z=κ/κ₀>1`, coefficient `εmc`. Dimensions, divergence, monotonicity, convexity, and limit paths are checked. The `κ₀→0` limit is `NONUNIFORM`: term vanishes at fixed `κ>0`, remains finite in boundary layer, and geodesic stays outside domain. Derivative counting allows up to fourth order, but degeneracy/constraints prevent an automatic instability conclusion. Hamiltonian analysis, causality, and observable are missing.

## UMCH-P2-0004 — Candidate C — `NON_IDENTIFIABLE`

Proper-time-window RMS is an `ALTERNATIVE_HYPOTHESIS`. Counterexample `[0,2]` at `κ₀=1` satisfies RMS while violating pointwise bound: `NOT_EQUIVALENT`. Physical kernel, dynamics, causality, instrument response, and uncertainty model are missing. C does not rescue A or B and needs separate ratification.

## UMCH-P2-0005 — Conservation, stability, and degrees of freedom

No candidate yet has complete equations and constraint classification. Geometric symmetry suggests conservative structures to derive, but authorizes neither formulas nor counts. No candidate is declared stable, ghost-free, or causal. Status remains open.

## UMCH-P2-0006 — Equivalence and standard limit

A and B exclude ideal geodesic data for every fixed `κ₀>0`, directly tensioning pointwise free fall. A recovers feasibility only exactly at zero; B has a nonuniform limit. No convergence of solutions or observables is established.

## UMCH-P2-0007 — Decision and downstream gate

`NO_GO_NOT_ESTABLISHED`: A and B are incomplete, not rejected. Paper III is not blocked formally, but cannot start scientifically until at least one pointwise dynamics passes variation, constraints, stability, causality, standard-limit, and identifiability checks. Operational status: downstream deferred.

## UMCH-P2-0008 — Reproducible evidence

Three deterministic scripts preserve KKT algebra, barrier behavior/limits, and RMS non-equivalence. None simulates worldline dynamics or data. Negative results and limitations remain in audit.
