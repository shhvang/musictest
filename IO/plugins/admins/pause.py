from pyrogram import filters
from pyrogram.types import Message

from Core import app
from Core.call import IOMusic
from IO.utils.database import is_music_playing, music_off
from IO.utils.decorators import AdminRightsCheck
from IO.utils.inline import close_markup
from config import BANNED_USERS


@app.on_message(filters.text & filters.group & ~BANNED_USERS)
@AdminRightsCheck
async def handle_message(cli, message: Message, _):
  chat_id = message.chat.id
  text = message.text.lower()  # Convert message text to lowercase for case-insensitive comparison

  # Check for custom triggers (modify triggers as needed)
  if text in ("hey io pause", "hey io cpause") or text.lower().startswith(("/pause", "/cpause")):
    if not await is_music_playing(chat_id):
      return await message.reply_text(_["admin_1"])
    await music_off(chat_id)
    await IOMusic.pause_stream(chat_id)
    await message.reply_text(
        _["admin_2"].format(message.from_user.mention), reply_markup=close_markup(_)
    )

print("Checking message text:", message.text)
if text in ("hey io pause", "hey io cpause") or text.lower().startswith(("/pause", "/cpause")):
  print("Trigger detected!")
  # Rest of your code
else:
  print("No trigger detected.")
