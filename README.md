# project-handoff-skill

Een Claude Code skill die een bestaande projectdirectory inspecteert en een complete handoff-map genereert waarmee iemand anders het project zelfstandig kan reproduceren.

## Wat het doet

De skill scant een project en levert:

- Een `HANDOFF.md` met prerequisites, installatie, configuratie, run/build/test commando's, architectuur en bekende valkuilen
- Een inventaris van dependencies (package manager, runtime versies, systeem-tools)
- Een lijst van verwachte environment variables (zonder secrets)
- Een reproduceerbare setup-flow die getest is op een schone machine

## Status

In ontwikkeling. Zie `PLAN.md` voor de roadmap en `backlog/` voor de actieve taken.

## Installatie

Nog niet klaar voor gebruik. Wordt na voltooiing beschikbaar als skill in `~/.claude/skills/project-handoff/`.

## Licentie

MIT
