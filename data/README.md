# data/

Deze map staat **niet** in git. Een deel van de opnames bevat stemmen (AVG). Alleen dit bestand wordt gecommit.

Download de data uit het Teams-kanaal van het Horti-Sensor cluster en zet de mappen zo neer:

```
data/
├── README.md                         # dit bestand
├── raw_data/                         # 150 WAV-opnames (YYYYMMDD_HHMMSS.WAV), ca. 1 GB
├── raw_labels/
│   └── buzzdetection_labels.csv      # handmatige labels, één rij per seconde
└── processed_data/
    └── bee_features_per_second.csv   # output van src/preprocessdata.py
```

De mapnamen moeten precies zo heten: `src/preprocessdata.py` en `notebooks/eda_gecombineerd.ipynb` zoeken op deze plekken.

Controle: in de hoofdmap van de repo mag `git status` hier niets uit `data/` tonen, behalve dit bestand.
