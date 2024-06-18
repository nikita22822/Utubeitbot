import re, os, time
import datetime


id_pattern = re.compile(r'^.\d+$') 


class Config:

    BOT_TOKEN = os.environ.get("7242829555:AAF_3l-ccXL2xxu12YTctCbHuE3a4atkLko")

    SESSION_NAME = ":memory:"

    API_ID = int(os.environ.get("23682259"))

    API_HASH = os.environ.get("2d37bb900bfa753d546ba475d8deb35a")

    CLIENT_ID = os.environ.get("648958063480-29qgcobnmodbidbovgtvlhtpve3netjk.apps.googleusercontent.com")

    CLIENT_SECRET = os.environ.get("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")

    BOT_OWNER = int(os.environ.get("@nikita20056")
    
    BOT_START_TIME = time.time()
    
    BOT_START_DATETIME = datetime.datetime.now().strftime("%B %d, %Y %I:%M:%S %p")

    DB_NAME = os.environ.get("DB_NAME", "Utubeitbot")  

    DB_URL = os.environ.get("DB_URL")

    SUPPORT_CHAT_LINK = os.environ.get("SUPPORT_CHAT_LINK")

    AUTH_USERS_TEXT = os.environ.get("AUTH_USERS", "")

    AUTH_USERS = [BOT_OWNER, 754495556] + (
        [int(user.strip()) for user in AUTH_USERS_TEXT.split(",")]
        if AUTH_USERS_TEXT
        else []
    )

    VIDEO_DESCRIPTION = (
        os.environ.get("VIDEO_DESCRIPTION", "").replace("<", "").replace(">", "")
    )

    VIDEO_CATEGORY = (
        int(os.environ.get("VIDEO_CATEGORY")) if os.environ.get("VIDEO_CATEGORY") else 0
    )

    VIDEO_TITLE_PREFIX = os.environ.get("VIDEO_TITLE_PREFIX", "")

    VIDEO_TITLE_SUFFIX = os.environ.get("VIDEO_TITLE_SUFFIX", "")

    DEBUG = bool(os.environ.get("DEBUG"))

    UPLOAD_MODE = os.environ.get("UPLOAD_MODE") or False
    if UPLOAD_MODE:
        if UPLOAD_MODE.lower() in ["private", "public", "unlisted"]:
            UPLOAD_MODE = UPLOAD_MODE.lower()
        else:
            UPLOAD_MODE = False

    CRED_FILE = "auth_token.txt"
