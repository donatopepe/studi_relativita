# Audit fondazionale — Italiano

## Ambito e metodo

Audit limitato ai claim geometrici portanti della prima formulazione italiana, traduzione inglese duplicata ed estensione successiva. Fonti: `FormigaRomero2006` per Frenet–Serret timelike e `Will2014` per quadro dei test relativistici. Controllo non convalida UMCH.

## Claim esaminati

| Claim | Esito | Sintesi |
|---|---|---|
| UMCH-CLM-0008 | `SUPPORTED_WITH_CONDITIONS` | Moto inerziale con quadri-accelerazione nulla è standard; `κ≥κ₀>0` resta postulato. |
| UMCH-CLM-0009 | `SUPPORTED_WITH_CONDITIONS` | Frenet–Serret timelike è formalismo standard sotto condizioni di regolarità. |
| UMCH-CLM-0010 | `CORRECTABLE` | Identità cinematica e disuguaglianza UMCH devono essere separate. |
| UMCH-CLM-0011 | `SUPPORTED_WITH_CONDITIONS` | Norma di impulso segue solo con `P=m₀U` e massa costante. |
| UMCH-CLM-0049 | `SUPPORTED_WITH_CONDITIONS` | Duplicato inglese del primo claim. |
| UMCH-CLM-0050 | `SUPPORTED_WITH_CONDITIONS` | Duplicato inglese del setup Frenet–Serret. |
| UMCH-CLM-0051 | `CORRECTABLE` | Duplicato inglese: separare identità da ipotesi. |
| UMCH-CLM-0052 | `SUPPORTED_WITH_CONDITIONS` | Duplicato inglese con assunzioni su massa e impulso. |
| UMCH-CLM-0092 | `SUPPORTED_WITH_CONDITIONS` | Setup metrico/tetrade ammesso; carica non produce limite minimo. |
| UMCH-CLM-0093 | `UNPROVEN` | `κ≥κ₀>0` non è derivato e confligge con geodesic motion ideale. |
| UMCH-CLM-0094 | `CORRECTABLE` | Preferire “curvatura propria della linea d'universo”; dichiarare dominio di `N`. |

## Derivazione indipendente minima

Da `u^μu_μ=-c²` e compatibilità metrica:

\[
\frac{D}{d\tau}(u^\mu u_\mu)=2u_\mu a^\mu=0.
\]

Per `a^μ≠0`, si può definire `κ=√(a^μa_μ)/c²` e `N^μ=a^μ/(c²κ)`. Quindi `a^μ=c²κN^μ`. Questa è identità definitoria, non dimostrazione di limite positivo. Su una geodesic timelike affinely parametrized, `a^μ=0`, dunque `κ=0`; `N^μ` non è determinato dalla formula. Ne segue tensione diretta con `κ₀>0`.

Per `P^μ=m₀u^μ` con `m₀` costante, `P^μP_μ=-m₀²c²`. Ortogonalità `u·a=0` preserva la norma della velocità, ma non dimostra da sola conservazione globale di energia-impulso né universalità del limite.

## Conclusione

Nucleo sopravvissuto: definizione condizionale della curvatura timelike e identità Frenet–Serret. Ipotesi universale resta `UNPROVEN`. Nessuna estensione a null, campi o vuoto segue da questi claim.
