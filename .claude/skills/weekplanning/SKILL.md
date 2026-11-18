---
name: weekplanning
description: Vrijdagreview van het Trello-bord van het hommelproject. Vergelijk het bord met de repo, meld wat niet klopt en stel de kaarten voor volgende week voor, verdeeld over de vijf teamleden. Pas na akkoord van Khaleel komen ze op het bord.
argument-hint: "<optioneel: extra info voor volgende week, bijvoorbeeld 'Tonna is er dinsdag niet'>"
disable-model-invocation: true
---

# Weekreview en planning

Invoer: `$ARGUMENTS`. Dat is optionele extra info voor de volgende week, zoals een afspraak met
Sam, een deadline van school of iemand die er niet is.
Draai dit het liefst in **plan mode**. Stap 1 tot en met 7 lezen alleen; het bord verandert pas na
akkoord van Khaleel.

## Vaste gegevens

- **Bord:** https://trello.com/b/nBwBFtpd/bumbble-bee
- **Team:** Malak Alshehabi, Ahmed Bashabeeb, Khaleel Al-Aqel, Tonna Tekle en Gamal Al-Sabeei.
- **Akkoord:** Khaleel beheert het bord en geeft akkoord.
- **Opdrachtgever:** dr. Sam Aerts. Zijn besluiten staan in `docs/besluiten-<jjjj-mm-dd>.md`.
- **Lijsten:**
  - **Wachten op**: dingen die bij Sam of een ander liggen;
  - **To Do <naam>**: een eigen lijst per teamlid;
  - daarna samen **In progress**, **For Review** en **Done week N**, met N de lesweek.
- **Weken:** we tellen in lesweken. Lesweek 11 is de week van 16-11-2026. De tabel in
  `docs/planning.md` zet elke lesweek naast de data; de kerstvakantie telt niet mee.
- **Einddatum:** het project is af op vrijdag 29-01-2027 (lesweek 19).
- **Tijd:** ieder teamlid werkt 4 uur per week aan het project.
- **Deadlines:** een kaart krijgt een deadline om 23:30 Amsterdamse tijd. Dat is 22:30 UTC in de
  wintertijd en 21:30 UTC in de zomertijd.
- **Vrijdag:** op vrijdag laten we Sam iets nieuws zien. Niet alles hoeft dan af te zijn, wel een
  paar kaarten.

## Fase 1: review (alleen lezen)

1. **Controleren of de tools er zijn.**
   - Zijn `trelloReadList`, `trelloReadCard`, `trelloWriteCard`, `trelloWriteChecklist` en
     `trelloSearch` er niet? Stop dan en meld dat. Zonder bord is er geen review.
   - Werkt `gh` niet? Meld dat. Lees de branches dan met `git fetch origin` en `git branch -r`, en
     sla de controles op PR's over.
2. **De week bepalen.**
   - Zoek de datum van vandaag op met `date`.
   - Zoek in de tabel van `docs/planning.md` de lesweek van nu en de volgende lesweek, met de data
     van maandag tot en met vrijdag.
   - Lees in `docs/planning.md` alleen het blok van de volgende lesweek, en de afspraken voor het
     modelleren.
   - Tel hoeveel lesweken er nog zijn tot 29-01-2027.
   - Valt de volgende week in de kerstvakantie? Doe dan alleen de review en plan geen kaarten.
3. **Het bord lezen.**
   - Haal de lijsten op met `trelloReadList`, actie `list_by_board`. Lees daarna elke lijst apart met
     `trelloReadCard`, actie `list_by_list`; het hele bord in één keer is te groot.
   - Van de Done-lijsten lees je alleen de nieuwste waar kaarten in staan.
   - Bekijk twee of drie recente kaarten om de stijl over te nemen: `trelloReadCard`, actie `get`.
     Let op de naam, de beschrijving, de deadline en de checklist.
4. **De repo lezen.**
   - Wat er sinds vorige vrijdag gebeurd is:
     - `git fetch origin`;
     - `git log origin/main --since=<datum> --format='%h %an %s'`;
     - `gh pr list --state merged --search "merged:>=<datum>" --json number,title,author,headRefName,reviewDecision`.
   - Wat nog open staat: `gh pr list` en `git branch -r`.
   - Het nieuwste `docs/besluiten-*.md`, als dat er is.
   - Het plan van aanpak alleen als je het doel of de normen nodig hebt. Het is een Word-bestand;
     lees het op een Mac met
     `textutil -convert txt -stdout docs/Plan_van_Aanpak_DataLab_III_Hommelgeluid_versie3.docx`.
     Hoofdstuk 4 is het doel, hoofdstuk 5 de fasen en rollen, paragraaf 6.4 de normen.
5. **Bord en repo naast elkaar leggen.** Zoek naar:
   - kaarten in For Review of In progress waarvan de PR al gemerged is;
   - kaarten over hun deadline, en kaarten die nog in To Do staan terwijl het werk al op `main` staat;
   - open PR's zonder kaart, kaarten in For Review zonder PR, en branches zonder PR;
   - commits die direct op `main` staan, en PR's die zonder review gemerged zijn. Dat mag niet
     volgens `CLAUDE.md`;
   - branches die niet heten zoals de afspraak is: `taak/korte-omschrijving`;
   - tegenstrijdigheden. Noemt de beschrijving een ander lid dan de lijst? Past de deadline niet bij
     de beschrijving? Bestaat dezelfde kaart twee keer?
   - acceptatiecriteria die niet zijn afgevinkt terwijl de PR gemerged is;
   - kaarten die al lang in Wachten op staan, zonder dat iemand ernaar vraagt;
   - besluiten van Sam die nergens als kaart staan;
   - achterstand op `docs/planning.md`: hoeveel werk ligt er nog, en haalt het team 29-01-2027 nog?
   - leden op het bord die geen teamlid zijn. Meld dat als vraag, niet als fout.
6. **De planning voor volgende week maken.**
   - **Bronnen:**
     - het blok van de volgende lesweek in `docs/planning.md`;
     - de besluiten van Sam;
     - werk dat is blijven liggen;
     - de extra info uit `$ARGUMENTS`.
   - **Tijd:**
     - Geef elke kaart een schatting in uren.
     - Per persoon is er 4 uur per week. Tel de kaarten mee die nog in To Do of In progress staan.
     - Past het niet? Schuif werk door naar een volgende week, en zeg wat dat betekent voor
       29-01-2027.
   - **Verdelen:**
     - Geef werk aan wie iets vergelijkbaars eerder deed. Dat zie je aan de leden in de Done-lijsten
       en aan de auteurs van PR's en commits. Twijfel je? Kijk dan naar de aandachtsgebieden in de
       README.
     - Kaarten die dezelfde bestanden raken, krijgt één persoon. Zo voorkom je mergeconflicten.
     - Houd de belasting per persoon gelijk: iedereen ongeveer 4 uur.
   - **Volgorde:** wat moet maandag vastliggen zodat anderen verder kunnen? Leg de afhankelijkheden
     vast, en zet de deadlines zo dat dat werk op tijd klaar is.
   - **Vrijdag:** kies minstens twee kaarten met iets wat je Sam kunt laten zien, zoals een grafiek,
     een score of een stuk tekst. Zet hun deadline op donderdag 23:30.
   - **Kaarten die op het werk van anderen wachten:** denk aan een antwoord of akkoord van Sam.
     Daarvoor komt een kaart in Wachten op.
7. **Stoppen en voorleggen.** Laat zien:
   - **De review:** elke fout of elk raar ding, met wat Khaleel eraan kan doen;
   - **De nieuwe kaarten per persoon:** naam, deadline, uren en een korte inhoud;
   - **Wijzigingen in bestaande kaarten**, als die nodig lijken. Alleen als voorstel;
   - **Wijzigingen in `docs/planning.md`**, als het team achterloopt. Alleen als voorstel;
   - **Wat Sam moet beslissen.**

   Vragen over inhoud of verdeling stel je met AskUserQuestion. Beslis ze niet zelf.

## Fase 2: na akkoord

8. **Kaarten maken** met `trelloWriteCard`, actie `create`, onderaan in de lijst **To Do <naam>**
   (`pos: "bottom"`).
   - **Werkkaarten** (code, notebook of tekst voor het rapport) krijgen de opbouw die
     `/start-kaart` leest:

     ```
     <één tot drie zinnen: wat en waarom>

     **Bron:** <docs/planning.md lesweek N; plan van aanpak hoofdstuk N; docs/besluiten-...>
     **Hangt af van:** <naam van een andere kaart, of "niets">
     **Buiten scope:** <wat er niet bij hoort>
     **Tijd:** ca. <N> uur
     **Branch:** taak/<korte-omschrijving>
     ```

     Laat **Branch** weg als het werk niet in de repo komt.
     Daarnaast krijgen ze een checklist **Acceptatiecriteria**: maak die met `trelloWriteChecklist`,
     actie `create`, en voeg de punten toe met `add_item` (`pos` 1, 2, 3...). Elk punt kun je met
     een controle aantonen.
   - **Overlegkaarten**, zoals de afspraak met Sam of een retrospective, krijgen één tot drie
     zinnen en geen checklist.
   - **Kaarten in Wachten op** krijgen alleen een naam, zonder deadline.
9. **Bestaande kaarten** pas je alleen aan als Khaleel die kaart in zijn akkoord noemt, en dan
   alleen het veld dat hij noemt. Verplaats, archiveer of rond niets af zonder dat hij erom vraagt.
10. **Controleren.** Lees de lijsten opnieuw met `trelloReadCard`, actie `list_by_list`.
    - Staat elke nieuwe kaart in de juiste lijst, met de juiste deadline en checklist?
    - Zijn de bestaande kaarten ongewijzigd, op de afgesproken wijzigingen na?
11. **Afsluiten.** Geef in je antwoord:
    - een tabel per persoon met de nieuwe kaarten, hun deadline en de uren;
    - wat Khaleel zelf nog moet doen. Leden kun je niet toevoegen via de Trello-tool, dus dat moet
      hij met de hand doen. Ook kaarten verplaatsen die je in de review noemde, hoort hierbij;
    - de open vragen voor Sam.

## Regels

- Plan alleen de volgende week, maar houd 29-01-2027 in het oog.
- Deze skill wijzigt geen bestanden in de repo en commit niets. Hij gaat alleen over het bord.
