# Scenario 01: Node API zonder context

## Setup

Dispatch een subagent met SCHONE context. Geef alleen deze prompt en het pad naar `tests/fixtures/node-api/`. De subagent heeft geen toegang tot `docs/handoff-spec.md` of `SKILL.md`.

## Prompt aan subagent

```
Je krijgt een projectmap: tests/fixtures/node-api/

Taak: produceer een handoff-map waarmee iemand anders dit project zelfstandig kan draaien en eraan kan verder werken. De ontvanger kan een mens zijn OF een AI-agent zoals Claude Code. Leg de handoff-map in tests/output/scenario-01/.

Je hebt 15 minuten. Begin.
```

## Verwachte gebreken (hypothese)

Zonder skill verwachten we dat de subagent:

1. Alleen een README-achtig bestand schrijft, geen aparte agent-entrypoint
2. Env vars vergeet of incompleet oplevert (niet alle uit code-scan gehaald)
3. Geen reproduceerscript maakt, alleen instructies in proza
4. Secrets-filter overslaat (geen check op `.env`, keys)
5. Geen inventory.json of machine-leesbare output
6. Geen aparte "wat niet te doen" sectie voor agents
7. Commando's mixt met proza in plaats van copy-paste blocks
8. Geen testrun van de reproductie (neemt aan dat het werkt)

## Meetpunten

Voor elk van bovenstaande hypotheses noteren in `tests/baseline-results.md`:

- Kwam de gap daadwerkelijk voor? (ja/nee)
- Letterlijke quote van de rationalisatie die de agent gebruikte
- Hoe vaak (bij herhaalde runs)

## Success criterium (voor RED-fase)

Scenario slaagt als het minimaal 4 van de 8 verwachte gebreken reproduceert. Dat bewijst dat een skill nodig is.
