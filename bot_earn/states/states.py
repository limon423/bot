from aiogram.dispatcher.filters.state import State, StatesGroup


class Events(StatesGroup):
    ask_num = State()

