# python-cli

Regression test python-cli

## Status

- **Branch:** main
- **Laatste commit:** 2026-04-13T21:25:54+02:00
- **Working tree:** wijzigingen aanwezig
- **Remote:** https://github.com/Jvdbreemen/project-handoff-skill.git

## Stack

- **Talen:** python
- **Runtimes:** python >=3.11
- **Package managers:** pip
- **Frameworks:** -

### Framework details

_geen framework details gedetecteerd_

## Prerequisites

Zorg dat onderstaande tools op je machine staan voordat je begint:

- python >=3.11
- pip

## Setup

```bash
git clone https://github.com/Jvdbreemen/project-handoff-skill.git
cd python-cli
pip install
```

## Environment variables

| Variabele | Status | Gebruikt in |
|-----------|--------|-------------|
| `FIXTURE_API_TOKEN` | REQUIRED | src/fixture_cli/main.py |
| `FIXTURE_BASE_URL` | REQUIRED | src/fixture_cli/main.py |

Kopieer `.env.example` naar `.env` en vul de waarden in. Variabelen gemarkeerd als REQUIRED zijn nodig om het project te draaien.

## Commando's

### Install
```bash
pip install
```

### Build
```bash
# geen build commando gedetecteerd
```

### Run
```bash
# geen run commando gedetecteerd
```

### Test
```bash
# geen test commando gedetecteerd
```

## Directorystructuur

```
python-cli/
├── src/
│   └── fixture_cli/
│       └── main.py
└── pyproject.toml
```

Totaal: 2 bestanden, ~21 regels code.

## Known issues en valkuilen

- TODO/FIXME markers in de code: 0


## Secrets

Deze handoff bevat GEEN echte secrets. `.env`, keys en tokens zijn uitgefilterd. Zie `.env.example` voor de lijst van variabelen die je moet instellen.

## Reproduceren

Draai `./REPRODUCE.sh` voor een geautomatiseerde setup op een schone machine. Het script is idempotent: opnieuw draaien is veilig.

---

Deze handoff is gegenereerd door de project-handoff skill op 2026-04-13 19:44 UTC.
