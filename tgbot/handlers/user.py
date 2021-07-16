import asyncio
import logging

from aiogram import Dispatcher, types
from aiogram.types import Message
from aiogram.utils.markdown import quote_html


async def user_start(message: Message):
    await message.reply("Hello, user!")




def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")
    # dp.bot.set_my_commands([
    #     types.BotCommand("start", "Установить фото в чате"),
    #     types.BotCommand("set_title", "Установить название группы"),
    #     types.BotCommand("set_description", "Установить описание группы"),
    #     types.BotCommand("ro", "Режим Read Only"),
    #     types.BotCommand("unro", "Отключить RO"),
    #     types.BotCommand("ban", "Забанить"),
    #     types.BotCommand("unban", "Разбанить"),
    # ])