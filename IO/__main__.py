import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from Core import LOGGER, app, userbot, sudo
from Core.call import IOMusic
from IO.plugins import ALL_MODULES
from IO.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await sudo()
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("IO.plugins" + all_module)
    LOGGER("IO.plugins").info("Successfully Imported Modules...")
    await userbot.start()
    await IOMusic.start()
    try:
        await IOMusic.stream_call("https://graph.org/file/ec8a35dd5f1ef90947167.mp4")
    except NoActiveGroupCall:
        LOGGER("IO").error(
            "Please turn on the videochat of your log group\channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass
    await IOMusic.decorators()
    LOGGER("IO").info(
        "IO Music Bot Started Successfully"
    )
    await idle()
    await app.stop()
    LOGGER("IO").info("Stopping IO Music Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())