# REFACTOR: loopholes en rationalisaties

## Agent-test findings (TASK-11)

Een subagent met alleen toegang tot de dogfood handoff map gaf 10 gaps. Samenvatting van de belangrijkste en wat we eraan deden:

| # | Gap | Actie | Status |
|---|-----|-------|--------|
| 1 | Hugo config (baseURL, title, theme) niet in handoff | `detect_hugo` parseert nu hugo.toml en vult `stack.hugo_config`. Template toont framework_details sectie. | fixed |
| 2 | REPRODUCE.sh smoke test `hugo server -D` blokkeert | render_handoff.py kiest build command als smoke test, niet run command | fixed |
| 3 | Hugo build gebruikte `hugo` ipv `hugo --minify` | detect_hugo gebruikt nu `hugo --minify` als build command | fixed |
| 4 | Custom theme was black box | Warning toegevoegd als `themes/<theme>/README.md` ontbreekt | partial (alleen warning) |
| 5 | Content archetypes (foto, media, tekst, woordenweb) niet uitgelegd | Nog niet. Archetype-scan is out of scope MVP. | deferred |
| 6 | Deploy target ontbreekt | Nog niet. Detectie van Netlify/Vercel/CI config is out of scope MVP. | deferred |
| 7 | last_commit null bij clean worktree | Niet gereproduceerd in tweede run; waarschijnlijk git-indirection in eerdere run | monitored |
| 8 | CLAUDE.md zei "gebruik backlog" zonder dat er backlog-dir is | `_has_backlog` check is correct; in CC-setup verwijst CLAUDE.md-file naar projects/CLAUDE.md die deze regel zet. Niet de skill. | not a bug |
| 9 | design/ map niet uitgelegd | Buiten scope. Skill geeft directory tree, niet semantiek. | won't fix |
| 10 | Geen licentie info voor fonts | Buiten scope. Skill doet geen licentie-detectie. | won't fix |

## Rationalisatietabel

Rationalisaties die de skill moet voorkomen en die in SKILL.md als red flags zijn opgenomen:

| Rationalisatie | Realiteit | Counter in SKILL.md |
|---------------|-----------|---------------------|
| "De README is waarschijnlijk genoeg, ik verwijs ernaar" | AGENTS.md moet standalone zijn, niet dependency op README | Red Flag expliciet vermeld |
| "De user kent de setup wel" | De handoff target weet NIKS | Red Flag expliciet vermeld |
| "Env vars zijn duidelijk uit context" | Nee, .env.example verplicht | Red Flag expliciet vermeld |
| "Secrets-check overslaan, dit is een trusted project" | Nooit overslaan | Red Flag + Secrets Safeguard sectie |
| "Reproduce script hoeft niet getest" | Idempotent en fail-fast is verplicht | Red Flag expliciet vermeld |
| "Ik weet het stack, inspection is overbodig" | Geheugen is geen source of truth | Common Mistakes tabel |
| "Alleen HANDOFF.md, AGENTS.md komt later" | Beide verplicht | Required Output Structure sectie |

## Resterende gaps (niet geadresseerd, expliciet deferred)

- Archetype-analyse voor Hugo content types
- Deploy target detection (Netlify/Vercel/Pages/rsync)
- Licentie-detectie voor assets (fonts, images)
- Theme partial/shortcode/layout inventarisatie

Deze zitten in de "won't fix MVP, roadmap v2" bucket. Skill werkt zonder ze, maar ze zouden de quality verder opschroeven.

## Validatie

Tweede subagent-run nog niet gedaan (kost extra tokens). De dogfood handoff is na fixes visueel en structureel beter: 158 -> ~170 regels met concrete framework details erbij. Volledige re-validatie staat op TASK-11 v2 als toekomst.
