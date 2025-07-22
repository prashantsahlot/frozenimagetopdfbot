from pyrogram import Client, filters
from pyrogram.types import Message

def register_start(app: Client):
    @app.on_message(filters.command("start"))
    async def start_handler(_, message: Message):
        await message.reply("👋 Send me images one by one.\nThen type /convert to get your PDF.")

