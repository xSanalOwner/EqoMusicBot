from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "28565438"))
API_HASH = getenv("API_HASH", "a38714503f1573651bb0ab1ab8f5b1a1")

BOT_TOKEN = getenv("BOT_TOKEN", "6843376045:AAHkLQpKxKxttqTXloXLTRYqH-2_2PjmTy0")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", "6972789052"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/37604c5f3a8eed43ba846.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/37604c5f3a8eed43ba846.jpg")

SESSION = getenv("SESSION","AgC6FgpFLKqb5KQVTC4u3oEKlJcAOwThKq81I-s67KQ-0G1bH212pysZzYPfLfAWvI1wmRFGSqBVam3ZNbQ1CTaDfMAUNwJvAsRSETLOkc45pIts6DDf5MgvKOb4Y4ZPvAFykC4PAyNDIqBrzoEnii76V04-RTDWtuJdEw-BRpnGE9LKYmSskiDzDxcoaMMEJCzEoczBzaRg6s3hv5KXk33eOViybQChnIukqLBSZOOjg7tkkyryy1MdP4Xkiiu9Rza7-gMetWDmoSDaxXepv06jc-ddrQ8Q6cTKVN5Ejkx_CZtGW6A0EyFG2MVWhn8yWJR_nOTcbJUsrVJTp5rmKDg5AAAAAU8ab7EA")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/sah_team")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/FerooBots")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6972789052").split()))


FAILED = "https://telegra.ph/file/37604c5f3a8eed43ba846.jpg"
