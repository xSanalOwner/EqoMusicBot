from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "22341875"))
API_HASH = getenv("API_HASH", "b13c2392d55ae8a4800d3b4ed40bffb2")

BOT_TOKEN = getenv("BOT_TOKEN", "6184599558:AAEOKp_B_4XOEuskoKcVODPzkvsAkfTukjE")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", "6513170849"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/70594049ed6facffd7578.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/70594049ed6facffd7578.jpg")

SESSION = getenv("SESSION","AgCInfoADronaLRqK7IYy02x5RxWt5u6I5nWH6AAvNVqLv1mZ0jviPKk7zi9citza8dyvsB7KRHDdNxSiRrSw00UUQWxeM9pm3WTJYayFJ8OOCwSvZqb-Z09CblsrA7G7qONuOpFkBwEJeNjo5a-fQjsvd69YMKI6aoVXlpOPsSMZ59TcpPe9ja3zHeLY4R-ALlpTr_uPQc2vwNpPBxpp2rq315gU90frHElcHjUHyM8qH7y5dZMWlDYve-MM2HtOdMTftTShSEfKOpkhXcYj7IP-Zq5lGgyiyUAYFTW2tI2J1GfXi6d3XX2Wl-oGMsMVE9TSUYo-u6cJVD8o41adaWI_Epx0wAAAAGLf_FFAA")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "doldur")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "doldur")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6513170849").split()))


FAILED = "https://telegra.ph/file/70594049ed6facffd7578.jpg"
