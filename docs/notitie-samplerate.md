# Notitie: resamplen naar 16 kHz en de 384 kHz-opnames

Lesweek 12, Khaleel. De analyse staat in `notebooks/samplerate_check.ipynb`.

## Aanleiding

`src/preprocessdata.py` laadt elke opname met `SAMPLE_RATE = 16000`. Bij de 384 kHz-recorder gaat daardoor alles boven 8 kHz verloren. Zit daar informatie die we nodig hebben?

## Wat we vonden

**1. De 384 kHz-recorder levert weinig data, en recorder en opnamedag vallen samen.**

| Recorder | Opnames | Seconden | Dagen |
|---|---|---|---|
| 16 kHz | 138 | 8.094 | 26-05-2026 |
| 384 kHz | 12 | 1.107 | 24-03, 08-04, 13-04 en 24-04-2026 |

**2. De labels zijn ongelijk verdeeld over de recorders.**

| Label | 16 kHz | 384 kHz |
|---|---|---|
| buzz | 89 | 50 |
| flight | 99 | 12 |
| noise | 289 | 12 |
| radio | 1.216 | 440 |
| voice | 1.505 | 4 |
| geen label | 4.894 | 588 |

`voice` komt bijna alleen bij 16 kHz voor. Een model kan daardoor de recorder (of de dag) leren in plaats van het gedrag.

**3. Boven 8 kHz onderscheidt hommelgeluid zich van ruis, maar buzz niet van flight.**

Mediaan van de energie per seconde in de 384 kHz-opnames, in dB:

| Label | 0-1 kHz | 1-8 kHz | 8-20 kHz | 20-50 kHz | Seconden |
|---|---|---|---|---|---|
| buzz | 77,5 | 67,9 | 70,1 | 74,4 | 50 |
| flight | 78,1 | 67,7 | 71,1 | 76,0 | 12 |
| noise | 81,2 | 73,4 | 72,5 | 68,5 | 12 |
| radio | 78,2 | 68,1 | 63,3 | 61,2 | 440 |
| voice | 78,9 | 68,0 | 63,9 | 57,0 | 4 |

- Tussen 20 en 50 kHz hebben `buzz` en `flight` 13 tot 19 dB meer energie dan `radio` en `voice`. Binnen dezelfde opname geldt dat ook: in 7 van de 8 opnames met hommelgeluid ligt de energie in die band 10 tot 17 dB hoger dan in de rest van de opname.
- `buzz` en `flight` verschillen boven 8 kHz nauwelijks van elkaar.
- De aantallen zijn klein (50 buzz- en 12 flight-seconden), dus dit is een aanwijzing, geen bewijs.

## Advies

1. **De hoofdpipeline blijft op 16 kHz.** Alleen dan zijn de features voor beide recorders gelijk. De nieuwe features van lesweek 13 (dominante frequentie, bandenergie) bouwen we tot 8 kHz.
2. **Buzz tegenover flight halen we uit de band onder 8 kHz.** Daar zit de grondfrequentie met haar harmonischen; boven 8 kHz helpt het niet voor dit onderscheid.
3. **Optioneel: een apart experiment op de 384 kHz-opnames.** Bandenergie boven 8 kHz lijkt te helpen bij hommel tegenover ruis. Dat kunnen we alleen op deze 12 opnames testen, en we rapporteren het apart.
4. **Rapporteer scores altijd per recorder** (CLAUDE.md, doel 3). Omdat recorder en dag samenvallen, zeggen die scores ook iets over de dag; dat noemen we als beperking.

## Vraag voor Sam (via Malak)

- Met welke recorder neemt het lectoraat in de toekomst op? Als dat 384 kHz wordt, loont het om features boven 8 kHz mee te nemen, en dan willen we meer gelabelde 384 kHz-opnames.
