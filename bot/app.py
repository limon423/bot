import asyncio
from loader import bot, create_db
import middlewares
from data.config import admin
import logging

logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)


async def on_startup(dp):
    middlewares.setup(dp)

    await asyncio.sleep(7)
    await create_db()
    await bot.send_message(admin, text='я запущен')


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp
    logging.info('Bot started')
    executor.start_polling(dp, on_startup=on_startup)