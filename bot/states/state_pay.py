from aiogram.dispatcher.filters.state import State, StatesGroup

class Paying(StatesGroup):
    choose_system = State()
    get_wallet = State()
    choose_quant = State()