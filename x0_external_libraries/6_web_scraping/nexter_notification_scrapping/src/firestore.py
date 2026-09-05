from __future__ import annotations

import logging
import time
from datetime import datetime, timezone
from typing import Any

from google.cloud import firestore

from .config import FIRESTORE_COLLECTION, PROCESSING_LEASE_SECONDS
from .firebase import initialize_firebase

logger = logging.getLogger(__name__)


class ProcessedNoticeStore:
    def __init__(self, client: Any | None = None, collection: str = FIRESTORE_COLLECTION):
        if client is None:
            initialize_firebase()
            client = firestore.Client()
        self._collection = client.collection(collection)

    def claim(self, notice_id: str) -> bool:
        """Atomically claim a notice, allowing recovery from stale in-flight work."""
        reference = self._collection.document(notice_id)
        transaction = self._collection._client.transaction()

        @firestore.transactional
        def claim_transaction(transaction: Any) -> bool:
            snapshot = reference.get(transaction=transaction)
            if snapshot.exists:
                data = snapshot.to_dict() or {}
                if data.get("status") == "processed":
                    return False
                started = data.get("processing_started_at")
                if isinstance(started, datetime):
                    age = time.time() - started.timestamp()
                    if age < PROCESSING_LEASE_SECONDS:
                        return False
                transaction.delete(reference)
            transaction.create(
                reference,
                {
                    "notice_id": notice_id,
                    "status": "processing",
                    "processing_started_at": datetime.now(timezone.utc),
                },
            )
            return True

        return claim_transaction(transaction)

    def mark_processed(self, notice: dict[str, Any]) -> None:
        reference = self._collection.document(notice["_id"])
        reference.set(
            {
                "notice_id": notice["_id"],
                "title": notice["title"],
                "created_at": notice.get("createdAt"),
                "processed_at": firestore.SERVER_TIMESTAMP,
                "status": "processed",
            },
            merge=True,
        )

    def release(self, notice_id: str) -> None:
        self._collection.document(notice_id).delete()
