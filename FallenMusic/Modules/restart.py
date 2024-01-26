import os
from pyrogram.types import Message
from pyrogram import filters
from config import OWNER_ID
from FallenMusic import app



@app.on_message(filters.command(["yenidenbaslat", "restart"]) & filters.user(OWNER_ID))
async def restart_bot(_, message: Message):
    try:
        msg = await message.reply_text("❖ Restarting bot...")
        print("[INFO]: BOT SERVER RESTARTED !!")
    except BaseException as err:
        print(f"[ERROR]: {err}")
        return
    await msg.edit_text("✅ Bot has restarted !\n\n» back active again in 5-10 seconds.")
    os.system(f"kill -9 {os.getpid()} && python3 -m FallenMusic")
