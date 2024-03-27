from pyrogram import filters
from pyrogram.types import Message

from IO import app
from IO.utils.misc import SUDOERS
from IO.utils.database import autoend_off, autoend_on


@app.on_message(filters.command("autoend") & SUDOERS)
async def auto_end_stream(_, message: Message):
    usage = "<b>Example :</b>\n\n/autoend [enable | disable]"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip().lower()
    if state == "enable":
        await autoend_on()
        await message.reply_text(
            "» Auto End stream enabled\n\nAssistant will automatically leave the VC when no one is listening"
        )
    elif state == "disable":
        await autoend_off()
        await message.reply_text("AutoEnd Stream disabled")
    else:
        await message.reply_text(usage)
