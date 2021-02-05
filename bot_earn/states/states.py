from aiogram.dispatcher.filters.state import State, StatesGroup


class Events(StatesGroup):
    buy = State()
    reviem = State()

