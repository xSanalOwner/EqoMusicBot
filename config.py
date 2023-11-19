from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "29171757"))
API_HASH = getenv("API_HASH", "f2a2d9619b545d116fc42b5fee5d592e")

BOT_TOKEN = getenv("BOT_TOKEN", "6184599558:AAEOKp_B_4XOEuskoKcVODPzkvsAkfTukjE")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", "6409880504"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/b7e66d35f9e3cc7f22771.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/b7e66d35f9e3cc7f22771.jpg")

SESSION = getenv("SESSION", "AgCInfoADronaLRqK7IYy02x5RxWt5u6I5nWH6AAvNVqLv1mZ0jviPKk7zi9citza8dyvsB7KRHDdNxSiRrSw00UUQWxeM9pm3WTJYayFJ8OOCwSvZqb-Z09CblsrA7G7qONuOpFkBwEJeNjo5a-fQjsvd69YMKI6aoVXlpOPsSMZ59TcpPe9ja3zHeLY4R-ALlpTr_uPQc2vwNpPBxpp2rq315gU90frHElcHjUHyM8qH7y5dZMWlDYve-MM2HtOdMTftTShSEfKOpkhXcYj7IP-Zq5lGgyiyUAYFTW2tI2J1GfXi6d3XX2Wl-oGMsMVE9TSUYo-u6cJVD8o41adaWI_Epx0wAAAAGLf_FFAA")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/OliqarxTeam")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/RelaxBlogs")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5615367098").split()))


FAILED = "https://telegra.ph/file/b7e66d35f9e3cc7f22771.jpg"
