# Datalab-lll – Hommelgedrag herkennen uit geluid

DataLab III-project van de opleiding Applied Data Science & AI (De Haagse Hogeschool) voor het lectoraat **Smart Sensor Systems**. Opdrachtgever: dr. Sam Aerts (s.h.aerts@hhs.nl). De opnames en labels komen uit een eerdere stage van Jasper Schoen.

We onderzoeken of het gedrag van hommels in de proefkas van Tomatoworld automatisch uit geluid te herkennen is: eerst hommel of ruis, daarna trilbestuiving (`buzz`) of vliegen (`flight`).

**Onderzoeksvraag:** Hoe nauwkeurig herkent een classificatiemodel het gedrag van hommels in geluidsfragmenten van één seconde uit de proefkas van Tomatoworld?

## Snel starten

Je hebt [git](https://git-scm.com/) en [uv](https://docs.astral.sh/uv/) nodig. De volledige uitleg voor Mac en Windows staat in [docs/werkwijze-git.md](docs/werkwijze-git.md).

```bash
git clone https://github.com/Khaleellll/Datalab-lll.git
cd Datalab-lll
uv sync                                                  # maakt .venv met Python 3.13 en alle packages
uv run nbstripout --install --attributes .gitattributes  # één keer per clone: geen notebook-outputs in git
```

Zet daarna de data in `data/` (zie [data/README.md](data/README.md)) en open het notebook:

```bash
uv run jupyter notebook notebooks/eda_gecombineerd.ipynb
```

In VS Code kies je als kernel de Python uit `.venv`.

## Mappenstructuur

```
Datalab-lll/
├── README.md                    # dit bestand
├── CLAUDE.md                    # teamregels en projectdoelen
├── pyproject.toml, uv.lock      # uv-project "bumblebee": packages en vaste versies
├── .python-version              # Python 3.13
├── .gitattributes               # nbstripout-filter voor notebooks
├── .github/
│   └── pull_request_template.md
├── data/                        # NIET in git, zie data/README.md
│   ├── raw_data/                # 150 WAV-opnames (YYYYMMDD_HHMMSS.WAV)
│   ├── raw_labels/              # buzzdetection_labels.csv
│   └── processed_data/          # bee_features_per_second.csv
├── src/
│   └── preprocessdata.py        # WAV + labels -> features per seconde
├── notebooks/
│   └── eda_gecombineerd.ipynb   # eerste data-analyse
└── docs/
    ├── werkwijze-git.md         # clonen, uv, data, branch, pull request
    └── Datakwaliteit hommelopnames.pdf   # datakwaliteit en vragen aan de opdrachtgever
```

Nieuwe code die je vaker gebruikt, zet je in `src/`. Analyses en experimenten zet je in `notebooks/`.

## Data

De data staat **niet** in deze repository, omdat een deel van de opnames stemmen bevat (AVG). Je vindt de data in het Teams-kanaal van het Horti-Sensor cluster. Zet de bestanden in `data/`, zoals beschreven in [data/README.md](data/README.md).

- **Ruwe data:** 150 WAV-opnames. De bestandsnaam is het starttijdstip van de opname (`YYYYMMDD_HHMMSS.WAV`).
- **Labels:** `buzzdetection_labels.csv`, handmatig gemaakt, met één rij per seconde (`start`, `end`, `label`, `opmerking`).
- **Features:** `bee_features_per_second.csv`, gemaakt door `src/preprocessdata.py`. Elke rij is één seconde geluid.

### Klassen

Volgens de opdrachtgever worden korte geluidsfragmenten ingedeeld in gedragsklassen zoals:

| Label | Betekenis |
|---|---|
| `buzz` | trilbestuiving (*buzz pollination*): lage, sterke trilling waarmee de hommel stuifmeel losschudt |
| `flight` | vlieggeluid |
| `radio` | radio of achtergrondstoring |
| `noise` | algemene ruis |
| `voice` | menselijke stem |
| `silence` | stilte of omgevingsgeluid (komt niet voor in het huidige labelbestand) |

## Preprocessing: `src/preprocessdata.py`

Het script zet de ruwe WAV-opnames en het labelbestand om in één feature-CSV voor het trainen van modellen. We mogen het script aanpassen en er andere features uit halen.

**Draaien** (vanuit de hoofdmap van de repo):

```bash
uv run preprocess
# of: uv run python src/preprocessdata.py
```

Het script toont de voortgang per bestand en een samenvatting. Let op: het **overschrijft** `data/processed_data/bee_features_per_second.csv`.

**Stap voor stap:**

1. **Labels inlezen:** `data/raw_labels/buzzdetection_labels.csv`, één rij per seconde met een `start`-tijdstip en een `label`.
2. **Bestandsnamen lezen:** elke WAV in `data/raw_data/` heet `YYYYMMDD_HHMMSS.WAV`; daaruit volgt het starttijdstip van de opname.
3. **Opsplitsen in seconden:** elke opname wordt geknipt in stukken van 1 seconde die niet overlappen.
4. **Labels koppelen:** per seconde wordt het tijdstip berekend (`start opname + offset`) en opgezocht in het labelbestand. Seconden die daar niet in staan, krijgen `label = NaN`.
5. **Features berekenen:** binnen elke seconde worden MFCC's berekend over korte, overlappende frames. Die worden gemiddeld tot één featurevector per seconde.
6. **Wegschrijven:** alle rijen gaan naar `data/processed_data/bee_features_per_second.csv`.

**Features per seconde:**

| Kolom(men) | Betekenis |
|---|---|
| `start`, `end` | absolute tijdstippen van deze seconde |
| `label` | gedragsklasse uit het labelbestand (`NaN` als er geen label is) |
| `source_file` | naam van de oorspronkelijke WAV |
| `mfcc_1_mean` – `mfcc_20_mean` | gemiddelde MFCC-coëfficiënten over de frames |
| `mfcc_1_std` – `mfcc_20_std` | standaarddeviatie van de MFCC-coëfficiënten |
| `delta_1_mean` – `delta_20_mean` | gemiddelde eerste afgeleide (verandering) van de MFCC's |
| `zcr_mean` | zero-crossing rate: hangt samen met ruis en toonhoogte |
| `rms_mean` | RMS-energie: totale luidheid |
| `spectral_centroid_mean` | "helderheid" van het geluid |
| `spectral_rolloff_mean` | frequentie waaronder 85% van de energie ligt |

**Instellingen** (constanten bovenaan het script):

| Variabele | Standaard | Betekenis |
|---|---|---|
| `SAMPLE_RATE` | `16000` | alle audio wordt omgezet naar deze samplerate (Hz) |
| `N_MFCC` | `20` | aantal MFCC-coëfficiënten |
| `N_FFT` | `512` | FFT-venster binnen elke seconde |
| `HOP_LENGTH` | `256` | stap tussen frames (~16 ms bij 16 kHz) |
| `N_MELS` | `64` | aantal Mel-filters |

**Bekend probleem:** het script zoekt eerst naar `*.WAV` en daarna naar `*.wav`. Op Windows en macOS vindt het daardoor elk bestand twee keer, en staat elke rij dubbel in de output. Het notebook ontdubbelt de data eerst; het script repareren staat op de takenlijst.

## Belangrijkste bevindingen uit de EDA

Meer details staan in het notebook en in [docs/Datakwaliteit hommelopnames.pdf](docs/Datakwaliteit%20hommelopnames.pdf).

- **Elke rij staat dubbel** in `bee_features_per_second.csv` (18.396 rijen, 9.198 unieke seconden). Zie het bekende probleem hierboven.
- **60% van de seconden heeft geen label.** Van de 3.716 gelabelde seconden zijn er maar 139 `buzz` en 111 `flight`.
- **Twee soorten recorders** (12 opnames op 384 kHz, 138 op 16 kHz) verschillen meer van elkaar dan de klassen. We rapporteren daarom per recorder.
- **Labels zijn geclusterd** in tijd en bestanden. Train/test splitsen we daarom per opname (`GroupKFold`).

## Samenwerken

- Werk nooit direct op `main`: één branch per taak (`taak/korte-omschrijving`), en alles gaat via een pull request met review.
- Commit nooit data.
- De volledige regels staan in [CLAUDE.md](CLAUDE.md). Het stappenplan staat in [docs/werkwijze-git.md](docs/werkwijze-git.md).

## Status

- [x] Eerste data-analyse
- [x] Repository-structuur en werkwijze
- [ ] `preprocessdata.py` repareren en features opnieuw genereren
- [ ] Labelcontrole (steekproef, Cohen's kappa)
- [ ] Modellen trainen en evalueren

## Team

| Naam | Aandachtsgebied |
|---|---|
| Malak Alshehabi | Coördinatie en rapportage |
| Ahmed Bashabeeb | Labelcontrole en geluidsanalyse |
| Khaleel Al-Aqel | Data en features |
| Tonna Tekle | Literatuur en bronnen |
| Gamal Al-Sabeei | Publieke datasets en externe validatie |

Begeleiding: Mike Huisman, Mirabai Vosteen.
