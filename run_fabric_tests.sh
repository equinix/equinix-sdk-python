#!/usr/bin/env bash
#
# Run the Fabric integration tests ON DEMAND (they are excluded from a normal
# `pytest` / build run by pytest.ini).
#
# Usage:
#   ./run_fabric_tests.sh                         # run all integration tests
#   ./run_fabric_tests.sh -k test1               # pass extra args through to pytest
#   ./run_fabric_tests.sh tests/services/fabricv4/test_internet_access_api.py
#
# Test data can come from EITHER an env var OR an env.json file:
#   TEST_DATA_UAT_USERS  JSON document with the per-user credentials, or
#   env.json             the same JSON written to a file (repo root). May also
#                        carry an "envUrl" key.
# Base URL:
#   ENV_URL              base URL of the target environment
#                        (e.g. https://uatapi.equinix.com), or an "envUrl"
#                        key inside env.json.
#
set -euo pipefail

cd "$(dirname "$0")"

if [[ -z "${TEST_DATA_UAT_USERS:-}" && ! -f env.json ]]; then
  echo "error: no test data. Set TEST_DATA_UAT_USERS or create env.json in the repo root" >&2
  exit 1
fi
if [[ -z "${ENV_URL:-}" ]] && ! grep -q '"envUrl"' env.json 2>/dev/null; then
  echo "error: no base URL. Set ENV_URL or add an \"envUrl\" key to env.json" >&2
  exit 1
fi

# Activate the project venv if present and not already active.
if [[ -z "${VIRTUAL_ENV:-}" && -f .venv/bin/activate ]]; then
  # shellcheck disable=SC1091
  source .venv/bin/activate
fi

# With FABRIC_DEBUG set, disable output capture so request logs stream live.
EXTRA=()
if [[ -n "${FABRIC_DEBUG:-}" && "${FABRIC_DEBUG}" != "0" ]]; then
  EXTRA+=(-s)
fi

# Write JUnit XML + HTML + JSON reports into ./reports/ (override dir with REPORTS_DIR).
REPORTS_DIR="${REPORTS_DIR:-reports}"
mkdir -p "$REPORTS_DIR"
EXTRA+=(
  "--junitxml=${REPORTS_DIR}/fabric-tests.xml"
  "--html=${REPORTS_DIR}/fabric-tests.html" "--self-contained-html"
  "--json-report" "--json-report-file=${REPORTS_DIR}/fabric-tests.json"
)

# `-m integration` overrides the default `-m "not integration"` from pytest.ini.
# ${EXTRA[@]+...} guards against "unbound variable" on bash 3.2 (macOS) under set -u.
exec python -m pytest -m integration -v ${EXTRA[@]+"${EXTRA[@]}"} "$@"
