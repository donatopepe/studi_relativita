# Paper II dimensional analysis

Conventions: `[x]=L`, `[s]=L`, `[τ]=T`, `[κ] = L⁻¹`, `[κ₀] = L⁻¹`, `[m]=M`, `[c]=LT⁻¹`, `[S] = M L² T⁻¹`.

## Candidate A

\[
S_A=S_0+\int ds\,\lambda(\kappa_0-\kappa).
\]

Since `[ds]=L` and `[κ₀-κ]=L⁻¹`, integrand factor multiplying `ds` requires `[λ]=[S]/L^0=M L² T⁻¹` if `s` is length and expression is read literally. Equivalently, if action is written as `-mc∫ds` and multiplier is factored as `mc\,\tilde λ`, dimensionless `\tilde λ` can be used. Therefore shorthand `[λ] = M L T⁻¹` applies only when multiplier is defined as a worldline Lagrangian coefficient before multiplication by dimensionless constraint `1-κ/κ₀`. The specification must state convention; dimensions alone do not establish dynamics.

For the normalized form

\[
S_A=S_0+\int ds\,\lambda_n(1-\kappa/\kappa_0),
\]

`[λ] = M L T⁻¹` for this normalized convention; this is convention used for matrix bookkeeping.

## Candidate B

\[
S_B=-mc\int ds+\epsilon mc\int ds\,f(\kappa/\kappa_0).
\]

`[ε] = 1`, ratio and `f` are dimensionless, `[mc]=M L T⁻¹`; multiplying by `ds` gives `[S] = M L² T⁻¹`. Candidate is dimensionally consistent. This does not establish stability, correct standard limit, or physicality.

## Candidate C

Weighted mean of `κ²` has `L⁻²`; square root gives `[κRMS] = L⁻¹`. Proper-time kernel may be dimensionless after normalized ratio, or carry reciprocal-time units in numerator/denominator consistently.

## Warning

Source conventions may use `ds=c dτ` or natural units. Every varied action must select one convention before deriving multiplier dimensions and boundary terms.
