from pyrogram import filters
from pyrogram.enums import ChatMembersFilter, ChatMemberStatus, ChatType
from pyrogram.types import Message

from HasiiMusic import app, config, db


@app.on_message(filters.command(["channelplay"]) & filters.group & ~app.bl_users)
async def channelplay_command(_, m: Message):
    """Enable or disable channel play mode."""
    # Check if user is admin
    member = await app.get_chat_member(m.chat.id, m.from_user.id)
    if member.status not in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
        return await m.reply_text("❌ Only admins can use this command.")

    if len(m.command) < 2:
        return await m.reply_text(
            f"**Channel Play Settings for {m.chat.title}**\n\n"
            "**To enable for linked channel:**\n"
            "`/channelplay linked`\n\n"
            "**To enable for any channel:**\n"
            "`/channelplay [channel_id]`\n\n"
            "**To disable channel play:**\n"
            "`/channelplay disable`"
        )

    query = m.text.split(None, 1)[1].lower().strip()

    # Disable channel play
    if query == "disable":
        await db.set_cmode(m.chat.id, None)
        return await m.reply_text("✅ **Channel play disabled.**")

    # Enable for linked channel
    elif query == "linked":
        chat = await app.get_chat(m.chat.id)
        if chat.linked_chat:
            channel_id = chat.linked_chat.id
            await db.set_cmode(m.chat.id, channel_id)
            return await m.reply_text(
                f"✅ **Channel play enabled for:** {chat.linked_chat.title}\n"
                f"**Channel ID:** `{chat.linked_chat.id}`"
            )
        else:
            return await m.reply_text("❌ **This chat doesn't have a linked channel.**")

    # Enable for specific channel
    else:
        try:
            chat = await app.get_chat(query)
        except:
            return await m.reply_text(
                "❌ **Failed to get channel.**\n\n"
                "Make sure you've added the bot as admin in the channel and promoted it as admin."
            )

        if chat.type != ChatType.CHANNEL:
            return await m.reply_text("❌ **Only channels are supported.**")

        # Check if user is owner of the channel
        try:
            async for user in app.get_chat_members(
                chat.id, filter=ChatMembersFilter.ADMINISTRATORS
            ):
                if user.status == ChatMemberStatus.OWNER:
                    owner_username = user.user.username
                    owner_id = user.user.id
        except:
            return await m.reply_text(
                "❌ **Failed to get channel.**\n\n"
                "Make sure you've added the bot as admin in the channel."
            )

        if owner_id != m.from_user.id:
            return await m.reply_text(
                f"❌ **You need to be the owner of channel {chat.title} to connect it with this group.**\n\n"
                f"**Channel's Owner:** @{owner_username}\n\n"
                "Alternatively, you can link your chat's channel and connect with `/channelplay linked`"
            )

        await db.set_cmode(m.chat.id, chat.id)
        return await m.reply_text(
            f"✅ **Channel play enabled for:** {chat.title}\n"
            f"**Channel ID:** `{chat.id}`"
        )
