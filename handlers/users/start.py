import asyncpg
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.contact_button import menu
from keyboards.inline.request_button import site_keys
from loader import dp, db, bot
from data.config import ADMINS


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    try:
        user = await db.add_user(
            telegram_id=message.from_user.id,
            full_name=message.from_user.full_name,
            username=message.from_user.username,
        )

        # Yangi foydalanuvchi qo'shilganda xabar yuborish
        count = await db.count_users()
        msg = (f"<b>{message.from_user.full_name}</b>\n"
               f"<b>@{message.from_user.username}</b>\n"
               f"<b>ID: {message.from_user.id}</b>\n"
               f"______________________________\n"
               f"Добавлено в базу данных\n"
               f"В базе данных <b>{count}</b> пользователей")
        await bot.send_message(chat_id=ADMINS[0], text=msg)

    except asyncpg.exceptions.UniqueViolationError:
        # Foydalanuvchi allaqachon mavjud bo'lsa
        user = await db.select_user(telegram_id=message.from_user.id)

        # Foydalanuvchi qayta start bosganda xabar yuborish
        again = (f"<b>{message.from_user.full_name}</b>\n"
                 f"<b>@{message.from_user.username}</b>\n"
                 f"<b>ID: {message.from_user.id}</b>\n\n"
                 f"🔄 пользователь снова нажал <code>/start</code>")
        await bot.send_message(chat_id=ADMINS[0], text=again)

    # Foydalanuvchiga xush kelibsiz xabarini yuborish
    photo_url = "https://1mo.pro/img/gallery/2.jpg"
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=photo_url,
        caption=(
            f"Здравствуйте👋 <b>{message.from_user.full_name}</b> \n"
            f"Добро пожаловать! 😊\n\n"
            f"Оставите заявку на нашем сайте - <a href='https://1mo.pro/'>1mo.pro</a>\n"
            f"Наша компания предлагает следующие клининговые услуги 🧹.\n"
            f"Нажмите кнопку ниже, чтобы просмотреть услуги на нашем сайте."),
        reply_markup=site_keys
    )
    await bot.send_message(
        chat_id=message.from_user.id,
        text="📞",
        reply_markup=menu
    )
