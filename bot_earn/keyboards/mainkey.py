from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

menu = ReplyKeyboardMarkup([
    [
        KeyboardButton('схема'), KeyboardButton('отзывы')
    ],
    [
        KeyboardButton('помощь'), KeyboardButton('оставить отзыв')
    ]
], resize_keyboard=True
)
