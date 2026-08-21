# Registro di audit UMCH

Questa directory separa inventario automatico e revisione scientifica.

## Artefatti

- `claims.csv`: una riga conservativa per ogni paragrafo sorgente. Una riga non equivale ancora a claim atomico validato.
- `equations/equations.csv`: candidati formula rilevati automaticamente.
- `inventory-summary.json`: conteggi riproducibili.

## Stati ammessi

`UNREVIEWED`, `SUPPORTED`, `SUPPORTED_WITH_CONDITIONS`, `CORRECTABLE`, `UNPROVEN`, `CONTRADICTED`, `OUT_OF_SCOPE`.

Tutti gli elementi iniziano `UNREVIEWED`. Classificazioni, settori e candidati formula sono euristiche utili a organizzare audit, non giudizi scientifici. Testo originale resta collegato tramite `UMCH-SRC-P####`; claim ed equazioni usano rispettivamente `UMCH-CLM-####` e `UMCH-EQ-####`.

Campi vuoti non devono essere riempiti con inferenze non verificate. Traduzione, LaTeX normalizzato, fonti, unità e decisioni richiedono revisione esplicita.
