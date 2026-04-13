# jimvandenbreemen.nl

Hugo portfolio site van Jim van den Breemen

## Status

- **Branch:** master
- **Laatste commit:** -
- **Working tree:** wijzigingen aanwezig
- **Remote:** geen remote

## Stack

- **Talen:** markdown
- **Runtimes:** hugo >=0.120
- **Package managers:** -
- **Frameworks:** hugo

### Framework details

- **Hugo site titel:** Jim van den Breemen
- **Base URL:** https://jimvandenbreemen.nl/
- **Theme:** `jvdb` (themes/jvdb/)
- **Config file:** `hugo.toml`

## Prerequisites

Zorg dat onderstaande tools op je machine staan voordat je begint:

- hugo >=0.120

## Setup

```bash
# Hugo heeft geen install step; zorg dat 'hugo' in PATH staat
```

## Environment variables

| Variabele | Status | Gebruikt in |
|-----------|--------|-------------|
| _geen env vars gedetecteerd_ | | |

Kopieer `.env.example` naar `.env` en vul de waarden in. Variabelen gemarkeerd als REQUIRED zijn nodig om het project te draaien.

## Commando's

### Install
```bash
# Hugo heeft geen install step; zorg dat 'hugo' in PATH staat
```

### Build
```bash
hugo --minify
```

### Run
```bash
hugo server -D
```

### Test
```bash
# geen test commando gedetecteerd
```

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

Totaal: 256 bestanden, ~1743 regels code.

## Known issues en valkuilen

- TODO/FIXME markers in de code: 0
- WARN: hugo theme 'jvdb' heeft geen README in themes/jvdb/

## Secrets

Deze handoff bevat GEEN echte secrets. `.env`, keys en tokens zijn uitgefilterd. Zie `.env.example` voor de lijst van variabelen die je moet instellen.

## Reproduceren

Draai `./REPRODUCE.sh` voor een geautomatiseerde setup op een schone machine. Het script is idempotent: opnieuw draaien is veilig.

---

Deze handoff is gegenereerd door de project-handoff skill op 2026-04-13 19:24 UTC.
