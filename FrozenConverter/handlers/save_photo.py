import os
from pyrogram import Client, filters
from pyrogram.types import Message

user_images = {}

def register_save_photo(app: Client):
    @app.on_message(filters.photo)
    async def save_photo_handler(_, message: Message):
        user_id = message.from_user.id
        user_dir = f"downloads/{user_id}"
        os.makedirs(user_dir, exist_ok=True)

        file_path = await message.download(file_name=f"{user_dir}/{message.id}.jpg")
        user_images.setdefault(user_id, []).append(file_path)

        await message.reply("✅ Photo saved. Send more or /convert.")

