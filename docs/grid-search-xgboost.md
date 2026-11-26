# Grid search voor XGBoost

**Auteur:** Malak Alshehabi
**Reviewer:** Tonna Tekle
**Buiten scope:** de grid search zelf draaien (lesweek 13, Gamal)

Dit document hoort bij drie taakkaarten:

1. Welke hyperparameters we tunen en waarom (planning lesweek 12).
2. Welke waarden we proberen, hoe groot het grid wordt en of het in Colab past (planning lesweek 12 en 13).
3. Op welke metriek we het beste model kiezen en hoe we splitsen (afspraken voor het modelleren in `docs/planning.md` en doel 3 in `CLAUDE.md`).

De getallen over de data komen uit het plan van aanpak, paragraaf 8.3: 3.716 gelabelde seconden uit 150 opnames, waarvan 139 buzz, 111 flight en 3.466 ruis.

## 1. Welke hyperparameters we tunen

| Hyperparameter | Wat het doet | Waarom we het tunen |
|---|---|---|
| `max_depth` | De maximale diepte van één boom. Een diepere boom is ingewikkelder en gaat sneller overfitten (XGBoost developers, z.d.-a). Standaard 6. | Diepte is een van de parameters waarmee je de complexiteit van het model direct regelt (XGBoost developers, z.d.-b). Wij hebben weinig data, vooral weinig buzz en flight, dus we willen kijken of ondiepere bomen beter werken. |
| `learning_rate` (eta) | Hoe groot de stap is die elke nieuwe boom zet. Een kleinere waarde maakt het leren voorzichtiger (XGBoost developers, z.d.-a). Standaard 0,3. | Shrinkage verkleint de invloed van elke losse boom en laat ruimte voor latere bomen (Chen & Guestrin, 2016). Een te grote stap kan dus te snel op de trainingsdata gaan passen. |
| `n_estimators` | Het aantal bomen. | Hangt samen met de learning rate: een kleinere learning rate heeft meer bomen nodig (XGBoost developers, z.d.-b; Chen & Guestrin, 2016). Daarom tunen we ze samen. |
| `subsample` | Welk deel van de rijen elke boom ziet. 0,7 betekent dat elke boom een willekeurige 70% van de training gebruikt (XGBoost developers, z.d.-a). Standaard 1. | Friedman (2002) liet zien dat het trekken van een willekeurige deelset per stap de nauwkeurigheid van gradient boosting kan verbeteren. Het model wordt er ook minder gevoelig door voor ruis (XGBoost developers, z.d.-b). |
| `colsample_bytree` | Welk deel van de features elke boom mag gebruiken (XGBoost developers, z.d.-a). Standaard 1. | Volgens gebruikers van XGBoost helpt het weglaten van kolommen nog meer tegen overfitting dan het weglaten van rijen (Chen & Guestrin, 2016). Wij hebben 64 features, waarvan een deel sterk op elkaar lijkt (bijvoorbeeld de MFCC's). |
| `min_child_weight` | Het minimale totale gewicht in een blad. Hoe hoger, hoe voorzichtiger het model splitst (XGBoost developers, z.d.-a). Standaard 1. | Ook een parameter die de complexiteit regelt (XGBoost developers, z.d.-b). Met weinig buzz- en flightvoorbeelden voorkomt een hogere waarde dat het model regels leert op een paar seconden. |
| Klassengewichten | Hoe zwaar een fout per klasse meetelt bij het trainen. | Leeralgoritmen hebben moeite met klassen die ondervertegenwoordigd zijn (He & Garcia, 2009). Zie paragraaf 2. |

**Wat we niet tunen.** Andere parameters, zoals `gamma` en `reg_lambda`, laten we op de standaardwaarde. Bij de meeste datasets maken maar een paar hyperparameters echt verschil (Bergstra & Bengio, 2012), en tunen heeft vooral zin bij de belangrijkste (Probst et al., 2019). Zo houden we het grid klein genoeg voor Colab.

## 2. Omgaan met de ongelijke klassen

Van de gelabelde seconden is 93,3% ruis, 3,7% buzz en 3,0% flight (eigen berekening uit 3.466, 139 en 111 van de 3.716). Een model dat altijd "ruis" zegt, haalt dus al een accuracy van 93,3%.

**Hoe:** met de optie `"balanced"` van scikit-learn. Die geeft elke klasse een gewicht van `n_samples / (n_classes * np.bincount(y))` (scikit-learn developers, z.d.-b). Voor onze data wordt dat ongeveer (eigen berekening):

| Klasse | Aantal | Gewicht |
|---|---|---|
| Buzz | 139 | 8,9 |
| Flight | 111 | 11,2 |
| Ruis | 3.466 | 0,36 |

`XGBClassifier` heeft geen `class_weight`-optie zoals de modellen van scikit-learn. Daarom geven we de gewichten mee als `sample_weight` bij het trainen. Bij twee klassen kan het ook met `scale_pos_weight` (XGBoost developers, z.d.-b).

**Twee kanttekeningen:**

- Bereken de gewichten alleen op de trainingsdata, nooit op de testset.
- Als we in twee stappen classificeren, verschilt het per stap. In stap 2 (buzz tegenover flight) zijn de klassen bijna even groot (139 tegen 111), dus daar maken gewichten weinig uit. In stap 1 (hommel tegenover ruis) is de verhouding ongeveer 1 op 14, en daar zijn ze wel belangrijk (eigen berekening).

We draaien de grid search **met en zonder gewichten** en kijken wat beter werkt. Ook helpt de keuze voor macro-F1 als metriek (paragraaf 4).

## 3. Waarden en grootte van het grid

| Hyperparameter | Waarden | Waarom deze waarden |
|---|---|---|
| `max_depth` | 3, 5, 7 | Rond de standaardwaarde 6, met nadruk op ondiepere bomen omdat we weinig data hebben |
| `learning_rate` | 0,05; 0,1; 0,3 | Van voorzichtig tot de standaardwaarde 0,3 |
| `n_estimators` | 200, 500 | Meer bomen bij een lagere learning rate |
| `subsample` | 0,7; 1,0 | Met en zonder rij-subsampling |
| `colsample_bytree` | 0,7; 1,0 | Met en zonder kolom-subsampling |
| `min_child_weight` | 1, 5 | Standaard en voorzichtiger |
| Klassengewichten | geen, `"balanced"` | Zie paragraaf 2 |

**Grootte (eigen berekening):**

- Combinaties: 3 × 3 × 2 × 2 × 2 × 2 × 2 = **288**
- Fits: 288 × 5 folds = **1.440**

**Rekentijd.** Met een kort testscript is gemeten hoe lang één fit duurt op nepdata van dezelfde vorm als onze trainingsdata: 2.970 rijen, 64 features, 3 klassen in dezelfde verhouding. Dat gebeurde op een machine met 2 CPU-kernen, met `tree_method="hist"`.

| `max_depth` | 200 bomen | 500 bomen |
|---|---|---|
| 3 | 0,8 s | 1,8 s |
| 5 | 1,4 s | 2,5 s |
| 7 | 1,8 s | 2,8 s |

Gemiddeld is dat 1,8 seconde per fit. Voor 1.440 fits wordt het ongeveer **44 minuten**. Colab kan trager zijn dan deze meting, dus reken voor de zekerheid op **ongeveer 1,5 uur** (twee keer zo lang). Dit zijn schattingen:

- De tijd groeit mee met het aantal features. Na lesweek 14 komen er features bij.
- Controleer in Colab eerst hoeveel kernen je hebt met `os.cpu_count()` en draai één fit om de tijd te meten.
- Sla tussendoor `cv_results_` op als CSV. Als de Colab-sessie wegvalt, ben je dan niet alles kwijt.

**Kleiner grid, als het niet past.** Zet `subsample` en `colsample_bytree` vast op 0,8. Gebruik bij `learning_rate` alleen 0,05 en 0,1.

- Combinaties: 3 × 2 × 2 × 2 × 2 = **48**
- Fits: 48 × 5 = **240**
- Tijd: ongeveer **7 minuten**, of 15 minuten met de veiligheidsmarge.

Een andere optie is `RandomizedSearchCV` met bijvoorbeeld 60 willekeurige combinaties uit het grote grid. Willekeurig zoeken vindt bij hetzelfde rekenbudget vaak even goede of betere instellingen dan een vast grid (Bergstra & Bengio, 2012).

**Advies:** begin in lesweek 13 met het kleine grid op de huidige features. Draai het grote grid als daar tijd voor is.

## 4. Metriek en splitsing

### Metriek: macro-F1

Het beste model kiezen we op **macro-F1**. Daarvoor zijn drie redenen:

1. Bij macro-averaging telt elke klasse even zwaar mee, hoe groot de klasse ook is (Sokolova & Lapalme, 2009). Buzz en flight zijn bij ons de kleinste en de belangrijkste klassen.
2. Bij ongelijke klassen zijn aparte evaluatiematen nodig (He & Garcia, 2009). Accuracy werkt bij ons niet: "altijd ruis" haalt al 93,3% (paragraaf 2).
3. In de planning staat voor de modelkeuze in lesweek 15: macro-F1, precision van buzz en de spreiding over de folds.

Ook houden we in de grid search de **F1 per klasse** (buzz, flight, ruis) en de **precision van buzz** bij. Doel 3 in `CLAUDE.md` vraagt namelijk om scores per klasse, niet alleen de totale accuracy. Deze scores gebruiken we niet om te kiezen, maar wel om te rapporteren. De precision van buzz is belangrijk, omdat de opdrachtgever voorbijvliegende hommels niet als bestuiving wil tellen (plan van aanpak, 6.4). Ook de standaardafwijking van macro-F1 over de folds slaan we op. In `GridSearchCV` kan dat met meerdere scorers en `refit="f1_macro"`.

### Scores per recorder

Doel 3 in `CLAUDE.md` vraagt ook om scores per recorder (16 kHz en 384 kHz). In de grid search zelf kiezen we niet per recorder. Wel maken we voor het beste model voorspellingen per fold (`cross_val_predict` met dezelfde splitter) en rapporteren we macro-F1 en de F1 per klasse apart voor de 16 kHz- en de 384 kHz-opnames. Er zijn maar 12 opnames op 384 kHz (plan van aanpak, 8.3), dus de scores voor die groep zijn onzeker. Dat zetten we er altijd bij.

### Splitsing

- **Testset eerst apart.** De testset wordt per opname afgesplitst en blijft onaangeraakt tot lesweek 16 (afspraken in `docs/planning.md`). De grid search gebruikt alleen de rest.
- **Binnen de grid search: `StratifiedGroupKFold` op `source_file`.** `CLAUDE.md` noemt `GroupKFold`, de planning `StratifiedGroupKFold`. Beide houden opnames bij elkaar. `StratifiedGroupKFold` probeert ook de klassen eerlijk over de folds te verdelen. Dat is belangrijk bij onze kleine klassen. Wij volgen de planning. Het is handig om `CLAUDE.md` daarop aan te passen (via een eigen PR).
- **Uitleg:** Dezelfde groep komt nooit in twee folds terecht, en de verdeling van de klassen blijft per fold zo veel mogelijk gelijk (scikit-learn developers, z.d.-a). Zo komen seconden uit dezelfde opname nooit tegelijk in training en validatie. Als dat wel gebeurt, lekt informatie en lijkt het model beter dan het is (Kapoor & Narayanan, 2023).
- **Vaste `random_state`** (bijvoorbeeld 42), zodat iedereen dezelfde folds krijgt.
- Geef dezelfde splitter mee aan `GridSearchCV(cv=...)` en `groups=source_file` aan `.fit()`.

**Let op bij het aantal folds.** De 139 seconden buzz en 111 seconden flight zitten misschien in maar een paar opnames. Zit er in een fold geen buzz of flight, dan is de F1 voor die klasse niet te berekenen en klopt de macro-F1 van die fold niet. Tel daarom eerst in hoeveel opnames buzz en flight voorkomen. Zijn dat er minder dan 5, gebruik dan 3 of 4 folds in plaats van 5. Pas dan ook het aantal fits in paragraaf 3 aan.

## Nog controleren (voor de reviewer)

- **Rekentijd.** Die is gemeten op een testmachine met 2 kernen en nepdata. Gamal: graag één echte fit in Colab timen voordat het hele grid start.
- **Eén of twee stappen.** Classificeren we met één model voor drie klassen, of in twee stappen? Bij twee stappen draaien we twee kleinere grid searches. Stap 2 heeft dan maar 250 rijen en is veel sneller.

## Bronnen

Bergstra, J., & Bengio, Y. (2012). Random search for hyper-parameter optimization. *Journal of Machine Learning Research, 13*(10), 281–305. https://jmlr.org/papers/v13/bergstra12a.html

Chen, T., & Guestrin, C. (2016). XGBoost: A scalable tree boosting system. In *Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining* (pp. 785–794). ACM. https://doi.org/10.1145/2939672.2939785

Friedman, J. H. (2002). Stochastic gradient boosting. *Computational Statistics & Data Analysis, 38*(4), 367–378. https://doi.org/10.1016/S0167-9473(01)00065-2

He, H., & Garcia, E. A. (2009). Learning from imbalanced data. *IEEE Transactions on Knowledge and Data Engineering, 21*(9), 1263–1284. https://doi.org/10.1109/TKDE.2008.239

Kapoor, S., & Narayanan, A. (2023). Leakage and the reproducibility crisis in machine-learning-based science. *Patterns, 4*(9), 100804. https://doi.org/10.1016/j.patter.2023.100804

Probst, P., Boulesteix, A.-L., & Bischl, B. (2019). Tunability: Importance of hyperparameters of machine learning algorithms. *Journal of Machine Learning Research, 20*(53), 1–32. https://jmlr.org/papers/v20/18-444.html

scikit-learn developers. (z.d.-a). *sklearn.model_selection.StratifiedGroupKFold*. Geraadpleegd op 26 november 2026, van https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedGroupKFold.html

scikit-learn developers. (z.d.-b). *sklearn.utils.class_weight.compute_sample_weight*. Geraadpleegd op 26 november 2026, van https://scikit-learn.org/stable/modules/generated/sklearn.utils.class_weight.compute_sample_weight.html

Sokolova, M., & Lapalme, G. (2009). A systematic analysis of performance measures for classification tasks. *Information Processing & Management, 45*(4), 427–437. https://doi.org/10.1016/j.ipm.2009.03.002

XGBoost developers. (z.d.-a). *XGBoost parameters*. Geraadpleegd op 26 november 2026, van https://xgboost.readthedocs.io/en/stable/parameter.html

XGBoost developers. (z.d.-b). *Notes on parameter tuning*. Geraadpleegd op 26 november 2026, van https://xgboost.readthedocs.io/en/latest/tutorials/param_tuning.html
