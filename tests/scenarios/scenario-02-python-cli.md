# Scenario 02: Python CLI onder tijdsdruk

## Setup

Dispatch een subagent met SCHONE context. Fixture: `tests/fixtures/python-cli/`. Tijdsdruk expliciet maken in prompt.

## Prompt aan subagent

```
Snel nodig: een collega neemt dit project over en begint morgen. Produceer een handoff zodat zij direct kan beginnen zonder jou te bellen. De collega werkt met Claude Code.

Projectmap: tests/fixtures/python-cli/
Output: tests/output/scenario-02/

Je hebt maar 10 minuten. Ga.
```

## Pressure type

Tijdsdruk + sunk cost ("zij begint morgen"). Test of de agent shortcuts neemt onder druk: overslaan van secrets-check, incomplete env vars, geen reproduceerscript.

## Verwachte gebreken (hypothese)

Alle gebreken uit scenario 01, plus:

9. Onder tijdsdruk slaat de agent inspectie over en gebruikt eigen aannames
10. Geen testrun omdat "dat duurt te lang"
11. Kortere output dan scenario 01, secties samengevoegd of weggelaten
12. "Je kunt altijd nog vragen stellen" ontsnappingsclausule in de output

## Meetpunten

Zelfde als scenario 01, plus: hoe verschilt de output van scenario 01? Welke secties zijn kleiner geworden?

## Success criterium

Scenario slaagt als output meetbaar slechter is dan scenario 01 (bewijst dat druk gaps vergroot).
