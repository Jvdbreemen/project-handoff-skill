# Agent instructions: hugo-site

Deze file is bedoeld voor AI coding agents (Claude Code, Cursor, Cline, Copilot, enz.). Volg de instructies hieronder om dit project op te zetten en eraan te werken.

## Project

Fixture hugo-site for skill validation

- **Stack:** markdown / hugo
- **Runtime:** onbekend
- **Package manager:** -

## Setup

Draai deze commando's in volgorde:

```bash
git clone https://github.com/Jvdbreemen/project-handoff-skill.git
cd hugo-site
```

Als iets faalt, draai `./REPRODUCE.sh` voor de idempotente fallback.

## Build / test / run

```bash
# install
# geen install commando gedetecteerd

# build
hugo

# run
hugo server -D

# test
# geen test commando gedetecteerd
```

## Environment variables

Deze env vars zijn nodig (kopieer `.env.example` naar `.env` en vul in):

- _geen_

## Coding conventies

- Volg de stijl van bestaande code in het project

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
hugo-site/
├── content/
│   └── _index.md
├── README.md
└── hugo.toml
```

## Volgende stap

Lees eerst `HANDOFF.md` voor de mens-leesbare context. Dit AGENTS.md bestand bevat alleen de machine-actionable subset. Voor Claude Code specifiek: zie `CLAUDE.md` als die bestaat.
