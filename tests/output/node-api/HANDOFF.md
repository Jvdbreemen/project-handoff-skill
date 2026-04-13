# node-api

Regression test node-api

## Status

- **Branch:** main
- **Laatste commit:** 2026-04-13T21:25:54+02:00
- **Working tree:** wijzigingen aanwezig
- **Remote:** https://github.com/Jvdbreemen/project-handoff-skill.git

## Stack

- **Talen:** javascript
- **Runtimes:** node >=20
- **Package managers:** npm
- **Frameworks:** -

### Framework details

_geen framework details gedetecteerd_

## Prerequisites

Zorg dat onderstaande tools op je machine staan voordat je begint:

- node >=20
- npm

## Setup

```bash
git clone https://github.com/Jvdbreemen/project-handoff-skill.git
cd node-api
```

## Environment variables

| Variabele | Status | Gebruikt in |
|-----------|--------|-------------|
| `API_KEY` | REQUIRED | src/server.js |
| `DATABASE_URL` | REQUIRED | src/server.js |
| `PORT` | REQUIRED | src/server.js |

Kopieer `.env.example` naar `.env` en vul de waarden in. Variabelen gemarkeerd als REQUIRED zijn nodig om het project te draaien.

## Commando's

### Install
```bash
# geen install commando gedetecteerd
```

### Build
```bash
# geen build commando gedetecteerd
```

### Run
```bash
npm run start
npm run dev
```

### Test
```bash
npm run test
```

## Directorystructuur

```
node-api/
├── src/
│   └── server.js
├── README.md
└── package.json
```

Totaal: 3 bestanden, ~19 regels code.

## Known issues en valkuilen

- TODO/FIXME markers in de code: 0


## Secrets

Deze handoff bevat GEEN echte secrets. `.env`, keys en tokens zijn uitgefilterd. Zie `.env.example` voor de lijst van variabelen die je moet instellen.

## Reproduceren

Draai `./REPRODUCE.sh` voor een geautomatiseerde setup op een schone machine. Het script is idempotent: opnieuw draaien is veilig.

---

Deze handoff is gegenereerd door de project-handoff skill op 2026-04-13 19:44 UTC.
