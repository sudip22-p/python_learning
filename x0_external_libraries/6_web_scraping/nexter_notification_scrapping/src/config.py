import os

from dotenv import load_dotenv

load_dotenv()

NEC_API_URL = (
    "https://nec.gov.np/api/trpc/"
    "notice.getLatestNoticesPublic,banner.getBannersPublic,"
    "category.getActiveCategories,notice.getNoticesPublic,"
    "notice.getPopupNoticesPublic?batch=1&input=%7B%221%22%3A%7B"
    "%22bannerStatus%22%3A%22ACTIVE%22%7D%2C%222%22%3A%7B%22serviceType%22%3A%22notice%22%7D%2C"
    "%223%22%3A%7B%22page%22%3A1%2C%22limit%22%3A4%2C%22sortBy%22%3A%22createdAt%22%2C"
    "%22sortOrder%22%3A%22desc%22%7D%7D"
)
NOTICE_KEYWORD = "साधारण दर्तावाला"
FCM_TOPIC = "nec_exam_notifications"
FIRESTORE_COLLECTION = "nec_processed_notices"
FCM_NOTIFICATION_TITLE = "NEC Exam Notice"
REQUEST_TIMEOUT_SECONDS = 30
PROCESSING_LEASE_SECONDS = 600
LOCAL_TEST_MODE = os.getenv("LOCAL_TEST_MODE", "false").lower() == "true"
LOCAL_PROCESSED_IDS_FILE = "processed_notice_ids.txt"
LOCAL_NOTIFICATION_DATA_FILE = "notification_data.txt"
