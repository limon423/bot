from load_all import dp, bot
from aiogram import types
from aiogram.dispatcher.filters import Text, Command
from keyboards import menu, sellmenu, button
from states import Events
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove


@dp.message_handler(Text(equals='помощь'))
async def help(message: types.Message):
    link = ''
    text = f'''появились вопросы?
нашли недоработку в боте?
пишите, администрация рассматривает каждый вопрос: {link}'''
    await message.answer(text)


@dp.message_handler(Text(equals='отзывы'))
async def reviems(message: types.Message):
    link = ''
    await message.answer(f'здесь вы найдете отзывы людей о боте: {link}')


@dp.message_handler(Text(equals='на главную'), state=[Events.buy, Events.reviem, None])
async def cancel(message: types.Message, state: FSMContext):
    await state.finish()
    text = 'вы вернулись в меню'
    await message.answer(text, reply_markup=menu)


@dp.message_handler(Command('start'))
async def start(message: types.Message):
    text = '''привет, это бот, который помогает людям зарабатывать деньги
как это работает? я ищу разные способы как обмануть системы игровых
сайтов, создаю на основе полученных данныхсхемы и продаю их за небольшую плату
(полученные средства пойдут на разработку бота и поддержания его 
работоспособности, я не получу денег с этого).
более подробная информация в меню(управлять ботом также через меню)
'''
    await message.answer(text, reply_markup=menu)

