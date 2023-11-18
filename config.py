from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "8953338"))
API_HASH = getenv("API_HASH", "fe21f223cb02d8f7c1cbda651f553a45")

BOT_TOKEN = getenv("BOT_TOKEN", "6875746501:AAG9-S7mdLH6LZ9U14lA8s7-WizPacUgbxU")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", "6513170849"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/b7e66d35f9e3cc7f22771.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/b7e66d35f9e3cc7f22771.jpg")

SESSION = getenv("SESSION", "AgDAVqDj3qpWhdYXR0IEjPfp1SyVc1r-oRk6bl2vQ1OcNeVSR9iOJYFMMut0FjDX4DE0Vj6Zt7lGcKl8jjA1BK0JK5brXU9MJN5vEciLcvgZrFyM541Owx12WcAUQxrqCaHmWlEuo4aaMZt2lCEwN-qeVyf4Er762XipTJcXyRj6yEHvDaLlp3EIZxtpBVtJJYeYnxLtnytpDSGUnN2d7BpdS0DaHtzTaOHP99Hbup1hTp1IvFyAMJ78TjwjxwK0x2z7il4qPTmL3Lnoj0eygSNX6h0A1K38IIoeVtZC3Vf-6yi_Ss0YMm6IgnbBFMvJdDoKZRK3CYvQkdB4LluY5iYnAAAAAZ5TQW8A")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/OliqarxTeam")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/RelaxBlogs")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5615367098").split()))


FAILED = "https://telegra.ph/file/b7e66d35f9e3cc7f22771.jpg"
