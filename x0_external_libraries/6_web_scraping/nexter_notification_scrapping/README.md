# NEC Notice Notification Worker

This worker checks the Nepal Engineering Council (NEC) public API every five minutes and sends a Firebase Cloud Messaging (FCM) notification when a new notice title contains `साधारण दर्तावाला`.

## Architecture

The worker fetches the NEC batched tRPC response, normalizes notice records, filters by the required title keyword, claims each new NEC `_id` in Firestore, sends an FCM topic notification, and marks the notice as processed only after FCM succeeds.

The parser currently uses the observed response entries from the requested endpoint:

- `notice.getLatestNoticesPublic` at batch index `0`
- `notice.getNoticesPublic` at batch index `3`, under `result.data.notices`
- `notice.getPopupNoticesPublic` at batch index `4`

Duplicate records across those entries are removed using the NEC `_id`.

## Configuration

The non-secret configuration is in `src/config.py`:

- NEC API: the exact batched endpoint requested for this worker
- Keyword: `साधारण दर्तावाला`
- FCM topic: `nec_exam_notifications`
- Firestore collection: `nec_processed_notices`

Each processed notice is stored with its NEC `_id` as the Firestore document ID, along with its title, creation time, processing time, and status.

## Firebase credentials

Never commit a Firebase service-account file, `.env` file, private key, or client email. The public GitHub repository expects the complete service-account JSON in the repository secret named `FIREBASE_SERVICE_ACCOUNT`.

For local development, copy the provided `.env` template and set `GOOGLE_APPLICATION_CREDENTIALS` to the path of a service-account JSON file stored outside this repository. Alternatively, set `FIREBASE_SERVICE_ACCOUNT` to the JSON service-account contents. No credentials are required for the unit tests. The application loads `.env` automatically.

The FCM notification uses title `NEC Exam Notice` and the actual NEC notice title as its body. Its data contract for the Flutter app is:

- `type=nec_notice`
- `action=open_notice`
- `screen=nec_notice`
- `notice_id=<NEC _id>`
- `notice_title=<notice title>`
- `attachment_path`, `attachment_file_name`, and `attachment_media_type` when supplied by NEC

The app should handle `screen == "nec_notice"` by opening its NEC notice screen and use `notice_id` to load or identify the notice. Attachment values are the paths returned by NEC; the worker does not invent a public URL.

## GitHub Actions deployment

1. Add the `FIREBASE_SERVICE_ACCOUNT` repository secret in GitHub.
2. Ensure the Firebase service account can send FCM messages and access the Firestore database.
3. Enable GitHub Actions for the repository.

The workflow in `.github/workflows/check_nec.yml` runs on Python 3.12 every five minutes and also supports `workflow_dispatch` for manual runs. It is a short-lived worker; no server process is required.

## Local development

```text
python -m venv .venv
.venv\\Scripts\\activate       # Windows
python -m pip install -r requirements.txt
python -m src.main
```

The provided `.env` enables `LOCAL_TEST_MODE=true`, so this command does not initialize Firebase or require credentials. It writes processed NEC IDs to `processed_notice_ids.txt` and notification JSON lines to `notification_data.txt`. Run it again to confirm previously stored IDs are skipped.

Set `LOCAL_TEST_MODE=false` when you want to run against real Firestore and FCM using the Firebase credentials described above.

## Testing

```text
python -m pytest -q
```

Tests mock external behavior and do not send FCM messages or require production credentials.

## Security and failure behavior

The worker uses the NEC `_id`, never a title or timestamp, for duplicate detection. A failed NEC request, Firestore operation, or FCM send is logged and causes the run to fail or release its in-progress claim; failed notifications are not left marked as processed, allowing a later scheduled run to retry.
