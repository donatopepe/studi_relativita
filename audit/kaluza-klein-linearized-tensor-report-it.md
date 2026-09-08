# Audit di conformità tensoriale 5D linearizzata

## Stato

```text
HIGHER_DIMENSIONAL_GRAVITY_DIRECTION=HUMAN_RATIFIED_RESEARCH_DIRECTION
MODEL=LINEARIZED_5D_COMPACT_KK_TOY_CONTROL
UMCH=UNPROVEN_SECONDARY_CANDIDATE
L_identified=false
ell0_identified=false
L_equals_ell0=NOT_DERIVED
extra_dimension_detected=false
structural_dead_end=NOT_DECLARED
NO_POSITIVE_DETECTION_CLAIM
MODEL_LEVEL_LINEARIZED_TENSOR_CONFORMANCE_NOT_EVIDENCE
```

Registro di chiusura diretta: `DIRECT_REVIEW_NO_SUBAGENT`. Non è revisione indipendente.

## Perimetro e convenzioni

Questo MVP inserisce il potenziale scalare esatto sul cerchio compatto nella metrica statica `d=5` per polvere, in gauge armonica e segnatura `(-,+,+,+,+)`. `Robinson2006Normalization` fissa inversione di traccia, potenziale newtoniano e convenzioni di segno. `AtondoRubio2008Linearized5D` sostiene solo il contesto di curvatura linearizzata; ansatz cilindrico e specializzazione `h_44=0` sono esclusi.

Il tensore grezzo completo `Riemann_5D`, le contrazioni, `R_0i0j`, i blocchi con indice compatto, il riferimento Hessiano scalare e le medie sul guscio radiale restano nell'artifact deterministico.

## Baseline deterministica

```text
L=1.0
r/L=2.0
y/L=0.7
shell_width/L=0.3
scale_factor=2.5
R_0101=-0.50548011
R_0202=0.20349714
R_0404=0.098485837
R_0104=-0.24481889
shell_R_0101=-0.51149219
point_conformance_residual=0.0
shell_conformance_residual=0.0
uniform_R_0404=0.0
uniform_R_1414=-0.125
source_ratio_residual=0.5
dimensionless_full_curvature_residual=0.0
```

I valori usano ampiezza efficace unitaria. Sono controlli adimensionali di modello, non misure o limiti fisici.

## Otto controlli

Tutti gli `8/8` controlli preregistrati passano:

1. inversione di traccia per polvere `d=5`;
2. residuo della gauge armonica;
3. contrazione indipendente di Riemann, conformità dell'operatore di Einstein e null Ricci nel vuoto regolare;
4. uguaglianza puntuale e sul guscio fra `R_0i0j` e Hessiano scalare precedente;
5. separazione localizzata fra indici compatti e modi non nulli;
6. il modo zero esattamente uniforme elimina le derivate in `y`, non il termine `R_i4j4` da derivate spaziali ordinarie;
7. un controesempio simbolico di stress diagonale cambia il completamento tensoriale a `h_00` fissato;
8. la dilatazione congiunta conserva la curvatura adimensionale e lascia `log L` nullo.

## Risultato limitato

```text
DECLARED_STATIC_5D_DUST_METRIC_RECOVERS_SCALAR_HESSIAN_AS_R0I0J_BUT_ADDS_COMPACT_INDEX_CURVATURE_WHILE_TENSOR_COMPLETION_REMAINS_SOURCE_DEPENDENT_AND_JOINT_DILATION_RETAINS_ABSOLUTE_SCALE_BLINDNESS_NOT_ELL0
PHYSICAL_5D_SOURCE_STRESS_LOCALIZATION_DYNAMICS_GAUGE_INVARIANT_OBSERVABLE_RADION_STABILIZATION_COUPLING_CALIBRATION_RECEIVER_NOISE_JOINT_COVARIANCE_DATA_AND_ELL0_LAW_NOT_DERIVED
```

La conformità corregge l'interpretazione scalare-tensore solo nelle convenzioni statiche dichiarate. Non rende i componenti grezzi osservabili gauge-invarianti indipendenti e non identifica `L`, non deriva `L=ell0`, non convalida UMCH e non rileva dimensioni extra. I registri scalari, di localizzazione finita e `F_0` restano preservati.
