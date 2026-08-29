# Audit dell'olonomia Schwarzschild su piani misti

Classificazione: `EXACT_SPACETIME_LEVI_CIVITA_HOLONOMY_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT`.

Stato: `EXACT_SCHWARZSCHILD_MIXED_PLANE_LEVI_CIVITA_HOLONOMY_NONABELIAN_PATH_ORDERED_BOUNDARY_DEPENDENT_AND_GEOMETRIC_SCALE_BLIND_NOT_ELL0`.

Ambito: `FOUR_DIMENSIONAL_SCHWARZSCHILD_LEVI_CIVITA_CONNECTION_ON_MATHEMATICAL_PIECEWISE_COORDINATE_LOOPS_NOT_DETECTOR_DERIVED`.

Gate: `PHYSICAL_CAUSAL_LOOP_FAMILY_PROPER_TIME_LENGTH_STANDARD_TETRAD_ANCHOR_DETECTOR_READOUT_AND_ELL0_LAW_NOT_DERIVED`.

## Derivazione e controesempi

Per la metrica esterna esatta, RK4 integra `dV/ds=-Gamma_mu dz^mu/ds V` su rettangoli equatoriali etichettati. Le matrici nella tetrade statica al punto base comune sono `H_tr` e `H_rphi`. Il residuo metrica-connessione è `6.680156279261934e-10`; il massimo residuo lorentziano è `1.7871742506134475e-13`. Le norme di non-identità sono `0.05483794566090526` e `0.09510550908422082`. L'inversione di orientazione soddisfa `H_reverse=H^-1` entro `6.93556937731235e-15`.

I prodotti tra piani misti dipendono genuinamente dall'ordine: norma di non-identità del commutatore `0.00368784364042176`, differenza dei prodotti ordinati `0.0036878373757369145`. non-Abelianity does not imply independent rank: entrambe le matrici derivano dalla stessa metrica, connessione e famiglia di bordi dichiarata.

Per un loop che si restringe, il residuo rispetto al flusso di curvatura locale per area coordinata è `8.119881880118987e-05`. Per il loop finito, il residuo rispetto a un singolo flusso ingenuo è `0.03959321213476851`. `H is not assumed equal to exp(integral R)`; il trasporto finito richiede `PATH_ORDERED_CONNECTION_HISTORY_REQUIRED`.

Rettangoli con uguale area coordinata ma bordi radiali traslati collidono nell'area e differiscono nell'olonomia raw di `0.03490123492447132`. È sensibilità a bordo/posizione, non landmark di `ell0`. I coefficienti caratteristici sotto reversal collidono entro `2.220446049250313e-16`; la coniugazione comune della tetrade preserva i coefficienti entro `8.881784197001252e-16`, benché le matrici raw ancorate possano differire.

## Scala e ambito

Sotto `(M,r,T)->(sM,sr,sT)`, con `s=1.47` e apertura angolare fissa, il massimo residuo delle olonomie è `2.59660112853674e-14`, mentre le scale proprie cambiano. Nessuna scala assoluta è identificata.

I loop sono mathematical piecewise-coordinate loops: not geodesic, not causal, not detector-derived. Le fonti stabiliscono solo la geometria Schwarzschild e il contesto curvatura--olonomia, non la scelta dei loop finiti, il readout numerico o UMCH.

UMCH: `UNPROVEN`. Risultato: `NO_POSITIVE_DETECTION_CLAIM`. `ell0_identified=false`; `structural_dead_end=NOT_DECLARED`.
