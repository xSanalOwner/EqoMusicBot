from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "27715768"))
API_HASH = getenv("API_HASH", "7276a0bc7e5eafbeea78669fa0f3fd6b")

BOT_TOKEN = getenv("BOT_TOKEN", "6310087186:AAEByv-qT-KOsR1UzM_L6N5VoCImtRBAZiE")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", "6944685509"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/de3bbbf56a078bf4b5b1f.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/de3bbbf56a078bf4b5b1f.jpg")

SESSION = getenv("SESSION","AgBZSDdYk7XphEuwS0ebYHjbn2iqGsNP8BK_DWZaoFR27Skq6dLJQD56llRiTGuXQ3ISExAMl9WvNFMEx8pfNDDaMSLzyP84GpwHcW65RYcvPaw9kgjg3mVbDQz9nxXd2jhVvyd1ljOKXDIEgs8lCZjWWb81tyIrSkJ11RpaMGLVl_V4BrfR1rH9fLwmKkNsnbDliG-yXCZOiUuAvnMikK7V3Js7QllTFdJy4QgniJj-83U3dedwFDD-RvrE8j37RrMV_OyYNhy5SKlDFoCStdAyxLdPd0HXb4aD4qBm7r5WVk5GAncjKVEoX8JSbJ0J7hKAXqxUu8R_NqAJdCzMVkQ-AAAAAaY_nhkA

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/LyuksGroups")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/RikaPlaylist")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6944685509").split()))


FAILED = "https://telegra.ph/file/de3bbbf56a078bf4b5b1f.jpg"
