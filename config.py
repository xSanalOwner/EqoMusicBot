from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "28167952"))
API_HASH = getenv("API_HASH", "27618e15dd9a461849bbe5800413346f")

BOT_TOKEN = getenv("BOT_TOKEN", "6370639090:AAGc3790U0o-19aMpnJUJbgDSmBCTnxkBa0")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", "5567060261"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/219642edbf3d6634e4a5e.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/219642edbf3d6634e4a5e.jpg")

SESSION = getenv("SESSION","AgADSTwbjnfTScnqVohIzWV9zHZsebypnlH8QmQx1vqlMWe6tTEWPA3ZusqHMswVKGFF_iWxT41nmgCrzgPndujQwwRAR9a6J2VWX9CvBZ2S8-XDyRT8NZjuNVGR6yc3JXgPZ24K5W6rmXjXstnfFWsDqYs72eO8PfLlPNlyQEgAheucfYAddzEsFbP7yq2JjYr8FdwjQbbnND-pOBwMSvAzn28ZdJAwfjNXrroRGsT5_NKcCV1nDOBYtmqnRvCSDMD7cepFHa0rkPb4VBszdQ3Tr1QOhk5EhrNCAUoP37osJCMjo0uCsSwTolO8eNqzjyPS9G3XOGCeLeKEzS4pUiLGAAAAAXTQeH8A")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/AmazingChatSS")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/ssmusiclist")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5567060261").split()))


FAILED = "https://telegra.ph/file/219642edbf3d6634e4a5e.jpg"
