from src.notification import build_notification_data


def test_notification_data_contains_app_navigation_and_attachment_data():
    notice = {
        "_id": "ABC123",
        "title": "साधारण दर्तावाला सूचना",
        "attachments": [
            {
                "image": "/uploads/Notice/notice.pdf",
                "fileName": "notice.pdf",
                "mediaType": "PDF",
            }
        ],
    }

    assert build_notification_data(notice) == {
        "type": "nec_notice",
        "action": "open_notice",
        "screen": "nec_notice",
        "notice_id": "ABC123",
        "notice_title": "साधारण दर्तावाला सूचना",
        "attachment_path": "/uploads/Notice/notice.pdf",
        "attachment_file_name": "notice.pdf",
        "attachment_media_type": "PDF",
    }