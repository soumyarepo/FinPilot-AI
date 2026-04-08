#!/usr/bin/env bash
set -euo pipefail
curl -fsS "${1:-http://localhost:8080/health}"
echo
