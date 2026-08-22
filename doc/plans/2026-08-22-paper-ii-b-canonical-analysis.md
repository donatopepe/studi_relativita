# Paper II-B Canonical Analysis Plan

## Task 1 — Source provenance

Add arXiv IDs `hep-th/0105040`, `hep-th/0111014` to bibliography/log. Record exact general formulas used: first-curvature Euler–Lagrange equations, momenta, Hessian, primary constraint, Hamiltonian potential, and constraint statements. Add tests.

## Task 2 — Symbolic barrier specialization

Test-first implement exact rational/symbolic expressions without external CAS dependency for dimensionless `l(z)=-1+ε/(z-1)` and derivatives. Verify signs, `Lκκ≠0`, Legendre invertibility on domain, Hessian eigenvalue factors, and deterministic output.

## Task 3 — Variational equations and stationary sectors

Specialize sourced curvature equations. Analyze planar constant-curvature condition exactly. Preregister parameter domain `ε>0`, `z>1`; solve existence equation and classify roots without numerical overclaim. Derive local planar curvature linearization and clearly limit its scope.

## Task 4 — Canonical specialization

Specialize highest momentum, conserved momentum, primary constraint, Legendre potential, and any sourced secondary/first-class structure. Do not claim complete reduced phase-space stability unless derived. Add algebra checks and provenance links.

## Task 5 — Standard limit and decision

Evaluate fixed-curvature, boundary-layer, and stationary-root paths as `κ₀→0`. Decide candidate state and Paper III gate. Missing full stability or observable mapping must keep gate blocked/deferred.

## Task 6 — Bilingual audit and paper

Create aligned Italian/English addenda or Paper II-B manuscript with equations, citations, candidate state, limitations, and AI disclosure. Extend CI and tests.

## Task 7 — Verify and PR

Run full test suite, all deterministic checks, `git diff --check`, and CI. Update roadmap/overview/Hermes. Remove this plan, push, verify SHA, open PR. No auto-merge unless conclusions remain conservative and CI is green.
