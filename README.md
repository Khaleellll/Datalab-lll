# Datalab-lll – Hommelgedrag herkennen uit geluid

DataLab III-project van de opleiding Applied Data Science & AI (De Haagse Hogeschool) voor het lectoraat **Smart Sensor Systems**. Opdrachtgever: dr. Sam Aerts.

We onderzoeken of het gedrag van hommels in de proefkas van Tomatoworld automatisch uit geluid te herkennen is: eerst hommel of ruis, daarna trilbestuiving (`buzz`) of vliegen (`flight`).

**Onderzoeksvraag:** Hoe nauwkeurig herkent een classificatiemodel het gedrag van hommels in geluidsfragmenten van één seconde uit de proefkas van Tomatoworld?

## Inhoud

| Bestand | Wat |
|---|---|
| `eda_gecombineerd.ipynb` | Eerste data-analyse in 6 stappen: context, structuur, kwaliteit, één variabele, relaties en vervolgvragen |

## Data

De data staat **niet** in deze repository, omdat een deel van de opnames stemmen bevat (AVG). De data staat in het Teams-kanaal van het Horti-Sensor cluster. Zet de bestanden naast het notebook:

```
datalab-lll/
├── eda_gecombineerd.ipynb
├── raw_data/                         # 150 WAV-opnames (YYYYMMDD_HHMMSS.WAV)
├── raw_labels/
│   └── buzzdetection_labels.csv      # handmatige labels, één rij per seconde
└── processed_data/
    └── bee_features_per_second.csv   # 64 features per seconde (preprocessdata.py)
```

## Installatie

Getest met Python 3.13.

```bash
pip install pandas numpy matplotlib scikit-learn soundfile jupyter
jupyter notebook eda_gecombineerd.ipynb
```

## Belangrijkste bevindingen uit de EDA

- **Elke rij staat dubbel** in `bee_features_per_second.csv` (18.396 rijen, 9.198 unieke seconden), omdat `preprocessdata.py` elk bestand twee keer inleest. Het notebook ontdubbelt de data eerst.
- **60% van de seconden heeft geen label.** Van de 3.716 gelabelde seconden zijn er maar 139 `buzz` en 111 `flight`.
- **Twee soorten recorders** (12 opnames op 384 kHz, 138 op 16 kHz) verschillen meer van elkaar dan de klassen. We rapporteren daarom per recorder.
- **Labels zijn geclusterd** in tijd en bestanden. Train/test splitsen we daarom per opname (`GroupKFold`).

## Status

- [x] Eerste data-analyse
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
