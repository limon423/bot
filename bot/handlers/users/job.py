from loader import dp, bot
from aiogram.dispatcher.filters import Text
from aiogram import types
from states.state_job import Job
from aiogram.dispatcher import FSMContext
from keyboards.default.mainmenu import go_to_menu, main_menu
import json
from .db_command import DBCommands
text = "🧑‍💻отправьте текст с капчи боту(каждая капча стоит 20 рублей💰)"

def counter(f=False):
    with open('./data/values.json', 'r') as j:
        file = json.load(j)
        num = file["count"]
        if num > 997:
            num = 1
        if f:
            num += 1
        data = {"count": num}
    with open('./data/values.json', 'w') as j:
        json.dump(data, j)
    return num


@dp.message_handler(Text(equals='👩‍💻начать работу'), state=None)
async def begin_work(message:types.Message):
    await Job.task.set()
    count = counter()
    img = open('./data/asdads/qwerty' + str(count)+'.jpg', 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=img, caption=text, reply_markup=go_to_menu)
    img.close()


@dp.message_handler(state=Job.task)
async def job(message:types.Message, state:FSMContext):
    answer = message.text
    count = counter()

    if answer == '⬅главное меню':
        await message.answer(text='вы вернулись в меню', reply_markup=main_menu)
        await state.finish()

    elif len(answer) == 6:
        count = counter(True)
        await DBCommands.add_money(20)

    else:
        await message.answer(text='попробуйте еще раз!')

    if answer != '⬅главное меню':
        img = open('./data/asdads/qwerty' + str(count)+'.jpg', 'rb')
        await bot.send_photo(chat_id=message.chat.id, photo=img, caption=text)
        img.close()
