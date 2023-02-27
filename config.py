import os

class Config:
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5955684071:AAEsLBFCiZOSPSJUGjCYMHanEN0Y2QdACRw")
    API_ID = int(os.environ.get("API_ID", "29138904"))
    API_HASH = os.environ.get("API_HASH", "0cdbc65bf2e0984ad00464dfd871e90c")
    BOT_OWNER = os.environ.get("BOT_OWNER", "RiyadAndMe")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "TTKSongBot")
    PLAYLIST_NAME = os.environ.get("PLAYLIST_NAME", "RiyaddBlogg")
    CHANNEL = os.environ.get("CHANNEL", "RiyaddBlogg")
    PLAYLIST_ID = int(os.environ.get("PLAYLIST_ID", "-1001726242069"))
