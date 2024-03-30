from pyrogram import filters
from pyrogram.types import Message

from Core import app
from Core.call import IOMusic
from IO.utils.database import set_loop
from IO.utils.decorators import AdminRightsCheck
from IO.utils.inline import close_markup
from config import BANNED_USERS


@app.on_message(filters.group & ~BANNED_USERS)
@AdminRightsCheck
async def stop_music(cli, message: Message, _, chat_id):
    if message.command[0] == 'end' or 'stop':
        if not len(message.command) == 1:
            return
        await IOMusic.stop_stream(chat_id)
        await set_loop(chat_id, 0)
        await message.reply_text(
            _["admin_5"].format(message.from_user.mention), reply_markup=close_markup(_)
        )
