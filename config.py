from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "24852083"))
API_HASH = getenv("API_HASH", "02dd65f0bae35e92f1692af0302c0c18")

BOT_TOKEN = getenv("BOT_TOKEN", "6875746501:AAEUwzo5JFdQr75Oll6e8E4MmeBG1-uGMak-2_2PjmTy0")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", "6859815593"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/1b08429e371b92a1fc483.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/1b08429e371b92a1fc483.jpg")

SESSION = getenv("SESSION","AgAeXOK34NLyG54hSV_hMaoXJ2XC-0AJ03FCtD5R_ywVZe93kjnL-trL9wNwuLsRkq9eLZMke0WY_-SzLZX2sJnJbuA5GLLKAUeXHeHbZfIU89gGGeMvfD92MQITc61y9v2s1kp7do2lLxllbTtePqe2VyowZNdoW1wPtT5ts7Q9gxnU0w7Lkmg8L_Kny5kQqwGRDyyTA0mx1MqiMM9MvnbgNIQw-GSDKDTyXRUFaenPx9dbqpUAg7mhubQmnD4QNgvszghg14omfSjCUsFjZxI30BCBD5J4Q6dEBcD6ox7NzWRlaIVC66l7uLmdSF3hUl41Jc9Rm8lisAPLi-MLxb44AAAAAZskFyEA")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/KarabakhSoldiers")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/PasterXmusic")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6859815593").split()))


FAILED = "https://telegra.ph/file/1b08429e371b92a1fc483.jpg"
