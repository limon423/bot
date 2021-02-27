from load_all import dp
from aiogram import types
from aiogram.dispatcher.filters import Text, Command
from keyboards import menu
from states import Events
from aiogram.dispatcher import FSMContext

nick = '@notfatcat'
nick_dev = '@devdef43'


@dp.message_handler(Text(equals='вернуться в меню'), state=[None, Events.ask_num])
async def cancel(message: types.Message, state: FSMContext):
    text = 'вы вернулись в меню'
    await state.finish()
    await message.answer(text, reply_markup=menu)


@dp.message_handler(Text(equals='помощь'))
async def help(message: types.Message):
    text = f'''появились вопросы?
нашли недоработку в боте?
проблемы с оплатой?
пишите, администрация рассматривает каждый вопрос: {nick}'''
    await message.answer(text)


@dp.message_handler(Command('start'))
async def start(message: types.Message):
    text = '''привет, это бот, который поможет тебе 
приобрести стратегии заработка для таких сайтов как: 
nvuti, play2x, up-x, cabura и другие
используй кнопки внизу чтобы пользоваться ботом
'''
    await message.answer(text, reply_markup=menu)


@dp.message_handler(Text(equals='нужен бот?'))
async def get_reviem(message: types.Message):
    text = f'''принимаем заказы на телеграм ботов для любых целей за скромную цену
чтобы заказать пишите разработчику: {nick_dev}'''
    await message.answer(text)
