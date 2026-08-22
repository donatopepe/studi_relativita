# Audit comparativo della dinamica classica — Italiano

## UMCH-P2-0001 — Ambito

Questo audit confronta tre proposte, senza convalidare `κ₀>0`, che resta `UNPROVEN`. Fonti su azioni di curvatura forniscono metodi, non prova di UMCH. Livelli ammessi: `KINEMATIC`, `SYMBOLIC`, `CONSTRAINT` algebraico, derivative-count `VARIATIONAL`, e `CONJECTURAL` per parti non derivate.

## UMCH-P2-0002 — Candidate A — `INCOMPLETE`

Vincolo duro: `g=κ₀-κ≤0`, `λ≥0`, `λg=0`. Check KKT preregistrato classifica interior, active, infeasible e limite zero. Per ogni `κ₀>0`, `κ=0` è infeasible; a `κ₀=0` torna solo ammissibilità algebrica. Mancano variazione covariante completa, boundary terms, active-set evolution, classificazione Dirac, stabilità, causalità e osservabile.

## UMCH-P2-0003 — Candidate B — `INCOMPLETE`

Barriera fissata: `f(z)=1/(z-1)`, `z=κ/κ₀>1`, coefficiente `εmc`. Dimensioni, divergenza, monotonia, convessità e cammini limite sono verificati. Limite `κ₀→0` è `NONUNIFORM`: termine svanisce per `κ>0` fisso, resta finito nel boundary layer, geodetica resta fuori dominio. Derivative counting permette fino al quarto ordine, ma degeneracy/constraints impediscono conclusione automatica di instabilità. Mancano Hamiltonian analysis, causalità e osservabile.

## UMCH-P2-0004 — Candidate C — `NON_IDENTIFIABLE`

RMS su proper-time window è `ALTERNATIVE_HYPOTHESIS`. Controesempio `[0,2]` con `κ₀=1` soddisfa RMS ma viola pointwise bound: `NOT_EQUIVALENT`. Mancano kernel fisico, dinamica, causalità, risposta strumentale e modello d'incertezza. C non salva A o B e richiede ratifica separata.

## UMCH-P2-0005 — Conservazione, stabilità e gradi di libertà

Nessun candidato dispone ancora di equazioni complete e constraint classification. Simmetria geometrica suggerisce strutture conservative da derivare, ma non autorizza formule o conteggi. Nessun candidato è dichiarato stable, ghost-free o causal. Stato resta aperto.

## UMCH-P2-0006 — Equivalenza e limite standard

A e B escludono ideal geodesic data per ogni fixed `κ₀>0`, tensione diretta con free fall pointwise. A recupera feasibility solo esattamente a zero; B ha limite non uniforme. Nessuna convergenza di soluzioni/osservabili è dimostrata.

## UMCH-P2-0007 — Decisione e gate downstream

`NO_GO_NOT_ESTABLISHED`: A e B sono incompleti, non respinti. Paper III is not blocked formalmente, ma non può iniziare scientificamente finché almeno una dinamica pointwise non supera variazione, constraints, stabilità, causalità, standard limit e identificabilità. Stato operativo: downstream deferred.

## UMCH-P2-0008 — Evidenze riproducibili

Tre script deterministici conservano KKT algebra, barrier behavior/limits e RMS non-equivalence. Nessuno simula worldline dynamics o dati. Risultati negativi e limiti sono parte dell'audit.
