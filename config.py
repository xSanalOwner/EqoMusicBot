from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "29171757"))
API_HASH = getenv("API_HASH", "f2a2d9619b545d116fc42b5fee5d592e")

BOT_TOKEN = getenv("BOT_TOKEN", "6875746501:AAG9-S7mdLH6LZ9U14lA8s7-WizPacUgbxU")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", "6859815593"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/1b08429e371b92a1fc483.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/1b08429e371b92a1fc483.jpg")

SESSION = getenv("SESSION","AgCyMAZ7yN4DLI01NwLIDu6nMVBPlUV_EoUuKpMmn7CiCjWtgVqosjxbZNiEA27kzpLr3wZgGMXvyLuNKZlVDHNAHBN4O8SShGsucQP9WKI_71prJHUU4xcsNWrl3ZOU-SrbiKcuwl1--JjrlJtjtS-GvoqJlvZayxy9-jMSLzco8V2H5Z8oWYxtq5pXhDrfdiHnNrS3sRJ38dFc-JsatcLrmAt3ebxGLLi6UQwdPXTaaVR-qdigAWxMFKQiZk8GLfFGjqgjkOq3s9EJH-MNX6AX9Gla7Yl--f4nCVS0h44b6_G6Er8xb6jHSu6kTrl1Jb8795uBWOiqC3X0mf8luCbuAAAAAYclCgAA")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/OliqarxTeam")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/PasterXmusic")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5615367098").split()))


FAILED = "https://telegra.ph/file/1b08429e371b92a1fc483.jpg"
