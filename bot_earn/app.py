from load_all import bot, admin, types
from aiogram import executor
from aiogram.types import ReplyKeyboardRemove


async def on_start(dp):
    await bot.send_message(admin, text='бот запущен!')


if __name__ == '__main__':
    from handlers import dp
    print('bot load...')
    executor.start_polling(dp, on_startup=on_start)

