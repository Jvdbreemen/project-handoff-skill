#!/usr/bin/env python3
"""Render a handoff folder from inventory.json + templates.

Usage:
    python render_handoff.py INVENTORY_JSON TEMPLATES_DIR OUTPUT_DIR [--summary TEXT]
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path


def join_or(items, sep=", ", fallback="-"):
    if not items:
        return fallback
    return sep.join(str(x) for x in items)


def render_value(template: str, key: str, value: str) -> str:
    return template.replace("{{" + key + "}}", value)


def build_context(inv: dict, summary: str | None) -> dict[str, str]:
    project = inv.get("project", {})
    git = project.get("git", {}) or {}
    stack = inv.get("stack", {}) or {}
    scripts = inv.get("scripts", {}) or {}
    env_vars = inv.get("env_vars", []) or []
    structure = inv.get("structure", {}) or {}
    issues = inv.get("issues", {}) or {}

    runtimes = stack.get("runtimes", []) or []
    runtimes_str = join_or([f"{r['name']} {r['version']}" for r in runtimes], fallback="onbekend")

    env_table_rows = "\n".join(
        f"| `{v['name']}` | REQUIRED | {', '.join(v.get('used_in', [])[:2]) or '-'} |"
        for v in env_vars
    ) or "| _geen env vars gedetecteerd_ | | |"
    env_table = "| Variabele | Status | Gebruikt in |\n|-----------|--------|-------------|\n" + env_table_rows

    env_plain = "\n".join(f"- `{v['name']}`" for v in env_vars) or "- _geen_"

    env_block = "\n".join(f"{v['name']}=" for v in env_vars) or "# geen env vars gedetecteerd"

    prereq_lines = []
    for r in runtimes:
        prereq_lines.append(f"- {r['name']} {r['version']}")
    for pm in stack.get("package_managers", []) or []:
        prereq_lines.append(f"- {pm}")
    if not prereq_lines:
        prereq_lines.append("- _geen specifieke runtimes gedetecteerd, zie project bestanden_")
    prereq_list = "\n".join(prereq_lines)

    prereq_check_lines = []
    for r in runtimes:
        name = r["name"]
        prereq_check_lines.append(
            f'command -v {name} >/dev/null 2>&1 || fail "{name} niet gevonden"'
        )
    prereq_check = "\n".join(prereq_check_lines) or 'true  # geen checks nodig'

    warnings = issues.get("warnings", []) or []
    warnings_list = "\n".join(f"- WARN: {w}" for w in warnings) or ""
    warnings_plain = warnings_list or "- _geen warnings_"

    install_cmds = "\n".join(scripts.get("install", [])) or "# geen install commando gedetecteerd"
    build_cmds = "\n".join(scripts.get("build", [])) or "# geen build commando gedetecteerd"
    run_cmds = "\n".join(scripts.get("run", [])) or "# geen run commando gedetecteerd"
    test_cmds = "\n".join(scripts.get("test", [])) or "# geen test commando gedetecteerd"

    setup_cmds_list = []
    if git.get("remote"):
        setup_cmds_list.append(f'git clone {git["remote"]}')
        setup_cmds_list.append(f'cd {project.get("name", "project")}')
    setup_cmds_list.extend(scripts.get("install", []))
    setup_cmds = "\n".join(setup_cmds_list) or "# handmatige setup, zie HANDOFF.md"

    # Smoke test: prefer build (non-blocking) over run (may block on dev server).
    build_lines = [l for l in (scripts.get("build") or []) if not l.strip().startswith("#")]
    test_lines = [l for l in (scripts.get("test") or []) if not l.strip().startswith("#")]
    if build_lines:
        smoke_test = build_lines[0]
    elif test_lines:
        smoke_test = test_lines[0]
    else:
        smoke_test = 'echo "geen smoke test gedefinieerd, zie HANDOFF.md"'

    hugo_config = stack.get("hugo_config") or {}
    framework_details_lines = []
    if hugo_config:
        if hugo_config.get("title"):
            framework_details_lines.append(f"- **Hugo site titel:** {hugo_config['title']}")
        if hugo_config.get("base_url"):
            framework_details_lines.append(f"- **Base URL:** {hugo_config['base_url']}")
        if hugo_config.get("theme"):
            framework_details_lines.append(f"- **Theme:** `{hugo_config['theme']}` (themes/{hugo_config['theme']}/)")
        if hugo_config.get("config_file"):
            framework_details_lines.append(f"- **Config file:** `{hugo_config['config_file']}`")
    framework_details = "\n".join(framework_details_lines) or "_geen framework details gedetecteerd_"

    coding_conv_lines = []
    langs = stack.get("languages", []) or []
    if "javascript" in langs or "typescript" in langs:
        coding_conv_lines.append("- ESM-modules, geen CommonJS tenzij het project het al doet")
        coding_conv_lines.append("- 2-space indent")
    if "python" in langs:
        coding_conv_lines.append("- PEP 8, 4-space indent, type hints waar mogelijk")
        coding_conv_lines.append("- f-strings voor string formatting")
    if "go" in langs:
        coding_conv_lines.append("- `gofmt` verplicht")
    if not coding_conv_lines:
        coding_conv_lines.append("- Volg de stijl van bestaande code in het project")
    coding_conv = "\n".join(coding_conv_lines)

    task_management = (
        "Dit project gebruikt Backlog.md voor taakbeheer. Orienteer via `backlog task list` voordat je begint."
        if _has_backlog(project.get("path"))
        else "Geen specifiek taakbeheer gedetecteerd. Gebruik `TodoWrite` voor interne tracking."
    )

    return {
        "project_name": project.get("name", "onbekend"),
        "one_line_summary": summary or f"Project {project.get('name', 'onbekend')}",
        "git_branch": git.get("branch") or "-",
        "git_last_commit": git.get("last_commit") or "-",
        "git_clean_label": "clean" if git.get("clean") else "wijzigingen aanwezig",
        "git_remote": git.get("remote") or "geen remote",
        "languages": join_or(langs),
        "runtimes": runtimes_str,
        "package_managers": join_or(stack.get("package_managers", [])),
        "frameworks": join_or(stack.get("frameworks", [])),
        "framework_details": framework_details,
        "prerequisites_list": prereq_list,
        "prerequisites_check": prereq_check,
        "setup_commands": setup_cmds,
        "env_vars_table": env_table,
        "env_vars_plain_list": env_plain,
        "env_vars_block": env_block,
        "install_commands": install_cmds,
        "build_commands": build_cmds,
        "run_commands": run_cmds,
        "test_commands": test_cmds,
        "smoke_test": smoke_test,
        "tree": structure.get("tree_depth_3", ""),
        "file_count": str(structure.get("file_count", 0)),
        "loc_estimate": str(structure.get("loc_estimate", 0)),
        "todo_count": str(issues.get("todos", 0)),
        "warnings_list": warnings_list,
        "warnings_plain_list": warnings_plain,
        "coding_conventions": coding_conv,
        "task_management_note": task_management,
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
    }


def _has_backlog(path: str | None) -> bool:
    if not path:
        return False
    return (Path(path) / "backlog").is_dir() or (Path(path) / ".backlog").is_dir()


def render_template(template_path: Path, context: dict[str, str]) -> str:
    text = template_path.read_text()
    for key, value in context.items():
        text = render_value(text, key, value)
    return text


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("inventory", type=Path)
    ap.add_argument("templates_dir", type=Path)
    ap.add_argument("output_dir", type=Path)
    ap.add_argument("--summary", default=None)
    ap.add_argument("--with-claude-md", action="store_true", default=True)
    args = ap.parse_args()

    inv = json.loads(args.inventory.read_text())
    context = build_context(inv, args.summary)

    args.output_dir.mkdir(parents=True, exist_ok=True)

    mapping = {
        "HANDOFF.md.tmpl": "HANDOFF.md",
        "AGENTS.md.tmpl": "AGENTS.md",
        "REPRODUCE.sh.tmpl": "REPRODUCE.sh",
        "env.example.tmpl": ".env.example",
    }
    if args.with_claude_md:
        mapping["CLAUDE.md.tmpl"] = "CLAUDE.md"

    for tmpl_name, out_name in mapping.items():
        tmpl_path = args.templates_dir / tmpl_name
        if not tmpl_path.exists():
            print(f"WARN: template missing: {tmpl_path}", file=sys.stderr)
            continue
        rendered = render_template(tmpl_path, context)
        out = args.output_dir / out_name
        out.write_text(rendered)
        if out_name.endswith(".sh"):
            out.chmod(0o755)

    (args.output_dir / "inventory.json").write_text(json.dumps(inv, indent=2, ensure_ascii=False))

    print(f"Handoff generated in {args.output_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
