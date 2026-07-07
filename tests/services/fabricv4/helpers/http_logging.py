from __future__ import annotations

import logging
import os

logger = logging.getLogger("fabric.http")


def _max_len() -> int:
    try:
        return int(os.getenv("FABRIC_LOG_MAXLEN", "2000"))
    except ValueError:
        return 2000


def _to_text(value) -> str:
    if value is None:
        return ""
    if isinstance(value, (bytes, bytearray)):
        return value.decode("utf-8", "replace")
    return str(value)


def _truncate(text: str) -> str:
    limit = _max_len()
    if limit and len(text) > limit:
        return f"{text[:limit]}... [{len(text)} chars total]"
    return text


def enable(api_client) -> None:
    rest_client = api_client.rest_client
    if getattr(rest_client, "_fabric_logging_wrapped", False):
        return
    original = rest_client.request

    def logged_request(method, url, headers=None, body=None,
                       post_params=None, _request_timeout=None):
        logger.info("--> %s %s", method, url)
        if body is not None:
            logger.info("    request body: %s", _truncate(_to_text(body)))
        if post_params:
            logger.info("    form params: %s", _truncate(_to_text(post_params)))
        response = original(
            method, url, headers=headers, body=body,
            post_params=post_params, _request_timeout=_request_timeout,
        )
        try:
            text = _to_text(response.read())
        except Exception:  # noqa: BLE001 - logging must never break the request
            text = "<unreadable response body>"
        logger.info("<-- %s %s -> HTTP %s", method, url, response.status)
        logger.info("    response body: %s", _truncate(text))
        return response

    rest_client.request = logged_request
    rest_client._fabric_logging_wrapped = True
