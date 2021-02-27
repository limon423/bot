from load_all import dp, bot, qiwi_token, qiwi_number, types, sql, db, s
from aiogram.dispatcher.filters import Text
from keyboards import menu, sellmenu
from states import Events
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from keyboards import checker
import re
import time
import json
import asyncio
import logging
parameters = {'rows': '10'}
price = 20


def create_check():
    return str(int(time.time()*1000) % (10000*1000))


def get_scheme():
    file = open('scheme.txt', encoding='utf-8')
    s = ''
    for i in file:
        s += i
    file.close()
    return s


def check_pay(message_id):
    h = s.get('https://edge.qiwi.com/payment-history/v1/persons/' + qiwi_number + '/payments', params=parameters)
    req = json.loads(h.text)
    result = sql.execute(f"SELECT * FROM users WHERE id = {message_id}").fetchone()

    logging.error(result)

    phone = result[1]
    random_code = result[3]
    sum = result[2]

    logging.error([req['data'][0]['account'], req['data'][0]['sum']['amount'], req['data'][0]['comment']])

    for i in range(len(req['data'])):
        if req['data'][i]['account'] == '+'+phone:
            logging.error(1)
            if req['data'][i]['sum']['amount'] >= sum:
                logging.error(2)
                if req['data'][i]['comment'] == random_code:
                    logging.error(3)
                    sql.execute(f"DELETE FROM users WHERE id = {message_id}")
                    db.commit()
                    return True
    return False


@dp.message_handler(Text(equals='купить схему'))
async def buying(message: types.Message):
    text = 'нажмите на оплату'
    await Events.ask_num.set()
    await message.answer("напишите номер киви по такому формату: +71113334455", reply_markup=sellmenu)


@dp.callback_query_handler(text_contains='qiwi')
async def check(call: CallbackQuery):
    await asyncio.sleep(0.5)
    check_num = sql.execute(f"SELECT checknum FROM users WHERE id = {call.from_user.id}").fetchone()[0]
    pay = check_pay(call.from_user.id)

    text = f"""при оплате укажите в комментарии: {check_num}
оплата не засчитана, попробуйте еще раз через 10 секунд"""
    rep = checker
    if pay:
        text = get_scheme()
        rep = None
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text, reply_markup=rep)
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text+'!', reply_markup=rep)


@dp.message_handler(state=Events.ask_num)
async def buying(message: types.Message, state: FSMContext):
    pattern = r'(\+7|7).*?(\d{10})'
    if re.search(pattern, message.text) != None:
        logging.error('work with base..')
        num = message.text
        if num[0] == '+':
            num = num[1:]
        check_num = create_check()
        sql.execute(f"SELECT id FROM users WHERE id = '{message.from_user.id}'")
        if sql.fetchone() == None:
            logging.error("write")
            sql.execute(f"INSERT INTO users VALUES (?,?,?,?)", (message.from_user.id, num, price, check_num))
            db.commit()
        else:
            logging.error("user on base")
            sql.execute(f"UPDATE users SET number = {num} WHERE id = '{message.from_user.id}'")
            sql.execute(f"UPDATE users SET checknum = {check_num} WHERE id = '{message.from_user.id}'")
            db.commit()


        text = f"""осталось только оплатить!
нажмите на кнопку ниже для оплаты
ВАЖНО!
в примечании к платежу укажите {check_num}
(иначе оплата не засчитается!)
после оплаты вам будет выслана 
ваша стратегия заработка
"""
        await state.finish()
        await message.answer(text, reply_markup=checker)
    else:
        text = 'неправильный формат номера, попробуйте еще!\nвводите номер по такому формату: +71113334455'
        await message.answer(text)
