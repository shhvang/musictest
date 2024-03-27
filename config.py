import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Telegram API credentials
API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN")

# Telegram credentials
OWNER_ID = int(getenv("OWNER_ID", 5552153244))
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/IOUpdate")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/IOSupportGroup")
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "https://t.me/IOLogs"))

# Bot Settings
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 600))
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", True)
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "5400"))

PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", 700))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", 700))

AUDIO_FILESIZE_LIMIT = int(getenv("AUDIO_FILESIZE_LIMIT", 104857600))
VIDEO_FILESIZE_LIMIT = int(getenv("VIDEO_FILESIZE_LIMIT", 1073741824))

# Database credentials
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

# Heroku credentials
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv("UPSTREAM_REPO","https://github.com/shhvang/iMusic")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "alpha")
GIT_TOKEN = getenv("GIT_TOKEN", None) 
# Fill this variable if your upstream repository is private

# Spotify credentials
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

# String Sessions
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

# Extras
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# Image Resources
START_IMAGE = getenv("START_IMG_URL", "https://telegra.ph/file/06fa3c0a658d5db463b58.jpg")
PING_IMAGE = getenv("PING_IMG_URL", "https://telegra.ph/file/e2ca803b13b7370b9c28a.jpg")

PLAY_IMAGE = "https://telegra.ph/file/cb1947522c0de4c4a63e8.jpg"
STATS_IMAGE = "https://telegra.ph/file/e2ca803b13b7370b9c28a.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/b8a11557d6d1020a04dc1.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/b8a11557d6d1020a04dc1.jpg"
YOUTUBE_IMAGE = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
SPOTIFY_ARTIST_IMAGE = "https://telegra.ph/file/6052dacda8d125f73bf4f.jpg"
SPOTIFY_ALBUM_IMAGE = "https://telegra.ph/file/c1502ac3e1ff972c95c08.jpg"
SPOTIFY_PLAYLIST_IMAGE = "https://telegra.ph/file/bf9ced2e71fae8dbe4e09.jpg"

# Ignore
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )