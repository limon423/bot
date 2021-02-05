from load_all import dp, bot, payload_token, types
from aiogram.dispatcher.filters import Text, Command, state
from keyboards import menu, sellmenu, button
from states import Events
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
from aiogram.types.message import ContentType


price = types.LabeledPrice(label='схема заработка', amount=100*100)


def get_scheme():
    file = open('scheme.txt')
    s = ''
    for i in file:
        s += i
    return s


@dp.message_handler(Text(equals='схема'))
async def scheme(message: types.Message):
    link_site = '2ip.ru'
    text = f'''эта схема для сайта {link_site}, 
с помощью нее вы сможете заработать денег, но не заигрываитесь!
эффективность схемы: 90%
в случае провала мы даем другую схему бесплатно!
нажмите "оплата" для продолжения
'''
    await Events.buy.set()
    await message.answer(text, reply_markup=sellmenu)


@dp.message_handler(Text(equals='купить схему'), state=Events.buy.state)
async def process_buy_command(message: types.Message):
    if payload_token.split(':')[1] == 'TEST':
        await bot.send_message(message.chat.id, 'это тестовый платеж')
    await bot.send_invoice(message.chat.id,
                           title='качественный контент',
                           description='описание',
                           provider_token=payload_token,
                           currency='rub',
                           is_flexible=False,  # True если конечная цена зависит от способа доставки
                           prices=[price],
                           start_parameter='scheme_example',
                           payload='оплачено'
                           )


@dp.pre_checkout_query_handler(lambda query: True)
async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def process_successful_payment(message: types.Message, state: FSMContext):
    print('successful_payment:')
    pmnt = message.successful_payment.to_python()
    for key, val in pmnt.items():
        print(f'{key} = {val}')
    await state.finish()
    await bot.send_message(
        message.chat.id,
        get_scheme().format(
            total_amount=message.successful_payment.total_amount // 100,
            currency=message.successful_payment.currency
        )
    )


