from aiogram import Dispatcher, Bot, types
from config import token, admin, qiwi_token, qiwi_number
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import sqlite3
import requests

bot = Bot(token, parse_mode='html')
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)

db = sqlite3.connect("database.db")
sql = db.cursor()

s = requests.Session()
s.headers['authorization'] = 'Bearer ' + qiwi_token
