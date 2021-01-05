from loader import dp
from aiogram.types import Message
from keyboards.default.mainmenu import main_menu, go_to_menu
from aiogram.dispatcher.filters import Text
from .db_command import DBCommands


@dp.message_handler(Text(equals=['назад', '⬅главное меню']), state=None)
async def show_menu(message: Message):
    text = 'вы вернулись в меню'
    await message.answer(text, reply_markup=main_menu)


@dp.message_handler(Text(equals='📊статистика'))
async def statistic(message: Message):
    users = await DBCommands.count_users()+14132
    text = f'👥посетители: {users} пользователей\n⏰статистика обновляется в реальном времени!'
    await message.answer(text, reply_markup=main_menu)


@dp.message_handler(Text(equals='💰баланс'))
async def balance(message: Message):
    balance = await DBCommands.check_balance()
    text = f'💵ваш баланс: {balance} rub'
    await message.answer(text, reply_markup=main_menu)


@dp.message_handler(Text(equals='💎купить vip-статус💎'))
async def extra_earn(message: Message):
    payment_count = 'link'
    text = f"""vip-статус стоит 400 рублей, но в честь праздников🎅 
мы решили вас порадовать и снизили цену до 100 рублей!❄️
купив vip-статус сможете:
  ✅решать капчу не за 20 рублей, а за 40!
  ✅сможете выводить средства!
  ✅иметь пассивный доход с капчи!
  ✅зарабатывать намного больше, чем у наших конкурентов!
  ✅получать новости об обновлениях и новостях первыми!
  ❓а также появится таинственная опция, которой нет у обычных юзеров...❓
❗поспеши, скидка действует только до 10 января❗
для покупки оплатите счет: {payment_count}"""
    await message.answer(text, reply_markup=go_to_menu)