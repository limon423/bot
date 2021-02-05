from os import getenv
import dotenv

dotenv.load_dotenv('E:\\python projects\\bot_earn\\.env')

token = getenv('TOKEN')
admin = getenv('ADMIN')
payload_token = getenv('PAYLOAD_TOKEN')