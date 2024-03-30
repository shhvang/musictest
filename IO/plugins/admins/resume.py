from pyrogram import filters
from pyrogram.types import Message

from Core import app
from Core.call import IOMusic
from IO.utils.database import is_music_playing, music_on
from IO.utils.decorators import AdminRightsCheck
from IO.utils.inline import close_markup
from config import BANNED_USERS


@app.on_message(filters.group & ~BANNED_USERS)
@AdminRightsCheck
async def resume_com(cli, message: Message, _, chat_id):
     if message.command[0] == 'resume' or 'cresume':
        if await is_music_playing(chat_id):
            return await message.reply_text(_["admin_3"])
        await music_on(chat_id)
        await IOMusic.resume_stream(chat_id)
        await message.reply_text(
            _["admin_4"].format(message.from_user.mention), reply_markup=close_markup(_)
        )
