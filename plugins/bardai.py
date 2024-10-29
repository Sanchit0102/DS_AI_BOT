import requests
from pyrogram import filters, Client
from pyrogram.types import Message
from pyrogram import Client, filters


@Client.on_message(filters.command(["bard", "gemini", "bardai", "geminiai"]))
async def bardandgemini(_: Client, message: Message):
    if len(message.command) < 2:
        return await message.reply_text("Abey Gadhe Command k baad kuch likh!!")

    query = " ".join(message.command[1:])    
    txt = await message.reply_text("⏳")
    app = f"https://horridapi2-0.onrender.com/bard?query={query}"
    response = requests.get(app)
    data = response.json()
    api = data['text']
    await txt.edit(f"ʜᴇʏ: {message.from_user.mention}\n\nϙᴜᴇʀʏ: {query}\n\nʀᴇsᴜʟᴛ:\n\n{api}")