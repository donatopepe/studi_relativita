# Foundational audit — English

## Scope and method

Audit limited to load-bearing geometric claims in the first Italian formulation, its English duplicate, and the later extension. Sources: `FormigaRomero2006` for timelike Frenet–Serret geometry and `Will2014` for the relativistic-test framework. This review does not validate UMCH.

## Reviewed claims

| Claim | Outcome | Summary |
|---|---|---|
| UMCH-CLM-0008 | `SUPPORTED_WITH_CONDITIONS` | Inertial motion with zero four-acceleration is standard; `κ≥κ₀>0` remains a postulate. |
| UMCH-CLM-0009 | `SUPPORTED_WITH_CONDITIONS` | Timelike Frenet–Serret is standard under regularity conditions. |
| UMCH-CLM-0010 | `CORRECTABLE` | Kinematic identity and UMCH inequality must be separated. |
| UMCH-CLM-0011 | `SUPPORTED_WITH_CONDITIONS` | Momentum norm follows only for `P=m₀U` and constant mass. |
| UMCH-CLM-0049 | `SUPPORTED_WITH_CONDITIONS` | English duplicate of the first claim. |
| UMCH-CLM-0050 | `SUPPORTED_WITH_CONDITIONS` | English duplicate of the Frenet–Serret setup. |
| UMCH-CLM-0051 | `CORRECTABLE` | English duplicate: separate identity from hypothesis. |
| UMCH-CLM-0052 | `SUPPORTED_WITH_CONDITIONS` | English duplicate with mass/momentum assumptions. |
| UMCH-CLM-0092 | `SUPPORTED_WITH_CONDITIONS` | Metric/tetrad setup is admissible; charge supplies no minimum bound. |
| UMCH-CLM-0093 | `UNPROVEN` | `κ≥κ₀>0` is not derived and conflicts with ideal geodesic motion. |
| UMCH-CLM-0094 | `CORRECTABLE` | Prefer “proper worldline curvature”; declare the domain of `N`. |

## Minimal independent derivation

From `u^μu_μ=-c²` and metric compatibility,

\[
\frac{D}{d\tau}(u^\mu u_\mu)=2u_\mu a^\mu=0.
\]

For `a^μ≠0`, define `κ=√(a^μa_μ)/c²` and `N^μ=a^μ/(c²κ)`. Thus `a^μ=c²κN^μ`. This is a definitional identity, not proof of a positive bound. On an affinely parametrized timelike geodesic, `a^μ=0`, hence `κ=0`; the formula does not determine `N^μ`. This creates direct tension with `κ₀>0`.

For `P^μ=m₀u^μ` and constant `m₀`, `P^μP_μ=-m₀²c²`. Orthogonality `u·a=0` preserves four-velocity norm, but alone proves neither global energy-momentum conservation nor universality of the bound.

## Conclusion

Surviving core: conditional timelike-curvature definition and Frenet–Serret identity. Universal hypothesis remains `UNPROVEN`. No null, field, or vacuum extension follows from these claims.
