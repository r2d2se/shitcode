import asyncio

from aiogram import Bot, Dispatcher

from tg_insert_data import tg_bot
from database import database1



ALOWED_UPDATES = ["message"]

bot = Bot(token="6537139791:AAG-dkwUAvH3HhpTlMEAQQ9KMS2lV3ErTzY")
dp = Dispatcher()

dp.include_router(tg_bot)

async def on_startup(dp):
    print('Бот вышел в онлайн')

async def on_shutdown(dp):
    print('Бот упал')

async def main():
    database1.sql_start()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=ALOWED_UPDATES, on_startup=on_startup, on_shutdown=on_shutdown)








asyncio.run(main())
