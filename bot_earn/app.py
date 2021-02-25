from load_all import bot, admin, types, db, sql
from aiogram import executor


async def on_start(dp):
    sql.execute("""CREATE TABLE IF NOT EXISTS users(
id INT, 
number TEXT,
sum INT, 
checknum TEXT)""")
    db.commit()
    await bot.send_message(admin, text='бот запущен!')


if __name__ == '__main__':
    from handlers import dp
    print('bot load...')
    executor.start_polling(dp, on_startup=on_start)

