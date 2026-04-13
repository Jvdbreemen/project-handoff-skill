# Agent instructions: jimvandenbreemen.nl

Deze file is bedoeld voor AI coding agents (Claude Code, Cursor, Cline, Copilot, enz.). Volg de instructies hieronder om dit project op te zetten en eraan te werken.

## Project

Hugo portfolio site van Jim van den Breemen

- **Stack:** markdown / hugo
- **Runtime:** hugo >=0.120
- **Package manager:** -

### Framework details

- **Hugo site titel:** Jim van den Breemen
- **Base URL:** https://jimvandenbreemen.nl/
- **Theme:** `jvdb` (themes/jvdb/)
- **Config file:** `hugo.toml`

## Setup

Draai deze commando's in volgorde:

```bash
# Hugo heeft geen install step; zorg dat 'hugo' in PATH staat
```

Als iets faalt, draai `./REPRODUCE.sh` voor de idempotente fallback.

## Build / test / run

```bash
# install
# Hugo heeft geen install step; zorg dat 'hugo' in PATH staat

# build
hugo --minify

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
- WARN: hugo theme 'jvdb' heeft geen README in themes/jvdb/

## Directorystructuur

```
jimvandenbreemen.nl/
├── archetypes/
│   ├── default.md
│   ├── foto.md
│   ├── media.md
│   └── tekst.md
├── assets/
├── content/
│   ├── foto/
│   │   ├── benny-sings/
│   │   ├── chernobyl/
│   │   └── _index.md
│   ├── media/
│   │   ├── geopolitiek-audio/
│   │   └── _index.md
│   ├── over/
│   │   └── _index.md
│   ├── tekst/
│   │   ├── benny-sings-zonnehuis/
│   │   ├── iftar-windesheim/
│   │   ├── interview-shindar/
│   │   ├── interview-thijs/
│   │   ├── privacy-column/
│   │   └── _index.md
│   └── woordenweb/
│       └── index.md
├── data/
├── design/
│   ├── Cowork's bit/
│   │   ├── claude-skills/
│   │   ├── img/
│   │   ├── thijs-assets/
│   │   ├── versies/
│   │   ├── CC-HANDOFF-PROMPT.md
│   │   ├── DESIGN-HANDOFF-CC.md
│   │   ├── HANDOFF-WOORDENWEB-PRETEXT.md
│   │   ├── IMMERSIVE-INTERVIEW-FRAMEWORK.md
│   │   ├── MASTER-BUNDLE-jimvandenbreemen.md
│   │   ├── SITE-IDEAS.md
│   │   ├── Top 8 Claude Skills for UI_UX Engineers _ Snyk.html
│   │   ├── V10-VERBETERPLAN.md
│   │   └── ... (32 more)
│   ├── demo-woordenweb/
│   │   ├── index.html
│   │   ├── poems.json
│   │   ├── woordenweb.css
│   │   └── woordenweb.js
│   ├── claude-code-prompt-hugo-theme.md
│   ├── files.zip
│   ├── hugo-site-architectuur.md
│   ├── hugo-theme-briefing.md
│   └── site-curatie-handleiding.md
├── i18n/
├── layouts/
├── static/
│   ├── data/
│   │   └── wordweb.json
│   ├── fonts/
│   │   ├── Wavehaus-128Bold.woff2
│   │   ├── Wavehaus-158ExtraBold.woff2
│   │   ├── Wavehaus-28Thin.woff2
│   │   ├── Wavehaus-42Light.woff2
│   │   ├── Wavehaus-66Book.woff2
│   │   └── Wavehaus-95SemiBold.woff2
│   └── robots.txt
├── themes/
│   └── jvdb/
│       ├── assets/
│       ├── layouts/
│       └── static/
├── CC-TAKEN.md
├── CLAUDE.md
├── HANDOFF.md
└── ... (2 more)
```

## Volgende stap

Lees eerst `HANDOFF.md` voor de mens-leesbare context. Dit AGENTS.md bestand bevat alleen de machine-actionable subset. Voor Claude Code specifiek: zie `CLAUDE.md` als die bestaat.
