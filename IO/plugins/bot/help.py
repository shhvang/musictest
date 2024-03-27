from typing import Union

from pyrogram import filters, types
from pyrogram.types import InlineKeyboardMarkup, Message

from IO import app
from IO.utils import help_pannel
from IO.utils.database import get_lang
from IO.utils.decorators.language import LanguageStart, languageCB
from IO.utils.inline.help import help_back_markup, private_help_panel
from config import BANNED_USERS, START_IMG_URL, SUPPORT_CHAT
from Locales import get_string, menu


@app.on_message(filters.command(["help"]) & filters.private & ~BANNED_USERS)
@app.on_callback_query(filters.regex("settings_back_helper") & ~BANNED_USERS)
async def helper_private(
    client: app, update: Union[types.Message, types.CallbackQuery]
):
    is_callback = isinstance(update, types.CallbackQuery)
    if is_callback:
        try:
            await update.answer()
        except:
            pass
        chat_id = update.message.chat.id
        language = await get_lang(chat_id)
        _ = get_string(language)
        keyboard = help_pannel(_, True)
        await update.edit_message_text(
            _["help_1"].format("https://t.me/IOSupportChat"), reply_markup=keyboard
        )
    else:
        try:
            await update.delete()
        except:
            pass
        language = await get_lang(update.chat.id)
        _ = get_string(language)
        keyboard = help_pannel(_)
        await update.reply_photo(
            photo=START_IMG_URL,
            caption=_["help_1"].format("https://t.me/IOSupportChat"),
            reply_markup=keyboard,
        )


@app.on_message(filters.command(["help"]) & filters.group & ~BANNED_USERS)
@LanguageStart
async def help_com_group(client, message: Message, _):
    keyboard = private_help_panel(_)
    await message.reply_text(_["help_2"], reply_markup=InlineKeyboardMarkup(keyboard))


@app.on_callback_query(filters.regex("help_callback") & ~BANNED_USERS)
@languageCB
async def helper_cb(client, CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    cb = callback_data.split(None, 1)[1]
    keyboard = help_back_markup(_)
    if cb == "hb1":
        await CallbackQuery.edit_message_text(menu.ADMINC, reply_markup=keyboard)
    elif cb == "hb2":
        await CallbackQuery.edit_message_text(menu.AUTHC, reply_markup=keyboard)
    elif cb == "hb3":
        await CallbackQuery.edit_message_text(menu.BROADC, reply_markup=keyboard)
    elif cb == "hb4":
        await CallbackQuery.edit_message_text(menu.BLCC, reply_markup=keyboard)
    elif cb == "hb5":
        await CallbackQuery.edit_message_text(menu.BLUC, reply_markup=keyboard)
    elif cb == "hb6":
        await CallbackQuery.edit_message_text(menu.CPLAYC, reply_markup=keyboard)
    elif cb == "hb7":
        await CallbackQuery.edit_message_text(menu.GBANC, reply_markup=keyboard)
    elif cb == "hb8":
        await CallbackQuery.edit_message_text(menu.LOOPC, reply_markup=keyboard)
    elif cb == "hb9":
        await CallbackQuery.edit_message_text(menu.MAINC, reply_markup=keyboard)
    elif cb == "hb10":
        await CallbackQuery.edit_message_text(menu.PINGC, reply_markup=keyboard)
    elif cb == "hb11":
        await CallbackQuery.edit_message_text(menu.PLAYC, reply_markup=keyboard)
    elif cb == "hb12":
        await CallbackQuery.edit_message_text(menu.SHUFFLEC, reply_markup=keyboard)
    elif cb == "hb13":
        await CallbackQuery.edit_message_text(menu.SEEKC, reply_markup=keyboard)
    elif cb == "hb14":
        await CallbackQuery.edit_message_text(menu.SONGC, reply_markup=keyboard)
    elif cb == "hb15":
        await CallbackQuery.edit_message_text(menu.SPEEDC, reply_markup=keyboard)
