import os
import base64
import mimetypes

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ChatAction

from lexica import AsyncClient, languageModels, Messages
from HasiiMusic import app


def get_prompt(message: Message) -> str | None:
    parts = message.text.split(' ', 1)
    return parts[1] if len(parts) > 1 else None


def extract_content(response) -> str | None:
    content = response.get('content')
    if isinstance(content, str):
        return content
    elif isinstance(content, list):
        return '\n'.join(item['text'] for item in content if isinstance(item, dict) and 'text' in item)
    elif isinstance(content, dict):
        if 'parts' in content and isinstance(content['parts'], list):
            return '\n'.join(part.get('text', '') for part in content['parts'] if 'text' in part)
        return content.get('text')
    return None


def format_response(model_name: str, content: str) -> str:
    return f"**ᴍᴏᴅᴇʟ:** `{model_name}`\n\n**ʀᴇsᴘᴏɴsᴇ:**\n{content}"


async def handle_text_model(message: Message, model, model_name: str, as_messages=False):
    prompt = get_prompt(message)
    if not prompt:
        return await message.reply_text("Please provide a prompt after the command.")

    await message._client.send_chat_action(message.chat.id, ChatAction.TYPING)

    lexica_client = AsyncClient()
    try:
        data = [Messages(content=prompt, role="user")] if as_messages else prompt
        response = await lexica_client.ChatCompletion(data, model)
        content = extract_content(response)
        await message.reply_text(format_response(model_name, content) if content else "No content received from the API.")
    except Exception as e:
        await message.reply_text(f"An error occurred: {e}")
    finally:
        await lexica_client.close()


@app.on_message(filters.command("bard"))
async def bard_handler(client: Client, message: Message):
    await handle_text_model(message, languageModels.bard, "Bard")


@app.on_message(filters.command("gemini"))
async def gemini_handler(client: Client, message: Message):
    await handle_text_model(message, languageModels.gemini, "Gemini", as_messages=True)


@app.on_message(filters.command("gpt"))
async def gpt_handler(client: Client, message: Message):
    await handle_text_model(message, languageModels.gpt, "GPT", as_messages=True)


@app.on_message(filters.command("llama"))
async def llama_handler(client: Client, message: Message):
    await handle_text_model(message, languageModels.llama, "LLaMA", as_messages=True)


@app.on_message(filters.command("mistral"))
async def mistral_handler(client: Client, message: Message):
    await handle_text_model(message, languageModels.mistral, "Mistral", as_messages=True)


@app.on_message(filters.command("geminivision"))
async def geminivision_handler(client: Client, message: Message):
    if not (message.reply_to_message and message.reply_to_message.photo):
        return await message.reply_text("Please reply to an image with the /geminivision command and a prompt.")

    prompt = get_prompt(message)
    if not prompt:
        return await message.reply_text("Please provide a prompt after the command.")

    await client.send_chat_action(message.chat.id, ChatAction.TYPING)
    status = await message.reply_text("Processing your image, please wait...")


    try:
        file_path = await client.download_media(message.reply_to_message.photo.file_id)
    except Exception as e:
        await status.delete()
        return await message.reply_text(f"❌ Failed to download image.\nError: {e}")

    lexica_client = AsyncClient()

    try:
        with open(file_path, "rb") as f:
            data = base64.b64encode(f.read()).decode()
        mime_type, _ = mimetypes.guess_type(file_path)
        image_info = [{"data": data, "mime_type": mime_type}]

        response = await lexica_client.ChatCompletion(prompt, languageModels.geminiVision, images=image_info)
        content = extract_content(response)
        await message.reply_text(format_response("Gemini Vision", content) if content else "No content received from the API.")
    except Exception as e:
        await message.reply_text(f"An error occurred: {e}")
    finally:
        await status.delete()
        await lexica_client.close()
        os.remove(file_path)
