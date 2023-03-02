import os

class Config:
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6109967361:AAEXZWE1hSoeHeadEDCiEyZMMuIoF7BDH8w")
    API_ID = int(os.environ.get("API_ID", "29138904"))
    API_HASH = os.environ.get("API_HASH", "0cdbc65bf2e0984ad00464dfd871e90c")
    BOT_OWNER = os.environ.get("BOT_OWNER", "WinstonAndMee")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "ModernSongBot")
    PLAYLIST_NAME = os.environ.get("PLAYLIST_NAME", "NewModernBlog")
    CHANNEL = os.environ.get("CHANNEL", "NewModernBlog")
    PLAYLIST_ID = int(os.environ.get("PLAYLIST_ID", "-1001705079927"))
