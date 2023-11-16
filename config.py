from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "29171757"))
API_HASH = getenv("API_HASH", "f2a2d9619b545d116fc42b5fee5d592e")

BOT_TOKEN = getenv("BOT_TOKEN", "6901836721:AAGMrdeDqWftd3jIjiZmlgqgTPFFw000ZPg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", "6513170849"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/014f150e478d23d62907d.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/014f150e478d23d62907d.jpg")

SESSION = getenv("SESSION","AgAk9x_MeiGX5JKFHtU5buSGjHNU99wsQ2crleXirBPIdmYdViY3QGab8_YSlpm9nGtIX_3CZQmUTtyGCV1DrbNRKnfCsZ-oXhSclOnw8j06NVfG6iMrmKzSxtRg17JPlYNBvUiQyMLvQmrgAstm18DisaoKS6AQl5NPGNPQqUVCwVJSDokZfaJX6L2LBX6pTPULk1wFBeZyXdqcwzXrTj6RBb6EfkUD4g6XdORwI5TcJbZIk98iERGblZfR3AuOJrmOKb4aeogMlw8uCXIPi5Ek4kt8W2OSb-7RoL99JPUGWeGjZ4bJtKzgbHIPSTqxVoD3ZOPir3dRrxDytUc4SUevAAAAAZ5TQW8A")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/OliqarxTeam")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/RelaxAndMee")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5615367098").split()))


FAILED = ""
