from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "20272501"))
API_HASH = getenv("API_HASH", "75dee2d6b24b0ed686ab19b42efa7a32")

BOT_TOKEN = getenv("BOT_TOKEN", "6875746501:AAEUwzo5JFdQr75Oll6e8E4MmeBG1-uGMak-2_2PjmTy0")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", "6184111182"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/1b08429e371b92a1fc483.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/1b08429e371b92a1fc483.jpg")

SESSION = getenv("SESSION","AgCWkXMzNaK69ZKWc_AOHSee_3HMJbWALGEGA2yvE-oP0ga17FVjl2M8wCsldK8r5IYvJoyNJcXVpA75Fm33Gqi9MwwNGt9BxL8PmIizo-tfAtpTBA-GyZKkI6SPAARtaEmaZFYY_LRePM83bRveeIj4UKEOxt13apHs-zudr-mR3CDyDZ6V9AbotZmg5e6rbw0kJsGk5DrliHbXsUQbDwisq1FAxyxZBA4I02v21_UcJhEmF5oRSpoTePOhzDNy7LmoUPFBItQInEZpbdbRhC5eMQkW5_36MBpbBky93bNW1mMK1Va6hXgfkYhjgNz84dUrI0-MBHhy0Y0el-L9y6bIAAAAAZGueh4A")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/KarabakhSoldiers")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/PasterXmusic")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6184111182").split()))


FAILED = "https://telegra.ph/file/1b08429e371b92a1fc483.jpg"
