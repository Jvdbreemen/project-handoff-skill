# project-handoff-skill

Claude Code skill die project handoff folders genereert voor mens en AI-agent

## Status

- **Branch:** main
- **Laatste commit:** 2026-04-13T21:44:32+02:00
- **Working tree:** wijzigingen aanwezig
- **Remote:** https://github.com/Jvdbreemen/project-handoff-skill.git

## Stack

- **Talen:** python
- **Runtimes:** python >=3.10
- **Package managers:** none (bare scripts)
- **Frameworks:** -

### Framework details

_geen framework details gedetecteerd_

## Prerequisites

Zorg dat onderstaande tools op je machine staan voordat je begint:

- python >=3.10
- none (bare scripts)

## Setup

```bash
git clone https://github.com/Jvdbreemen/project-handoff-skill.git
cd project-handoff-skill
# Geen package manifest; zorg dat python3 >=3.10 in PATH staat
```

## Environment variables

| Variabele | Status | Gebruikt in |
|-----------|--------|-------------|
| _geen env vars gedetecteerd_ | | |

Kopieer `.env.example` naar `.env` en vul de waarden in. Variabelen gemarkeerd als REQUIRED zijn nodig om het project te draaien.

## Commando's

### Install
```bash
# Geen package manifest; zorg dat python3 >=3.10 in PATH staat
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
project-handoff-skill/
├── backlog/
│   ├── archive/
│   ├── completed/
│   ├── decisions/
│   ├── docs/
│   ├── drafts/
│   ├── milestones/
│   ├── tasks/
│   └── config.yml
├── docs/
│   ├── handoff-spec.md
│   └── research.md
├── handoff/
│   ├── AGENTS.md
│   ├── CLAUDE.md
│   ├── HANDOFF.md
│   ├── REPRODUCE.sh
│   └── inventory.json
├── scripts/
│   ├── handoff_inspect.py
│   └── render_handoff.py
├── skills/
│   └── project-handoff/
├── templates/
│   ├── AGENTS.md.tmpl
│   ├── CLAUDE.md.tmpl
│   ├── HANDOFF.md.tmpl
│   ├── REPRODUCE.sh.tmpl
│   └── env.example.tmpl
├── tests/
│   ├── dogfood/
│   ├── fixtures/
│   ├── output/
│   ├── scenarios/
│   ├── agent-test.md
│   ├── baseline-results.md
│   ├── dogfood.md
│   └── refactor-notes.md
├── LICENSE
├── PLAN.md
└── README.md
```

Totaal: 79 bestanden, ~686 regels code.

## Known issues en valkuilen

- TODO/FIXME markers in de code: 5


## Secrets

Deze handoff bevat GEEN echte secrets. `.env`, keys en tokens zijn uitgefilterd. Zie `.env.example` voor de lijst van variabelen die je moet instellen.

## Reproduceren

Draai `./REPRODUCE.sh` voor een geautomatiseerde setup op een schone machine. Het script is idempotent: opnieuw draaien is veilig.

---

Deze handoff is gegenereerd door de project-handoff skill op 2026-04-13 20:07 UTC.
