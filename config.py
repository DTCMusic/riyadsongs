import os

class Config:
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5831058141:AAHzICeQsVgmkH6GDgAhHNA_vYkLZ-naa4U")
    API_ID = int(os.environ.get("API_ID", "16102648"))
    API_HASH = os.environ.get("API_HASH", "378a73e340eb634cf67c8c42bafa9f37")
    BOT_OWNER = os.environ.get("BOT_OWNER", "RiyadAndMe")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "N1SongBot")
    PLAYLIST_NAME = os.environ.get("PLAYLIST_NAME", "RiyaddBlogg")
    CHANNEL = os.environ.get("CHANNEL", "RiyaddBlogg")
    PLAYLIST_ID = int(os.environ.get("PLAYLIST_ID", "-1001726242069"))
