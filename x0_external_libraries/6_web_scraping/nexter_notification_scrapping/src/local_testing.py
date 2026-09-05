from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .notification import build_notification_payload


class LocalNoticeStore:
    """Small file-backed substitute for Firestore during local testing."""

    def __init__(self, ids_file: str, notification_file: str):
        self.ids_file = Path(ids_file)
        self.notification_file = Path(notification_file)
        self._claims: set[str] = set()

    def _processed_ids(self) -> set[str]:
        if not self.ids_file.exists():
            return set()
        return {
            line.strip()
            for line in self.ids_file.read_text(encoding="utf-8").splitlines()
            if line.strip()
        }

    def claim(self, notice_id: str) -> bool:
        if notice_id in self._processed_ids() or notice_id in self._claims:
            return False
        self._claims.add(notice_id)
        return True

    def mark_processed(self, notice: dict[str, Any]) -> None:
        self.ids_file.parent.mkdir(parents=True, exist_ok=True)
        with self.ids_file.open("a", encoding="utf-8") as file:
            file.write(f"{notice['_id']}\n")

    def release(self, notice_id: str) -> None:
        self._claims.discard(notice_id)


def save_local_notification(notice: dict[str, Any], output_file: str) -> str:
    """Append the notification payload that would otherwise be sent through FCM."""
    payload = {
        **build_notification_payload(notice),
        "notice": notice,
    }
    path = Path(output_file)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as file:
        file.write(json.dumps(payload, ensure_ascii=False) + "\n")
    return "local-test"