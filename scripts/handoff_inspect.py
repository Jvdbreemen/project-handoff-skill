#!/usr/bin/env python3
"""Inspect a project directory and emit inventory.json for the handoff skill.

Usage:
    python inspect.py PROJECT_PATH [--out OUTFILE]

Exits nonzero on fatal errors. Warnings (potential secrets, unknown stack)
are written to stderr and included in inventory.json under "issues.warnings".
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

SECRET_FILENAME_PATTERNS = [
    re.compile(r"^\.env(\..+)?$"),
    re.compile(r".*\.key$"),
    re.compile(r".*\.pem$"),
    re.compile(r".*\.(p12|pfx)$"),
    re.compile(r"^id_(rsa|ed25519|dsa|ecdsa).*$"),
    re.compile(r".*credentials.*\.json$", re.IGNORECASE),
    re.compile(r".*service[_-]account.*\.json$", re.IGNORECASE),
    re.compile(r".*(token|secret|password|apikey).*", re.IGNORECASE),
]

SECRET_CONTENT_RE = re.compile(
    r"(api[_-]?key|secret|token|password|bearer)\s*[:=]\s*['\"]?[A-Za-z0-9+/=_\-]{16,}",
    re.IGNORECASE,
)

ENV_VAR_PATTERNS = [
    re.compile(r"process\.env\.([A-Z_][A-Z0-9_]*)"),
    re.compile(r"process\.env\[['\"]([A-Z_][A-Z0-9_]*)['\"]\]"),
    re.compile(r"os\.getenv\(['\"]([A-Z_][A-Z0-9_]*)['\"]"),
    re.compile(r"os\.environ\[['\"]([A-Z_][A-Z0-9_]*)['\"]\]"),
    re.compile(r"os\.environ\.get\(['\"]([A-Z_][A-Z0-9_]*)['\"]"),
    re.compile(r"ENV\[['\"]([A-Z_][A-Z0-9_]*)['\"]\]"),
]

IGNORE_DIRS = {
    ".git", "node_modules", "__pycache__", ".venv", "venv", ".mypy_cache",
    ".pytest_cache", "dist", "build", ".next", ".nuxt", "target",
    ".idea", ".vscode", ".DS_Store", "public/hugo_stats", "resources",
}

SOURCE_EXTENSIONS = {
    ".js", ".mjs", ".cjs", ".ts", ".tsx", ".jsx",
    ".py", ".rb", ".go", ".rs", ".java", ".kt",
    ".sh", ".bash", ".php", ".ex", ".exs",
}


@dataclass
class Inventory:
    project: dict = field(default_factory=dict)
    stack: dict = field(default_factory=dict)
    scripts: dict = field(default_factory=dict)
    env_vars: list = field(default_factory=list)
    dependencies: dict = field(default_factory=dict)
    structure: dict = field(default_factory=dict)
    issues: dict = field(default_factory=lambda: {"todos": 0, "warnings": []})


def warn(inv: Inventory, msg: str) -> None:
    print(f"WARN: {msg}", file=sys.stderr)
    inv.issues["warnings"].append(msg)


def walk_project(root: Path):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in IGNORE_DIRS and not d.startswith(".")]
        for fn in filenames:
            yield Path(dirpath) / fn


def collect_git_state(root: Path) -> dict:
    def run(args: list[str]) -> str | None:
        try:
            out = subprocess.run(
                ["git", "-C", str(root)] + args,
                capture_output=True, text=True, check=True,
            ).stdout.strip()
            return out or None
        except (subprocess.CalledProcessError, FileNotFoundError):
            return None

    remote = run(["remote", "get-url", "origin"])
    branch = run(["branch", "--show-current"])
    last_commit = run(["log", "-1", "--format=%cI"])
    status = run(["status", "--porcelain"])
    return {
        "remote": remote,
        "branch": branch,
        "last_commit": last_commit,
        "clean": status == "" or status is None,
    }


def detect_node(root: Path, inv: Inventory) -> None:
    pkg = root / "package.json"
    if not pkg.exists():
        return
    try:
        data = json.loads(pkg.read_text())
    except json.JSONDecodeError as e:
        warn(inv, f"package.json invalid: {e}")
        return
    inv.stack.setdefault("languages", []).append("javascript")
    inv.stack.setdefault("package_managers", []).append(_detect_node_pm(root))
    if "engines" in data and "node" in data["engines"]:
        inv.stack.setdefault("runtimes", []).append(
            {"name": "node", "version": data["engines"]["node"]}
        )
    scripts = data.get("scripts", {})
    for key in ("install", "build", "test", "run", "start", "dev"):
        if key in scripts:
            inv.scripts.setdefault(_script_bucket(key), []).append(f"npm run {key}")
    inv.dependencies.setdefault("runtime", []).extend(
        {"name": k, "version": v} for k, v in data.get("dependencies", {}).items()
    )
    inv.dependencies.setdefault("dev", []).extend(
        {"name": k, "version": v} for k, v in data.get("devDependencies", {}).items()
    )


def _detect_node_pm(root: Path) -> str:
    if (root / "pnpm-lock.yaml").exists():
        return "pnpm"
    if (root / "yarn.lock").exists():
        return "yarn"
    if (root / "bun.lockb").exists():
        return "bun"
    return "npm"


def _script_bucket(key: str) -> str:
    if key in ("install",):
        return "install"
    if key in ("build",):
        return "build"
    if key in ("test",):
        return "test"
    return "run"


def detect_python(root: Path, inv: Inventory) -> None:
    pyproject = root / "pyproject.toml"
    requirements = root / "requirements.txt"
    if not pyproject.exists() and not requirements.exists():
        return
    inv.stack.setdefault("languages", []).append("python")
    pm = "uv" if (root / "uv.lock").exists() else (
        "poetry" if (root / "poetry.lock").exists() else "pip"
    )
    inv.stack.setdefault("package_managers", []).append(pm)
    if pyproject.exists():
        text = pyproject.read_text()
        m = re.search(r'requires-python\s*=\s*["\']([^"\']+)["\']', text)
        if m:
            inv.stack.setdefault("runtimes", []).append(
                {"name": "python", "version": m.group(1)}
            )
        deps = re.findall(r'^\s*"([^"=<>~\[]+)', text, re.MULTILINE)
        for d in deps:
            inv.dependencies.setdefault("runtime", []).append({"name": d.strip(), "version": "*"})
    inv.scripts.setdefault("install", []).append(f"{pm} sync" if pm == "uv" else f"{pm} install")


def detect_hugo(root: Path, inv: Inventory) -> None:
    for name in ("hugo.toml", "hugo.yaml", "config.toml", "config.yaml"):
        if (root / name).exists():
            inv.stack.setdefault("languages", []).append("markdown")
            inv.stack.setdefault("frameworks", []).append("hugo")
            inv.scripts.setdefault("run", []).append("hugo server -D")
            inv.scripts.setdefault("build", []).append("hugo")
            return


def detect_go(root: Path, inv: Inventory) -> None:
    gomod = root / "go.mod"
    if not gomod.exists():
        return
    inv.stack.setdefault("languages", []).append("go")
    inv.stack.setdefault("package_managers", []).append("go")
    text = gomod.read_text()
    m = re.search(r"^go\s+([\d.]+)", text, re.MULTILINE)
    if m:
        inv.stack.setdefault("runtimes", []).append({"name": "go", "version": m.group(1)})


def scan_env_vars(root: Path, inv: Inventory) -> None:
    found: dict[str, set[str]] = {}
    for path in walk_project(root):
        if path.suffix not in SOURCE_EXTENSIONS:
            continue
        try:
            text = path.read_text(errors="ignore")
        except Exception:
            continue
        for pat in ENV_VAR_PATTERNS:
            for name in pat.findall(text):
                found.setdefault(name, set()).add(str(path.relative_to(root)))
    inv.env_vars = [
        {"name": name, "required": True, "used_in": sorted(files)}
        for name, files in sorted(found.items())
    ]


def scan_secrets(root: Path, inv: Inventory) -> None:
    for path in walk_project(root):
        rel = path.relative_to(root)
        for pat in SECRET_FILENAME_PATTERNS:
            if pat.match(path.name):
                if path.name == ".env.example":
                    continue
                warn(inv, f"potential secret file ignored: {rel}")
                break
        else:
            if path.suffix in SOURCE_EXTENSIONS or path.suffix in {".yaml", ".yml", ".json", ".toml"}:
                try:
                    text = path.read_text(errors="ignore")
                except Exception:
                    continue
                if SECRET_CONTENT_RE.search(text):
                    warn(inv, f"potential secret content in: {rel}")


def count_todos(root: Path, inv: Inventory) -> None:
    todo_re = re.compile(r"\b(TODO|FIXME|XXX|HACK)\b")
    count = 0
    for path in walk_project(root):
        if path.suffix not in SOURCE_EXTENSIONS:
            continue
        try:
            text = path.read_text(errors="ignore")
        except Exception:
            continue
        count += len(todo_re.findall(text))
    inv.issues["todos"] = count


def build_tree(root: Path, depth: int = 3) -> str:
    lines = []

    def walk(path: Path, prefix: str, level: int) -> None:
        if level > depth:
            return
        entries = sorted(
            [p for p in path.iterdir() if p.name not in IGNORE_DIRS and not p.name.startswith(".")],
            key=lambda p: (p.is_file(), p.name),
        )
        for i, entry in enumerate(entries[:20]):
            connector = "└── " if i == len(entries) - 1 else "├── "
            lines.append(f"{prefix}{connector}{entry.name}{'/' if entry.is_dir() else ''}")
            if entry.is_dir():
                extension = "    " if i == len(entries) - 1 else "│   "
                walk(entry, prefix + extension, level + 1)

    lines.append(f"{root.name}/")
    walk(root, "", 1)
    return "\n".join(lines)


def inspect(root: Path) -> Inventory:
    inv = Inventory()
    inv.project = {
        "name": root.name,
        "path": str(root.resolve()),
        "git": collect_git_state(root),
    }
    detect_node(root, inv)
    detect_python(root, inv)
    detect_hugo(root, inv)
    detect_go(root, inv)
    scan_env_vars(root, inv)
    scan_secrets(root, inv)
    count_todos(root, inv)
    file_count = sum(1 for _ in walk_project(root))
    inv.structure = {
        "tree_depth_3": build_tree(root, depth=3),
        "file_count": file_count,
        "loc_estimate": _estimate_loc(root),
    }
    if not inv.stack.get("languages"):
        warn(inv, "no known stack detected")
    return inv


def _estimate_loc(root: Path) -> int:
    total = 0
    for path in walk_project(root):
        if path.suffix not in SOURCE_EXTENSIONS:
            continue
        try:
            total += sum(1 for _ in path.open(errors="ignore"))
        except Exception:
            continue
    return total


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("project", type=Path)
    ap.add_argument("--out", type=Path, default=None)
    args = ap.parse_args()
    if not args.project.is_dir():
        print(f"not a directory: {args.project}", file=sys.stderr)
        return 2
    inv = inspect(args.project)
    data = asdict(inv)
    text = json.dumps(data, indent=2, ensure_ascii=False)
    if args.out:
        args.out.write_text(text)
    else:
        print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
