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
    app = f"https://horridapi.onrender.com/bard?query={query}"
    response = requests.get(app)
    data = response.json()
    api = data['text']
    await txt.edit(f"ᴊᴀɪ sʜʀᴇᴇ ᴋʀɪsʜɴᴀ {message.from_user.mention}. \nʏᴏᴜʀ ǫᴜᴇʀʏ : {query}\n\n[ʙᴀʀᴅ ᴀɪ](https://t.me/DS_BARD_AI_BOT) : \n{api}")
