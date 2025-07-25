import os
import img2pdf
from PIL import Image
from pyrogram import Client, filters
from pyrogram.types import Message

# === Bot Config ===
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("bot_token")

app = Client("ph2oto2pdf_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Store user uploads temporarily
user_images = {}

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("👋 Send me images one by one.\nThen type /convert to get your PDF.")

@app.on_message(filters.photo)
async def save_photo(client, message: Message):
    user_id = message.from_user.id
    user_dir = f"downloads/{user_id}"
    os.makedirs(user_dir, exist_ok=True)

    file_path = await message.download(file_name=f"{user_dir}/{message.id}.jpg")
    user_images.setdefault(user_id, []).append(file_path)

    await message.reply("✅ Photo saved. Send more or /convert.")


@app.on_message(filters.command("convert"))
async def convert_to_pdf(client, message: Message):
    user_id = message.from_user.id
    images = user_images.get(user_id, [])

    if not images:
        await message.reply("❌ You haven't sent any images yet.")
        return

    output_pdf = f"downloads/{user_id}/output.pdf"
    image_objs = []

    for img_path in sorted(images):
        img = Image.open(img_path)
        if img.mode != "RGB":
            img = img.convert("RGB")
        image_objs.append(img)

    image_objs[0].save(output_pdf, save_all=True, append_images=image_objs[1:])

    await message.reply_document(output_pdf, caption="📝 Here's your PDF!")

    # Cleanup
    for path in images:
        os.remove(path)
    os.remove(output_pdf)
    user_images[user_id] = []

app.run()




