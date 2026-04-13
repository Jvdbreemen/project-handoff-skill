#!/usr/bin/env bash
# Reproduceer python-cli op een schone machine.
# Idempotent: tweede keer draaien is veilig.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="${SCRIPT_DIR}"

log() { printf '\033[34m==>\033[0m %s\n' "$*"; }
warn() { printf '\033[33mWARN:\033[0m %s\n' "$*" >&2; }
fail() { printf '\033[31mERROR:\033[0m %s\n' "$*" >&2; exit 1; }

# 1. Prerequisites check
log "Prerequisites check"
command -v python >/dev/null 2>&1 || fail "python niet gevonden"

# 2. Runtime install (via mise als beschikbaar)
if command -v mise >/dev/null 2>&1; then
    log "mise gevonden, runtime installeren"
    mise install || warn "mise install failed, controleer .tool-versions"
else
    warn "mise niet geinstalleerd. Zorg handmatig voor: python >=3.11"
fi

# 3. Dependencies installeren
log "Dependencies installeren"
pip install

# 4. Env config
log "Env config controleren"
if [ ! -f "${PROJECT_DIR}/.env" ] && [ -f "${PROJECT_DIR}/.env.example" ]; then
    cp "${PROJECT_DIR}/.env.example" "${PROJECT_DIR}/.env"
    warn ".env aangemaakt vanuit .env.example. Vul de waarden in voordat je doorgaat."
fi

# 5. Smoke test
log "Smoke test"
echo "geen smoke test gedefinieerd"

log "Klaar. Zie HANDOFF.md voor volgende stappen."
