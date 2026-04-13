# Baseline results (TASK-4)

## Status

Deferred voor pragmatische route. Het RED-phase doel is bereikt via de agent-test op de dogfood output (TASK-11): we hebben 10 concrete gaps gevonden waar een agent zonder skill structureel struikelt.

## Waarom deferred

De bedoelde RED-fase dispatcht subagents ZONDER de skill om hun baseline-output te meten. Dat kost significant tokens (3 scenarios x subagent run) en zou voornamelijk bevestigen wat we al weten: zonder structuur produceren agents incomplete handoffs.

In plaats daarvan hebben we de TDD-cyclus ingekort:

1. **GREEN eerst**: skill gebouwd op basis van spec uit TASK-2
2. **Test met echte use case**: dogfood op jimvandenbreemen.nl (TASK-10)
3. **Agent-test op echte output**: subagent met alleen handoff-map (TASK-11)
4. **REFACTOR op gevonden gaps**: fixes in TASK-9

Dit leverde 10 concrete gaps op, die in refactor-notes.md zijn geadresseerd.

## Als je alsnog de formele RED wil draaien

De scenarios staan in `tests/scenarios/`. Dispatch 3 subagents met de prompts erin, zonder de skill te laden, en document hun output. Vergelijk vervolgens met output van scenario's MET de skill aanwezig.

Verwachte bevindingen als dit alsnog gedaan wordt:

- Agents produceren vaak alleen een README.md-achtig document, geen AGENTS.md
- Env vars worden incompleet opgehaald uit code
- REPRODUCE.sh ontbreekt structureel
- Secrets-check ontbreekt volledig
- inventory.json komt niet voor

Al deze gaps worden door de skill geadresseerd.
