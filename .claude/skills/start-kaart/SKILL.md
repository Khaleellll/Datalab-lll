---
name: start-kaart
description: Begin aan een Trello-kaart van het hommelproject. Lees de kaart en de bronnen erbij, stel een plan voor, en maak pas na akkoord de branch en zet de kaart op In progress.
argument-hint: "<link naar de Trello-kaart, of het kaartnummer zoals #12>"
disable-model-invocation: true
---

# Begin aan een kaart

Invoer: `$ARGUMENTS`. Dat is een link naar een kaart (voorkeur), het kaartnummer (`#12`) of een deel
van de naam.
Draai dit het liefst in **plan mode**. Stap 1 tot en met 4 lezen alleen; er verandert niets tot een
mens akkoord geeft.

## Het bord

Bord: https://trello.com/b/nBwBFtpd/bumbble-bee

- Iedereen heeft een eigen lijst: **To Do Malak**, **To Do Ahmed**, **To Do Khaleel**,
  **To Do Tonna** en **To Do Gamal**.
- Daarna gaat een kaart naar **In progress**, dan naar **For Review** (als de PR open staat) en na
  de merge naar **Done week N**, met N de lesweek. Dat laatste doet Khaleel.
- In **Wachten op** staan dingen waar we op Sam of een ander wachten. Daar begin je niet aan.

## Opbouw van een kaart

```
<één tot drie zinnen: wat en waarom>

**Bron:** docs/planning.md lesweek 12; plan van aanpak hoofdstuk 6
**Hangt af van:** <naam van een andere kaart, of "niets">
**Buiten scope:** <wat er niet bij hoort>
**Tijd:** ca. 1,5 uur
**Branch:** taak/xgboost-baseline
**Reviewer:** Ahmed (GitHub: `AhmedBashabeeb`)
```

Met een checklist **Acceptatiecriteria**: elk punt is iets wat je met een controle kunt aantonen.

Overlegkaarten, zoals de afspraak met Sam, en reviewkaarten (`Review: PR's van <naam>`) zijn niet
voor deze skill bedoeld.

## Reviewers

Vast voor het hele project. De **Reviewer** op de kaart komt uit deze tabel:

| Werk van | Reviewer | GitHub-naam reviewer |
|---|---|---|
| Khaleel | Gamal | `Gamal-alsa2026` |
| Gamal | Ahmed | `AhmedBashabeeb` |
| Ahmed | Tonna | `25154133` |
| Tonna | Malak | `malakje` |
| Malak | Khaleel | `Khaleellll` |

## Fase 1: plan (alleen lezen)

1. **De kaart lezen.**
   - Link: lees de kaart met `trelloReadCard`, actie `get`. Daar staan de titel, de beschrijving, de
     checklist **Acceptatiecriteria** en de comments.
   - Naam: zoek de kaart met `trelloSearch`, actie `search_cards`, op het bord van het hommelproject.
   - Nummer: het nummer staat in de link van de kaart (`/c/<code>/12-...`). Haal de kaarten op met
     `trelloReadCard`, actie `list_by_board`, en zoek de link die met dat nummer begint.
   - Zijn er geen Trello-tools, of mislukt het lezen? Vraag de mens dan om de beschrijving en de
     checklist te plakken. Niet raden.
   - Staat de kaart in **Wachten op** of in de lijst van iemand anders? Meld dat eerst.
   - Ontbreken de acceptatiecriteria? Stel ze dan zelf voor in het plan; de mens beslist.
2. **De context lezen.** Lees alleen wat de kaart bij **Bron** noemt:
   - het blok van de genoemde lesweek in `docs/planning.md`, en de afspraken voor het modelleren;
   - `docs/besluiten-*.md` voor besluiten van Sam;
   - het plan van aanpak alleen als de kaart een hoofdstuk noemt. Het is een Word-bestand; lees het
     op een Mac met
     `textutil -convert txt -stdout docs/Plan_van_Aanpak_DataLab_III_Hommelgeluid_versie3.docx`.

   Hangt de kaart af van een kaart die nog niet in Done staat? Zeg dat.
3. **Kijken wat er al is.**
   - Zoek in `src/`, `notebooks/` en `docs/` naar code, notebooks en tekst die je kunt uitbreiden.
     Zo maak je niets dubbel.
   - Draai `gh pr list` en kijk of een open PR dezelfde bestanden raakt. Dan kun je straks een
     conflict krijgen. Werkt `gh` niet? Gebruik dan `git fetch origin` en `git branch -r`.
4. **Een plan voorstellen, en dan stoppen voor akkoord.** Het plan bevat:
   - elk acceptatiecriterium, uitgeschreven als een of meer controles;
   - de bestanden die je maakt of wijzigt, per map: `src/`, `notebooks/`, `docs/`;
   - wijzigingen in `src/preprocessdata.py`, apart vermeld. Dat script maakt de featurebestanden
     voor iedereen;
   - nieuwe packages, met reden. Die voeg je toe met `uv add`; dan veranderen `pyproject.toml` en
     `uv.lock`;
   - bij modellen: hoe je splitst. Altijd per opname (`StratifiedGroupKFold` op `source_file`), ook
     binnen de grid search. De testset raak je niet aan, behalve in de eindevaluatie;
   - de branchnaam. Gebruik de **Branch** van de kaart; staat die er niet, kies dan
     `taak/korte-omschrijving`, met kleine letters en streepjes;
   - de reviewer. Gebruik de **Reviewer** van de kaart; staat die er niet, neem dan de reviewer uit
     de tabel bij Reviewers;
   - open vragen. Vragen over inhoud of over wat Sam wil, gaan naar de mens. Beslis die nooit zelf.
     Wijk je af van de normen in paragraaf 6.4 van het plan, zeg dat dan expliciet.

## Fase 2: na akkoord

5. **Branch maken** vanaf de nieuwste `main`:
   `git switch main && git pull && git switch -c <branch>`.
   Staan er wijzigingen die nog niet gecommit zijn? Stop dan en vraag wat ermee moet.
6. **De kaart bijwerken.** Lukt dat niet in Trello, vraag de mens dan om het met de hand te doen.
   - Zet de kaart op **In progress**: `trelloWriteCard`, actie `move`. Het id van de lijst vind je
     met `trelloReadList`, actie `list_by_board`.
   - Plaats een comment met `trelloWriteCard`, actie `comment`: `Gestart op branch <branch>.`, met
     het afgesproken plan in 3 tot 6 punten.
7. **Bouwen.**
   - Draai alles via uv, vanuit de hoofdmap: `uv run ...`.
   - Paden naar data zijn relatief: `data/...` vanuit de root, `../data/...` vanuit een notebook.
   - Werk je in Google Colab, bijvoorbeeld voor een grid search? Zet het notebook daarna terug in
     `notebooks/`, met paden die ook lokaal werken.
   - Vink een acceptatiecriterium op de kaart pas af als het werk ervoor er is:
     `trelloWriteChecklist`, actie `update_item`.
8. **Controleren**:
   - Een notebook draait van boven naar beneden zonder fouten:
     `uv run jupyter nbconvert --to notebook --execute <notebook> --output-dir <tijdelijke map>`.
     Duurt dat te lang, bijvoorbeeld door een grid search? Zeg dat, en zeg welke cellen je wel
     hebt gedraaid.
   - Code in `src/` start zonder fouten: `uv run python -m py_compile src/*.py`.
   - `git status` toont geen bestanden uit `data/`, geen WAV en geen CSV.
   - `uv run nbstripout --status` zegt dat nbstripout is geïnstalleerd.
9. **Afronden.**
   - Laat de mens de wijzigingen zien met `git diff`.
   - Commit pas na akkoord. Schrijf het bericht in het Nederlands, kort en beschrijvend.
   - Push de branch en open een PR met het sjabloon uit `.github/pull_request_template.md`. Voeg de
     reviewer meteen toe: `gh pr create ... --reviewer <github-naam van de Reviewer>`.
   - Zet de kaart daarna op **For Review**, met een comment met de link naar de PR.

## Regels

- Maak nooit zelf nieuwe kaarten. Vind je vervolgwerk of iets wat ontbreekt? Zet het als comment op
  deze kaart en meld het aan de mens; die beslist of het een kaart wordt.
- Blijf binnen de kaart. Wat onder **Buiten scope** staat, bouw je niet.
- Commit nooit data (zie `CLAUDE.md`).
- Push nooit naar `main`, merge nooit zelf en zet een kaart nooit op Done. Dat doet Khaleel na de
  review door een teamgenoot.
