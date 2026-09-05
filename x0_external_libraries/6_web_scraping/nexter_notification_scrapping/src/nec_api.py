from __future__ import annotations

import logging
from typing import Any

import requests

from .config import NEC_API_URL, REQUEST_TIMEOUT_SECONDS

logger = logging.getLogger(__name__)


class NecApiError(RuntimeError):
    """Raised when the NEC API cannot provide a valid response."""


def _notice_list(value: Any) -> list[dict[str, Any]]:
    if not isinstance(value, list):
        return []
    return [notice for notice in value if isinstance(notice, dict)]


def _extract_notice_payloads(payload: Any) -> list[dict[str, Any]]:
    if not isinstance(payload, list):
        raise NecApiError("Unexpected NEC response: expected a tRPC batch list")

    notices: list[dict[str, Any]] = []
    for index in (0, 3, 4):
        if index >= len(payload) or not isinstance(payload[index], dict):
            continue
        result = payload[index].get("result")
        if not isinstance(result, dict):
            continue
        data = result.get("data")
        if index == 3 and isinstance(data, dict):
            notices.extend(_notice_list(data.get("notices")))
        else:
            notices.extend(_notice_list(data))
    return notices


def normalize_notices(payload: Any) -> list[dict[str, Any]]:
    """Convert the observed NEC tRPC batch response to stable notice records."""
    normalized: list[dict[str, Any]] = []
    seen_ids: set[str] = set()
    for notice in _extract_notice_payloads(payload):
        notice_id = notice.get("_id")
        title = notice.get("title")
        if not isinstance(notice_id, str) or not notice_id:
            logger.warning("Skipping NEC notice without a valid _id")
            continue
        if not isinstance(title, str):
            logger.warning("Skipping NEC notice %s without a valid title", notice_id)
            continue
        if notice_id in seen_ids:
            continue
        seen_ids.add(notice_id)
        normalized.append(
            {
                "_id": notice_id,
                "title": title,
                "createdAt": notice.get("createdAt"),
                "attachments": notice.get("attachments", []),
            }
        )
    return normalized


def fetch_notices(
    url: str = NEC_API_URL,
    timeout: int = REQUEST_TIMEOUT_SECONDS,
    session: Any = requests,
) -> list[dict[str, Any]]:
    """Fetch, validate, and normalize notices from NEC."""
    try:
        response = session.get(url, timeout=timeout)
        response.raise_for_status()
        payload = response.json()
    except requests.RequestException as error:
        raise NecApiError(f"NEC request failed: {error}") from error
    except ValueError as error:
        raise NecApiError("NEC returned invalid JSON") from error

    return normalize_notices(payload)
