from keyboards.callback import payment
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from load_all import qiwi_number
qiwi_url = f'https://qiwi.com/payment/form/99?currency=643&extra[%27account%27]={qiwi_number}&amountInteger=1&amountFraction=0&blocked[0]=account'
checker = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='купить', url=qiwi_url)
        ],
        [
            InlineKeyboardButton(text='проверить оплату', callback_data=payment.new(id=231))
        ]
    ]
)
