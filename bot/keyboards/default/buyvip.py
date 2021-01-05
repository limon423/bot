from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

end_menu = ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(text='💎купить vip-статус💎')
        ],
        [
            KeyboardButton(text='⬅главное меню')
        ],
    ], resize_keyboard=True
)

cancel = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='❌отмена')]], resize_keyboard=True)
