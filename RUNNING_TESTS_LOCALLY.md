# Running the Fabric tests locally (step by step)

How to run the Fabric integration tests on your own machine from scratch.
The tests are **on-demand** — a plain `pytest` does not run them.

> Run every command from the repo root:
> `~/PycharmProjects/equinix-sdk-python`

---

## 0. Prerequisites

- **Python 3.10** (see `.python-version`).
- Network access (corporate VPN) to the Fabric environment you test against
  (`ENV_URL`, e.g. `https://uatapi.equinix.com`).
- The **test-data JSON** (credentials per user). See step 3.

---

## 1. Virtualenv + dependencies

```bash
# venv (a .venv already exists in the repo; from scratch:)
python3 -m venv .venv
source .venv/bin/activate

# the SDK in editable mode + test deps (pytest, requests)
pip install --upgrade pip
pip install -e .
pip install -r tests/requirements.txt
```

Confirm the SDK imports:

```bash
python -c "from equinix.services import fabricv4; print('SDK import OK')"
```

---

## 2. Quick sanity check (no network)

Confirms the tests are collected correctly and **skipped by default**:

```bash
pytest -q                                   # -> deselected  (not run on a build)
pytest -m integration --collect-only -q     # -> lists the tests
```

---

## 3. Provide the test data (`env.json`)

The tests read user credentials from a JSON document. Save it as **`env.json`**
(or `file.json`) in the repo root — the suite auto-loads it. This is the same
content stored in CI as the `TEST_DATA_UAT` GitHub secret.

Preferred shape — keyed by user name (`fcr` / `fnv`). You may put `envUrl`
next to the users instead of exporting `ENV_URL`:

```json
{
  "envUrl": "https://uatapi.equinix.com",
  "fnv": {
    "client_id": "...",
    "client_secret": "...",
    "projectId": "...",
    "accountNumberEIA": "...",
    "iaProfileUuid": "..."
  },
  "fcr": {
    "client_id": "...",
    "client_secret": "...",
    "projectId": "..."
  }
}
```

The legacy shape `{"users": [{"name": "fnv", ...}]}` is also accepted. A user
value may be a JSON-encoded string, and field names may be snake_case or
camelCase (`client_id`/`clientId`, etc.).

How the tests resolve data (in order):
1. the `TEST_DATA_UAT_USERS` env var (if set), otherwise
2. a JSON file — `TEST_DATA_FILE`, else `env.json`/`file.json` in the cwd, then
   the repo root.

> The user key in the JSON (`fnv`/`fcr`) must match the one the test uses.
> `test_internet_access_api.py` uses `UserName.PANTHERS_FNV` → key `"fnv"`.

---

## 4. Environment base URL

If you didn't put `envUrl` in the data file, export it:

```bash
export ENV_URL="https://uatapi.equinix.com"
```

---

## 5. Run the tests

```bash
./run_fabric_tests.sh
```

The script activates `.venv`, checks that test data (env var or data file) and
a base URL are available, then runs `pytest -m integration -v`.

Filtering / extra args pass through to pytest:

```bash
./run_fabric_tests.sh -k test_3                              # one scenario
./run_fabric_tests.sh tests/services/fabricv4/test_internet_access_api.py
./run_fabric_tests.sh -s                                     # show print()/logs live
```

Or without the script:

```bash
pytest -m integration -v
```

---

## See the HTTP requests (logging)

Set `FABRIC_DEBUG` to log every request, its **body**, and the **response**:

```bash
FABRIC_DEBUG=1 ./run_fabric_tests.sh
```

Example output (run script adds `-s` so logs stream live):

```
fabric.http INFO --> POST https://uatapi.equinix.com/fabric/v4/ports/search
fabric.http INFO     request body: {'filter': {'or': [...]}, 'pagination': {...}}
fabric.http INFO <-- POST .../fabric/v4/ports/search -> HTTP 200
fabric.http INFO     response body: {"pagination":{...},"data":[...]}
```

- `FABRIC_DEBUG=1` — request URL + request body + response status + response
  body. Headers are **not** logged, so the auth token never appears.
- `FABRIC_LOG_MAXLEN` — truncate logged bodies to N chars (default 2000;
  `0` = no truncation), e.g. `FABRIC_LOG_MAXLEN=0 FABRIC_DEBUG=1 ./run_fabric_tests.sh`.
- `FABRIC_DEBUG=body` — additionally dumps full headers. **Debugging only** —
  this prints the `Authorization: Bearer ...` header.

A non-2xx status in the log is a failed request; the test assertion then
reports the failure (`with_http_info` calls assert on the status code).

---

## Test reports

`run_fabric_tests.sh` always writes three reports into `./reports/` (git-ignored):

| File | Format | Use |
|---|---|---|
| `reports/fabric-tests.xml`  | JUnit XML | CI (GitHub Actions, Jenkins) |
| `reports/fabric-tests.html` | HTML (self-contained) | open in a browser |
| `reports/fabric-tests.json` | JSON | machine-readable / dashboards |

Change the directory with `REPORTS_DIR=out ./run_fabric_tests.sh`.

---

## All in one (shortcut)

```bash
source .venv/bin/activate
# put the test-data JSON in env.json (repo root), then:
export ENV_URL="https://uatapi.equinix.com"   # or add "envUrl" to env.json
./run_fabric_tests.sh                          # data file auto-loaded
```

---

## Troubleshooting

| Symptom | Cause / fix |
|---|---|
| `skipped` instead of running | no test data or base URL — provide `env.json` and `ENV_URL` (steps 3–4) |
| `User 'fnv' not found` | the user key in the JSON doesn't match the `UserName` used by the test |
| `401/403` from the Fabric API | wrong `client_id`/`client_secret` or wrong `ENV_URL` |
| timeout / no connection to `ENV_URL` | not on the corporate VPN |
| import error `equinix.services.fabricv4` | running on code before the SDK fixes — update your branch |

> `env.json` / `file.json` contain secrets — do not commit them (they are
> git-ignored).
