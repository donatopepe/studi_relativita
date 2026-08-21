# First constraint study: free-fall identifiability

Question: can existing free-fall/equivalence tests be converted into a model-independent upper bound on `κ₀` using only audited UMCH foundations?

Result: `NO_BOUND_DERIVABLE`.

Reason: the audited kinematic definition `κ=a/c²` relates curvature to proper acceleration, but UMCH has no action or equations connecting experimental residuals (differential acceleration, coordinate trajectory, instrument noise, or equivalence-violation parameters) to a universal nonzero proper acceleration of each body. Substituting an experimental sensitivity for `a` would add an undeclared dynamical mapping.

This is a reproducible negative result, not evidence for or against a specific numerical value. `analysis.py` includes a synthetic direct-mapping case to test units and arithmetic. That synthetic branch is not applied to real data.

Run:

```bash
python3 studies/free-fall-identifiability/analysis.py
python3 studies/free-fall-identifiability/analysis.py --check
```
