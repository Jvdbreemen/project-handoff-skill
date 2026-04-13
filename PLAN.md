# Plan: project-handoff skill

## Doel

Een Claude Code skill die een projectdirectory inspecteert en een zelfstandige handoff-map produceert. Met die map moet zowel een mens als een AI-agent (Claude Code, Cowork) het project zonder aanvullende uitleg kunnen reproduceren, opstarten en eraan verder werken.

## Scope

### In scope
- Automatische inspectie van een projectdirectory (package managers, runtimes, env vars, services, build/run/test commando's, git-state, architectuur)
- Genereren van een HANDOFF-map met:
  - `HANDOFF.md` voor mensen (prerequisites, install, config, run, architectuur, bekende valkuilen)
  - `CLAUDE.md` of vergelijkbaar agent-entrypoint zodat een AI-agent het project direct kan oppakken
  - `.env.example` (zonder secrets) uit code-scan
  - `REPRODUCE.sh` of gelijkwaardig script voor schone-machine setup
- Secrets-safeguard: nooit `.env`, keys, tokens, credentials meenemen. Wel flaggen waar ze nodig zijn
- Dogfood op echt project van Jim (bijv. `jimvandenbreemen.nl` of `ideeen/Vault`)

### Out of scope
- Automatische deploy of CI-configuratie
- Vendor lock-in (Docker optioneel, niet verplicht)
- Publiceren van het handoff-document online

## Deliverables

1. `skills/project-handoff/SKILL.md` in deze repo, deploybaar naar `~/.claude/skills/project-handoff/`
2. Inspectie-script (`scripts/inspect.py` of `.sh`) voor auto-detectie
3. Templates: `HANDOFF.md.tmpl`, `CLAUDE.md.tmpl`, `REPRODUCE.sh.tmpl`
4. Testfixtures: dummy-projecten (Python, Node, Hugo) om skill tegen te valideren
5. Baseline en refactor test-transcripties in `tests/`

## Methodiek (TDD voor skills)

Volgens `superpowers:writing-skills`:

1. **RED** - Baseline pressure scenarios draaien met subagent zonder skill. Documenteer wat ze produceren en welke gaps er zitten
2. **GREEN** - SKILL.md schrijven die die specifieke gaps adresseert. Opnieuw testen tot compliance
3. **REFACTOR** - Nieuwe rationalisaties vinden, loopholes dichten, herhalen tot bulletproof

## Agent-compatibiliteit (nieuwe eis)

De handoff moet door Claude Code of Cowork direct oppakbaar zijn. Dat betekent:

- `CLAUDE.md` in de handoff-map met: projectdoel, stack, commando's, niet-doen-lijst, directe startinstructie
- Duidelijke commando-blokken die een agent letterlijk kan uitvoeren
- Geen impliciete kennis: elke stap moet in de map staan
- Getest door een subagent dispatch: schone context, alleen de handoff-map, kan de agent het project draaien?

## Fases

| Fase | Inhoud | Exit-criterium |
|------|--------|----------------|
| 1 | Research + scope-definitie | Deliverable structuur vastgelegd |
| 2 | RED baseline tests | Rationalisatietabel met >=3 rijen |
| 3 | GREEN eerste skill + inspectiescript | Skill compliant op dummy-project |
| 4 | REFACTOR loopholes dichten | Bulletproof tegen pressure scenarios |
| 5 | Dogfood op echt project | Handoff werkt eind-tot-eind |
| 6 | Agent-test | Subagent start project vanaf alleen de handoff-map |
| 7 | Deploy + publiceren | Skill in `~/.claude/skills/`, repo public op GitHub |

## Risico's

- Secrets lekken: aanpakken via expliciete allowlist voor bestandstypes, blocklist voor extensies
- Over-engineering: inspectie moet pragmatisch zijn, geen volledige AST-analyse
- Skill te generiek: dogfood op concrete projecten voorkomt "werkt op papier"
