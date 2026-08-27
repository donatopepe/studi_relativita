# Registro di audit UMCH

Questa directory separa inventario automatico e revisione scientifica.

## Artefatti

- `unified-claims.csv`: ledger atomico autorevole dei claim `UMCH-U-*` del paper unificato, con classificazione epistemica, stato, evidenza, limite e falsificatore.
- `unified-equations.csv`: ledger autorevole delle equazioni `eq:u-*`, con dimensioni, dominio, stato, limiti e failure gates.
- `unified-assumptions.csv`: registro delle assunzioni attive, dipendenze, effetti del fallimento e gate di risoluzione; impedisce di trattare assunzioni aperte come risultati.
- `claims.csv`: una riga conservativa per ogni paragrafo sorgente storico. Una riga non equivale ancora a claim atomico validato.
- `equations/equations.csv`: candidati formula rilevati automaticamente.
- `inventory-summary.json`: conteggi riproducibili.

## Stati ammessi

`UNREVIEWED`, `SUPPORTED`, `SUPPORTED_WITH_CONDITIONS`, `CORRECTABLE`, `UNPROVEN`, `CONTRADICTED`, `OUT_OF_SCOPE`.

Tutti gli elementi iniziano `UNREVIEWED`. Classificazioni, settori e candidati formula sono euristiche utili a organizzare audit, non giudizi scientifici. Testo originale resta collegato tramite `UMCH-SRC-P####`; claim ed equazioni usano rispettivamente `UMCH-CLM-####` e `UMCH-EQ-####`.

Campi vuoti non devono essere riempiti con inferenze non verificate. Traduzione, LaTeX normalizzato, fonti, unità e decisioni richiedono revisione esplicita.
