# Agent instructions: python-cli

Deze file is bedoeld voor AI coding agents (Claude Code, Cursor, Cline, Copilot, enz.). Volg de instructies hieronder om dit project op te zetten en eraan te werken.

## Project

Fixture python-cli for skill validation

- **Stack:** python / -
- **Runtime:** python >=3.11
- **Package manager:** pip

## Setup

Draai deze commando's in volgorde:

```bash
git clone https://github.com/Jvdbreemen/project-handoff-skill.git
cd python-cli
pip install
```

Als iets faalt, draai `./REPRODUCE.sh` voor de idempotente fallback.

## Build / test / run

```bash
# install
pip install

# build
# geen build commando gedetecteerd

# run
# geen run commando gedetecteerd

# test
# geen test commando gedetecteerd
```

## Environment variables

Deze env vars zijn nodig (kopieer `.env.example` naar `.env` en vul in):

- `FIXTURE_API_TOKEN`
- `FIXTURE_BASE_URL`

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

- TODO/FIXME markers in code: 0 bekend
- _geen warnings_

## Directorystructuur

```
python-cli/
├── src/
│   └── fixture_cli/
│       └── main.py
└── pyproject.toml
```

## Volgende stap

Lees eerst `HANDOFF.md` voor de mens-leesbare context. Dit AGENTS.md bestand bevat alleen de machine-actionable subset. Voor Claude Code specifiek: zie `CLAUDE.md` als die bestaat.
