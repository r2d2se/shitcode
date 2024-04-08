import asyncio
import os

from aiogram import Bot, Dispatcher,F

from tg_insert_data import tg_bot
from database import database

ALOWED_UPDATES = ["message"]

token = os.environ['TOKEN']

bot = Bot(token=token)
dp = Dispatcher()

dp.include_router(tg_bot)

# async def on_startup(dp):
# print('Бот вышел в онлайн')

# async def on_shutdown(dp):
# print('Бот упал')


async def main():
    database.sql_start()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=ALOWED_UPDATES)


asyncio.run(main())
