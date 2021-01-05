import os

from dotenv import load_dotenv

path = './.env'
load_dotenv(dotenv_path=path)
BOT_TOKEN = os.getenv('TOKEN')
admin = os.getenv('ADMIN_ID')
host = os.getenv('PGHOST')
PG_USER = os.getenv('PG_USER')
PG_PASS = os.getenv('PG_PASS')
