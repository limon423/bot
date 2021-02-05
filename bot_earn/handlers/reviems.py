from load_all import dp, bot
from aiogram import types
from aiogram.dispatcher.filters import Text, Command
from keyboards import menu, sellmenu, button
from states import Events
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

link = 'link'
nick = 'nickname'


@dp.message_handler(Text(equals='оставить отзыв'))
async def get_reviem(message: types.Message):
    text = f'''напишите свой отзыв админу и он будет опубликован в группе 
админ:{nick}
группа:{link}'''
    await message.answer(text, reply_markup=button)
