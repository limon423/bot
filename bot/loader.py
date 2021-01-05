from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from sql import create_pool, create_db
from data.config import BOT_TOKEN

loop = asyncio.get_event_loop()
bot = Bot(token=BOT_TOKEN, parse_mode='HTML')
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage, loop=loop)
db = loop.run_until_complete(create_pool())
