# CLAUDE.md

Regels en context voor iedereen die aan deze repo werkt: teamleden en Claude Code.

## Project

DataLab III (ADS&AI, De Haagse Hogeschool) voor het lectoraat Smart Sensor Systems, opdrachtgever dr. Sam Aerts.
We herkennen hommelgedrag uit geluidsopnames van één seconde uit de proefkas van Tomatoworld.

**Onderzoeksvraag:** Hoe nauwkeurig herkent een classificatiemodel het gedrag van hommels in geluidsfragmenten van één seconde uit de proefkas van Tomatoworld?

## Doelen

1. **Hommel of ruis:** seconden met hommelgeluid (`buzz`, `flight`) onderscheiden van ruis (`radio`, `voice`, `noise`).
2. **Buzz of flight:** binnen het hommelgeluid trilbestuiving (`buzz`) onderscheiden van vliegen (`flight`).
3. **Eerlijke evaluatie:** train/test splitsen per opname (`GroupKFold` op `source_file`), scores per klasse en per recorder (16 kHz / 384 kHz) rapporteren, niet alleen de totale accuracy.
4. **Betrouwbare data:** `preprocessdata.py` repareren (dubbele rijen), labels controleren met een steekproef (Cohen's kappa), en de open vragen over datakwaliteit met de opdrachtgever afstemmen.
5. **Reproduceerbaar werk:** iedereen kan met `uv sync` en de data in `data/` alle resultaten opnieuw maken.

## Teamregels

- **Nooit direct op `main` werken.** `main` verandert alleen via een pull request die is gemerged.
- **Eén branch per taak**, met de naam `taak/korte-omschrijving` (kleine letters, koppeltekens), bijvoorbeeld `taak/fix-dubbele-rijen`.
- **Alles via een pull request met review.** Minstens één teamgenoot keurt de PR goed voordat hij wordt gemerged. Je merget niet je eigen PR zonder review.
- **Geen data committen.** Geen WAV, CSV of andere bestanden uit `data/`, ook geen uitsneden of samples. De opnames bevatten stemmen (AVG).
- **Geen notebook-outputs committen.** nbstripout haalt ze weg; installeer het na het clonen (zie hieronder).
- Begin elke taak met een `git pull` op `main`, zodat je branch up-to-date is.
- Kleine, duidelijke commits met een beschrijvende boodschap in het Nederlands.

## Structuur

| Map | Inhoud |
|---|---|
| `data/` | data, niet in git (zie `data/README.md`) |
| `src/` | herbruikbare Python-code, o.a. `preprocessdata.py` |
| `notebooks/` | analyses en experimenten; paden naar data beginnen met `../data/` |
| `docs/` | werkwijze en verslagen |

## Commando's

Alles draait vanuit de hoofdmap van de repo.

```bash
uv sync                                                  # omgeving maken of bijwerken
uv run nbstripout --install --attributes .gitattributes  # één keer per clone
uv run preprocess                                        # features opnieuw maken (overschrijft de CSV in data/processed_data/)
uv run jupyter notebook                                  # Jupyter starten
uv add <package>                                         # package toevoegen; commit pyproject.toml en uv.lock
```

## Afspraken voor code

- Packages beheren we alleen met uv. Gebruik geen `pip install` in de projectomgeving.
- Paden naar data altijd relatief: vanuit de root `data/...`, vanuit een notebook `../data/...`.
- Notebooks en documentatie schrijven we in het Nederlands.
- Wijzig `data/` nooit vanuit code, behalve via `src/preprocessdata.py` naar `data/processed_data/`.
