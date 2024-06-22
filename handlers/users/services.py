from aiogram import types
from handlers.users.contact_handler import send_link
from loader import dp


# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await send_link(message)