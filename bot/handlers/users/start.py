from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.mainmenu import main_menu
from loader import dp
from .db_command import DBCommands

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await DBCommands.add_new_user()
    text = """✋Привет, это новый проект по заработку на капче,
тут можно зарабатывать до 1000 рублей в день за обычную капчу😜
на сайтах наших конкурентов люди тратят много сил и времени за копейки😖
у нас же работники получают достойную плату за свой труд😎
для управления ботом воспользуйтесь меню👇🏿
"""
    await message.answer(text, reply_markup=main_menu)
#{message.from_user.full_name}