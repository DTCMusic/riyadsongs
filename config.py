import os

class Config:
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5809046574:AAFJ2sKtZ33gB_qYEO8loCWprz1dbldG9R8")
    API_ID = int(os.environ.get("API_ID", "12878302"))
    API_HASH = os.environ.get("API_HASH", "1ce756e879790d465304f48c36294883")
    BOT_OWNER = os.environ.get("BOT_OWNER", "RiyadAndMe")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "DTGSongBot")
    PLAYLIST_NAME = os.environ.get("PLAYLIST_NAME", "RiyaddBlogg")
    CHANNEL = os.environ.get("CHANNEL", "RiyaddBlogg")
    PLAYLIST_ID = int(os.environ.get("PLAYLIST_ID", "-1001726242069"))
