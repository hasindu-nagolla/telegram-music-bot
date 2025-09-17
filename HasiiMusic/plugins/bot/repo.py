# from pyrogram import filters
# from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
# from HasiiMusic import app
# from config import BOT_USERNAME

# repo_caption = """**
# 🚀 ᴄʟᴏɴᴇ ᴀɴᴅ ᴅᴇᴘʟᴏʏ – ᴄᴇʀᴛɪꜰɪᴇᴅ ᴄᴏᴅᴇʀꜱ ʀᴇᴘᴏ 🚀

# ➤ ᴅᴇᴘʟᴏʏ ᴇᴀsɪʟʏ ᴏɴ ʜᴇʀᴏᴋᴜ ᴡɪᴛʜᴏᴜᴛ ᴇʀʀᴏʀꜱ  
# ➤ ɴᴏ ʜᴇʀᴏᴋᴜ ʙᴀɴ ɪꜱꜱᴜᴇ  
# ➤ ɴᴏ ɪᴅ ʙᴀɴ ɪꜱꜱᴜᴇ  
# ➤ ᴜɴʟɪᴍɪᴛᴇᴅ ᴅʏɴᴏꜱ  
# ➤ ʀᴜɴ 24/7 ʟᴀɢ ꜰʀᴇᴇ

# ɪꜰ ʏᴏᴜ ꜰᴀᴄᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ, ꜱᴇɴᴅ ꜱꜱ ɪɴ ꜱᴜᴘᴘᴏʀᴛ
# **"""

# @app.on_message(filters.command("repo"))
# async def show_repo(_, msg):
#     buttons = [
#         [InlineKeyboardButton("➕ ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ ✨", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
#         [
#             InlineKeyboardButton("👑 ᴏᴡɴᴇʀ", url="https://t.me/Hasindu_Lakshan"),
#             InlineKeyboardButton("💬 ꜱᴜᴘᴘᴏʀᴛ", url="https://t.me/CertifiedCodes")
#         ],
#         [
#             InlineKeyboardButton("🛠️ ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ", url="https://t.me/srilankandragonhouse"),
#             InlineKeyboardButton("🎵 ɢɪᴛʜᴜʙ", url="https://github.com/hasindu-nagolla/HasiiMusicBot")
#         ]
#     ]

#     reply_markup = InlineKeyboardMarkup(buttons)

#     await msg.reply_photo(
#         photo="https://i.ibb.co/tprHKhYc/hasii.png",
#         caption=repo_caption,
#         reply_markup=reply_markup
#     )

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
        [InlineKeyboardButton("💬 Support", url="https://t.me/CertifiedCodes")]
    ]

    reply_markup = InlineKeyboardMarkup(buttons)

    await msg.reply_photo(
        photo="https://i.ibb.co/tprHKhYc/hasii.png",
        caption=repo_caption,
        reply_markup=reply_markup
    )

