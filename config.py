from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "19485442"))
API_HASH = getenv("API_HASH", "a03fcb372b3ec4e406b5d52f84b02e53")

BOT_TOKEN = getenv("BOT_TOKEN", "5366398706:AAGkdiAIw7ybwBAPP3RwxEA45puuusClxds")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", "571698989"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/7d9a9179531af47fac165.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/7d9a9179531af47fac165.jpg")

SESSION = getenv("SESSION", "AgBQd427Lqc70-TotQySylDguBtk9BTsERk1aZtLbp3Rsf7_l7xu4ha-dQvaelbGJVmoRuX61YwjG-i0TYDrrAhAvZL6_io9lmaL9xJ2xBvKXL_Y4nH-ASt-mNyrF0NNHAEF8QnZDAxouUbOCwqdtMFFKb5p8pmIYRPXEjXUEQRnZ5-O-kYPQZL95pyow0uiru28uiG3EmjWVS_sBj3bTmiE4xic_ENekQ1k68z2NKy0Nl2_7g79acDk6j-YwuKicORmuNPmnQPKAfA6SOtNpk2QOGg1mY3zJrEMkEwpYEmQmqIepP3sO5SlXj7cHszrmhasx65yF0efFE5lABy49dMDAAAAAWV6XysA")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/KarabakhChatAz")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/qruzda")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6625863678").split()))


FAILED = "https://telegra.ph/file/7d9a9179531af47fac165.jpg"
