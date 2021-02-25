from os import getenv
import dotenv

dotenv.load_dotenv('./.env')

qiwi_token = getenv('QIWI_TOKEN')
token = getenv('TOKEN')
admin = getenv('ADMIN')
qiwi_number = getenv('QIWI_NUMBER')