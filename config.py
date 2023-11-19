from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "22341875"))
API_HASH = getenv("API_HASH", "b13c2392d55ae8a4800d3b4ed40bffb2")

BOT_TOKEN = getenv("BOT_TOKEN", "6875746501:AAG9-S7mdLH6LZ9U14lA8s7-WizPacUgbxU")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", "6513170849"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/b7e66d35f9e3cc7f22771.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/b7e66d35f9e3cc7f22771.jpg")

SESSION = getenv("SESSION","AgC1K4x0KosMYoQz80jGerXkQ70EpxMhbuscw5uXcVPSjfHvLpMAXwUp_bZ7cx5ihr7FCDP9yOyFDYwwPbiyOaydng_g3GMp6n2-xq0l4zvBpz7IV2Ed3ZyH9VCN-5-VxYKz7L6sWJOLYerNrJjFTLgy86IMyminOQj2nUYuPJcu8TeZREtKxyR9pG5J7EnYnZKuKjJRmVEfTFqIhUOIOC4TPdV5kMkXaYBx0VJfUDlZju9_3e1-lRa01eefIWsg2ejVUmWs-OrfORUuIAce-gifQLrSMaxpriHFhjx2TrnhA4sf4ePzhIfqtYKmGaQ-dxMzmbSUesKcrZRfrBDGafJ6AAAAAZ5TQW8A")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/OliqarxTeam")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/PasterXmusic")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6513170849").split()))


FAILED = "https://telegra.ph/file/b7e66d35f9e3cc7f22771.jpg"
