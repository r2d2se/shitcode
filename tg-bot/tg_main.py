import asyncio

from aiogram import Bot, Dispatcher

from tg_insert_data import tg_bot

ALOWED_UPDATES = ["message"]

bot = Bot(token="")
dp = Dispatcher()

dp.include_router(tg_bot)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=ALOWED_UPDATES)


asyncio.run(main())
