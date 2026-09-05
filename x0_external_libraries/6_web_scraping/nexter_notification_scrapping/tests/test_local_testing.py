import json

from src.local_testing import LocalNoticeStore, save_local_notification


def test_local_store_persists_ids_and_notification_payload(tmp_path):
    ids_file = tmp_path / "processed_notice_ids.txt"
    notification_file = tmp_path / "notification_data.txt"
    notice = {
        "_id": "ABC123",
        "title": "साधारण दर्तावाला सूचना",
        "createdAt": "2026-09-01T10:00:00.000Z",
        "attachments": [],
    }
    store = LocalNoticeStore(str(ids_file), str(notification_file))

    assert store.claim("ABC123")
    save_local_notification(notice, str(notification_file))
    store.mark_processed(notice)
    assert not store.claim("ABC123")
    assert ids_file.read_text(encoding="utf-8").strip() == "ABC123"

    payload = json.loads(notification_file.read_text(encoding="utf-8"))
    assert payload["data"] == {
        "type": "nec_notice",
        "action": "open_notice",
        "screen": "nec_notice",
        "notice_id": "ABC123",
        "notice_title": "साधारण दर्तावाला सूचना",
    }
    assert payload["notification"]["body"] == notice["title"]