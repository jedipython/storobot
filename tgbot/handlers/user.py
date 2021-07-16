import asyncio
import logging

from aiogram import Dispatcher, types
from aiogram.types import Message
from aiogram.utils.markdown import quote_html
from tgbot.misc.checking import connect_to_telethon


async def user_start(message: Message):
    text = '''Привет! Я СтоРобот, твой помощник и главный аналитик.
    
- Выполняю полный анализ телеграм групп и каналов
- Выявляю удаленные аккаунты, ботов,спамеров и неактивных юзеров

Чтобы я всегда мог помочь тебе с анализом, добавь меня в Администраторы своего канала или группы с правом на добавление админов.

Итак, добавил? А теперь, пришли @юзернейм канала или группы и я начну работу!
'''
    await message.answer(text=text)


async def others_message(message: Message):
    await message.answer(text="Похоже, вы отправили мне немного не то, что нужно. "
                              "Пришлите @юзернейм канала/группы ")


async def channel_link(message: Message):
    message_text = message.text
    if message_text[0] == '@':
        try:
            result = await connect_to_telethon(message_text)
            await message.answer(result)
        except Exception as err:
            await message.answer(err)

    else:
        await others_message(message)
    
    
def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")
    dp.register_message_handler(channel_link, content_types=types.ContentType.TEXT,state="*")
    dp.register_message_handler(others_message, state="*")
    # dp.bot.set_my_commands([
    #     types.BotCommand("start", "Установить фото в чате"),
    #     types.BotCommand("set_title", "Установить название группы"),
    #     types.BotCommand("set_description", "Установить описание группы"),
    #     types.BotCommand("ro", "Режим Read Only"),
    #     types.BotCommand("unro", "Отключить RO"),
    #     types.BotCommand("ban", "Забанить"),
    #     types.BotCommand("unban", "Разбанить"),
    # ])