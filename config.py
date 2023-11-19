from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "22341875"))
API_HASH = getenv("API_HASH", "b13c2392d55ae8a4800d3b4ed40bffb2")

BOT_TOKEN = getenv("BOT_TOKEN", "6875746501:AAG9-S7mdLH6LZ9U14lA8s7-WizPacUgbxU")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", "6513170849"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/3a93f74fb963187f2fb1c.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/2e2a5f6d9112c10b5826b.jpg")

SESSION = getenv("SESSION","AgAF7JiTaEs5IX_VxQwF9vHwO02iLoJuLfhnGabS-E5foHVsc7gSAUuA7YyJnN4AQsZgsZCI-2sMZ8e5ccSDddyuKuPbKSh1-9csNT6KIPyhaZ6BAboW0oMdd6_uWAGtnhimZOuPd8_PWl-CG_Vhb5N6lSsnt__PFcqc549NABxtQ4UuxukI8-s-8oMSbn-pw3OSmVs0-d4UDxQdZv9fGakBI5O3Jdfex_gCvY8M4r-vsqjCNjkOzaP5k6UlgDkIyjwcmLuSiA9RhLeMDH_O2Ij6dUoKuUmHRo-wP67GIIbXbvKpFCvj41tRDr7aHFc0wn87ouJsaDYfJH-xC1JQTsTBAAAAAZ5TQW8A")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/OliqarxTeam/4545")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/ElikoResmi")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6513170849").split()))


FAILED = "https://telegra.ph/file/797d7fcda824e03ce099b.jpg"
