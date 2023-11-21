from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "29171757"))
API_HASH = getenv("API_HASH", "f2a2d9619b545d116fc42b5fee5d592e")

BOT_TOKEN = getenv("BOT_TOKEN", "6875746501:AAG9-S7mdLH6LZ9U14lA8s7-WizPacUgbxU")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", "6513170849"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/1b08429e371b92a1fc483.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/1b08429e371b92a1fc483.jpg")

SESSION = getenv("SESSION","AgAIO2hRJuQVbYBHK-zNY9x17pV1LNQobfd4Q0d41P0zRs93369AKMaPYXPaGwXzmBotkURYFOA5U2M17KH5VmGL1zwiQlW4_QVIjf0a_2EWh5kx8h87mBg5tvfSAfqGzlXOAxguU16z1DatyuNutInW0O6qPiZrZCr13Et-4o0kDapbhsjiFSjfSe1ixspDfvVY_Ym3Qwene8hPzAowffJleJzzAhD0-qwX0VDcR0xN6Hz1WQAUuGXSVMMCsG2XWcR0NmEC0zbsDrIogMtmPGPY6RXFLjBy6nq6TepVx5lHdfsdmE4qR-h0TKr-bYINr0-34c5Ti4Scualc_PzEdCxVAAAAAZ5TQW8A")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/OliqarxTeam")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/PasterXmusic")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5615367098").split()))


FAILED = "https://telegra.ph/file/1b08429e371b92a1fc483.jpg"
