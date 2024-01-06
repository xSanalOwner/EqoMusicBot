from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "24852083"))
API_HASH = getenv("API_HASH", "02dd65f0bae35e92f1692af0302c0c18")

BOT_TOKEN = getenv("BOT_TOKEN", "6875746501:AAEUwzo5JFdQr75Oll6e8E4MmeBG1-uGMak-2_2PjmTy0")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", "6859815593"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/1b08429e371b92a1fc483.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/1b08429e371b92a1fc483.jpg")

SESSION = getenv("SESSION","AgCQd-ZHEO4Q3z_LCqWNBnEffUuD1-XjM2UHhCP4cfIN9ttzVXUKB6oQDweDEFx71fePr_YLqLEAtSkoUnZ6iEYMwDR-YxhXk_-bJGFutGGuuOWf12sQRWLq-PNTshhIiLkC5xwQ02Ziy9gDvGtVCkuz_PyY9VrICrymCBof9D4NJG3aiyoUrDc0VstxQC8KVhHyBlThvS1t7k48pmK4Ilf7BFX1oSqyvbIdq0iGdY2h2tVi32c5gxoW2WKIUI9ke2h0DLumWG7bFJD8Xp72OgQxKLnx_GpIL-Q8Ji5s1eSn4bmrYD40cwLZBw8gu2exRao4Bg2z0HFac9LSnotIyrBKAAAAAZskFyEA")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/KarabakhSoldiers")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/PasterXmusic")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6859815593").split()))


FAILED = "https://telegra.ph/file/1b08429e371b92a1fc483.jpg"
