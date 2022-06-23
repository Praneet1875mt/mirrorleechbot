## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQBKjaaZT7DDr71-SEcAT0g-ZfY-3iLFe0o9tIyGBO6ykifhwGzw_Ht1R8V0MUUAJcGNKs4YQqbIlApMxiMMXfJoBGQAV_4NoVXYMIHebKmSnXuqx_J9o2ORSX-YnTb0dtTz11EO9wqlxw6kjSMnsn-bcfbUzrXqRE0S2BjQasVyQunCeRqvjHP_nahn42ACN-PrDiwR7wFb7bbOWyus1mMmPVlPZiGOHCurALaXGSVQQ1XWR5oEIWZOnpjhhyrGrxC7Jg7XSBXvO_O-T0_zJxgR27_ITeIHK9TRvh9eKsDkWcJbuE2cTvXtr6rx-G-BbAeLo-MMxlki4W3GW2mh-iiAQavGuwA")
BOT_TOKEN = getenv("BOT_TOKEN", "5027556274:AAEs78T3PIfkmu2d80RZ17KqUihI1kAhtpE")
BOT_NAME = getenv("BOT_NAME", "videoplayerpraneetbot")
API_ID = int(getenv("API_ID", "7028372"))
API_HASH = getenv("API_HASH", "10bc5c7771a121c180ab8859ab438bb8")
OWNER_NAME = getenv("OWNER_NAME", "🅟🅡🅐🅝🅔🅔🅣")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Praneet1875")
ALIVE_NAME = getenv("ALIVE_NAME", "🅟🅡🅐🅝🅔🅔🅣")
BOT_USERNAME = getenv("BOT_USERNAME", "videoplayerpraneetbot")
OWNER_ID = getenv("OWNER_ID", "1101776571")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Assistent1875bot")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "TheSupportChat")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "TheUpdatesChannel")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1669178360").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/a414e2cdfeaa7d4414b89.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ITZ-ZAID/Zaid-Vc-Player")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/c540aac0249486854787b.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6f1cfec700087f6fcb391.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/c3547532105a0cb67229d.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/c3401a572375b569138c3.png")
