from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "23918923"))
API_HASH = getenv("API_HASH", "70c754805279d6e670658b17367853b6")

BOT_TOKEN = getenv("BOT_TOKEN", "6875746501:AAEUwzo5JFdQr75Oll6e8E4MmeBG1-uGMak")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", "6501496600"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/32787c71a347e0613a944.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/32787c71a347e0613a944.jpg")

SESSION = getenv("SESSION","BABToMYe5kz8KUH5OnqIm_F0X7-VGcM5ToVF9_b8YYXcW2a3AOnggiQvBHV51wcaGVlWQmrG4wx82TftpAQkL7XKwY2wcaRrzLePy4gW6WwH2UmzkTq0GoS9iojFNYlRg7_kDA4fbq_BBZ42Zm_k35p5YR1fyZXlqwunBlG7JQnK0BmzOAGW_Ui_yC0HgU5A8-SmyKL08Jb48L3oza4Q7G_OdF22CHCsq1uTsL6CwVHrR4HToC4cBx9KkEy0cKdS-BdTwRnsdiVEABWbM18yK1fIOLUauXde57P7fmvw1hZYEuxyKHrNYLyu2w61hcUlA6HZySY7taq84jqquqHJ04mMAAAAAZLZtwYA")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/FearlesTeams")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/PasterXmusic")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6501496600").split()))


FAILED = "https://telegra.ph/file/32787c71a347e0613a944.jpg"
