from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "23470094"))
API_HASH = getenv("API_HASH", "e5e62ee565db697cf390cdc0f2d7cefa")

BOT_TOKEN = getenv("BOT_TOKEN", "6757156032:AAFy5alKCFaIZVCMm8AIaCfr19-4n99cO4w")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", "26090016"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/6e111cd5542ba1ae0d731.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/6e111cd5542ba1ae0d731.jpg")

SESSION = getenv("SESSION","AgCy7T0ucAzfrLR8V-4UG0agpZ-z9Jufex51s456oqbEO4mZylRm3jL68-TZBc_i32AByoqxo6Kk4T_4Wh-RrW-6EYMp--XOvq261cEprESQhdGztSbNZnZq4QNLXVF80zBUbj7SX0SxnjBMZ7nEq4XBrrlVg9gs-3e3FDjkLdPWIUjnsbbxOdQpeIxEU45tb05jY_x0D5RsZWH0G7bqb0tvvx5_dzkkDysW5nQwr0lNPxmrEBKOUm562Niyw0xnnub0nwXcUHDGC9VLdwxmVKhUnupaTdVw4FULfefEJ_Jn9TLkL8u7-agkLMF8pdpyA7wBqH0s7p9Gt7OrxjZg7wd3AAAAAZGxhY0A")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/sah_team")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/feroobots")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "26090016").split()))


FAILED = "https://telegra.ph/file/6e111cd5542ba1ae0d731.jpg"
