from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(resize_keyboard=True,
                               keyboard=[
                                   [
                                       KeyboardButton(text="Оставьте заявку 🌐",),
                                       KeyboardButton(text="Контакт 📱", request_contact=True),
                                   ]
                               ])