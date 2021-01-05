from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

for_pay = ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(text='🥝киви кошелек'),KeyboardButton(text='💳банковская карта')
         ],
        [
            KeyboardButton(text='❌отмена')
        ]
    ], resize_keyboard=True
)
