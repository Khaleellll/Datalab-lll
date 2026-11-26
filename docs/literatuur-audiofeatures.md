# Literatuur: audiofeatures voor buzz en flight

**Auteur:** Malak Alshehabi
**Reviewer:** Tonna Tekle
**Buiten scope:** de features zelf programmeren (lesweek 13 en 14, Khaleel)

Dit bestand heeft drie delen:

- **Deel 1:** de grondfrequentie van buzz en flight (taakkaart lesweek 11).
- **Deel 2:** welke spectrale features de literatuur gebruikt, wat ze meten en welke venstergrootte de bronnen gebruiken (taakkaart lesweek 11).
- **Deel 3:** advies voor Khaleel: welke features eerst bouwen in lesweek 13 en 14, en waarom.

De bronnen van alle drie de delen staan samen onderaan.

# Deel 1: grondfrequentie

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

**Switzer et al. (2016)** is de enige bron in de tabel die op **tomaat** heeft gemeten, wel met een andere hommelsoort. *Bombus impatiens* buzzte rond 240 Hz. Ze namen op met een microfoon op minder dan 3 cm van de bij, dus met hetzelfde soort meting als onze opnames. Het precieze getal voor vliegen staat alleen in de bijlage van het artikel. In de tekst staat wel dat het lager is dan de buzz.

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

# Deel 2: spectrale features

## Vraag

Welke spectrale features gebruikt de literatuur om insectengeluid of hommelgedrag te herkennen? Wat meet elke feature, laten de bronnen zien dat hij buzz en flight van elkaar onderscheidt, en welke venstergrootte gebruiken ze?

## Kort antwoord

- In de bronnen die ik vond, is **MFCC** de feature die het vaakst wordt gebruikt bij bijen en hommels. Eén bron laat zien dat buzz en flight in MFCC duidelijk verschillen (Ribeiro et al., 2021).
- **Grondfrequentie en dominante frequentie** worden ook veel gebruikt, vaak samen met MFCC. Het verschil tussen buzz en flight in grondfrequentie is goed onderbouwd (zie deel 1).
- **Spectrogrammen** worden vooral gebruikt als invoer voor deep learning en om data met het oog te labelen.
- **Spectral centroid en spread (bandwidth)** zijn gebruikt om hommelgeluid te scheiden van ander geluid (Heise et al., 2020). Dat past bij onze stap 1 (hommel of ruis).
- Voor **spectral flatness en spectral flux** heb ik geen bron gevonden die ze bij bijen of hommels test. Of ze buzz en flight onderscheiden, is dus onbekend.
- Geen enkele bron vergelijkt alle features met elkaar voor buzz tegenover flight. Dat moeten wij zelf testen.

## Per feature

| Feature | Wat het meet | Gebruikt bij bijen of hommels? | Onderscheidt buzz en flight volgens de bronnen? |
|---|---|---|---|
| **FFT, dominante frequentie en bandenergie** | Hoeveel energie er in elke frequentie zit. De dominante frequentie is de piek met de meeste energie. Bandenergie is de energie binnen een gekozen frequentieband. | Ja. Rodríguez Ballesteros et al. (2024) maten de dominante frequentie en de energie van de eerste en tweede boventoon. Heise et al. (2020) gebruikten de grondfrequentie. | **Ja, voor de grondfrequentie** (deel 1). Voor bandenergie heb ik geen studie gevonden die buzz en flight vergelijkt. |
| **Spectrogram** | Hoe de frequenties in een geluid over de tijd veranderen. Een mel-spectrogram doet hetzelfde op de mel-schaal, die lage frequenties beter onderscheidt dan hoge (Kawakita & Ichikawa, 2019). | Ja. buzzdetect gebruikt het model YAMNet, dat werkt met log-mel-spectrogrammen (Hearon et al., 2025; TensorFlow, z.d.). Bij buzzdetect is ook gelabeld door te luisteren en tegelijk naar het spectrogram te kijken. | **Niet getest.** buzzdetect herkent vlieggeluid van insecten tegenover ander geluid, niet buzz tegenover flight. Wel bruikbaar als voorbeeld voor stap 1. |
| **MFCC** | Een korte beschrijving van de vorm van het spectrum, de "klankkleur" (Meister et al., 2022), op de mel-schaal. MFCC is beter in het onderscheiden van lage dan van hoge frequenties (Kawakita & Ichikawa, 2019). | Ja: Ribeiro et al. (2021), Kawakita & Ichikawa (2019), Rodríguez Ballesteros et al. (2024). | **Ja.** Volgens Ribeiro et al. (2021) zijn buzz en flight in MFCC goed van elkaar te onderscheiden. Hun doel was wel bijensoorten herkennen, niet het gedrag. |
| **Spectral centroid** | Het zwaartepunt van het spectrum: ligt de energie gemiddeld hoog of laag? | Ja. Heise et al. (2020) gebruikten centroid en spread onder 400 Hz om hommelgeluid uit opnames te filteren. | **Niet getest in een bron.** In onze eigen EDA lag de centroid van buzz iets hoger dan die van de andere klassen (plan van aanpak, 8.3). |
| **Spectral bandwidth** | Hoe breed de energie rond de centroid verspreid is (Meister et al., 2022). | Ja, als "spectral spread" bij Heise et al. (2020). | **Niet getest.** |
| **Spectral flatness** | Hoeveel een geluid op ruis lijkt in plaats van op een toon. Een waarde dicht bij 1 betekent dat het spectrum op witte ruis lijkt (librosa, z.d.). | Geen bron gevonden bij bijen of hommels. | **Geen bron.** Onze verwachting: buzz en flight hebben allebei een duidelijke toon, dus flatness helpt waarschijnlijk meer bij stap 1 (hommel of ruis) dan bij stap 2. Dit is onze eigen redenering. |
| **Spectral flux** | Hoe snel het spectrum verandert van het ene korte stukje naar het volgende (Meister et al., 2022). | Geen bron gevonden bij bijen of hommels. | **Geen bron.** Een buzz bestaat vaak uit een paar korte trillingen achter elkaar (De Luca & Vallejo-Marín, 2022). Daardoor kan flux bij buzz anders zijn dan bij een vlucht. Dit is onze eigen redenering en moet worden getest. |

**Wat valt op?** Ribeiro et al. (2021) vergeleken ook een aanpak met alleen de grondfrequentie met een aanpak met MFCC. Voor het herkennen van bijensoorten werkte MFCC beter. Arvelos et al. (2025) vonden juist dat de grondfrequentie de belangrijkste feature was om soorten te herkennen. Kawakita & Ichikawa (2019) gebruikten MFCC en grondfrequentie samen. Voor ons project lijkt een combinatie van grondfrequentie en MFCC daarom het meest logisch. Dat is een conclusie over soortherkenning, niet over gedrag, dus we moeten het voor buzz tegenover flight zelf testen.

## Venstergrootte in de bronnen

Bij features zijn er twee soorten "vensters":

- het **frame**: het korte stukje waarop de FFT wordt berekend (meestal tientallen milliseconden);
- het **fragment**: het hele stuk geluid dat één label krijgt (bij ons nu 1 seconde, in lesweek 14 ook 250 en 500 ms).

| Bron | Frame (FFT) | Fragment |
|---|---|---|
| Kawakita & Ichikawa (2019) | 1.024 samples bij 44,1 kHz, met Hamming-venster (ongeveer 23 ms, eigen berekening) | Meeste opnames 0,3 tot 1,0 seconde |
| Heise et al. (2020) | Vensters van 100 ms zonder overlap, voor de harmonic ratio | – |
| Rodríguez Ballesteros et al. (2024) | 4.098 samples bij 48 kHz, 90% overlap, Hann-venster (ongeveer 85 ms, eigen berekening) | Hele vlucht; begin, midden en eind elk ongeveer 10% van de opname |
| Hearon et al. (2025), buzzdetect | YAMNet berekent intern een log-mel-spectrogram | 0,96 seconde, met een nieuw fragment elke 0,48 seconde (TensorFlow, z.d.) |
| Ribeiro et al. (2021) | Standaardinstellingen, niet genoemd | Gemiddeld ongeveer 1,54 seconde |
| librosa, standaard (librosa, z.d.) | n_fft = 2.048 samples, hop = 512 samples (bij 16 kHz: 128 ms en 32 ms, eigen berekening) | – |

**Wat dit betekent voor lesweek 14 (vensters van 250 en 500 ms):**

1. **250 en 500 ms passen bij de literatuur.** De bronnen gebruiken fragmenten tussen 0,3 en ongeveer 1,5 seconde. Heise et al. (2020) werkten zelfs met stukjes van 100 ms. Een buzz duurt gemiddeld ongeveer 0,75 seconde (Vallejo-Marín & Lundgren, 2026), dus een venster van 500 ms valt meestal binnen één buzz. Bij buzzdetect, dat vlieggeluid van insecten herkent, duurde ongeveer de helft van de geluiden rond 1 seconde (Hearon et al., 2025).
2. **Let op het aantal frames.** Met de standaardinstellingen van librosa (frame van 128 ms, stap van 32 ms bij 16 kHz) zitten er in 250 ms ongeveer 8 frames en in 500 ms ongeveer 16 (eigen berekening). Gemiddelden over 8 frames zijn minder stabiel dan over 32 frames in 1 seconde.
3. **Het frame mag niet te kort worden.** Een frame van 2.048 samples bij 16 kHz geeft stappen van ongeveer 7,8 Hz in het spectrum (eigen berekening). Dat is ruim fijn genoeg om 137 Hz (flight) en 313 Hz (buzz) uit elkaar te houden. Een veel korter frame, bijvoorbeeld 256 samples (62,5 Hz per stap), wordt te grof voor de grondfrequentie.
4. **Geen bron heeft vensters vergeleken** voor buzz tegenover flight. Welke lengte het beste werkt, moeten we dus zelf testen.

## Nog controleren (deel 2)

- Fengler et al. (2026): de auteurslijst kon ik niet volledig zien. Controleren of er meer dan vijf auteurs zijn.
- Een overzichtsartikel (Fengler et al., 2026) noemt studies naar insectengeluid die flatness en flux gebruiken, maar ik kon de tabel niet volledig lezen. Als we een bron voor flatness of flux bij insecten willen, is dit een goed startpunt.
- Bij Arvelos et al. (2025) staan de precieze features en vensters in de volledige tekst, die achter een betaalmuur zit.

# Deel 3: advies voor Khaleel (lesweek 13 en 14)

## Vraag

Welke nieuwe features kan Khaleel het beste eerst bouwen, en waarom? Werken ze voor de opnames van 16 kHz én 384 kHz?

## Eerst één afspraak: alles op 16 kHz

Volgens de README worden alle features berekend na omzetten naar 16 kHz (plan van aanpak, 8.3). Mijn advies is om dat bij de nieuwe features ook zo te doen, ook voor de 384 kHz-opnames:

- De grondtonen van buzz en flight liggen onder 500 Hz en de belangrijkste boventonen onder 8 kHz (deel 1). Boven 8 kHz zit dus weinig informatie die we nodig hebben.
- In de EDA verschilden de twee recorders al meer van elkaar dan de klassen (plan van aanpak, 8.3). Als de 384 kHz-opnames extra informatie boven 8 kHz krijgen, wordt dat verschil groter en kan het model de recorder leren herkennen in plaats van het gedrag. Dit is onze eigen redenering.
- Er zijn maar 12 opnames op 384 kHz tegenover 138 op 16 kHz (plan van aanpak, 8.3). Een feature die alleen bij 384 kHz werkt, helpt dus weinig.

Met die afspraak werken alle features hieronder bij beide recorders. In de tabel staat per feature waar je op moet letten.

## Features op volgorde van belang

| Nr. | Feature | Waarom eerst (bron) | 16 kHz | 384 kHz |
|---|---|---|---|---|
| 1 | **Grondfrequentie of dominante frequentie** in de band 100–500 Hz | Het sterkst onderbouwde verschil: buzz ligt bij *B. terrestris* rond 310–365 Hz, flight rond 135–200 Hz (Pritchard & Vallejo-Marín, 2020; Morgan et al., 2016). Bij een buzz is de grondtoon meestal ook de sterkste piek (De Luca & Vallejo-Marín, 2022). Bij soortherkenning was de grondfrequentie de belangrijkste feature (Arvelos et al., 2025). | Ja | Ja, na omzetten naar 16 kHz |
| 2 | **Bandenergie** in een flight-band (ongeveer 120–220 Hz) en een buzz-band (ongeveer 195–400 Hz), plus de **verhouding** tussen die twee | Deze banden gebruikten Switzer & Combes (2016) om de vleugelslag en de buzz te vinden. Een verhouding hangt minder af van de afstand tot de microfoon dan losse energie. Dat laatste is onze eigen redenering: buzz is zachter (Morgan et al., 2016), maar het volume verschilt ook per opname. | Ja | Ja, na omzetten naar 16 kHz |
| 3 | **MFCC** (staan al in de dataset: 20 stuks) | In de bronnen die ik vond de meest gebruikte feature bij bijen; buzz en flight zijn er goed in te onderscheiden (Ribeiro et al., 2021). Kawakita & Ichikawa (2019) combineerden MFCC met de grondfrequentie. Niet opnieuw bouwen, wel opnieuw berekenen op de nieuwe vensters van lesweek 14. | Ja | Ja, alleen als ook deze eerst naar 16 kHz gaan. Anders verschillen de mel-banden per recorder. |
| 4 | **Harmonic ratio** (hoe harmonisch, toonachtig, het geluid is) | Staat niet op de planning, maar Heise et al. (2020) gebruikten dit als belangrijkste feature om hommelgeluid te scheiden van ander geluid. Dat helpt vooral bij stap 1 (hommel of ruis). | Ja | Ja |
| 5 | **Spectral centroid en bandwidth**, berekend op de band onder 1 kHz | Heise et al. (2020) gebruikten centroid en spread onder 400 Hz. Op het hele spectrum zegt de centroid weinig over de grondtoon (deel 1, punt 3). | Ja | Ja |
| 6 | **Spectral flatness** | Meet of iets op ruis of op een toon lijkt (librosa, z.d.). Geen bron bij bijen. Waarschijnlijk vooral nuttig voor stap 1. | Ja | Ja |
| 7 | **Spectral flux** | Meet hoe snel het spectrum verandert (Meister et al., 2022). Geen bron bij bijen. Een buzz bestaat vaak uit korte trillingen achter elkaar (De Luca & Vallejo-Marín, 2022), dus het kan iets toevoegen, maar dat is onze eigen redenering. | Ja | Ja |

**Waarom deze volgorde?** Nummer 1 en 2 hebben de meeste onderbouwing voor buzz tegenover flight. Nummer 3 hebben we al. Nummer 4 en 5 zijn getest bij hommels, maar voor het scheiden van hommel en ruis. Nummer 6 en 7 hebben geen bron bij bijen of hommels. Die zou ik pas bouwen als er tijd over is, en alleen houden als de feature importance van Ahmed (lesweek 14) laat zien dat ze iets toevoegen.

## Tips voor de vensters (lesweek 14)

- Begin met **500 ms**. Een buzz duurt gemiddeld ongeveer 0,75 seconde (Vallejo-Marín & Lundgren, 2026), dus een venster van 500 ms valt meestal binnen één buzz. Daarna 250 ms.
- Houd de FFT-frame lang genoeg voor de grondfrequentie: met 2.048 samples bij 16 kHz zijn de stappen in het spectrum ongeveer 7,8 Hz (eigen berekening, zie deel 2). Dat is ruim genoeg om 137 en 313 Hz uit elkaar te houden.
- Bereken de features bij beide vensterlengtes op dezelfde manier, zodat Gamal de modellen eerlijk kan vergelijken.

## Bronnen

Arvelos, C. A., Resende, C. R., Pereira, J. P. S., Brito, L. C., Duarte, M. A. V., & Brito, V. L. G. de. (2025). Flight and floral acoustic signals for bee species identification. *Neotropical Entomology, 54*, Artikel 105. https://doi.org/10.1007/s13744-025-01315-0

De Luca, P. A., Bussière, L. F., Souto-Vilaros, D., Goulson, D., Mason, A. C., & Vallejo-Marín, M. (2013). Variability in bumblebee pollination buzzes affects the quantity of pollen released from flowers. *Oecologia, 172*(3), 805–816. https://doi.org/10.1007/s00442-012-2535-1

De Luca, P. A., & Vallejo-Marín, M. (2013). What's the 'buzz' about? The ecology and evolutionary significance of buzz-pollination. *Current Opinion in Plant Biology, 16*(4), 429–435. https://doi.org/10.1016/j.pbi.2013.05.002

De Luca, P. A., & Vallejo-Marín, M. (2022). Blooms and buzzing bees: Bridging buzz pollination and biotremology. In P. S. M. Hill, V. Mazzoni, N. Stritih-Peljhan, M. Virant-Doberlet, & A. Wessel (Eds.), *Biotremology: Physiology, ecology, and evolution* (pp. 261–292). Springer. https://doi.org/10.1007/978-3-030-97419-0_11

Fengler, B., Seyidbayli, C., Reinhardt, A., Anders, M., & Westphal, C. (2026). A review of acoustic systems for insect monitoring: From recording technologies to species recognition performance. *Ecological Informatics, 95*, Artikel 103733. https://doi.org/10.1016/j.ecoinf.2026.103733

Hearon, L. E., Johnson, L. H. P., Underwood, J., Lin, C.-H., & Johnson, R. M. (2025). buzzdetect: An open-source deep learning tool for automated bioacoustic pollinator monitoring. *Journal of Insect Science, 25*(6), ieaf104. https://doi.org/10.1093/jisesa/ieaf104

Heise, D., Miller, Z., Wallace, M., & Galen, C. (2020). Bumble bee traffic monitoring using acoustics. In *2020 IEEE International Instrumentation and Measurement Technology Conference (I2MTC)* (pp. 1–6). IEEE. https://doi.org/10.1109/I2MTC43012.2020.9129582

Kawakita, S., & Ichikawa, K. (2019). Automated classification of bees and hornet using acoustic analysis of their flight sounds. *Apidologie, 50*, 71–79. https://doi.org/10.1007/s13592-018-0619-6

librosa. (z.d.). *librosa.feature.spectral_flatness*. Geraadpleegd op 26 november 2026, van https://librosa.org/doc/main/generated/librosa.feature.spectral_flatness.html

Meister, J. A., Nguyen, K. A., & Luo, Z. (2022). Audio feature ranking for sound-based COVID-19 patient detection. In G. Marreiros, B. Martins, A. Paiva, B. Ribeiro, & A. Sardinha (Eds.), *Progress in artificial intelligence: EPIA 2022* (Lecture Notes in Computer Science, Vol. 13566, pp. 146–158). Springer.

Miller-Struttmann, N. E., Heise, D., Schul, J., Geib, J. C., & Galen, C. (2017). Flight of the bumble bee: Buzzes predict pollination services. *PLOS ONE, 12*(6), e0179273. https://doi.org/10.1371/journal.pone.0179273

Morgan, T., Whitehorn, P., Lye, G. C., & Vallejo-Marín, M. (2016). Floral sonication is an innate behaviour in bumblebees that can be fine-tuned with experience in manipulating flowers. *Journal of Insect Behavior, 29*(2), 233–241. https://doi.org/10.1007/s10905-016-9553-5

Pritchard, D. J., & Vallejo-Marín, M. (2020). Floral vibrations by buzz-pollinating bees achieve higher frequency, velocity and acceleration than flight and defence vibrations. *Journal of Experimental Biology, 223*(11), jeb220541. https://doi.org/10.1242/jeb.220541

Ribeiro, A. P., da Silva, N. F. F., Mesquita, F. N., Araújo, P. C. S., Rosa, T. C., & Mesquita-Neto, J. N. (2021). Machine learning approach for automatic recognition of tomato-pollinating bees based on their buzzing-sounds. *PLOS Computational Biology, 17*(9), e1009426. https://doi.org/10.1371/journal.pcbi.1009426

Rodríguez Ballesteros, A., Desjonquères, C., Hevia, V., García Llorente, M., Ulloa, J. S., & Llusia, D. (2024). Towards acoustic monitoring of bees: Wingbeat sounds are related to species and individual traits. *Philosophical Transactions of the Royal Society B: Biological Sciences, 379*(1904), 20230111. https://doi.org/10.1098/rstb.2023.0111

Switzer, C. M., & Combes, S. A. (2016). *Bombus impatiens* (Hymenoptera: Apidae) display reduced pollen foraging behavior when marked with bee tags vs. paint. *Journal of Melittology*, (62). https://doi.org/10.17161/jom.v0i62.5679

Switzer, C. M., & Combes, S. A. (2017). Bumblebee sonication behavior changes with plant species and environmental conditions. *Apidologie, 48*(2), 223–233. https://doi.org/10.1007/s13592-016-0467-1

Switzer, C. M., Hogendoorn, K., Ravi, S., & Combes, S. A. (2016). Shakers and head bangers: Differences in sonication behavior between Australian *Amegilla murrayensis* (blue-banded bees) and North American *Bombus impatiens* (bumblebees). *Arthropod-Plant Interactions, 10*, 1–8. https://doi.org/10.1007/s11829-015-9407-7

TensorFlow. (z.d.). *Transfer learning with YAMNet for environmental sound classification*. Geraadpleegd op 26 november 2026, van https://www.tensorflow.org/tutorials/audio/transfer_learning_audio

Vallejo-Marín, M., & Lundgren, A. (2026). Gradual pollen release in a buzz-pollinated plant: Investigating pollen presentation theory under bee visitation. *Functional Ecology, 40*(2), 476–485. https://doi.org/10.1111/1365-2435.70189
