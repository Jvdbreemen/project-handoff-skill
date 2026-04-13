# Handoff-map specificatie

Dit document legt vast welke bestanden de skill produceert en welke secties elk bestand bevat. Alle latere taken (inspectiescript, templates, SKILL.md) verwijzen hiernaar.

## Map-structuur

```
handoff/
├── HANDOFF.md            verplicht, mens-entrypoint
├── AGENTS.md             verplicht, agent-entrypoint (standaard)
├── CLAUDE.md             optioneel, Claude Code specifiek
├── REPRODUCE.sh          verplicht, scripted setup
├── .env.example          verplicht als env vars gedetecteerd
├── inventory.json        verplicht, machine-leesbare inspectie-output
└── architecture.md       optioneel, bij complexe codebases
```

## HANDOFF.md (mens)

Doel: een ontwikkelaar die het project nooit heeft gezien kan het binnen 30 minuten draaien.

| Sectie | Verplicht | Inhoud | Inspectie-metadata |
|--------|-----------|--------|--------------------|
| Titel + 1-zin samenvatting | ja | Wat doet het project, voor wie | uit README + git log |
| Status | ja | actief, bevroren, archief + laatste commit | uit git state |
| Stack | ja | talen, runtimes, frameworks, db, externe services | uit package manifests |
| Prerequisites | ja | system tools + versies die al op machine moeten staan | uit lockfiles + shebangs |
| Setup | ja | stap-voor-stap: clone, install deps, config, seeds | uit package scripts + README |
| Environment variables | ja als env-vars bestaan | lijst met beschrijving + of waarde verplicht is | uit code-scan + .env.example |
| Run / build / test | ja | commando's met wat ze doen | uit package.json, Makefile, pyproject.toml etc |
| Architectuur | optioneel | directorystructuur + dataflow in 1 alinea | uit tree + grote bestanden |
| Known issues / valkuilen | ja | wat werkt wel/niet, TODO markers, open bugs | uit TODO-scan + git issues |
| Externe dependencies | ja als aanwezig | APIs, services, accounts die nodig zijn | uit code-scan |
| Contact | optioneel | auteur of team | uit git log |

## AGENTS.md (agent-entrypoint, platform-agnostisch)

Doel: een AI agent zonder context kan het project direct oppakken en eraan verder werken.

Sectie-structuur volgt [agents.md](https://agents.md/):

```markdown
# Agent instructions

## Project
Kort: wat, waarvoor, welke stack.

## Setup
Exacte commando's voor install en eerste run.

## Build / test / run
Commando's, een per regel, machine-copy-paste.

## Coding conventies
Indent, line length, tools (linter, formatter). Detecteerbaar uit configs.

## Wat niet te doen
Geen framework-migraties, geen dependency-upgrades, geen files deleten buiten scope.

## Waar op te letten
Bekende valkuilen, legacy code zones, generated files.
```

Regels voor de inhoud:

- Alles wat een mens impliciet weet moet hier letterlijk staan
- Commando's in fenced blocks met shell-type
- Geen vage instructies ("doe het goed"), altijd concreet
- Korter is beter maar niet ten koste van volledigheid
- Bron: AGENTS.md convention (open format)

## CLAUDE.md (optioneel, Claude Code specifiek)

Alleen genereren als de doeluser Claude Code gebruikt. Bevat:

- Verwijzing naar AGENTS.md als baseline
- Claude-specifieke zaken: welke skills/tools gebruiken, welke hooks actief zijn, welke MCP-servers nodig
- Backlog.md afspraken als project Backlog gebruikt

## REPRODUCE.sh

Doel: op een schone machine het project draaiend krijgen met 1 commando.

Structuur:

```bash
#!/usr/bin/env bash
set -euo pipefail

# 1. Prerequisites check
# 2. Clone of cd
# 3. Install runtime (via mise als beschikbaar)
# 4. Install dependencies
# 5. Config (.env copy, placeholders waarschuwen)
# 6. Smoke-test commando
# 7. Print next steps
```

Regels:

- Idempotent: tweede keer draaien mag niks breken
- Elke stap logt wat het doet
- Fail-fast met duidelijke error messages
- Geen hardcoded paths (gebruik `$(dirname "$0")`)

## .env.example

Gegenereerd uit code-scan (grep naar `process.env.FOO`, `os.getenv("FOO")`, `ENV["FOO"]` patronen).

Regels:

- Een variabele per regel
- Comment erboven met waar het gebruikt wordt en waarvoor
- Nooit echte waarden, alleen placeholders of lege string
- Duidelijk aangeven welke verplicht zijn (`# REQUIRED` comment)

## inventory.json

Machine-leesbare output van het inspectiescript. Schema:

```json
{
  "project": {
    "name": "string",
    "path": "string",
    "git": {
      "remote": "string|null",
      "branch": "string",
      "last_commit": "iso8601",
      "clean": "boolean"
    }
  },
  "stack": {
    "languages": ["string"],
    "runtimes": [{"name": "string", "version": "string"}],
    "package_managers": ["string"],
    "frameworks": ["string"]
  },
  "scripts": {
    "install": ["string"],
    "build": ["string"],
    "test": ["string"],
    "run": ["string"]
  },
  "env_vars": [{"name": "string", "required": "boolean", "used_in": ["string"]}],
  "dependencies": {
    "runtime": [{"name": "string", "version": "string"}],
    "dev": [{"name": "string", "version": "string"}]
  },
  "structure": {
    "tree_depth_3": "string",
    "file_count": "number",
    "loc_estimate": "number"
  },
  "issues": {
    "todos": "number",
    "warnings": ["string"]
  }
}
```

## Secrets-regels (kritiek)

De skill mag NOOIT de volgende bestanden of inhoud opnemen:

- `.env`, `.env.local`, `.env.*` (behalve `.env.example`)
- `*.key`, `*.pem`, `*.p12`, `*.pfx`
- `id_rsa*`, `id_ed25519*`, `*.crt`
- `credentials.json`, `service-account*.json`
- Bestanden met `token`, `secret`, `password`, `apikey` in de naam
- Inhoud van bestanden die matchen op regex: `(api[_-]?key|secret|token|password|bearer)\s*[:=]\s*['"]?[A-Za-z0-9+/=_-]{16,}`

Als het inspectiescript een potentieel secret detecteert: flag in `inventory.json` als warning, exclude uit output, log naar stderr.

## Volledigheidscriteria

Een handoff-map is compleet als:

1. Alle verplichte bestanden bestaan
2. `REPRODUCE.sh` draait zonder errors op schone machine (getest in agent-test fase)
3. `inventory.json` valideert tegen schema
4. Geen secrets lekken (automatisch gecheckt)
5. AGENTS.md bevat minimaal de 6 standaardsecties

Dit is de meetlat voor TASK-8 (GREEN test) en TASK-11 (agent-test).
