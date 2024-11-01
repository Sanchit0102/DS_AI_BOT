import asyncio
from pyrogram import Client, filters
from helper.database import total_users

@Client.on_message(filters.private & filters.command("users"))
async def users(bot, update):
    users = await total_users_count()  # Get total users from the database
    text = "Bot Status\n"
    text += f"\nTotal Users: {users}"  # Format the response message
    await update.reply_text(
        text=text,
        quote=True,
        disable_web_page_preview=True  # Disable web page preview in the reply
    )
