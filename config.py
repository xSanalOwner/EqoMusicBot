from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "25540216"))
API_HASH = getenv("API_HASH", "08d15f61e57431d7f5711ac8567e5937")

BOT_TOKEN = getenv("BOT_TOKEN", "6370639090:AAEY8mVE4QdtlcPrwSm3dU04YzcJRAg5iiE-uGMak")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", "5567060261"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/219642edbf3d6634e4a5e.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/219642edbf3d6634e4a5e.jpg")

SESSION = getenv("SESSION","AQBh4QP_PAbxoo5nTrT5yvvD9KkVv2iGo_c0xSQ-iRxTt9qAXH9h80g77zdvrf13xH7teNDDfT8PnsMsUZG6W5yHxF9XWLeelRjDJ76UO2pcri6fkHZwHoPQIR6fCeRR5iM8zNGtSF27jEpYD7j0DZmEA2XQFNct2lHE856HK4-iZO4xi1X8sZSW6oRv1pG3ZX6AxFqDn7rqOaeH2osk7r3EVoA5RjTqW03PNWLDsUnHgeplC7qrbcBzdZrpk-OFuJbiyoJ6HrFsZO6UsbOCti0HVDncXBi3AVTyrVl_w0PQ5p2dj0NNTjR64QeThdHST31-BNZlwHHXt57CLhtDeoAAAAATBROT4A")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/AmazingChatSS")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/ssmusiclist")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5567060261").split()))


FAILED = "https://telegra.ph/file/219642edbf3d6634e4a5e.jpg"
