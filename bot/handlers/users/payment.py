from loader import dp
from aiogram.types import Message
import keyboards
from aiogram.dispatcher.filters import Text
from aiogram import types
from states.state_pay import Paying
from aiogram.dispatcher import FSMContext
from .db_command import DBCommands

mess = f'укажите ваши реквизиты'


@dp.message_handler(Text(equals=["💸вывод денег"]))
async def money(message:types.Message):
    await Paying.choose_system.set()
    text = 'выберите, куда хотите вывести деньги💵'
    await message.answer(text, reply_markup=keyboards.default.for_pay)


@dp.message_handler(Text(equals=['❌отмена', "⬅главное меню"]), state=[Paying.choose_system, Paying.get_wallet, Paying.choose_quant])
async def cancel(message: Message, state: FSMContext):
    text = "🚫вы отменили операцию"
    if message.text == '⬅главное меню':
        text = "вы вернулись в меню"
    await message.answer(text, reply_markup=keyboards.default.main_menu)
    await state.finish()


@dp.message_handler(Text(equals='🥝киви кошелек'), state=Paying.choose_system)
async def qiwi_wallet(message: Message):
    await message.answer(mess, reply_markup=keyboards.default.go_to_menu)
    await Paying.get_wallet.set()


@dp.message_handler(Text(equals='💳банковская карта'), state=Paying.choose_system)
async def bank_card(message: Message):
    await message.answer(mess, reply_markup=keyboards.default.go_to_menu)
    await Paying.get_wallet.set()


@dp.message_handler(state=Paying.get_wallet)
async def bank_card(message: Message):
    balance = await DBCommands.check_balance()
    text = f'ваш баланс:{balance} \nукажите сумму, которую хотите вывести'
    await message.answer(text)
    await Paying.choose_quant.set()


@dp.message_handler(state=Paying.choose_quant)
async def bank_card(message: Message,state: FSMContext):
    balance = await DBCommands.check_balance()
    text = f'недостаточно средств на балансе😞\nбаланс:{balance}'
    key = None
    if balance>int(message.text):
        text = 'чтобы начать выводить деньги, вам нужно купить vip-статус,\nболее подробно вы узнаете, нажав на кнопку \"💎купить vip-статус💎\"'
        await state.finish()
        key = keyboards.default.end_menu
    await message.answer(text, reply_markup=key)

