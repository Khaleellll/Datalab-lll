# Literatuur: grondfrequentie van hommels bij buzz en flight

**Taak:** literatuuronderzoek grondfrequentie (planning lesweek 11)
**Auteur:** Malak Alshehabi
**Reviewer:** Tonna Tekle
**Buiten scope:** de features zelf programmeren (lesweek 13, Khaleel)

## Vraag

Welke grondfrequentie (F0) hoort bij trilbestuiving (*buzz*) en welke bij vliegen (*flight*) van hommels, en hoe groot is het verschil? We gebruiken het antwoord bij het kiezen van features in lesweek 13 en bij deelvraag 2 uit het plan van aanpak.

## Kort antwoord

- Bij *Bombus terrestris* ligt de **buzz** meestal tussen **310 en 365 Hz** (Pritchard & Vallejo-Marín, 2020; De Luca et al., 2013; Vallejo-Marín & Lundgren, 2026; Morgan et al., 2016).
- **Flight** ligt tussen ongeveer **135 en 200 Hz** (Pritchard & Vallejo-Marín, 2020; Morgan et al., 2016).
- Buzz ligt dus ongeveer **165 tot 175 Hz hoger**. Dat is **1,8 tot 2,3 keer** zo hoog.
- Bij een andere hommelsoort of plant kan een buzz lager liggen, rond 240 Hz (Switzer et al., 2016). Dan komt hij dicht bij vlieggeluid.
- Een vaste grens zoals "boven 250 Hz is buzz" is daarom niet veilig. We moeten in onze eigen data kijken waar de grens ligt.

| Bron | Soort | Hoe gemeten | Buzz (Hz) | Flight (Hz) | Verschil |
|---|---|---|---|---|---|
| Pritchard & Vallejo-Marín (2020) | *B. terrestris* | Laser en trillingssensor | 313 ± 3 | 137 ± 2 | 176 Hz (×2,3) |
| Morgan et al. (2016) | *B. terrestris* | Opnames van werksters | 363 ± 25 (n = 584) | 198 ± 9 (n = 585) | 165 Hz (×1,8) |
| De Luca et al. (2013) | *B. terrestris* | Opnames op *Solanum rostratum* | 324 ± 4 (215 buzzes, 54 hommels) | – | – |
| Vallejo-Marín & Lundgren (2026) | *B. terrestris* | 2.101 buzzes van 13 werksters | 340 ± 26 | – | – |
| Switzer et al. (2016) | *B. impatiens*, op **tomaat** | Microfoon op minder dan 3 cm | ongeveer 240 (n = 53) | lager dan buzz (n = 53) | – |

*Het verschil is buzz min flight binnen dezelfde studie. Bij Morgan et al. (2016) en Vallejo-Marín & Lundgren (2026) is het getal na de ± de standaarddeviatie (SD). Bij de andere studies moet dat nog worden gecontroleerd.*

## Wat de bronnen zeggen

**Pritchard & Vallejo-Marín (2020)** maten dezelfde hommels in drie situaties. Op de bloem was de frequentie gemiddeld 313,09 ± 2,63 Hz, bij een afweerbuzz 236,32 ± 4,29 Hz en tijdens het vliegen 136,95 ± 1,73 Hz. Ze maten de trilling van het lijf met een laser en een trillingssensor, dus niet het geluid in de lucht. Tijdens het vliegen zaten de hommels vast. De afweerbuzz ligt tussen buzz en flight in.

**Morgan et al. (2016)** vonden hetzelfde patroon. Tijdens het vliegen lag de frequentie op 197,58 ± 8,8 Hz (n = 585), tijdens trilbestuiving op 362,7 ± 24,8 Hz (n = 584). De buzzes waren ook zachter dan het vlieggeluid. Naarmate een hommel vaker een bloem had bezocht, werd de buzzfrequentie iets lager.

**De Luca et al. (2013)** namen 215 buzzes op van 54 hommels (*B. terrestris*). De piekfrequentie was gemiddeld 324 ± 3,67 Hz. In een latere studie vonden **Vallejo-Marín & Lundgren (2026)** voor 2.101 buzzes een grondfrequentie van 340 ± 26 Hz. Eén buzz duurde gemiddeld 0,748 ± 0,604 seconde.

**Switzer et al. (2016)** is de enige bron die op **tomaat** heeft gemeten, wel met een andere hommelsoort. *Bombus impatiens* buzzte rond 240 Hz. Ze namen op met een microfoon op minder dan 3 cm van de bij, dus met hetzelfde soort meting als onze opnames. Het precieze getal voor vliegen staat alleen in de bijlage van het artikel. In de tekst staat wel dat het lager is dan de buzz.

**Miller-Struttmann et al. (2017)** gaan over vlieggeluid in het veld. In hun voorbeeld ligt de vleugelslag van een hommel rond 175 Hz, met boventonen op twee, drie, vier keer die frequentie. Ze vonden ook dat hommels met langere vleugels met een lagere toon vliegen.

**Waarom is buzz hoger?** Bij een buzz bewegen de vleugels niet. Daardoor is er minder luchtweerstand en staan de spieren strakker, en dat geeft een hogere frequentie (Pritchard & Vallejo-Marín, 2020).

## Waar het verschil kleiner wordt

- **Hommelsoort.** Buzz van *B. impatiens* op tomaat (ongeveer 240 Hz) ligt een stuk lager dan die van *B. terrestris* (310–365 Hz). Welke soort er in de proefkas zit, weten we nog niet zeker.
- **Plant en weer.** Dezelfde hommel buzzt anders op verschillende planten. In het veld hing de frequentie ook samen met de luchtvochtigheid en de datum (Switzer & Combes, 2017).
- **Algemeen.** Buzzes op bloemen hebben een grondtoon tussen 100 en 400 Hz (De Luca & Vallejo-Marín, 2013). De boventonen gaan door tot ongeveer 8 kHz (De Luca & Vallejo-Marín, 2022).

Kort gezegd: bij één soort op één plant is het verschil groot, bijna een factor 2. Tussen soorten en planten kan een lage buzz dicht bij een hoge vlucht komen.

## Wat dit betekent voor ons project

Dit zijn tips voor de features in lesweek 13 en 14. Het programmeren zelf doet Khaleel.

1. **Dominante frequentie (lesweek 13).** Bij een buzz is de grondtoon meestal ook de sterkste piek (De Luca & Vallejo-Marín, 2022). Een FFT-piek tussen 100 en 500 Hz geeft voor buzz dus ongeveer de grondfrequentie. Of dat bij vlieggeluid ook zo is, heb ik niet in een bron gevonden. Dat kunnen we nakijken in de spectrogrammen van Ahmed (lesweek 13).
2. **Bandenergie (lesweek 13).** Als begin kunnen we de banden van Switzer & Combes (2016) nemen: zij zochten de vleugelslag tussen 120 en 220 Hz en de buzz tussen 195 en 400 Hz. De banden overlappen een beetje, dus we moeten op onze eigen data testen of ze werken.
3. **Spectral centroid zegt weinig over de grondtoon.** In onze EDA lag de spectral centroid van buzz rond 1.156 Hz en die van de andere klassen rond 1.026–1.077 Hz (plan van aanpak, paragraaf 8.3). Dat is veel hoger dan de grondtonen uit de literatuur, omdat de centroid ook boventonen en ruis meetelt.
4. **16 kHz-recorder.** Zie de aparte alinea hieronder.
5. **Kortere vensters (lesweek 14).** Een buzz duurt gemiddeld ongeveer 0,75 seconde (Vallejo-Marín & Lundgren, 2026). In een fragment van 1 seconde kan dus een stuk buzz en een stuk vlucht zitten. Vensters van 250 of 500 ms passen beter. Dit kan ook verklaren waarom sommige labels niet lijken te kloppen.
6. **Volume.** Buzz is zachter dan vlieggeluid (Morgan et al., 2016). Maar de afstand tot de microfoon verschilt per opname, dus alleen het volume gebruiken is riskant.
7. **Geen vaste grens.** Kijk naar hoe de grondfrequentie per klasse verdeeld is in onze data, en laat het model de grens leren.
8. **Andere meting.** Pritchard & Vallejo-Marín (2020) maten de trilling van het lijf. Wij hebben geluid via een microfoon. Wij verwachten dat de grondfrequentie ongeveer gelijk is, omdat het geluid uit dezelfde trilling komt. Dat is onze eigen redenering en is niet gemeten. Switzer et al. (2016) gebruikten wel een microfoon. Die bron lijkt dus het meest op onze opnames.

## Wat dit betekent voor de 16 kHz-recorder

Een recorder van 16 kHz kan geluid meten tot 8 kHz, de helft van de samplefrequentie. De grondtoon van een buzz ligt bij *B. terrestris* tussen 310 en 365 Hz en bij *B. impatiens* rond 240 Hz. Vlieggeluid ligt tussen ongeveer 135 en 200 Hz (zie de tabel). Die grondtonen vallen dus ruim binnen wat de recorder meet. De boventonen van een buzz gaan door tot ongeveer 8 kHz (De Luca & Vallejo-Marín, 2022). Alleen de hoogste boventonen kunnen dus wegvallen. Dat is geen groot verlies, want het meeste geluid van een buzz zit in het lage deel: tussen 450 en 1.000 Hz zit duidelijk minder energie dan tussen 100 en 400 Hz (De Luca & Vallejo-Marín, 2013). Voor features als de grondfrequentie, de dominante frequentie en de bandenergie onder 1.000 Hz is de 16 kHz-recorder dus goed genoeg. De opnames van 384 kHz worden voor de features ook eerst omgezet naar 16 kHz (README, zie plan van aanpak paragraaf 8.3). Daarna bevatten beide recorders hetzelfde frequentiebereik. Het verschil tussen de recorders dat we in de EDA zagen, komt volgens ons daarom niet door het frequentiebereik, maar door iets anders, zoals de microfoon of het achtergrondgeluid. Dat is onze eigen inschatting en moet nog worden getest (lesweek 15, resultaten per recorder).

## Open vragen

- **Welke hommelsoort zit in de proefkas?** Navragen bij Sam Aerts of opzoeken in de README. Bij *B. terrestris* verwachten we de buzz rond 310–365 Hz, bij *B. impatiens* rond 240 Hz.
- **Afweerbuzz.** Komen afweerbuzzes (rond 236 Hz) voor in onze opnames? En zijn ze dan als buzz gelabeld? Dat zou de klasse buzz vervuilen.

## Nog controleren (voor de reviewer)

- Pritchard & Vallejo-Marín (2020) en De Luca et al. (2013): is het getal na de ± een SD of een standaardfout (SE)?
- Switzer et al. (2016): het getal voor vliegen staat in hun Online Resource 1 (Table II). Die heb ik niet kunnen openen.

## Bronnen

De Luca, P. A., Bussière, L. F., Souto-Vilaros, D., Goulson, D., Mason, A. C., & Vallejo-Marín, M. (2013). Variability in bumblebee pollination buzzes affects the quantity of pollen released from flowers. *Oecologia, 172*(3), 805–816. https://doi.org/10.1007/s00442-012-2535-1

De Luca, P. A., & Vallejo-Marín, M. (2013). What's the 'buzz' about? The ecology and evolutionary significance of buzz-pollination. *Current Opinion in Plant Biology, 16*(4), 429–435. https://doi.org/10.1016/j.pbi.2013.05.002

De Luca, P. A., & Vallejo-Marín, M. (2022). Blooms and buzzing bees: Bridging buzz pollination and biotremology. In P. S. M. Hill, V. Mazzoni, N. Stritih-Peljhan, M. Virant-Doberlet, & A. Wessel (Eds.), *Biotremology: Physiology, ecology, and evolution* (pp. 261–292). Springer. https://doi.org/10.1007/978-3-030-97419-0_11

Miller-Struttmann, N. E., Heise, D., Schul, J., Geib, J. C., & Galen, C. (2017). Flight of the bumble bee: Buzzes predict pollination services. *PLOS ONE, 12*(6), e0179273. https://doi.org/10.1371/journal.pone.0179273

Morgan, T., Whitehorn, P., Lye, G. C., & Vallejo-Marín, M. (2016). Floral sonication is an innate behaviour in bumblebees that can be fine-tuned with experience in manipulating flowers. *Journal of Insect Behavior, 29*(2), 233–241. https://doi.org/10.1007/s10905-016-9553-5

Pritchard, D. J., & Vallejo-Marín, M. (2020). Floral vibrations by buzz-pollinating bees achieve higher frequency, velocity and acceleration than flight and defence vibrations. *Journal of Experimental Biology, 223*(11), jeb220541. https://doi.org/10.1242/jeb.220541

Switzer, C. M., & Combes, S. A. (2016). *Bombus impatiens* (Hymenoptera: Apidae) display reduced pollen foraging behavior when marked with bee tags vs. paint. *Journal of Melittology*, (62). https://doi.org/10.17161/jom.v0i62.5679

Switzer, C. M., & Combes, S. A. (2017). Bumblebee sonication behavior changes with plant species and environmental conditions. *Apidologie, 48*(2), 223–233. https://doi.org/10.1007/s13592-016-0467-1

Switzer, C. M., Hogendoorn, K., Ravi, S., & Combes, S. A. (2016). Shakers and head bangers: Differences in sonication behavior between Australian *Amegilla murrayensis* (blue-banded bees) and North American *Bombus impatiens* (bumblebees). *Arthropod-Plant Interactions, 10*, 1–8. https://doi.org/10.1007/s11829-015-9407-7

Vallejo-Marín, M., & Lundgren, A. (2026). Gradual pollen release in a buzz-pollinated plant: Investigating pollen presentation theory under bee visitation. *Functional Ecology, 40*(2), 476–485. https://doi.org/10.1111/1365-2435.70189
