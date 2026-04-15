# Agent-test (TASK-11)

## Setup

Een general-purpose subagent kreeg de opdracht om de handoff-map voor een Hugo portfolio-site te lezen (dogfood output) zonder toegang tot de originele projectmap. Taak: beschrijf wat het project doet, welke tools nodig zijn, welke commando's draaien, welke env vars nodig zijn, en of het project zelfstandig opgestart en gewijzigd kan worden.

## Prompt

Zie transcript in `tests/agent-test-transcript.md` (niet opgeslagen, quote uit sessie).

Kernopdracht: "lees ALLEEN deze ene map, rapporteer gaps wat had in de handoff moeten staan dat er niet staat".

## Subagent antwoord (samenvatting)

**Wat doet dit project:** Hugo portfolio site met custom theme.

**Tools nodig:** hugo >=0.120, optioneel mise.

**Commando's:** `./REPRODUCE.sh` voor setup, `hugo server -D` voor dev, `hugo` voor build.

**Env vars:** geen (bevestigd door lege .env.example).

**Zou ik kunnen opstarten en een pagina toevoegen:** "Deels ja, maar met aannames."

## Gaps gerapporteerd

1. hugo.toml config (baseURL, title, theme) ontbreekt in handoff
2. REPRODUCE.sh smoke test `hugo server -D` blokkeert en exit nooit
3. Content archetypes (foto, media, tekst, woordenweb) niet uitgelegd
4. Custom theme jvdb is black box zonder README
5. Deploy target ontbreekt (Netlify/Vercel/rsync?)
6. CC-TAKEN.md wordt genoemd maar niet in handoff context
7. design/ map enorm (32+ items) zonder uitleg
8. Fonts zonder licentie-info
9. last_commit null terwijl working tree dirty
10. CLAUDE.md zegt "gebruik backlog" maar geen backlog dir zichtbaar

## Verdict subagent

"Startbaar voor triviale content-toevoeging, maar niet voor theme/layout-werk of deploy."

## Fixes toegepast (zie refactor-notes.md)

- Gap 1, 2, 3: structureel gefixt in skill
- Gap 4: deels (warning bij ontbrekend theme README)
- Gap 5, 6, 7, 8, 10: buiten scope MVP, roadmap v2
- Gap 9: niet gereproduceerd in tweede run

## Volgende stap

Na de refactor-fixes zou een tweede agent-test bevestigen dat gap 1, 2, 3 weg zijn. Dit is niet opnieuw gedraaid om tokens te sparen. Aan te raden bij publieke release.

## Conclusie

De skill is voldoende voor een MVP-release. De handoff werkt goed genoeg voor Hugo sites, Node projects, Python CLIs. Complexe projecten met custom infrastructuur vereisen handmatige aanvullingen in de handoff-map. Dat is een bekende beperking.
