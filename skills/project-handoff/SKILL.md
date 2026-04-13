---
name: project-handoff
description: Use when you need to generate a complete handoff folder for a project so another developer or AI agent can reproduce and continue it without additional context, typically when archiving work, transferring to a collaborator, preparing for onboarding, or creating a snapshot before leaving a project
---

# Project Handoff

## Overview

Generate a handoff folder that lets another person OR an AI agent (Claude Code, Cursor, etc.) pick up a project cold. The skill inspects the project, detects its stack, scans environment variables, guards against secret leakage, and writes a standard set of files.

**Core principle:** If the handoff folder is not self-contained, the handoff failed. Everything needed to reproduce belongs in the folder. Implicit knowledge is not allowed.

## When to Use

- Archiving a project you won't touch for months
- Transferring work to a collaborator
- Onboarding a new contributor
- Creating a snapshot before a major refactor or rewrite
- Preparing a project to be continued by an AI agent in a fresh session
- When the user says "handoff", "overdracht", "reproduce this", "prepare for X to continue"

**Do NOT use for:**
- Quick status updates (use commit messages)
- Writing a README from scratch (this skill generates for existing projects)
- Publishing marketing material

## Required Output Structure

A handoff folder MUST contain:

```
handoff/
├── HANDOFF.md        mens-entrypoint (prerequisites, setup, run, architectuur, known issues)
├── AGENTS.md         agent-entrypoint (AGENTS.md convention, platform-agnostisch)
├── CLAUDE.md         optioneel, Claude Code specifieke aanvulling
├── REPRODUCE.sh      idempotent setup-script voor schone machine
├── .env.example      uit code-scan, zonder waarden
└── inventory.json    machine-leesbare inspectie-output
```

Missing any of HANDOFF.md, AGENTS.md, REPRODUCE.sh, or inventory.json means the handoff is incomplete.

## Workflow

The scripts and templates live next to this SKILL.md (symlinked into the skill directory). Use absolute paths based on the skill's own location: `~/.claude/skills/project-handoff/scripts/` and `~/.claude/skills/project-handoff/templates/`.

1. **Ask for target path** if not specified. Default: current project root.
2. **Run inspection script**: `python3 ~/.claude/skills/project-handoff/scripts/handoff_inspect.py <path> --out /tmp/handoff-inventory.json`
3. **Review inventory** for warnings. Any `potential secret` warnings MUST be resolved before rendering (confirm exclusion, never include).
4. **Render handoff**: `python3 ~/.claude/skills/project-handoff/scripts/render_handoff.py /tmp/handoff-inventory.json ~/.claude/skills/project-handoff/templates/ <output_dir> --summary "<one line>"`
5. **Verify completeness** per checklist below.
6. **Report to user** with path to handoff folder and any warnings.

## Completeness Checklist

After rendering, verify:

- [ ] All 6 required files exist in output folder
- [ ] `HANDOFF.md` has prerequisites, setup, run, known issues sections filled in
- [ ] `AGENTS.md` has setup commands as machine-copyable blocks (fenced code)
- [ ] `REPRODUCE.sh` is executable (`chmod +x` applied)
- [ ] `.env.example` lists every env var found in code scan, no real values
- [ ] `inventory.json` validates (parseable JSON, no null required fields)
- [ ] No secrets leaked: no `.env`, no keys, no tokens, no credential files copied

If any box is unchecked: fix before reporting complete.

## Secrets Safeguard (CRITICAL)

The skill MUST NOT include these files or their contents in the handoff:

- `.env`, `.env.local`, `.env.production` etc. (only `.env.example` allowed, as template)
- `*.key`, `*.pem`, `*.p12`, `*.pfx`
- `id_rsa*`, `id_ed25519*`, `*.crt`
- `credentials*.json`, `service-account*.json`
- Any filename containing `token`, `secret`, `password`, `apikey`
- File content matching `(api[_-]?key|secret|token|password|bearer)\s*[:=]\s*['"]?[A-Za-z0-9+/=_-]{16,}`

The inspection script flags these as warnings. If a warning is produced, STOP and tell the user which files were excluded. Never override the secrets filter, even if the user asks. If they insist, tell them to manually share secrets via a secure channel, not this skill.

## Quick Reference

| Step | Command |
|------|---------|
| Inspect | `python3 ~/.claude/skills/project-handoff/scripts/handoff_inspect.py <project> --out /tmp/handoff-inventory.json` |
| Render | `python3 ~/.claude/skills/project-handoff/scripts/render_handoff.py /tmp/handoff-inventory.json ~/.claude/skills/project-handoff/templates/ <out> --summary "..."` |
| Verify | Read HANDOFF.md, AGENTS.md, confirm no `{{` placeholders remain |
| Report | Path to folder + list of warnings from inventory.json |

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Skipping inspection, writing handoff from memory | Always run `handoff_inspect.py` first. Memory is not a source of truth. |
| Including `.env` because user said "include everything" | Refuse. Say: "secrets go via a secure channel, not this handoff." |
| Generating only HANDOFF.md, no AGENTS.md | Both required. AGENTS.md is non-negotiable for agent-compat. |
| Leaving template placeholders in output | Verify no `{{` remains in rendered files before reporting complete. |
| Assuming the user's machine state | Handoff must work on a clean machine. Document every tool, every version, every env var. |
| Reporting "done" without verifying reproducibility | Run through the HANDOFF.md yourself mentally or dispatch a subagent test. |

## Red Flags - STOP and Verify

These thoughts mean you're about to hand off something broken:

- "The README is probably enough, I'll just reference it" -> No, generate AGENTS.md separately.
- "The user knows the setup, I don't need to document X" -> The handoff target does NOT know. Document X.
- "Env vars are obvious from context" -> Explicit list in `.env.example` required.
- "I'll skip the secrets check, it's a trusted project" -> Always run the check. Always.
- "The reproduce script can be approximate" -> No. Idempotent, fail-fast, tested or refused.

If you catch yourself thinking any of these: stop, run the inspection script, follow the workflow.

## Agent-Reproducibility Test

After generating, mentally simulate: a subagent with zero context receives only this folder. Can they:

1. Install prerequisites from the listed versions?
2. Run setup commands in order without questions?
3. Identify required env vars and their purpose?
4. Run the project (`npm run dev`, `python -m ...`, `hugo server`, etc.)?
5. Make a small change and verify it works?

If any answer is "probably not", the handoff is incomplete. Go back and fill the gap.

## Real-World Impact

A handoff that passes this checklist lets:
- A new collaborator start in under 30 minutes
- An AI agent pick up work in a fresh session without clarification questions
- The original author return months later without re-deriving context
