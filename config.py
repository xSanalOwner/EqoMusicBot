from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "24852083"))
API_HASH = getenv("API_HASH", "02dd65f0bae35e92f1692af0302c0c18")

BOT_TOKEN = getenv("BOT_TOKEN", "6875746501:AAG9-S7mdLH6LZ9U14lA8s7-WizPacUgbxU")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", "6859815593"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/1b08429e371b92a1fc483.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/1b08429e371b92a1fc483.jpg")

SESSION = getenv("SESSION","AgBf58J80YA8STiDzbrKXo4kgr8JV9TSXpUyDkNxSxkNAMAff8vSQy5XXhDBB70YYxXkoc9xr4AiUCyWqtf2Pr8UHfnaYJiMsge9OepPgbaHxp7B2jzglzqxS04wTkXSoHBuw7Kdig-VUrBMs8l56WUj6KupgO3dtGOYbzENBz7NNuH19j9XrEsjGxlv8-cVaqtLLvwymvJvcvAfLhKq_uCyXFn54ekoFa1PtSqaTSdoHfCdmClNYjiPzW2rm9vOwi51WGI7wn2CPJBPg-C5AsdNFs-RvMsMSVq_9xTuEMm1XffiYCG6snskkc2gNgiMx419QnQ-UatqNo01Iigv9RYTAAAAAZskFyEA")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/OliqarxTeam")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/PasterXmusic")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5615367098").split()))


FAILED = "https://telegra.ph/file/1b08429e371b92a1fc483.jpg"
