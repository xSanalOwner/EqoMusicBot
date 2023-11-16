from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "29171757"))
API_HASH = getenv("API_HASH", "f2a2d9619b545d116fc42b5fee5d592e")

BOT_TOKEN = getenv("BOT_TOKEN", "6875746501:AAG9-S7mdLH6LZ9U14lA8s7-WizPacUgbxU")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", "6513170849"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/b7e66d35f9e3cc7f22771.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/b7e66d35f9e3cc7f22771.jpg")

SESSION = getenv("SESSION","AgCbIEHS5SDs_yh-Q8RolLNsyapotT6vs8jv2p6gZw5PnEekr37bEGGc4nwSL2lbdGs1fCvhBDSnzlc44YKgR7ZYfGe3o92Ae4DSKMapRjFhW9xcPpIh0SJAzRZznmgjf1SzfcCV_MAZIzTCL577MTfpDG232XQVdN1nfoc7tGUhLAE-3_i-hugdzhEKM7gVGt_4iGbevMh6B3e4nfJoFj8uX8kB1JTxkq_2smzZY6jyFfUGU-jhD0QgqbNQ6A8dJBCw20gHtFfWsCECBUaW99vkUWfJT0T3GMGmOieFGGpM2WO26UaBgVN1emdjyVb_OjCC79Qo8pDU5i2kNdqitTdPAAAAAZ5TQW8A")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "OliqarxTeam")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "RelaxAndMee")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5615367098").split()))


FAILED = "https://telegra.ph/file/b7e66d35f9e3cc7f22771.jpg"
