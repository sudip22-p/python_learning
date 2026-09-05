from src.nec_api import normalize_notices


def test_normalize_observed_batched_response_and_deduplicates_ids():
    notice = {
        "_id": "ABC123",
        "title": "साधारण दर्तावाला सूचना",
        "createdAt": "2026-09-01T10:00:00.000Z",
        "attachments": [{"fileName": "notice.pdf", "image": "/uploads/notice.pdf"}],
    }
    payload = [
        {"result": {"data": [notice]}},
        {"result": {"data": {"banners": []}}},
        {"result": {"data": []}},
        {"result": {"data": {"notices": [notice]}}},
        {"result": {"data": [notice]}},
    ]

    assert normalize_notices(payload) == [notice]


def test_normalize_skips_notice_without_id_or_title():
    payload = [
        {"result": {"data": [{"title": "missing id"}, {"_id": "ABC"}]}},
        {},
        {},
        {},
        {},
    ]

    assert normalize_notices(payload) == []