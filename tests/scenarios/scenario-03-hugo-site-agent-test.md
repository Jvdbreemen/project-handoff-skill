# Scenario 03: Hugo site + agent-reproduceer-test

## Setup

Twee subagents na elkaar:

**Subagent A** (producer): krijgt `tests/fixtures/hugo-site/` en de taak om een handoff te maken.
**Subagent B** (reproducer): krijgt ALLEEN de output van subagent A. Taak: project draaien en een kleine wijziging maken.

## Prompt subagent A

```
Produceer een handoff-map voor het project in tests/fixtures/hugo-site/.
Output in tests/output/scenario-03/.

De ontvanger is een AI-agent die alleen de handoff-map krijgt, niet het originele project. Die agent moet het project clonen of kopieren, draaiend krijgen, en een wijziging maken. Schrijf de handoff zo dat dat kan.
```

## Prompt subagent B

```
Je krijgt alleen de map tests/output/scenario-03/.

Taak:
1. Volg de instructies in de map om het Hugo-project op te zetten vanuit de originele fixture op tests/fixtures/hugo-site/
2. Start de Hugo development server
3. Voeg een pagina toe met de titel "Test Page"
4. Bevestig dat de pagina zichtbaar is

Je hebt alleen de handoff-map. Als iets ontbreekt, rapporteer wat er mist.
```

## Pressure type

End-to-end agent-reproducibility test. Dit is de harde meetlat: slaagt B, dan werkt het. Faalt B, dan weten we precies welke stappen ontbreken.

## Verwachte gebreken (hypothese)

Zonder skill verwachten we dat subagent B vastloopt op:

1. Onduidelijke setup-volgorde (wat eerst: Hugo install of module download?)
2. Ontbrekende Hugo versie-eis
3. Geen expliciete "hoe start je de dev server" zonder te moeten raden uit config
4. Geen info over waar pagina's toegevoegd worden (content/posts/ of content/page/?)
5. Geen commando voor het toevoegen van een pagina (hugo new)

## Meetpunten

- Gaat subagent B door tot eind zonder vast te lopen? Ja/nee
- Hoeveel keer moet B raden of aannames maken?
- Welke stappen ontbraken in de handoff?
- Hoe lang duurde het voor B?

## Success criterium

Voor RED-fase: B loopt vast op minimaal 1 stap. Dat bewijst dat handoffs zonder skill niet agent-reproduceerbaar zijn.

Na GREEN/REFACTOR: B slaagt zonder raden.
