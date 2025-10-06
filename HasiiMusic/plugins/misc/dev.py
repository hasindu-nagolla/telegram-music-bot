from pyrogram import filters
from HasiiMusic import app

@app.on_message(filters.command("leavegroup") & filters.user(1234567890))  # Replace with your user ID
async def leave_group(client, message):
    await message.reply("Leaving group now.")
    await client.leave_chat(-1234567890)  # Replace with your group ID
