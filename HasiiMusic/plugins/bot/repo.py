from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from HasiiMusic import app

# Updated repository caption
repo_caption = """**
🚀 ᴄʟᴏɴᴇ ᴀɴᴅ ᴅᴇᴘʟᴏʏ – ʀᴇᴘᴏ 🚀

➤ ᴅᴇᴘʟᴏʏ ᴇᴀsɪʟʏ ᴏɴ ʜᴇʀᴏᴋᴜ ᴡɪᴛʜᴏᴜᴛ ᴇʀʀᴏʀꜱ  
➤ ɴᴏ ʜᴇʀᴏᴋᴜ ʙᴀɴ ɪꜱꜱᴜᴇ  
➤ ɴᴏ ɪᴅ ʙᴀɴ ɪꜱꜱᴜᴇ  
➤ ᴜɴʟɪᴍɪᴛᴇᴅ ᴅʏɴᴏꜱ  
➤ ʀᴜɴ 24/7 ʟᴀɢ ꜰʀᴇᴇ

✨ ᴄʀᴇᴅɪᴛ ᴛᴏ ᴄᴇʀᴛɪꜰɪᴇᴅ ᴄᴏᴅᴇʀꜱ – ᴛʜᴇ ᴏʀɪɢɪɴᴀʟ ᴍɪɴᴅs ʙᴇʜɪɴᴅ ᴛʜɪs ʙᴏᴛ ✨

ɪꜰ ʏᴏᴜ ʀᴜɴ ɪɴᴛᴏ ᴘʀᴏʙʟᴇᴍꜱ, ᴊᴜꜱᴛ ꜱᴇɴᴅ ᴀ ꜱꜱ ɪɴ ᴏᴜʀ ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ
**"""

@app.on_message(filters.command("repo"))
async def show_repo(_, msg):
    buttons = [
        [InlineKeyboardButton("➕ ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ ✨", url="https://t.me/HasiiMucisBot?startgroup=true")],
        [InlineKeyboardButton("🚀 Hosted by", url="https://t.me/Hasindu_Lakshan")],
        [InlineKeyboardButton("💬 Support", url="https://t.me/Hasindu_Lakshan")]
    ]

    reply_markup = InlineKeyboardMarkup(buttons)

    await msg.reply_photo(
        photo="https://i.ibb.co/tprHKhYc/hasii.png",
        caption=repo_caption,
        reply_markup=reply_markup
    )

