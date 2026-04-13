# Agent instructions: node-api

Deze file is bedoeld voor AI coding agents (Claude Code, Cursor, Cline, Copilot, enz.). Volg de instructies hieronder om dit project op te zetten en eraan te werken.

## Project

Minimal Express API fixture

- **Stack:** javascript / -
- **Runtime:** node >=20
- **Package manager:** npm

## Setup

Draai deze commando's in volgorde:

```bash
git clone https://github.com/Jvdbreemen/project-handoff-skill.git
cd node-api
```

Als iets faalt, draai `./REPRODUCE.sh` voor de idempotente fallback.

## Build / test / run

```bash
# install
# geen install commando gedetecteerd

# build
# geen build commando gedetecteerd

# run
npm run start
npm run dev

# test
npm run test
```

## Environment variables

Deze env vars zijn nodig (kopieer `.env.example` naar `.env` en vul in):

- `API_KEY`
- `DATABASE_URL`
- `PORT`

## Coding conventies

- ESM-modules, geen CommonJS tenzij het project het al doet
- 2-space indent

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
node-api/
├── src/
│   └── server.js
├── README.md
└── package.json
```

## Volgende stap

Lees eerst `HANDOFF.md` voor de mens-leesbare context. Dit AGENTS.md bestand bevat alleen de machine-actionable subset. Voor Claude Code specifiek: zie `CLAUDE.md` als die bestaat.
