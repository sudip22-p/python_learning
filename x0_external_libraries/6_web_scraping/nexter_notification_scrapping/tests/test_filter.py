import pytest

from src.main import is_relevant_notice, process_notices


class FakeStore:
    def __init__(self, processed=()):
        self.processed = set(processed)
        self.claimed = []
        self.released = []

    def claim(self, notice_id):
        if notice_id in self.processed or notice_id in self.claimed:
            return False
        self.claimed.append(notice_id)
        return True

    def mark_processed(self, notice):
        self.processed.add(notice["_id"])

    def release(self, notice_id):
        self.released.append(notice_id)
        self.claimed.remove(notice_id)


def test_keyword_matching():
    assert is_relevant_notice({"title": "साधारण दर्तावाला सम्बन्धी सूचना"})


def test_unrelated_notice_does_not_match():
    assert not is_relevant_notice({"title": "व्यावसायिक इन्जिनियरको सूचना"})


def test_empty_title_does_not_crash():
    assert not is_relevant_notice({"title": ""})
    assert not is_relevant_notice({})


def test_missing_id_is_skipped():
    store = FakeStore()
    assert process_notices(lambda: [{"title": "साधारण दर्तावाला"}], store, lambda _: None) == 0
    assert store.claimed == []


def test_existing_id_does_not_send():
    store = FakeStore(processed={"ABC123"})
    sent = []
    process_notices(
        lambda: [{"_id": "ABC123", "title": "साधारण दर्तावाला"}],
        store,
        sent.append,
    )
    assert sent == []


def test_new_id_sends_and_marks_processed():
    store = FakeStore()
    sent = []
    assert process_notices(
        lambda: [{"_id": "ABC123", "title": "साधारण दर्तावाला"}],
        store,
        sent.append,
    ) == 1
    assert [notice["_id"] for notice in sent] == ["ABC123"]
    assert "ABC123" in store.processed


def test_fcm_failure_does_not_mark_processed():
    store = FakeStore()

    def fail(_notice):
        raise RuntimeError("FCM unavailable")

    with pytest.raises(RuntimeError, match="FCM unavailable"):
        process_notices(
            lambda: [{"_id": "ABC123", "title": "साधारण दर्तावाला"}],
            store,
            fail,
        )
    assert "ABC123" not in store.processed
    assert store.released == ["ABC123"]
