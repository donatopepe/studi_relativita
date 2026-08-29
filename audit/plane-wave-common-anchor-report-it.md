# Audit del common anchor nell'onda piana esatta — Italiano

## Ledger

- Classificazione: `EXACT_SPACETIME_CROSS_CHANNEL_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT`.
- Stato: `EXACT_PLANE_WAVE_COMMON_ORIENTED_ANCHOR_RECOVERS_REVERSAL_SIGN_CONDITIONALLY_NOT_ELL0`.
- Gate aperto: `PHYSICAL_ORIENTED_ENDPOINT_ANCHOR_NOT_DERIVED`.
- UMCH remains `UNPROVEN`.
- Conclusione: `NO_POSITIVE_DETECTION_CLAIM`.

## Risultato counterexample-first

Per lo stesso `K(u)` dell'onda piana esatta, intervallo centrato, screen parallelo e boundary vertex dei gate precedenti, il reversal dà `W_rev=W` e `B_rev=B^T`. Definiamo `a(B)=(B21-B12)/2`. Un profilo asimmetrico generico dà `a(B)` non nullo.

- Con common anchor orientato fisicamente, `B -> Q B Q^T` con `Q in SO(2)`: `a(B)` è invariante e il reversal ne cambia il segno.
- Con common anchor non orientato `O(2)`: una riflessione cambia il segno, quindi la handedness resta ambigua.
- Con endpoint indipendenti `SO(2) x SO(2)`: `B` e `B^T` restano equivalenti nella stessa orbita.
- Con rescaling affine/del profilo: `a(B)/L` è preservato, quindi la scala assoluta del supporto resta non identificata.

Il common anchor orientato recupera dunque condizionalmente l'orientazione del profilo, ma non deriva la scala assoluta né introduce `ell0`.

## Scope

Coley–McNutt–Milson (2012), DOI `10.1088/0264-9381/29/23/235023`, supporta onde piane di Brinkmann esatte nel vuoto e deviazione geodetica guidata dalla curvatura. Common endpoint anchor, handedness, finestra finita, boundary vertex, calibrazione del detector, UMCH, `ell0` e detection sono scelte o claim progettuali, non stabiliti dalla fonte.

Il controllo esatto usa una trivializzazione matematica dello screen parallelo; non deriva identificazione fisica delle tetradi source/observer né calibrazione di parità. La route resta aperta e non è un vicolo cieco strutturale. Nessun dato o claim di detection.
