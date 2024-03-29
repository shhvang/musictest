from pyrogram import filters
from pyrogram.types import Message

from Core import app
from Core.call import IOMusic
from IO.utils.database import is_music_playing, music_off
from IO.utils.decorators import AdminRightsCheck
from IO.utils.inline import close_markup
from config import BANNED_USERS



@app.on_message(filters.command(["pause", "cpause"]) & filters.group & ~BANNED_USERS)
@AdminRightsCheck
async def handle_message(cli, message: Message, _):
    chat_id = message.chat.id
    if not await is_music_playing(chat_id):
        return await message.reply_text(_["admin_1"])
    await music_off(chat_id)
    await IOMusic.pause_stream(chat_id)
    await message.reply_text(
    _["admin_2"].format(message.from_user.mention), reply_markup=close_markup(_)
    )

@app.on_message(filters.text([
    "hey io pause",
    "Hey io pause"]) & filters.group & ~BANNED_USERS)
@AdminRightsCheck
async def pause_hey(cli, message: Message, _):
    if message.text.lower().startswith("hey io pause"):
        chat_id = messgae.chat.id
        if not await is_music_playing(chat_id):
            return await message.reply_text(_["admin_1"])
        await music_off(chat_id)
        await IOMusic.pause_stream(chat_id)
        await message.reply_text(
            _["admin_2"].format(message.from_user.mention), reply_markup=close_markup(_)
        )