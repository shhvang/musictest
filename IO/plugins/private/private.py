
from pyrogram import filters
from pyrogram.types import Message

from pytgcalls import filters as fl
from pytgcalls import PyTgCalls
from pytgcalls.types import ChatUpdate
from pytgcalls.types import MediaStream
from pytgcalls.types import Update

from Core import app
from Core.call import IOMusic

test_stream = 'http://docs.evostream.com/sample_content/assets/' \
              'sintel1m720p.mp4'


@app.on_message(filters.regex('!call'))
async def play_handler(client, message: Message):
    await IOMusic.play(
        message.chat.id,
        MediaStream(
            test_stream,
        ),
    )


@app.on_message(filters.regex('!hangup'))
async def stop_handler(client, message: Message):
    await IOMusic.leave_call(
        message.chat.id,
    )


@IOMusic.on_update(fl.chat_update(ChatUpdate.Status.INCOMING_CALL))
async def incoming_handler(_: PyTgCalls, update: Update):
    await IOMusic.mtproto_client.send_message(
        update.chat_id,
        'You are calling me!',
    )
    await IOMusic.play(
        update.chat_id,
        MediaStream(
            test_stream,
        ),
    )