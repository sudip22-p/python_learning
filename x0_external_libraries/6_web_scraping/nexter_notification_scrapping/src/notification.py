from __future__ import annotations

from typing import Any

from .config import FCM_NOTIFICATION_TITLE


def build_notification_data(notice: dict[str, Any]) -> dict[str, str]:
    """Build the data contract consumed by the Flutter notification handler."""
    data = {
        "type": "nec_notice",
        "action": "open_notice",
        "screen": "nec_notice",
        "notice_id": notice["_id"],
        "notice_title": notice["title"],
    }
    attachments = notice.get("attachments")
    if isinstance(attachments, list) and attachments and isinstance(attachments[0], dict):
        attachment = attachments[0]
        fields = {
            "image": "attachment_path",
            "fileName": "attachment_file_name",
            "mediaType": "attachment_media_type",
        }
        for source, target in fields.items():
            value = attachment.get(source)
            if isinstance(value, str) and value:
                data[target] = value
    return data


def build_notification_payload(notice: dict[str, Any]) -> dict[str, Any]:
    return {
        "notification": {
            "title": FCM_NOTIFICATION_TITLE,
            "body": notice["title"],
        },
        "data": build_notification_data(notice),
    }