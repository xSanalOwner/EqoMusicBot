from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "26150211"))
API_HASH = getenv("API_HASH", "ece732fb4b6d28a4d7279e0705664ce2")

BOT_TOKEN = getenv("BOT_TOKEN", "6875746501:AAG9ejQ-GRKaXO2C6AhI9yH7bh2n2UkujmA")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", "7406471382"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/de3bbbf56a078bf4b5b1f.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/de3bbbf56a078bf4b5b1f.jpg")

SESSION = getenv("SESSION","BAGPBUMAKbGxnAY4N_Ld4limntU14zOf4XjX1fFumniYAzdlZ9BbOzMAdMU1-C8JwZCKFS08nEDMr0aO-iSOoIajJmfY5eAl-krtnKHJwdrm4jEuKNqIKsyeuBbsufibEdYQuJJZ6BO57lU9ohna18JbcLrwgJXtBrXZpFblf6ZhU_SI8faJXxsD_uY3rtOewnVnA3VD5C8nIrmMLXghPPhxJ0IvlrzLSzC4uADXnxb5t-dEcS2drGjND1pUB8PN3Jpv7lXJz3ZVL0TEwODuLJiNGTHoHIGyeTsaVQQqei5wuvSah_zS_OlVymmGe4tpnhCsuITmPNaidSoZsODUkfbvCGZRTAAAAAGS2bcGAA")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/sohbetazerbaycan1")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/RikaPlaylist")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6944685509").split()))


FAILED = "https://telegra.ph/file/de3bbbf56a078bf4b5b1f.jpg"
