#!/usr/bin/env bash
# Reproduceer jimvandenbreemen.nl op een schone machine.
# Idempotent: tweede keer draaien is veilig.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="${SCRIPT_DIR}"

log() { printf '\033[34m==>\033[0m %s\n' "$*"; }
warn() { printf '\033[33mWARN:\033[0m %s\n' "$*" >&2; }
fail() { printf '\033[31mERROR:\033[0m %s\n' "$*" >&2; exit 1; }

# 1. Prerequisites check
log "Prerequisites check"
command -v hugo >/dev/null 2>&1 || fail "hugo niet gevonden"

# 2. Runtime install (via mise als beschikbaar)
if command -v mise >/dev/null 2>&1; then
    log "mise gevonden, runtime installeren"
    mise install || warn "mise install failed, controleer .tool-versions"
else
    warn "mise niet geinstalleerd. Zorg handmatig voor: hugo >=0.120"
fi

# 3. Dependencies installeren
log "Dependencies installeren"
# Hugo heeft geen install step; zorg dat 'hugo' in PATH staat

# 4. Env config
log "Env config controleren"
if [ ! -f "${PROJECT_DIR}/.env" ] && [ -f "${PROJECT_DIR}/.env.example" ]; then
    cp "${PROJECT_DIR}/.env.example" "${PROJECT_DIR}/.env"
    warn ".env aangemaakt vanuit .env.example. Vul de waarden in voordat je doorgaat."
fi

# 5. Smoke test
log "Smoke test"
hugo server -D

log "Klaar. Zie HANDOFF.md voor volgende stappen."
