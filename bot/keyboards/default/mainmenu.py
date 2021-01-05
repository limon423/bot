from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

main_menu = ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(text='👩‍💻начать работу'),
         ],
        [
            KeyboardButton(text='💰баланс'),   KeyboardButton(text='📊статистика'),
        ],
        [
            KeyboardButton(text='💸вывод денег'),  KeyboardButton(text='💎купить vip-статус💎')
        ],
    ], resize_keyboard=True
)

go_to_menu = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='⬅главное меню')]], resize_keyboard=True)