from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

sellmenu = ReplyKeyboardMarkup([
    [
        KeyboardButton('купить схему')
    ],
    [
        KeyboardButton('на главную')
    ]

], resize_keyboard=True
)

button = ReplyKeyboardMarkup([
    [
        KeyboardButton('на главную')
    ]
], resize_keyboard=True
)
