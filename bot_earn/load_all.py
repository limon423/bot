import aiogram
from aiogram import Dispatcher, Bot, types
from config import token, admin, payload_token
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(token, parse_mode='html')
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)

