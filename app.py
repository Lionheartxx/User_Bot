# from aiogram import executor
#
# from loader import dp, db
# import middlewares, filters, handlers
# from utils.notify_admins import on_startup_notify
# from utils.set_bot_commands import set_default_commands
#
#
# async def on_startup(dispatcher):
#     # await db.drop_users()
#     await db.create()
#     # await db.create_table_users()
#
#     # Birlamchi komandalar (/star va /help)
#     await set_default_commands(dispatcher)
#
#     # Bot ishga tushgani haqida adminga xabar berish
#     await on_startup_notify(dispatcher)
#
#
# if __name__ == "__main__":
#     executor.start_polling(dp, on_startup=on_startup)

import logging
from aiogram import executor, types
from aiogram.types import InputFile
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from keyboards.inline.request_button import site_keys
from loader import dp, db, bot
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands

logging.basicConfig(level=logging.INFO)

scheduler = AsyncIOScheduler()

async def send_ad_to_all():
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
        # await bot.send_media_group(chat_id=user_id, media=album)
        # await bot.send_message(chat_id=user_id, text="Для просмотра услуг на нашем сайте нажмите кнопку ниже 👇", reply_markup=site_keys)
        try:
            await bot.send_media_group(chat_id=user_id, media=album)
            await bot.send_message(chat_id=user_id, text="Для просмотра услуг на нашем сайте нажмите кнопку ниже 👇",
                                   reply_markup=site_keys)
        except Exception as e:
            logging.error(f"Error sending message to {user_id}: {e}")

async def on_startup(dispatcher):
    # await db.drop_users()
    await db.create()
    # await db.create_table_users()

    # Birlamchi komandalar (/start va /help)
    await set_default_commands(dispatcher)

    # Bot ishga tushgani haqida adminga xabar berish
    await on_startup_notify(dispatcher)

    # Jadvalga avtomatik xabar yuborish funksiyasini qo'shish
    scheduler.add_job(send_ad_to_all, 'cron', hour=7, minute=0)
    scheduler.start()


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup)
