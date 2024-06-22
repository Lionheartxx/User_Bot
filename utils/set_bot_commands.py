# from aiogram import types
#
#
# async def set_default_commands(dp):
#     await dp.bot.set_my_commands(
#         [
#             types.BotCommand("start", "Запустить бота"),
#             types.BotCommand("help", "Помощь"),
#             types.BotCommand("services", "Услуги"),
#             types.BotCommand("reklama", "Услуги"),
#             types.BotCommand("allusers", "Услуги"),
#         ]
#     )
from aiogram import types
from data.config import ADMINS  # ADMINS ro'yxatini o'zgartiring, kerak bo'lsa

async def set_default_commands(dp):
    commands = [
        types.BotCommand("start", "Запустить бота"),
        types.BotCommand("help", "Помощь"),
        types.BotCommand("services", "Услуги"),
    ]

    if ADMINS:
        commands.extend([
            types.BotCommand("reklama", "Реклама (виден только администраторам)"),
            types.BotCommand("allusers", "Все пользователи (виден только администраторам)"),
        ])

    await dp.bot.set_my_commands(commands)