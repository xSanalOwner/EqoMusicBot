from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "22341875"))
API_HASH = getenv("API_HASH", "b13c2392d55ae8a4800d3b4ed40bffb2")

BOT_TOKEN = getenv("BOT_TOKEN", "6184599558:AAEh3RHPzEqLsJvlSJfs7ohNTAaWTsVdcQg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", "6513170849"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/3a93f74fb963187f2fb1c.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/2e2a5f6d9112c10b5826b.jpg")

SESSION = getenv("SESSION","AgDAVqDj3qpWhdYXR0IEjPfp1SyVc1r-oRk6bl2vQ1OcNeVSR9iOJYFMMut0FjDX4DE0Vj6Zt7lGcKl8jjA1BK0JK5brXU9MJN5vEciLcvgZrFyM541Owx12WcAUQxrqCaHmWlEuo4aaMZt2lCEwN-qeVyf4Er762XipTJcXyRj6yEHvDaLlp3EIZxtpBVtJJYeYnxLtnytpDSGUnN2d7BpdS0DaHtzTaOHP99Hbup1hTp1IvFyAMJ78TjwjxwK0x2z7il4qPTmL3Lnoj0eygSNX6h0A1K38IIoeVtZC3Vf-6yi_Ss0YMm6IgnbBFMvJdDoKZRK3CYvQkdB4LluY5iYnAAAAAZ5TQW8A")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/OliqarxTeam/4545")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/ElikoResmi")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6513170849").split()))


FAILED = "https://telegra.ph/file/797d7fcda824e03ce099b.jpg"
