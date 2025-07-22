import os
import img2pdf
from pyrogram import Client, filters
from pyrogram.types import Message
from .save_photo import user_images

def register_convert(app: Client):
    @app.on_message(filters.command("convert"))
    async def convert_handler(_, message: Message):
        user_id = message.from_user.id
        images = user_images.get(user_id, [])

        if not images:
            await message.reply("❌ You haven't sent any images yet.")
            return

        output_pdf = f"downloads/{user_id}/output.pdf"

        with open(output_pdf, "wb") as f:
            f.write(img2pdf.convert(images))

        await message.reply_document(output_pdf, caption="📝 Here's your high-quality PDF!")

        for path in images:
            os.remove(path)
        os.remove(output_pdf)
        user_images[user_id] = []

