# Research: bestaande handoff-formats en tools

## Bronnen

1. **AGENTS.md standaard** - Open format voor AI agent entrypoints in projecten, complementair aan README. Bevat build steps, tests, conventions die niet in README thuishoren. (Bron: [agents.md](https://agents.md/), [Augment Code guide](https://www.augmentcode.com/guides/how-to-build-agents-md))

2. **CLAUDE.md conventie** - Claude Code leest dit bestand aan het begin van elke sessie. Gebruikt voor coding standards, architectuurbeslissingen, voorkeursbibliotheken. Claude-specifiek bovenop AGENTS.md. (Bron: [HumanLayer](https://www.humanlayer.dev/blog/writing-a-good-claude-md), [Dometrain](https://dometrain.com/blog/creating-the-perfect-claudemd-for-claude-code/))

3. **Repomix** - Packt hele repo in 1 AI-vriendelijk bestand voor LLM-context. MCP-server variant laat agents dynamisch queryen. Use case: context delen, niet reproductie. (Bron: [repomix.com](https://repomix.com/), [GitHub](https://github.com/yamadashy/repomix))

4. **DevContainers** - Docker-based preconfigured development environments. Sterke reproductie, maar zware dependency (Docker verplicht). (Bron: [containers.dev/features](https://containers.dev/features))

5. **Mise** - Cross-platform versie-manager voor runtimes en tools, opvolger van asdf. Lichter dan devcontainers, werkt zonder Docker. Kan ook binnen devcontainers gebruikt worden. (Bron: [mise-en-place.dev](https://mise.jdx.dev/), [Reza Chegini](https://rezachegini.com/2025/10/14/mise-and-dev-containers-simple-setup-guide/))

6. **Klassieke project-handover templates** - Standaardsecties: project overview, status, stakeholder directory, risks/issues, key documents, lessons learned, next steps, sign-off. Meer management-georienteerd dan technisch. (Bron: [Deep Project Manager](https://deeprojectmanager.com/project-handover-document/), [Monday blog](https://monday.com/blog/project-management/project-handoff/))

## Beslissingen voor de skill

### Wel adopteren

- **AGENTS.md als primaire agent-entrypoint**. Dit is de emerging standaard, platform-agnostisch. Onze skill genereert dit als hoofdagent-bestand.
- **CLAUDE.md als optionele aanvulling** voor Claude Code specifieke instructies (bijv. "gebruik backlog, niet todos").
- **HANDOFF.md voor mensen** met een afgeslankte versie van de klassieke handover-secties: overview, prerequisites, setup, run/test, architectuur, known issues, contact.
- **mise-referentie** in templates. Als het doelproject een `.tool-versions` of `mise.toml` heeft, neemt het inspectiescript dat over. Als dat niet bestaat, suggereren we runtime-versies in de HANDOFF maar verplichten mise niet.
- **Secrets-blocklist**: harde regex-filters op `.env`, `*.key`, `*.pem`, `credentials.json`, `id_rsa*`, bestanden met "token"/"secret"/"password" in de naam.

### Niet adopteren

- **Volledig repomix context-dump**. Dat is een ander probleem (LLM-context) dan reproduceerbaarheid. Te zwaar voor een handoff-map. Wel als optionele output vermelden (`--with-context` flag bijvoorbeeld).
- **DevContainers als verplicht**. Docker-afhankelijkheid is te veel overhead voor simpele projecten. Wel detecteren als het al aanwezig is en doorverwijzen.
- **Klassieke management-handover secties** (sign-off, stakeholder directory, risks log). Dat is PM-output, niet dev-output. Voor onze scope niet relevant.
- **Commerciele template-platforms** (ClickUp, Monday, Miro). Open source only.

### Open vragen

- Moet de skill een losse map produceren of inline in de bestaande repo schrijven (als bijv. `.handoff/`)? Voorlopig: losse map (non-destructief).
- Moet er versioning zijn (handoff v1, v2)? Voorlopig: nee, markdown + git-history is genoeg.
- Welke taal voor het inspectiescript? Bash is portable maar beperkt, Python geeft meer structuur. Voorlopig: Python met uv-shebang zodat het zonder installatie draait.

## Referentie-architectuur

```
handoff/                  genegereerde map
├── HANDOFF.md            primair mens-entrypoint
├── AGENTS.md             primair agent-entrypoint (standaard)
├── CLAUDE.md             optioneel, Claude Code specifiek
├── REPRODUCE.sh          scripted setup op schone machine
├── .env.example          uit code-scan, zonder waarden
├── inventory.json        machine-leesbare output van inspectiescript
└── architecture.md       optioneel, als codebase groot genoeg is
```
