# Agent instructions: project-handoff-skill

Deze file is bedoeld voor AI coding agents (Claude Code, Cursor, Cline, Copilot, enz.). Volg de instructies hieronder om dit project op te zetten en eraan te werken.

## Project

Claude Code skill die project handoff folders genereert voor mens en AI-agent

- **Stack:** python / -
- **Runtime:** python >=3.10
- **Package manager:** none (bare scripts)

### Framework details

_geen framework details gedetecteerd_

## Setup

Draai deze commando's in volgorde:

```bash
git clone https://github.com/Jvdbreemen/project-handoff-skill.git
cd project-handoff-skill
# Geen package manifest; zorg dat python3 >=3.10 in PATH staat
```

Als iets faalt, draai `./REPRODUCE.sh` voor de idempotente fallback.

## Build / test / run

```bash
# install
# Geen package manifest; zorg dat python3 >=3.10 in PATH staat

# build
# geen build commando gedetecteerd

# run
# geen run commando gedetecteerd

# test
# geen test commando gedetecteerd
```

## Environment variables

Deze env vars zijn nodig (kopieer `.env.example` naar `.env` en vul in):

- _geen_

## Coding conventies

- PEP 8, 4-space indent, type hints waar mogelijk
- f-strings voor string formatting

## Wat niet te doen

- Verwijder of hernoem bestanden buiten de scope van je taak
- Doe geen framework-migraties of major dependency-upgrades zonder opdracht
- Commit geen secrets: `.env`, keys, tokens horen niet in git
- Bypass geen pre-commit hooks met `--no-verify`
- Maak geen nieuwe branches zonder te vragen

## Waar op te letten

- TODO/FIXME markers in code: 5 bekend
- _geen warnings_

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

## Volgende stap

Lees eerst `HANDOFF.md` voor de mens-leesbare context. Dit AGENTS.md bestand bevat alleen de machine-actionable subset. Voor Claude Code specifiek: zie `CLAUDE.md` als die bestaat.
