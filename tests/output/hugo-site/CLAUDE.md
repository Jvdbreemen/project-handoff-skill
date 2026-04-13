# Claude Code instructies: hugo-site

Dit bestand vult `AGENTS.md` aan met Claude Code specifieke instructies.

## Baseline

Lees eerst `AGENTS.md` voor de algemene agent-brief. Alles daarin geldt ook hier.

## Taakbeheer

Geen specifiek taakbeheer gedetecteerd. Gebruik `TodoWrite` voor interne tracking.

## Tools en skills

- Gebruik `Bash` voor setup commando's uit `REPRODUCE.sh`
- Gebruik `Read`/`Edit` voor file wijzigingen, niet `sed`/`awk`
- Gebruik `Grep` voor zoeken, niet `grep`/`rg` direct
- Bij onzekerheid over library-API: raadpleeg Context7 MCP voor actuele docs

## Workflow

1. Lees `HANDOFF.md` en `AGENTS.md` volledig door
2. Draai `./REPRODUCE.sh` om het project op te zetten
3. Bevestig dat tests slagen voordat je wijzigingen maakt
4. Maak een nieuwe branch voor je werk
5. Commit per logische eenheid, niet grote dumps
6. Push niet zonder expliciete toestemming

## Niet doen

- Niet pushen naar main zonder approval
- Niet `git reset --hard` zonder checken wat je kwijtraakt
- Niet hooks bypassen
- Geen TODO's toevoegen zonder tracking (gebruik backlog als dat project het heeft)

## Contact

Als iets onduidelijk is of de handoff incompleet blijkt, stop en rapporteer terug. Liever vragen dan raden.
