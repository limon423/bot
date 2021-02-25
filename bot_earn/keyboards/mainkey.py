from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

menu = ReplyKeyboardMarkup([
    [
        KeyboardButton('купить схему'),
    ],
    [
        KeyboardButton('нужен бот?'), KeyboardButton('помощь')
    ]
], resize_keyboard=True
)
