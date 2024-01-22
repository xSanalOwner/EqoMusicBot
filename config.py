from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "20272501"))
API_HASH = getenv("API_HASH", "75dee2d6b24b0ed686ab19b42efa7a32")

BOT_TOKEN = getenv("BOT_TOKEN", "6875746501:AAEUwzo5JFdQr75Oll6e8E4MmeBG1-uGMak")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", "6184111182"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/f1b8f168573133d4f0e93.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/f1b8f168573133d4f0e93.jpg")

SESSION = getenv("SESSION","AgBx0QVbZhEUf7YHfSsW6Smf0LIewXEcWK0u6kmCjO32Pqkx1f7rIziqPA4OFgm4aKc7mn7HnnBGnlVdQeufyN3lZjL243XyIe1x41dkZXLsgbV8gaje85A5lWitPHZQaqaUwiIV1Dps9SVyGMlKhOGOnsVPs5Us9sVik5ITRx9_sSswalQYz2FpeZRlWMf6tECE3qOUHP-V7oetBNQ--5eVO2VKLty4RFBhahJ8J29iV-rDZv99w378CIMSM8crLmF9flTgrcj9lLmF3BJTzHHqSd9l-ntUe6GFq3FFz44-K2pt-iBmtnNuwztXzB-GbaGEr5Iy8dSznGQsNa74lDSVAAAAAZGueh4A")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/MonsterFamilyAz")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/PasterXmusic")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6184111182").split()))


FAILED = "https://telegra.ph/file/f1b8f168573133d4f0e93.jpg"
