from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "21891603"))
API_HASH = getenv("API_HASH", "a0410f8f403e4b150f3118c725a83cc1")

BOT_TOKEN = getenv("BOT_TOKEN", "6713345760:AAEzkY8484n1Ceitqz6X3aw2cLQdTEipJw0")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", "5997196226"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/7fd65ce55771e1daa6530.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/7fd65ce55771e1daa6530.jpg")

SESSION = getenv("SESSION","AgCM8cgJBsGXtrGSzcOjNKYC07fQe0HiVnP5a-XkTKO1ArCdDHwBtTb4R6wuuDL66rHdtyy0lTQEGuJA2G6TG1pc6GWfBp932025czSb-Kn6TFjVqcN5yYl7eSdAcXZWqv10v5zHlaIYaELhBxN9L4R-bzeCdk2Y-JboVS-VNtqdSoi9oYviMWghynzs5YAYYjn7zA-Xv5sIQiWv9mEagYlGR7f5gf6ern4h2ylhUFe5i7fS9s4hYIaMM2dQ0vIuMip5ryG2AgHaqajothyVjnWlwNKmDXZp5S3tAZUTvIiSy8GhicjUDIBl1BwNqZP8srt6lmaoPi1_a1GGUQbGsPK0AAAAAYlTB5YA")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/AmazingChatSS")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/EqoMusicPlaylist")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6184111182").split()))


FAILED = "https://telegra.ph/file/7fd65ce55771e1daa6530.jpg"
