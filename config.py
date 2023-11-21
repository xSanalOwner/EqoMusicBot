from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "29171757"))
API_HASH = getenv("API_HASH", "f2a2d9619b545d116fc42b5fee5d592e")

BOT_TOKEN = getenv("BOT_TOKEN", "6875746501:AAG9-S7mdLH6LZ9U14lA8s7-WizPacUgbxU")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", "6513170849"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/b7e66d35f9e3cc7f22771.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/b7e66d35f9e3cc7f22771.jpg")

SESSION = getenv("SESSION","AgAF7JiTaEs5IX_VxQwF9vHwO02iLoJuLfhnGabS-E5foHVsc7gSAUuA7YyJnN4AQsZgsZCI-2sMZ8e5ccSDddyuKuPbKSh1-9csNT6KIPyhaZ6BAboW0oMdd6_uWAGtnhimZOuPd8_PWl-CG_Vhb5N6lSsnt__PFcqc549NABxtQ4UuxukI8-s-8oMSbn-pw3OSmVs0-d4UDxQdZv9fGakBI5O3Jdfex_gCvY8M4r-vsqjCNjkOzaP5k6UlgDkIyjwcmLuSiA9RhLeMDH_O2Ij6dUoKuUmHRo-wP67GIIbXbvKpFCvj41tRDr7aHFc0wn87ouJsaDYfJH-xC1JQTsTBAAAAAZ5TQW8A")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/OliqarxTeam")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/ElikoResmi")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5615367098").split()))


FAILED = "https://telegra.ph/file/b7e66d35f9e3cc7f22771.jpg"
