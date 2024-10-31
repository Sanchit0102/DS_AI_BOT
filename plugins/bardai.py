# import requests
# from pyrogram import filters, Client
# from pyrogram.types import Message
# from pyrogram import Client, filters


# @Client.on_message(filters.command(["bard", "gemini", "bardai", "geminiai"]))
# async def bardandgemini(_: Client, message: Message):
#     if len(message.command) < 2:
#         return await message.reply_text("Abey Gadhe Command k baad kuch likh!!")

#     query = " ".join(message.command[1:])    
#     txt = await message.reply_text("⏳")
#     app = f"https://horridapi.onrender.com/bard?query={query}"
#     response = requests.get(app)
#     data = response.json()
#     api = data['text']
#     await txt.edit(f"ᴊᴀɪ sʜʀᴇᴇ ᴋʀɪsʜɴᴀ {message.from_user.mention}. \nʏᴏᴜʀ ǫᴜᴇʀʏ : {query}\n\n[ʙᴀʀᴅ ᴀɪ](https://t.me/DS_BARD_AI_BOT) : \n{api}")

import requests
from pyrogram import filters, Client
from pyrogram.types import *
from pyrogram import Client, filters
from info import STICKERS_ID, LOG_CHANNEL

@Client.on_message(filters.command(["bard", "gemini", "bardai", "geminiai"]))
async def bardandgemini(_: Client, message: Message):
    if len(message.command) < 2:
        return await message.reply_text("Abey Gadhe Command k baad kuch likh!!")

    query = " ".join(message.command[1:])    
    #sticker = await message.reply_sticker(STICKERS_ID)
    p = await message.reply_sticker("CAACAgUAAxkBAAEEAAHoZufJzlT42agC8QLQHLA0j9_88qQAAt0KAAKJV2FXGYHS3ZDNMqweBA") 
        await asyncio.sleep(15)
        await p.delete()
    #txt = await message.reply_text("⏳")
    app = f"https://horridapi.onrender.com/bard?query={query}"
    response = requests.get(app)
    data = response.json()
    api = data['text']
    await message.reply_text(
        text=f"ᴊᴀɪ sʜʀᴇᴇ ᴋʀɪsʜɴᴀ {message.from_user.mention}. \nʏᴏᴜʀ ǫᴜᴇʀʏ : {query}\n\n[ʙᴀʀᴅ ᴀɪ](https://t.me/DS_BARD_AI_BOT) : \n{api}",
        reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    "Dᴇᴠ ❤",
                                    url=f"https://t.me/THE_DS_OFFICIAL",
                                )
                            ]
                        ]
                    ),
                    disable_web_page_preview=True,
                )
    
    #await sticker.delete()
    await _.send_message(
                    LOG_CHANNEL,
                    text=f"user: @{message.from_user.username}\n\nID : <code>{message.from_user.id}</code>\n\nAsked to Bard Ai : {query}\n\nAi Responce: {api}", 
                )
