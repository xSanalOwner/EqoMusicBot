from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "29171757"))
API_HASH = getenv("API_HASH", "f2a2d9619b545d116fc42b5fee5d592e")

BOT_TOKEN = getenv("BOT_TOKEN", "6184599558:AAEOKp_B_4XOEuskoKcVODPzkvsAkfTukjE")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", "6409880504"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/b7e66d35f9e3cc7f22771.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/b7e66d35f9e3cc7f22771.jpg")

SESSION = getenv("SESSION", "AgAjRm7-F8o-ZPMmrNBw5kunmu33epAYSGiDjaiDLi8csbpRxaGZZ3p9ZIlf3ub52t1XhYfUt4IEBfG7X6PiBzIllswd6t0qywIgqhsNhlLiwH6o2qBsg4mMQU1upvEKvZ_9FXfI0ScQnlGarXUqiuldk0mnGTWCn9aa_IAsOtGoHQvwTAzoznpQrcPe3h0HDyC725SwxkOpVGZbxagM3XnBmNv4mWZj_d0alEmC9a1iFI_Ssimsl6npmvf5Yia3hbs5C3wFNSmK0ddXsi32qboFo89srYk8VhcP5vs_l7qwiILwjJxS1AjRe01Dq_rUuThVpvUrOueA4yg3aqnkXJ1GAAAAAYt_8UUA")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/OliqarxTeam")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/RelaxBlogs")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5615367098").split()))


FAILED = "https://telegra.ph/file/b7e66d35f9e3cc7f22771.jpg"
