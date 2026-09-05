from __future__ import annotations

import logging
from typing import Any, Callable

from .config import (
    LOCAL_NOTIFICATION_DATA_FILE,
    LOCAL_PROCESSED_IDS_FILE,
    LOCAL_TEST_MODE,
    NOTICE_KEYWORD,
)
from .firebase import send_notice_notification
from .firestore import ProcessedNoticeStore
from .local_testing import LocalNoticeStore, save_local_notification
from .nec_api import fetch_notices

logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


def is_relevant_notice(notice: dict[str, Any]) -> bool:
    title = notice.get("title", "")
    return isinstance(title, str) and NOTICE_KEYWORD in title


def process_notices(
    fetch: Callable[[], list[dict[str, Any]]] = fetch_notices,
    store: ProcessedNoticeStore | None = None,
    send: Callable[[dict[str, Any]], str] = send_notice_notification,
) -> int:
    logger.info("Fetching notices from NEC")
    notices = fetch()
    logger.info("Retrieved %d notices", len(notices))
    relevant = [notice for notice in notices if is_relevant_notice(notice)]
    logger.info("Found %d relevant notice(s)", len(relevant))
    store = store or ProcessedNoticeStore()
    sent_count = 0

    for notice in relevant:
        notice_id = notice.get("_id")
        if not isinstance(notice_id, str) or not notice_id:
            logger.warning("Skipping relevant notice without _id")
            continue
        logger.info("Checking notice ID: %s", notice_id)
        if not store.claim(notice_id):
            logger.info("Notice already processed or in progress, skipping")
            continue
        try:
            logger.info("New NEC notice found: %s", notice_id)
            logger.info("Sending FCM notification")
            send(notice)
            logger.info("FCM notification sent successfully")
            store.mark_processed(notice)
            sent_count += 1
            logger.info("Notice marked as processed")
        except Exception:
            logger.exception("Failed to process notice %s", notice_id)
            try:
                store.release(notice_id)
            except Exception:
                logger.exception("Failed to release notice claim %s", notice_id)
            raise

    if sent_count == 0:
        logger.info("No new notices found")
    return sent_count


def main() -> None:
    logger.info("Starting NEC notice checker")
    if LOCAL_TEST_MODE:
        logger.info("LOCAL_TEST_MODE enabled; Firebase is disabled")
        store = LocalNoticeStore(
            LOCAL_PROCESSED_IDS_FILE,
            LOCAL_NOTIFICATION_DATA_FILE,
        )
        process_notices(
            store=store,
            send=lambda notice: save_local_notification(
                notice,
                LOCAL_NOTIFICATION_DATA_FILE,
            ),
        )
        return
    process_notices()


if __name__ == "__main__":
    main()
