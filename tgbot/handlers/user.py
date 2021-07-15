import asyncio

from aiogram import Dispatcher, types
from aiogram.types import Message


async def user_start(message: Message):
    await message.reply("Hello, user!")


async def hello_user(message: Message):
    members = ", ".join(m.get_mention(as_html=True) for m in message.new_chat_members)
    msg = await message.reply(f"Привет, {members}")
    await asyncio.sleep(10)
    await message.delete()
    await msg.delete()


async def bye_user(message: Message):
    await message.delete()


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")
    dp.register_message_handler(hello_user, content_types=types.ContentTypes.NEW_CHAT_MEMBERS,  state="*")
    dp.register_message_handler(bye_user, content_types=types.ContentTypes.LEFT_CHAT_MEMBER,  state="*")
    dp.bot.set_my_commands([
        types.BotCommand("set_photo", "Установить фото в чате"),
        types.BotCommand("set_title", "Установить название группы"),
        types.BotCommand("set_description", "Установить описание группы"),
        types.BotCommand("ro", "Режим Read Only"),
        types.BotCommand("unro", "Отключить RO"),
        types.BotCommand("ban", "Забанить"),
        types.BotCommand("unban", "Разбанить"),
    ])