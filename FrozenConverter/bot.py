from pyrogram import Client
from utils.config import API_ID, API_HASH, BOT_TOKEN
from handlers.start import register_start
from handlers.save_photo import register_save_photo
from handlers.convert import register_convert

app = Client("photo2pdf_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Register handlers
register_start(app)
register_save_photo(app)
register_convert(app)

app.run()

