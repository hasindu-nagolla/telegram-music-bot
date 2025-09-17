from pyrogram import filters
from pyrogram.types import Message
from HasiiMusic import app
from HasiiMusic.mongo.pretenderdb import (
    impo_off, impo_on, check_pretender,
    add_userdata, get_userdata, usr_data
)
from HasiiMusic.utils.admin_filters import admin_filter


async def update_userdata(user):
    """Helper to update user info in the database."""
    await add_userdata(
        user.id,
        user.username,
        user.first_name,
        user.last_name
    )


@app.on_message(filters.group & ~filters.bot & ~filters.via_bot, group=69)
async def chk_usr(_, message: Message):
    if message.sender_chat or not await check_pretender(message.chat.id):
        return

    if not await usr_data(message.from_user.id):
        return await update_userdata(message.from_user)

    prev_username, prev_first, prev_last = await get_userdata(message.from_user.id)
    user = message.from_user
    msg = ""

    # Username change
    if prev_username != user.username:
        prev_name = f"@{prev_username}" if prev_username else "​🇳​​🇴​ ​🇺​​🇸​​🇪​​🇷​​🇳​​🇦​​🇲​​🇪​"
        new_name = f"@{user.username}" if user.username else "​🇳​​🇴​ ​🇺​​🇸​​🇪​​🇷​​🇳​​🇦​​🇲​​🇪​"
        msg += f"""
**🐻‍❄️ ᴄʜᴀɴɢᴇᴅ ᴜsᴇʀɴᴀᴍᴇ 🐻‍❄️**
━━━━━━━━━━━━━━━  
**🎭 ꜰʀᴏᴍ** : {prev_name}
**🍜 ᴛᴏ** : {new_name}
━━━━━━━━━━━━━━━  \n
"""
        await update_userdata(user)

    # First name change
    if prev_first != user.first_name:
        msg += f"""
**🪧 ᴄʜᴀɴɢᴇs ғɪʀsᴛ ɴᴀᴍᴇ 🪧**
━━━━━━━━━━━━━━━  
**🔐 ꜰʀᴏᴍ** : {prev_first}
**🍓 ᴛᴏ** : {user.first_name}
━━━━━━━━━━━━━━━  \n
"""
        await update_userdata(user)

    # Last name change
    if prev_last != user.last_name:
        prev_last = prev_last or "​🇳​​🇴​ ​🇱​​🇦​​🇸​​🇹​ ​🇳​​🇦​​🇲​​🇪​"
        new_last = user.last_name or "​🇳​​🇴​ ​🇱​​🇦​​🇸​​🇹​ ​🇳​​🇦​​🇲​​🇪​​"
        msg += f"""
**🪧 ᴄʜᴀɴɢᴇ​​🇸​​ ʟᴀ​🇸​​ᴛ ɴᴀᴍᴇ 🪧**
━━━━━━━━━━━━━━━  
**🚏 ꜰʀᴏᴍ** : {prev_last}
**🍕 ᴛᴏ** : {new_last}
━━━━━━━━━━━━━━━  \n
"""
        await update_userdata(user)

    if msg:
        await message.reply_photo(
            "https://i.ibb.co/tprHKhYc/hasii.png",
            caption=f"**🔓 ᴘʀᴇᴛᴇɴᴅᴇʀ ᴅᴇᴛᴇᴄᴛᴇᴅ 🔓**\n━━━━━━━━━━━━━━━\n{msg}"
        )


@app.on_message(filters.group & filters.command("imposter") & ~filters.bot & ~filters.via_bot & admin_filter)
async def set_mataa(_, message: Message):
    if len(message.command) == 1:
        return await message.reply(
            "ᴅᴇᴛᴇᴄᴛ ᴘʀᴇᴛᴇɴᴅᴇʀ ᴜsᴇʀs **ᴜsᴀɢᴇ:** `/imposter enable|disable`"
        )

    action = message.command[1].lower()
    if action == "enable":
        if await impo_on(message.chat.id):
            await message.reply("**ᴘʀᴇᴛᴇɴᴅᴇʀ ᴍᴏᴅᴇ ɪs ᴀʟʀᴇᴀᴅʏ ᴇɴᴀʙʟᴇᴅ.**")
        else:
            await impo_on(message.chat.id)
            await message.reply(f"**sᴜᴄᴄᴇssғᴜʟʟʏ ᴇɴᴀʙʟᴇᴅ ᴘʀᴇᴛᴇɴᴅᴇʀ ᴍᴏᴅᴇ ғᴏʀ** {message.chat.title}")

    elif action == "disable":
        if not await impo_off(message.chat.id):
            await message.reply("**ᴘʀᴇᴛᴇɴᴅᴇʀ ᴍᴏᴅᴇ ɪs ᴀʟʀᴇᴀᴅʏ ᴅɪsᴀʙʟᴇᴅ.**")
        else:
            await impo_off(message.chat.id)
            await message.reply(f"**sᴜᴄᴄᴇssғᴜʟʟʏ ᴅɪsᴀʙʟᴇᴅ ᴘʀᴇᴛᴇɴᴅᴇʀ ᴍᴏᴅᴇ ғᴏʀ** {message.chat.title}")

    else:
        await message.reply("**ᴅᴇᴛᴇᴄᴛ ᴘʀᴇᴛᴇɴᴅᴇʀ ᴜsᴇʀs ᴜsᴀɢᴇ : ᴘʀᴇᴛᴇɴᴅᴇʀ ᴏɴ|ᴏғғ**")
