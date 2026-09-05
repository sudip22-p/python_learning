from __future__ import annotations

import json
import logging
import os
from typing import Any

import firebase_admin
from dotenv import load_dotenv
from firebase_admin import credentials, messaging

from .config import FCM_NOTIFICATION_TITLE, FCM_TOPIC
from .notification import build_notification_data

logger = logging.getLogger(__name__)


def initialize_firebase() -> Any:
    """Initialize Firebase from the GitHub secret or local ADC configuration."""
    load_dotenv()
    if firebase_admin._apps:
        return firebase_admin.get_app()

    service_account_json = os.getenv("FIREBASE_SERVICE_ACCOUNT")
    if service_account_json:
        try:
            credential = credentials.Certificate(json.loads(service_account_json))
        except (TypeError, ValueError, json.JSONDecodeError) as error:
            raise RuntimeError("FIREBASE_SERVICE_ACCOUNT is not valid JSON") from error
        return firebase_admin.initialize_app(credential)

    return firebase_admin.initialize_app()


def send_notice_notification(notice: dict[str, Any]) -> str:
    initialize_firebase()
    notice_id = notice["_id"]
    message_data = build_notification_data(notice)

    message = messaging.Message(
        notification=messaging.Notification(
            title=FCM_NOTIFICATION_TITLE,
            body=notice["title"],
        ),
        data=message_data,
        topic=FCM_TOPIC,
    )
    return messaging.send(message)
