from aiogram import types
from aiogram.types import InputFile
from aiogram.types import Message
from keyboards.default.site_link import link
from keyboards.inline.request_button import site_keys
from loader import dp, db, bot
from data.config import ADMINS


@dp.message_handler(content_types='contact')
async def get_contact(message: Message):
    contact = message.contact
    if contact is not None:
        # Foydalanuvchining telefon raqamini bazaga qo'shish
        user = await db.add_user_contact(
            telegram_id=contact.user_id,
            phone_number=contact.phone_number
        )
        await message.answer(f"Спасибо, <b>{contact.full_name}</b>.\n\n"
                             f"Мы получили ваш номер {contact.phone_number}.\n📞Наш администратор свяжется с вами.",
                             reply_markup=link)
        await bot.send_message(
            chat_id=ADMINS[0],
            text=f"Пользователь {contact.full_name} @{message.from_user.username} \nотправил ({contact.phone_number}) номер телефона.\n "
        )


@dp.message_handler(text="Оставьте заявку 🌐")
async def send_link(message: Message):
    album = types.MediaGroup()
    photo1 = InputFile(path_or_bytesio="photos/1.jpg")
    photo3 = "https://1mo.pro/img/gallery/5.jpg"
    photo4 = "https://1mo.pro/img/gallery/1.jpg"
    photo5 = "https://1mo.pro/img/gallery/6.jpg"
    photo6 = "https://1mo.pro/img/gallery/4.jpg"
    photo7 = "https://1mo.pro/img/gallery/3.jpg"
    album.attach_photo(photo=photo7)
    album.attach_photo(photo=photo4)
    album.attach_photo(photo=photo1)
    album.attach_photo(photo=photo5)
    album.attach_photo(photo=photo6)
    album.attach_photo(photo=photo3, caption="🔹 <b>Наша компания работает с 2019 года и предлагает следующие клининговые услуги для физических и юридических лиц:</b> \n"
                                             "🧹Генеральная уборка \n"
                                             "🧽Поддерживающая уборка \n"
                                             "🏠Уборка после ремонта \n"
                                             "🪟Мытье окон \n"
                                             "🧼Мытье плинтусов \n"
                                             "🏢Мытье фасадов \n"
                                             "🧴Глубокая уборка \n"
                                             "🔬Химическая чистка \n"
                                             "🌧️Уборка водостоков \n"
                                             "🪑Уборка паркета \n"
                                             "🧹Уборка плитки 🪟жалюзи 🪟ставней 🏊бассейна и.т.д.\n"
                                             "\n✨ <i>Многие люди хотят, чтобы их дом был наполнен светом через чистые окна и имел красивый фасад, радующий глаз.</i>")

    await message.answer_media_group(media=album)
    await message.answer("Для просмотра услуг на нашем сайте нажмите кнопку ниже 👇", reply_markup=site_keys)