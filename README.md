# project-handoff-skill

Claude Code skill die een bestaande projectdirectory inspecteert en een complete handoff-map genereert waarmee zowel een mens als een AI-agent het project zelfstandig kan reproduceren, opstarten en verder bewerken.

## Wat het doet

Gegeven een projectmap, produceert de skill:

| Bestand | Doelgroep | Inhoud |
|---------|-----------|--------|
| `HANDOFF.md` | mens | overview, status, stack, prerequisites, setup, env vars, commando's, architectuur, known issues |
| `AGENTS.md` | willekeurige AI agent | platform-agnostische agent-brief volgens [agents.md](https://agents.md/) |
| `CLAUDE.md` | Claude Code | aanvulling op AGENTS.md met Claude-specifieke workflow |
| `REPRODUCE.sh` | CI / schone machine | idempotent setup-script |
| `.env.example` | configuratie | gegenereerd uit code-scan, zonder waarden |
| `inventory.json` | tooling | machine-leesbare inspectie-output |

## Installatie

```bash
git clone https://github.com/Jvdbreemen/project-handoff-skill.git ~/Claude/projects/project-handoff-skill
mkdir -p ~/.claude/skills
ln -sfn ~/Claude/projects/project-handoff-skill/skills/project-handoff ~/.claude/skills/project-handoff
```

Claude Code pikt de skill automatisch op bij de volgende sessie.

## Gebruik

Roep de skill aan in Claude Code:

```
/project-handoff
```

Of in proza: "maak een handoff van dit project in `./handoff/`".

Handmatige aanroep van de pipeline:

```bash
# 1. Inspecteer een project
python3 ~/.claude/skills/project-handoff/scripts/handoff_inspect.py /pad/naar/project --out /tmp/inv.json

# 2. Render de handoff
python3 ~/.claude/skills/project-handoff/scripts/render_handoff.py \
  /tmp/inv.json \
  ~/.claude/skills/project-handoff/templates/ \
  /pad/naar/output \
  --summary "Korte beschrijving van het project"
```

## Wat wordt gedetecteerd

- **Talen en runtimes:** JavaScript/TypeScript (Node), Python, Go, Hugo sites
- **Package managers:** npm, pnpm, yarn, bun, uv, poetry, pip, go modules
- **Scripts:** uit `package.json`, `pyproject.toml`
- **Environment variables:** via regex-scan van sourcecode (`process.env.X`, `os.getenv("X")`, `ENV["X"]` etc.)
- **Git state:** remote, branch, laatste commit, of working tree clean is
- **TODO/FIXME markers:** totaaltelling
- **Potentiele secrets:** flagt en excludeert (nooit meegenomen in de handoff)

## Secrets-filter

De skill neemt nooit de volgende bestanden of hun inhoud mee:

- `.env`, `.env.local`, `.env.production` (alleen `.env.example` als template)
- `*.key`, `*.pem`, `*.p12`, `*.pfx`
- `id_rsa*`, `id_ed25519*`, `*.crt`
- `credentials*.json`, `service-account*.json`
- Bestanden met `token`, `secret`, `password`, `apikey` in de naam
- Regel-inhoud die matcht op gevoelige patronen

Waarschuwingen worden naar stderr gelogd en opgenomen in `inventory.json` onder `issues.warnings`.

## Testfixtures

`tests/fixtures/` bevat 3 minimale projecten waarop de skill is gevalideerd:

- `node-api/` - Express API met env vars
- `python-cli/` - Typer CLI met httpx
- `hugo-site/` - Minimal Hugo site

Test zelf:

```bash
python3 scripts/handoff_inspect.py tests/fixtures/node-api --out /tmp/inv.json
python3 scripts/render_handoff.py /tmp/inv.json templates/ tests/output/node-api
```

## Beperkingen

- Detecteert alleen de stacks hierboven. PHP, Ruby, Rust, Java: nog niet.
- Env var detectie is regex-based, mist dynamische lookups (`os.environ[var_name]`).
- `REPRODUCE.sh` wordt niet automatisch gedraaid. Handmatig testen op schone machine blijft verstandig.
- Geen DevContainers of Docker detectie (staat op de roadmap).

## Ontwikkeling

- Plan: `PLAN.md`
- Spec: `docs/handoff-spec.md`
- Research: `docs/research.md`
- Taken: `backlog task list`

## Licentie

MIT
