from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from HasiiMusic import app
from HasiiMusic.misc import SUDOERS, db
from HasiiMusic.utils.database import (
    get_authuser_names,
    get_cmode,
    get_lang,
    get_upvote_count,
    is_active_chat,
    is_maintenance,
    is_nonadmin_chat,
    is_skipmode,
)
from config import SUPPORT_CHAT, adminlist, confirmer
from strings import get_string
from ..formatters import int_to_alpha


# ---------------------------- AdminRightsCheck ---------------------------- #
def AdminRightsCheck(mystic):
    async def wrapper(client, message):
        # Maintenance lock
        if await is_maintenance() is False:
            if message.from_user.id not in SUDOERS:
                return await message.reply_text(
                    text=f"{app.mention} ɪs ᴜɴᴅᴇʀ ᴍᴀɪɴᴛᴇɴᴀɴᴄᴇ, "
                         f"ᴠɪsɪᴛ <a href={SUPPORT_CHAT}>sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ</a> ғᴏʀ ᴅᴇᴛᴀɪʟs.",
                    disable_web_page_preview=True,
                )

        # Delete user command to keep group clean
        try:
            await message.delete()
        except Exception:
            pass

        # Language
        try:
            language = await get_lang(message.chat.id)
            _ = get_string(language)
        except Exception:
            _ = get_string("en")

        # Skip anonymous senders
        if message.sender_chat:
            upl = InlineKeyboardMarkup(
                [[InlineKeyboardButton("ʜᴏᴡ ᴛᴏ ғɪx ?", callback_data="AnonymousAdmin")]]
            )
            return await message.reply_text(_["general_3"], reply_markup=upl)

        # Resolve channel‑mode chat
        if message.command[0][0] == "c":
            chat_id = await get_cmode(message.chat.id)
            if chat_id is None:
                return await message.reply_text(_["setting_7"])
            try:
                await app.get_chat(chat_id)
            except Exception:
                return await message.reply_text(_["cplay_4"])
        else:
            chat_id = message.chat.id

        # Require active chat
        if not await is_active_chat(chat_id):
            return await message.reply_text(_["general_5"])

        # Admin privilege enforcement
        is_non_admin = await is_nonadmin_chat(message.chat.id)
        uid = message.from_user.id
        if not is_non_admin and uid not in SUDOERS:
            try:
                member = await app.get_chat_member(message.chat.id, uid)

                # Check by privilege OR status
                is_admin = bool(
                    getattr(member, "privileges", None)
                    or member.status in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]
                )

                if not is_admin:
                    # Normal user — block or start vote, depending on skipmode
                    if await is_skipmode(message.chat.id):
                        upvote = await get_upvote_count(chat_id)
                        text = (
                            f"<b>ᴀᴅᴍɪɴ ʀɪɢʜᴛs ɴᴇᴇᴅᴇᴅ</b>\n\n"
                            f"ʀᴇғʀᴇsʜ ᴀᴅᴍɪɴ ᴄᴀᴄʜᴇ ᴠɪᴀ : /reload\n\n"
                            f"» {upvote} ᴠᴏᴛᴇs ɴᴇᴇᴅᴇᴅ ғᴏʀ ᴘᴇʀғᴏʀᴍɪɴɢ ᴛʜɪs ᴀᴄᴛɪᴏɴ."
                        )
                        command = message.command[0].lstrip("c")
                        if command == "speed":
                            return await message.reply_text(_["admin_14"])
                        MODE = command.title()
                        upl = InlineKeyboardMarkup(
                            [[
                                InlineKeyboardButton(
                                    "ᴠᴏᴛᴇ",
                                    callback_data=f"ADMIN UpVote|{chat_id}_{MODE}"
                                )
                            ]]
                        )
                        if chat_id not in confirmer:
                            confirmer[chat_id] = {}
                        try:
                            vidid = db[chat_id][0]["vidid"]
                            file = db[chat_id][0]["file"]
                        except Exception:
                            return await message.reply_text(_["admin_14"])
                        senn = await message.reply_text(text, reply_markup=upl)
                        confirmer[chat_id][senn.id] = {"vidid": vidid, "file": file}
                        return
                    else:
                        return await message.reply_text(_["admin_14"])
            except Exception:
                return await message.reply_text(_["admin_14"])

        return await mystic(client, message, _, chat_id)

    return wrapper


# ---------------------------- AdminActual ---------------------------- #
def AdminActual(mystic):
    async def wrapper(client, message):
        if await is_maintenance() is False:
            if message.from_user.id not in SUDOERS:
                return await message.reply_text(
                    text=f"{app.mention} ɪs ᴜɴᴅᴇʀ ᴍᴀɪɴᴛᴇɴᴀɴᴄᴇ, "
                         f"ᴠɪsɪᴛ <a href={SUPPORT_CHAT}>sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ</a> ғᴏʀ ᴅᴇᴛᴀɪʟs.",
                    disable_web_page_preview=True,
                )

        try:
            await message.delete()
        except Exception:
            pass

        try:
            language = await get_lang(message.chat.id)
            _ = get_string(language)
        except Exception:
            _ = get_string("en")

        if message.sender_chat:
            upl = InlineKeyboardMarkup(
                [[InlineKeyboardButton("ʜᴏᴡ ᴛᴏ ғɪx ?", callback_data="AnonymousAdmin")]]
            )
            return await message.reply_text(_["general_3"], reply_markup=upl)

        if message.from_user.id not in SUDOERS:
            try:
                member = await app.get_chat_member(message.chat.id, message.from_user.id)
                if not (
                    getattr(member, "privileges", None)
                    or member.status in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]
                ):
                    return await message.reply_text(_["general_4"])
            except Exception:
                return await message.reply_text(_["general_4"])

        return await mystic(client, message, _)

    return wrapper


# ---------------------------- ActualAdminCB ---------------------------- #
def ActualAdminCB(mystic):
    async def wrapper(client, CallbackQuery):
        if await is_maintenance() is False:
            if CallbackQuery.from_user.id not in SUDOERS:
                return await CallbackQuery.answer(
                    f"{app.mention} ɪs ᴜɴᴅᴇʀ ᴍᴀɪɴᴛᴇɴᴀɴᴄᴇ.",
                    show_alert=True,
                )

        try:
            language = await get_lang(CallbackQuery.message.chat.id)
            _ = get_string(language)
        except Exception:
            _ = get_string("en")

        if CallbackQuery.message.chat.type == ChatType.PRIVATE:
            return await mystic(client, CallbackQuery, _)

        is_non_admin = await is_nonadmin_chat(CallbackQuery.message.chat.id)
        if not is_non_admin:
            try:
                member = await app.get_chat_member(
                    CallbackQuery.message.chat.id,
                    CallbackQuery.from_user.id,
                )
                if not (
                    getattr(member, "privileges", None)
                    or member.status in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]
                ):
                    return await CallbackQuery.answer(_["general_4"], show_alert=True)
            except Exception:
                return await CallbackQuery.answer(_["general_4"], show_alert=True)

        return await mystic(client, CallbackQuery, _)

    return wrapper
