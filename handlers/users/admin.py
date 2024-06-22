import asyncio
from aiogram.types import InputFile
from aiogram import types
from handlers.users.contact_handler import send_link
from data.config import ADMINS
from keyboards.inline.request_button import site_keys
from loader import dp, db, bot


@dp.message_handler(text="/reklama", user_id=ADMINS)
async def send_ad_to_all(message: types.Message):
    users = await db.select_all_users()
    for user in users:
        # print(user[3])
        user_id = user[3]
        album = types.MediaGroup()
        photo1 = InputFile(path_or_bytesio="photos/1.jpg")
        photo3 = "https://1mo.pro/img/gallery/5.jpg"
        photo4 = "https://1mo.pro/img/gallery/1.jpg"
        photo5 = "https://1mo.pro/img/gallery/6.jpg"
        photo6 = "https://1mo.pro/img/gallery/4.jpg"
        photo7 = "https://1mo.pro/img/gallery/3.jpg"

        # Attaching photos to the media group
        album.attach_photo(photo=photo7)
        album.attach_photo(photo=photo4)
        album.attach_photo(photo=photo1)
        album.attach_photo(photo=photo5)
        album.attach_photo(photo=photo6)
        album.attach_photo(photo=photo3,
                           caption="🔹 <b>Наша компания работает с 2019 года и предлагает следующие клининговые услуги для физических и юридических лиц:</b> \n"
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

        # Sending the media group and additional message
        await bot.send_media_group(chat_id=user_id, media=album)
        await bot.send_message(chat_id=user_id, text="Для просмотра услуг на нашем сайте нажмите кнопку ниже 👇", reply_markup=site_keys)
        await asyncio.sleep(0.05)

@dp.message_handler(commands=['allusers'], user_id=ADMINS)
async def get_all_users(message: types.Message):
    count = await db.count_users()  # Foydalanuvchilar sonini hisoblash
    await message.answer(f"В базе <b>{count}</b> пользователя")  # Javobni foydalanuvchiga jo'natish