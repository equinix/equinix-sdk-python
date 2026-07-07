import logging
import os

import pytest

from services.fabricv4.helpers import utils

_DEBUG_OFF = {"", "0", "false", "off", "no"}


def pytest_configure(config):
    # Always emit request/response logs at INFO so pytest captures them into the
    # reports (junit/html), regardless of FABRIC_DEBUG.
    logging.getLogger("fabric.http").setLevel(logging.INFO)

    mode = os.getenv("FABRIC_DEBUG", "").strip().lower()
    if mode in _DEBUG_OFF:
        return
    # FABRIC_DEBUG only adds LIVE console output (and urllib3 / header dumps).
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s"))
    for name in ("fabric.http", "urllib3"):
        log = logging.getLogger(name)
        log.setLevel(logging.DEBUG)
        log.addHandler(handler)
    if mode in ("body", "full", "2"):
        import http.client as http_client
        http_client.HTTPConnection.debuglevel = 1


def pytest_collection_modifyitems(config, items):
    missing = []
    if not utils.test_data_available():
        missing.append("test data (TEST_DATA_UAT_USERS or env.json)")
    if not utils.env_url_available():
        missing.append("base URL (ENV_URL or envUrl in the data file)")
    if not missing:
        return
    skip_integration = pytest.mark.skip(
        reason=f"integration prerequisites missing: {', '.join(missing)}"
    )
    for item in items:
        if "integration" in item.keywords:
            item.add_marker(skip_integration)
