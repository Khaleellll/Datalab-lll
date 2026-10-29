# Werkwijze: van clonen tot pull request

Stap voor stap, voor Mac en Windows. Waar de commando's verschillen, staan ze apart. Op Windows gebruik je **PowerShell** of **Git Bash**; de git- en uv-commando's zijn hetzelfde.

## 1. Eenmalig: programma's installeren

### Git

- **Mac:** open Terminal en typ `git --version`. Als git er nog niet is, vraagt macOS om de "Command Line Tools" te installeren; klik op Installeer.
- **Windows:** download en installeer [Git for Windows](https://git-scm.com/download/win). Laat de standaardinstellingen staan. Daarmee krijg je ook Git Bash.

Stel daarna je naam en e-mail in (hetzelfde e-mailadres als op GitHub):

```bash
git config --global user.name "Voornaam Achternaam"
git config --global user.email "jij@voorbeeld.nl"
```

### uv

- **Mac** (Terminal):

  ```bash
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```

- **Windows** (PowerShell):

  ```powershell
  powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
  ```

Sluit de terminal en open hem opnieuw. Controleer met `uv --version`.

Python hoef je niet zelf te installeren: uv haalt automatisch Python 3.13 op (zie `.python-version`).

## 2. Eenmalig: de repo clonen

Ga naar de map waarin je wilt werken en clone de repo:

```bash
git clone https://github.com/Khaleellll/Datalab-lll.git
cd Datalab-lll
```

Vraag Khaleel om toegang als je nog geen lid bent van de repo op GitHub.

## 3. Eenmalig: de omgeving opzetten met uv

In de map `Datalab-lll`:

```bash
uv sync
uv run nbstripout --install --attributes .gitattributes
```

- `uv sync` maakt de map `.venv` met Python en alle packages uit `uv.lock`. Iedereen heeft zo precies dezelfde versies. `.venv` staat niet in git.
- `nbstripout --install` zorgt dat git de outputs van notebooks weglaat bij een commit. Dit moet **in elke clone één keer**, omdat de instelling lokaal in `.git/config` staat.

Controleer met `uv run nbstripout --status`. Daar moet `nbstripout is installed` staan.

## 4. Eenmalig: de data op de juiste plek zetten

De data staat in het Teams-kanaal van het Horti-Sensor cluster, niet in git. Download de mappen en zet ze in `data/`:

```
Datalab-lll/
└── data/
    ├── raw_data/            # 150 WAV-bestanden
    ├── raw_labels/          # buzzdetection_labels.csv
    └── processed_data/      # bee_features_per_second.csv
```

- **Mac:** sleep de mappen in Finder naar `Datalab-lll/data/`.
- **Windows:** sleep de mappen in Verkenner naar `Datalab-lll\data\`.

Controleer daarna met `git status`. Er mag **niets** uit `data/` verschijnen. Zie je toch WAV- of CSV-bestanden, commit dan niets en vraag het in de groep.

## 5. Elke taak: van branch tot pull request

### a. Begin met de nieuwste versie van `main`

```bash
git switch main
git pull
uv sync            # alleen nodig als iemand packages heeft toegevoegd, maar kan geen kwaad
```

### b. Maak een branch voor je taak

Naam: `taak/korte-omschrijving`, in kleine letters met koppeltekens.

```bash
git switch -c taak/fix-dubbele-rijen
```

### c. Werk en commit

Werk aan je taak. Draai code altijd via uv, vanuit de hoofdmap:

```bash
uv run preprocess
uv run jupyter notebook
```

In VS Code kies je bij een notebook rechtsboven de kernel `.venv` (Python 3.13).

Kijk wat er veranderd is en voeg alleen de bestanden toe die bij je taak horen:

```bash
git status
git add src/preprocessdata.py notebooks/mijn_analyse.ipynb
git commit -m "Dubbele rijen in preprocessdata.py verwijderd"
```

Gebruik liever geen `git add .`, zodat je niet per ongeluk iets meeneemt wat er niet in hoort.

Heb je een package nodig? Voeg het toe met uv en commit beide bestanden:

```bash
uv add scipy
git add pyproject.toml uv.lock
```

### d. Push je branch

De eerste keer:

```bash
git push -u origin taak/fix-dubbele-rijen
```

Daarna is `git push` genoeg.

### e. Open een pull request

1. Ga naar de repo op GitHub. Bovenaan staat een melding over je branch; klik op **Compare & pull request**.
2. Controleer dat **base** `main` is en **compare** jouw branch.
3. Vul het template in: Wat, Waarom, Hoe getest, checklist.
4. Kies rechts bij **Reviewers** minstens één teamgenoot.
5. Klik op **Create pull request**.

### f. Review en merge

- De reviewer leest de wijzigingen en kiest **Approve** of **Request changes**.
- Moet er iets anders? Pas het aan op dezelfde branch, commit en `git push`. De PR wordt vanzelf bijgewerkt.
- Na goedkeuring klik je op **Merge pull request** en daarna op **Delete branch**.

### g. Opruimen

```bash
git switch main
git pull
git branch -d taak/fix-dubbele-rijen
```

## 6. Je branch bijwerken als `main` veranderd is

Als een ander tijdens jouw taak iets in `main` heeft gemerged:

```bash
git switch main
git pull
git switch taak/fix-dubbele-rijen
git merge main
```

Bij een conflict geeft git aan in welke bestanden het zit. Los het daar op (VS Code helpt hierbij), en daarna:

```bash
git add <bestand>
git commit
git push
```

## 7. Veelvoorkomende problemen

| Probleem | Oplossing |
|---|---|
| `uv: command not found` | Open een nieuwe terminal na het installeren van uv. |
| `FileNotFoundError` voor een bestand in `data/` | Controleer of de mappen precies `data/raw_data`, `data/raw_labels` en `data/processed_data` heten. Draai scripts vanuit de hoofdmap; notebooks vanuit `notebooks/`. |
| Notebook vindt een package niet | Kies de kernel uit `.venv` en draai `uv sync`. |
| Je hebt per ongeluk op `main` gewerkt (nog niet gecommit) | `git switch -c taak/naam`: je wijzigingen gaan mee naar de nieuwe branch. |
| Er staat data in `git status` | Niet committen. Controleer `.gitignore` en vraag het in de groep. |
| Windows: waarschuwingen over `LF will be replaced by CRLF` | Die zijn onschuldig. Git for Windows regelt de regeleinden. |
