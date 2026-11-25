# Planning per week

Ieder teamlid werkt 4 uur per week aan het project. Het project is af op vrijdag 29-01-2027.
We tellen in lesweken. De Done-lijst op Trello heet naar de lesweek: **Done week 11**, **Done week 12**, enzovoort.
Tonna is de contactpersoon voor Sam en doet coördinatie en rapportage; Malak doet literatuur en methode (de rollen zijn in lesweek 12 omgewisseld).
De fasen komen uit het plan van aanpak, hoofdstuk 5. Daar staat de oplevering in lesweek 18; lesweek 19 is de laatste week.

## Lesweken

| Lesweek | Data | Fase |
|---|---|---|
| 11 | 16-11 t/m 20-11-2026 | bord en werkwijze; start feature engineering |
| 12 | 23-11 t/m 27-11-2026 | XGBoost en eerste nieuwe features |
| 13 | 30-11 t/m 04-12-2026 | features uit de audio; grid search |
| 14 | 07-12 t/m 11-12-2026 | kortere vensters; modellen op de nieuwe features |
| 15 | 14-12 t/m 18-12-2026 | modelkeuze |
| – | 21-12-2026 t/m 01-01-2027 | kerstvakantie, geen kaarten |
| 16 | 04-01 t/m 08-01-2027 | eindevaluatie |
| 17 | 11-01 t/m 15-01-2027 | rapport en factsheet |
| 18 | 18-01 t/m 22-01-2027 | oplevering voorbereiden |
| 19 | 25-01 t/m 29-01-2027 | afronden |

## Afspraken voor het modelleren

- Train/test splitsen we altijd per opname (`StratifiedGroupKFold` op `source_file`), ook binnen de grid search.
- De testset gebruiken we één keer, in lesweek 16.
- Grid search mag in Google Colab. Het notebook gaat daarna terug in de repo, zonder outputs en met paden die ook lokaal werken.
- Nieuwe packages, zoals `xgboost`, voegen we toe met `uv add`.

## Lesweek 11 (16-11 t/m 20-11)
- Khaleel: skills `weekplanning` en `start-kaart` bouwen; Trello-bord inrichten.
- Tonna: Sam vragen of de opnames in Google Drive en Colab mogen staan (AVG); open vragen uit het datakwaliteitsrapport opvolgen; eerste besluitenverslag in `docs/`.
- Ahmed: feature importance op de huidige 64 features (permutation importance en mutual information): welke features hebben de meeste invloed op de klasse?
- Gamal: `xgboost` toevoegen met `uv add`; een Colab-notebook opzetten dat de repo en de data laadt.
- Malak: literatuur: welke audiofeatures onderscheiden buzz en flight (grondfrequentie, FFT, spectrogram, andere spectrale features)?

## Lesweek 12 (23-11 t/m 27-11)
- Khaleel: `preprocessdata.py` repareren (geen dubbele rijen) en de features opnieuw maken.
- Gamal: eerste XGBoost-model met groepsgewijze kruisvalidatie, vergeleken met de SVM uit `hommel_classificatie.ipynb`.
- Ahmed: features weglaten op basis van de importance: wordt het model beter of slechter?
- Malak: hyperparameters voor de grid search van XGBoost onderbouwen (welke, en welke waarden).
- Tonna: afspraak met Sam voorbereiden: resultaten van lesweek 11 en 12; opzet van het adviesrapport.

## Lesweek 13 (30-11 t/m 04-12)
- Khaleel: nieuwe features uit de wav-bestanden: dominante frequentie en bandenergie (FFT).
- Ahmed: spectrogrammen van buzz, flight en radio maken en vergelijken; steekproef labelcontrole, beoordelaar 1.
- Gamal: grid search XGBoost in Colab op de huidige features.
- Malak: steekproef labelcontrole, beoordelaar 2 (onafhankelijk van Ahmed).
- Tonna: factsheet opzetten; besluitenverslag bijwerken.

## Lesweek 14 (07-12 t/m 11-12)
- Khaleel: meer spectrale features (bandwidth, contrast, flatness, flux) en kortere vensters (250 en 500 ms).
- Gamal: grid search XGBoost op de nieuwe features.
- Ahmed: Cohen's kappa en een oordeel over de labelkwaliteit; feature importance op de nieuwe features.
- Malak: SVM en logistische regressie opnieuw op de nieuwe features, ter vergelijking.
- Tonna: resultaten samenvatten voor Sam: is de data voldoende (beslismoment uit het plan)?

## Lesweek 15 (14-12 t/m 18-12)
- Gamal: alle modellen vergelijken en een keuze maken (macro-F1, precision buzz, spreiding over de folds).
- Khaleel: resultaten per recorder (16 kHz en 384 kHz); pipeline opschonen.
- Ahmed: fouten van het gekozen model beluisteren (kwalitatieve foutanalyse).
- Malak: methodehoofdstuk van het adviesrapport.
- Tonna: resultatenhoofdstuk opzetten.

## Kerstvakantie (21-12-2026 t/m 01-01-2027): geen kaarten

## Lesweek 16 (04-01 t/m 08-01)
- Gamal: eindmodel één keer testen op de testset; confusion matrix en metrics.
- Khaleel: betrouwbaarheidsintervallen en spreiding over de folds.
- Ahmed: foutanalyse van het eindmodel uitschrijven.
- Malak: discussie en beperkingen.
- Tonna: eerste versie van de factsheet.

## Lesweek 17 (11-01 t/m 15-01)
- Khaleel: code documenteren en de README bijwerken voor de overdracht aan het lectoraat.
- Gamal: externe validatie op publieke data, alleen als de minimumnorm gehaald is; anders robuustheid per recorder uitschrijven.
- Ahmed: poster.
- Tonna en Malak: adviesrapport: conclusie en advies.

## Lesweek 18 (18-01 t/m 22-01)
- Iedereen: review van rapport, factsheet en code.
- Gamal en Ahmed: presentatie.
- Tonna: alles samenvoegen tot de opleverversie.

## Lesweek 19 (25-01 t/m 29-01)
- Iedereen: eindpresentatie en individueel portfolio.
- Vrijdag 29-01: alles opgeleverd.
