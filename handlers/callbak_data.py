import asyncio
import json

from aiogram import types
from misc import dp, bot
from .sqlit import change_status,get_username,update_status, change_all
from .sqlit import reg_user, get_username
import random

text_stop = "👆🏻 Сначала посмотри кругляш, потом на кнопку нажимай :)"


time_flag = 1 # 0 - режим разработчика, где отключены тайм.слипы

from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

content = -1002246038271
logi_voronka = -1002205252407
reg_user(1,'1')  # Запуск в БД


class reg_p(StatesGroup):
    step1 = State()
    step2 = State()
    step3 = State()


async def progrev(user_id):
   pass


@dp.message_handler(content_types=['photo'])
async def photo_message(message: types.Message, state: FSMContext):
    print(message.photo[0].file_id)


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message, state: FSMContext):
    if len(message.text) == 6:
        reg_user(message.chat.id, '1')  # Регистрация в БД
    else:
        reg_user(message.chat.id, message.text[7:])  # Регистрация в БД

    update_status(message.chat.id, 1)

    markup = types.InlineKeyboardMarkup()
    bat_a = types.InlineKeyboardButton(text="🔗 ЧАСТЬ 2/36", callback_data='go_2')
    markup.add(bat_a)

    await bot.send_message(chat_id=message.chat.id, text= "⚙️ Запускаю практикум...")
    await asyncio.sleep(1)
    q = await bot.copy_message(from_chat_id=content, chat_id=message.chat.id, message_id=227)
    await asyncio.sleep(3)
    await bot.delete_message(chat_id=message.chat.id, message_id= q.message_id)
    await asyncio.sleep(2)
    await bot.copy_message(from_chat_id=content, chat_id=message.chat.id, message_id=4)
    await asyncio.sleep(6)
    await bot.copy_message(from_chat_id=content, chat_id=message.chat.id, message_id = 212,reply_markup=markup)




    await state.update_data(v0='start')


    if time_flag == 1:
        await asyncio.sleep(180)
    if ((await state.get_data())['v0']) != 'ready': # Человек бездействует 24 часа
        await bot.copy_message(from_chat_id=content, chat_id=message.chat.id, message_id = 303)
    else:
        return

    if time_flag == 1:
        await asyncio.sleep(180)
    if ((await state.get_data())['v0']) != 'ready': # Человек бездействует 24 часа
        await bot.send_message(chat_id= message.chat.id, text = f"""{message.from_user.first_name}, закрою тебе доступ после 30 минут бездействия. жми на кнопку и начинай проходить обучение""")
    else:
        return

    if time_flag == 1:
        await asyncio.sleep(86400)
    if ((await state.get_data())['v0']) != 'ready': # Человек бездействует 24 часа
        await bot.copy_message(from_chat_id=content, chat_id=message.chat.id, message_id = 232)
    else:
        return


    if time_flag == 1:
        await asyncio.sleep(86400)
    if ((await state.get_data())['v0']) != 'ready': # Человек бездействует 24 часа
        await bot.copy_message(from_chat_id=content, chat_id=message.chat.id, message_id = 233)
    else:
        return


    if time_flag == 1:
        await asyncio.sleep(86400)
    if ((await state.get_data())['v0']) != 'ready': # Человек бездействует 24 часа
        await bot.copy_message(from_chat_id=content, chat_id=message.chat.id, message_id = 235)
    else:
        return


    if time_flag == 1:
        await asyncio.sleep(86400)
    if ((await state.get_data())['v0']) != 'ready': # Человек бездействует 24 часа
        await bot.copy_message(from_chat_id=content, chat_id=message.chat.id, message_id = 236)
    else:
        return





# 7 ЧАСТЬ (ЧЕЛОВЕК СОЗДАЛ КАНАЛ)
@dp.message_handler(content_types=['text'], state=reg_p.step1)
async def all_message(message: types.Message, state: FSMContext):
    if 't.me' in message.text or '@' in message.text:
        await state.finish()
        update_status(message.chat.id, 7)
        await state.update_data(v5='ready')
        await state.update_data(v6='stop')

        print('Домашка выполнена!')

        markup = types.InlineKeyboardMarkup()
        bat_a = types.InlineKeyboardButton(text='🔗 ЧАСТЬ 8/36', callback_data='go_8')
        markup.add(bat_a)

        await bot.copy_message(from_chat_id=content, chat_id=message.chat.id, message_id=216)
        await asyncio.sleep(2)
        await bot.send_message(chat_id=message.chat.id, text= '<b>🔥 Молодец! Теперь у тебя есть собственный канал</b>')
        await asyncio.sleep(2)
        await bot.copy_message(from_chat_id=content, chat_id=message.chat.id, message_id=310)
        await asyncio.sleep(1)
        await bot.copy_message(from_chat_id=content, chat_id = message.chat.id, message_id=74, reply_markup=markup)

        if time_flag == 1:
            await asyncio.sleep(86400)
        if ((await state.get_data())['v6']) != 'ready':  # Человек бездействует 24 часа
            await bot.copy_message(from_chat_id=content, chat_id=message.chat.id, message_id=232)
        else:
            return

        if time_flag == 1:
            await asyncio.sleep(86400)
        if ((await state.get_data())['v6']) != 'ready':  # Человек бездействует 24 часа
            await bot.copy_message(from_chat_id=content, chat_id=message.chat.id, message_id=233)
        else:
            return

        if time_flag == 1:
            await asyncio.sleep(86400)
        if ((await state.get_data())['v6']) != 'ready':  # Человек бездействует 24 часа
            await bot.copy_message(from_chat_id=content, chat_id=message.chat.id, message_id=235)
        else:
            return

        if time_flag == 1:
            await asyncio.sleep(86400)
        if ((await state.get_data())['v6']) != 'ready':  # Человек бездействует 24 часа
            await bot.copy_message(from_chat_id=content, chat_id=message.chat.id, message_id=236)
        else:
            return


@dp.message_handler(content_types=['text'])
async def all_messageff(message: types.Message, state: FSMContext):
    if message.text == '1012':
        # 10 ЧАСТЬ (ЧЕЛОВЕК ОФОРМИЛ КАНАЛ)
        update_status(message.chat.id, 10)
        await state.update_data(v8='ready')
        await state.update_data(v9='stop')
        print('Домашка выполнена!')

        markup = types.InlineKeyboardMarkup()
        bat_a = types.InlineKeyboardButton(text='🔗 ЧАСТЬ 11/36', callback_data='go_11')
        markup.add(bat_a)

        await asyncio.sleep(1)
        await message.answer("<b>Домашка выполнена ✅ Доступ открыт!</b>")
        await asyncio.sleep(1)
        await bot.copy_message(from_chat_id=content, chat_id=message.chat.id, message_id=219)
        await asyncio.sleep(3)
        await bot.copy_message(from_chat_id=content, chat_id = message.chat.id, message_id=97, reply_markup=markup)


        if time_flag == 1:
            await asyncio.sleep(10) #Защита от скипа
        await state.update_data(v9='start')

        if time_flag == 1:
            await asyncio.sleep(86400)
        if ((await state.get_data())['v9']) != 'ready':  # Человек бездействует 24 часа
            await bot.copy_message(from_chat_id=content, chat_id=message.chat.id, message_id=232)
        else:
            return

        if time_flag == 1:
            await asyncio.sleep(86400)
        if ((await state.get_data())['v9']) != 'ready':  # Человек бездействует 24 часа
            await bot.copy_message(from_chat_id=content, chat_id=message.chat.id, message_id=233)
        else:
            return

        if time_flag == 1:
            await asyncio.sleep(86400)
        if ((await state.get_data())['v9']) != 'ready':  # Человек бездействует 24 часа
            await bot.copy_message(from_chat_id=content, chat_id=message.chat.id, message_id=235)
        else:
            return

        if time_flag == 1:
            await asyncio.sleep(86400)
        if ((await state.get_data())['v9']) != 'ready':  # Человек бездействует 24 часа
            await bot.copy_message(from_chat_id=content, chat_id=message.chat.id, message_id=236)
        else:
            return


    if message.text == '2278':
        # 22 ЧАСТЬ (ЧЕЛОВЕК ОТПРАВИЛ РОЛИК)
        update_status(message.chat.id, 22)
        await state.update_data(v20='ready')
        await state.update_data(v21='stop')

        print('Домашка выполнена!')

        markup = types.InlineKeyboardMarkup()
        bat_a = types.InlineKeyboardButton(text='🔗 ЧАСТЬ 23/36', callback_data='go_23')
        markup.add(bat_a)

        await asyncio.sleep(1)
        await message.answer("<b>Домашка выполнена ✅ Доступ открыт!</b>")
        await asyncio.sleep(1)
        await bot.copy_message(from_chat_id=content, chat_id=message.chat.id, message_id=226)
        await asyncio.sleep(3)
        await bot.copy_message(from_chat_id=content, chat_id = message.chat.id, message_id=147, reply_markup=markup)


        if time_flag == 1:
            await asyncio.sleep(10) #Защита от скипа
        await state.update_data(v21='start')


        if time_flag == 1:
            await asyncio.sleep(86400)
        if ((await state.get_data())['v21']) != 'ready':  # Человек бездействует 24 часа
            await bot.copy_message(from_chat_id=content, chat_id=message.chat.id, message_id=232)
        else:
            return

        if time_flag == 1:
            await asyncio.sleep(86400)
        if ((await state.get_data())['v21']) != 'ready':  # Человек бездействует 24 часа
            await bot.copy_message(from_chat_id=content, chat_id=message.chat.id, message_id=233)
        else:
            return

        if time_flag == 1:
            await asyncio.sleep(86400)
        if ((await state.get_data())['v21']) != 'ready':  # Человек бездействует 24 часа
            await bot.copy_message(from_chat_id=content, chat_id=message.chat.id, message_id=235)
        else:
            return

        if time_flag == 1:
            await asyncio.sleep(86400)
        if ((await state.get_data())['v21']) != 'ready':  # Человек бездействует 24 часа
            await bot.copy_message(from_chat_id=content, chat_id=message.chat.id, message_id=236)
        else:
            return


#ready_name

@dp.callback_query_handler(lambda call: True, state = '*')
async def answer_push_inline_button(call, state: FSMContext):
    try:
        await bot.answer_callback_query(call.id)
    except:
        pass

    if call.data == 'answer_bussines':
        await call.message.answer("<b>Нет. С бизнес-тематикой мы работать не будем. Посмотри кругляш еще раз и нажми на другую кнопку</b>")

    if call.data == 'answer_news':
        await call.message.answer("<b>Нет. С новостной тематикой мы работать не будем. Посмотри кругляш еще раз и нажми на другую кнопку</b>")

    if call.data == 'get_movie':
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=118)

    if call.data == 'get_channel_link':
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=283)

    if call.data == 'inshot':
        markup = types.InlineKeyboardMarkup()
        bat_1 = types.InlineKeyboardButton(text='ОТПРАВИТЬ Д/З [22/36]', url='t.me/SteveSup')
        markup.add(bat_1)

        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=299)
        await asyncio.sleep(1)
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=300)
        await asyncio.sleep(10)
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=301)
        await asyncio.sleep(5)
        await bot.send_message(chat_id=call.message.chat.id,text="""<b>Отправь ролик на проверку, чтобы получить доступ к следующему уроку</b>""",reply_markup=markup)

    if call.data == 'ready_ava':
        photos = [
            types.InputMediaPhoto(media='AgACAgQAAxkBAAIB_WZlqXisgAxqfycgLJ9xKNjGSneWAALSvzEb_ZcwU3Pe3F8EwYAXAQADAgADcwADNQQ'),
            types.InputMediaPhoto(media='AgACAgIAAxkBAAIB52ZlqFXSK6CksZs1OHhjNEi-K2_qAALn2jEbQzoxS2NwchifquejAQADAgADcwADNQQ'),
            types.InputMediaPhoto(media='AgACAgQAAxkBAAIB_mZlqXtVZi7x2mNOnH6ymHyLlqZkAALTvzEb_ZcwU0sWzfgWssNHAQADAgADcwADNQQ'),

            types.InputMediaPhoto(media='AgACAgIAAxkBAAIB6WZlqF-_BIMmNFhIg0VFNOeZ93t5AALp2jEbQzoxS8qlxeJF2v72AQADAgADcwADNQQ'),
            types.InputMediaPhoto(media='AgACAgIAAxkBAAIB6mZlqGHBJI75GdX8Tzno8Iuh_0oGAALq2jEbQzoxSxGgR2pHcdYdAQADAgADcwADNQQ'),
            types.InputMediaPhoto(media='AgACAgIAAxkBAAIB6GZlqFwFYMPn4Cq3MRKxPm2QypDSAALo2jEbQzoxS2AyZergzMBrAQADAgADcwADNQQ'),

            types.InputMediaPhoto(media='AgACAgIAAxkBAAIB5mZlqFGeEQqCL07Byk_8VICa7r7wAALi2jEbQzoxS5MiR-6K7YTBAQADAgADcwADNQQ'),
            types.InputMediaPhoto(media='AgACAgIAAxkBAAIB7WZlqGk66HGw2Lqz8_0n1xXTTMCzAALt2jEbQzoxS8pRW61yhJPSAQADAgADcwADNQQ'),
        ]

        await bot.send_media_group(chat_id=call.message.chat.id ,media=photos)
        await asyncio.sleep(1)
        await call.message.answer("✅☝🏻 Можно использовать эти аватарки ")

    if call.data == 'ready_name':
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=284)


    if call.data == 'go_2':
        update_status(call.message.chat.id, 2)
        await state.update_data(v0='ready')
        await state.update_data(v1='stop')
        markup = types.InlineKeyboardMarkup()
        bat_a = types.InlineKeyboardButton(text='🔗 ЧАСТЬ 3/36', callback_data='go_3')
        markup.add(bat_a)

        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=51, reply_markup=markup)
        if time_flag == 1:
            await asyncio.sleep(10) #Защита от скипа
        await state.update_data(v1='start')


        if time_flag == 1:
            await asyncio.sleep(150)
        if ((await state.get_data())['v1']) != 'ready':  # Человек бездействует 3 мин
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=305)
        else:
            return

        if time_flag == 1:
            await asyncio.sleep(86400)
        if ((await state.get_data())['v1']) != 'ready':  # Человек бездействует 24 часа
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=232)
        else:
            return

        if time_flag == 1:
            await asyncio.sleep(86400)
        if ((await state.get_data())['v1']) != 'ready':  # Человек бездействует 24 часа
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=233)
        else:
            return

        if time_flag == 1:
            await asyncio.sleep(86400)
        if ((await state.get_data())['v1']) != 'ready':  # Человек бездействует 24 часа
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=235)
        else:
            return

        if time_flag == 1:
            await asyncio.sleep(86400)
        if ((await state.get_data())['v1']) != 'ready':  # Человек бездействует 24 часа
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=236)
        else:
            return




    if call.data == 'go_3':
        try:
            if ((await state.get_data())['v1']) == 'start':
                flag = True
            else:
                flag = False

        except:
            flag = True

        if flag == False:
            await call.message.answer(text_stop)

        else:
            update_status(call.message.chat.id, 3)
            await state.update_data(v1='ready')
            await state.update_data(v2='stop')

            markup = types.InlineKeyboardMarkup()
            bat_1 = types.InlineKeyboardButton(text='🔗 ЧАСТЬ 4/36', callback_data='go_4')
            markup.add(bat_1)



            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=306)
            await asyncio.sleep(2)
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=307)
            await asyncio.sleep(1.5)
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=308)
            await asyncio.sleep(1)
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=54,reply_markup=markup)
            if time_flag == 1:

                await asyncio.sleep(10) #Защита от скипа
            await state.update_data(v2='start')

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v2']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=232)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v2']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=233)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v2']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=235)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v2']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=236)
            else:
                return

    if call.data == 'go_4':
        try:
            if ((await state.get_data())['v2']) == 'start':
                flag = True
            else:
                flag = False

        except:
            flag = True

        if flag == False:
            await call.message.answer(text_stop)

        else:
            update_status(call.message.chat.id, 4)
            await state.update_data(v2='ready')
            await state.update_data(v3='stop')

            markup = types.InlineKeyboardMarkup()
            bat_1 = types.InlineKeyboardButton(text='👨‍💼 Бизнес', callback_data='answer_bussines')
            bat_2 = types.InlineKeyboardButton(text='📰 Новости', callback_data='answer_news')
            bat_3 = types.InlineKeyboardButton(text='🍿 Фильмы', callback_data='go_5')
            markup.add(bat_1)
            markup.add(bat_2)
            markup.add(bat_3)

            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=309)
            await asyncio.sleep(1)
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=56)
            await asyncio.sleep(5)
            await bot.send_message(chat_id=call.message.chat.id, text="""<b>В какой тематике мы будем работать?</b>""",reply_markup=markup)

            if time_flag == 1:
                await asyncio.sleep(10)  # Защита от скипа
            await state.update_data(v3='start')


            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v3']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=232)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v3']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=233)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v3']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=235)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v3']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=236)
            else:
                return


    if call.data == 'go_5':
        try:
            if ((await state.get_data())['v3']) == 'start':
                flag = True
            else:
                flag = False

        except:
            flag = True

        if flag == False:
            await call.message.answer(text_stop)

        else:
            update_status(call.message.chat.id, 5)
            await state.update_data(v3='ready')
            await state.update_data(v4='stop')

            markup = types.InlineKeyboardMarkup()
            bat_1 = types.InlineKeyboardButton(text='🔗 ЧАСТЬ 6/36', callback_data='go_6')
            markup.add(bat_1)
            await bot.send_message(chat_id=call.message.chat.id, text = "<b>✅Верно! Мы будем работать с фильмами</b>")
            await asyncio.sleep(1)
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=65,
                                   reply_markup=markup)
            if time_flag == 1:
                await asyncio.sleep(10)  # Защита от скипа
            await state.update_data(v4='start')


            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v4']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=232)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v4']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=233)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v4']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=235)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v4']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=236)
            else:
                return



    if call.data == 'go_6':
        try:
            if ((await state.get_data())['v4']) == 'start':
                flag = True
            else:
                flag = False

        except:
            flag = True

        if flag == False:
            await call.message.answer(text_stop)

        else:
            update_status(call.message.chat.id, 6)
            await state.set_state(reg_p.step1)
            await reg_p.step1.set()
            await state.update_data(v4='ready')
            await state.update_data(v5='stop')

            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=67)
            await asyncio.sleep(3)
            await bot.send_message(chat_id=call.message.chat.id, text="<b>Отправь сюда ссылку на твой канал, чтобы получить доступ к следующему уроку </b>")


            if time_flag == 1:
                await asyncio.sleep(300)  # Человек бездействует

            if ((await state.get_data())['v5']) != 'ready':
                markup = types.InlineKeyboardMarkup()
                bat_1 = types.InlineKeyboardButton(text='⁉️Где взять ссылку', callback_data='get_channel_link')
                bat_2 = types.InlineKeyboardButton(text='📁Готовые названия', callback_data='ready_name')
                bat_3 = types.InlineKeyboardButton(text='📁Готовые аватарки', callback_data='ready_ava')
                markup.add(bat_1)
                markup.add(bat_2)
                markup.add(bat_3)

                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=69, reply_markup = markup)


            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v5']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=232)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v5']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=233)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v5']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=235)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v5']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=236)
            else:
                return




    if call.data == 'go_7':
        # вынесли в домашку
        pass




    if call.data == 'go_8':
            update_status(call.message.chat.id, 8)
            await state.update_data(v6='ready')
            await state.update_data(v7='stop')

            markup = types.InlineKeyboardMarkup()
            bat_1 = types.InlineKeyboardButton(text='🔗 ЧАСТЬ 9/36', callback_data='go_9')
            markup.add(bat_1)

            await bot.send_message(chat_id=call.message.chat.id, text = "<b>Супер! Теперь мы добавим подписи</b>")
            await asyncio.sleep(3)
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=87,reply_markup=markup)
            if time_flag == 1:
                await asyncio.sleep(10)  # Защита от скипа
            await state.update_data(v7='start')


            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v7']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=232)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v7']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=233)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v7']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=235)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v7']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=236)
            else:
                return


    if call.data == 'go_9':
        try:
            if ((await state.get_data())['v7']) == 'start':
                flag = True
            else:
                flag = False

        except:
            flag = True

        if flag == False:
            await call.message.answer(text_stop)

        else:
            update_status(call.message.chat.id, 9)
            await state.update_data(v7='ready')
            await state.update_data(v8='stop')

            markup = types.InlineKeyboardMarkup()
            bat_1 = types.InlineKeyboardButton(text='📚 Отправить Д.З (10/36)', url='t.me/SteveSup')
            markup.add(bat_1)

            await bot.send_message(chat_id=call.message.chat.id, text="<b>Осталось добавить смайлики 😜 чтобы посты стали красивее </b>")
            await asyncio.sleep(3)

            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=89)
            await asyncio.sleep(5)

            await bot.send_message(chat_id= call.message.chat.id , text = "<b>Отправь <a href = 'http://t.me/SteveSup'>мне</a> ссылку на твой канал, я все проверю, и выдам доступ к следующему уроку</b>", reply_markup=markup, disable_web_page_preview=True)
            await asyncio.sleep(15)

            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=311)



            if time_flag == 1:
                await asyncio.sleep(10)  # Защита от скипа
            await state.update_data(v8='start')

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v8']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=232)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v8']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=233)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v8']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=235)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v8']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=236)
            else:
                return



    if call.data == 'go_10':
        # вынесли в домашку
        pass



    if call.data == 'go_11':
        try:
            if ((await state.get_data())['v9']) == 'start':
                flag = True
            else:
                flag = False

        except:
            flag = True

        if flag == False:
            await call.message.answer(text_stop)

        else:
            update_status(call.message.chat.id, 11)
            await state.update_data(v9='ready')
            await state.update_data(v10='stop')

            markup = types.InlineKeyboardMarkup()
            bat_1 = types.InlineKeyboardButton(text='🔗 ЧАСТЬ 12/36', callback_data='go_12')
            markup.add(bat_1)

            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=106,
                                   reply_markup=markup)
            if time_flag == 1:
                await asyncio.sleep(10)  # Защита от скипа
            await state.update_data(v10='start')

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v10']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=232)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v10']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=233)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v10']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=235)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v10']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=236)
            else:
                return






    if call.data == 'go_12':
        try:
            if ((await state.get_data())['v10']) == 'start':
                flag = True
            else:
                flag = False

        except:
            flag = True

        if flag == False:
            await call.message.answer(text_stop)

        else:
            update_status(call.message.chat.id, 12)
            await state.update_data(v10='ready')
            await state.update_data(v11='stop')

            markup = types.InlineKeyboardMarkup()
            bat_1 = types.InlineKeyboardButton(text='🔗 ЧАСТЬ 13/36', callback_data='go_13')
            markup.add(bat_1)

            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=221)
            await asyncio.sleep(3)
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=110,reply_markup=markup)


            if time_flag == 1:
                await asyncio.sleep(10)  # Защита от скипа
            await state.update_data(v11='start')

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v11']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=232)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v11']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=233)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v11']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=235)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v11']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=236)
            else:
                return



    if call.data == 'go_13':
        try:
            if ((await state.get_data())['v11']) == 'start':
                flag = True
            else:
                flag = False

        except:
            flag = True

        if flag == False:
            await call.message.answer(text_stop)

        else:
            update_status(call.message.chat.id, 13)
            await state.update_data(v11='ready')
            await state.update_data(v12='stop')

            markup = types.InlineKeyboardMarkup()
            bat_1 = types.InlineKeyboardButton(text='🔗 ЧАСТЬ 14/36', callback_data='go_14')
            markup.add(bat_1)

            await asyncio.sleep(1)
            await bot.send_message(call.message.chat.id, text = "<b>Более подробно про поисковой трафик я вам расскажу в конце курса</b>")
            await asyncio.sleep(2)
            await bot.send_message(call.message.chat.id,text="<b>А сейчас мы разберем 3-й способ набора подписчиков 👇🏻</b>")
            await asyncio.sleep(2)
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=112,
                                   reply_markup=markup)
            if time_flag == 1:
                await asyncio.sleep(10)  # Защита от скипа
            await state.update_data(v12='start')

            # поставить таймер на 30  минут!!
            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v12']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=232)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v12']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=233)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v12']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=235)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v12']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=236)
            else:
                return



    if call.data == 'go_14':
        try:
            if ((await state.get_data())['v12']) == 'start':
                flag = True
            else:
                flag = False

        except:
            flag = True

        if flag == False:
            await call.message.answer(text_stop)

        else:
            update_status(call.message.chat.id, 14)
            await state.update_data(v12='ready')
            await state.update_data(v13='stop')

            markup = types.InlineKeyboardMarkup()
            bat_1 = types.InlineKeyboardButton(text='🍿 СКАЧАТЬ ФИЛЬМ', callback_data='get_movie')
            bat_2 = types.InlineKeyboardButton(text='🔥 ПРОДОЛЖИТЬ 15/36', callback_data='go_15')
            markup.add(bat_1)
            markup.add(bat_2)

            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=114,
                                   reply_markup=markup)
            if time_flag == 1:
                await asyncio.sleep(10)  # Защита от скипа
            await state.update_data(v13='start')

            # поставить таймер на 30  минут!!
            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v13']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=232)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v13']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=233)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v13']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=235)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v13']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=236)
            else:
                return



    if call.data == 'go_15':
        try:
            if ((await state.get_data())['v13']) == 'start':
                flag = True
            else:
                flag = False

        except:
            flag = True

        if flag == False:
            await call.message.answer(text_stop)

        else:
            update_status(call.message.chat.id, 15)
            await state.update_data(v13='ready')
            await state.update_data(v14='stop')

            markup = types.InlineKeyboardMarkup()
            bat_1 = types.InlineKeyboardButton(text='🎞CupCup на Android', url = 'https://play.google.com/store/apps/details/CapCut?id=com.lemon.lvoverseas&hl=ru&pli=1')
            bat_2 = types.InlineKeyboardButton(text='🎞CupCup на Iphone', url = 'https://apps.apple.com/us/app/capcut-video-editor/id1500855883')
            markup.add(bat_1)
            markup.add(bat_2)

            markup2 = types.InlineKeyboardMarkup()
            bat_3 = types.InlineKeyboardButton(text='🔗 ЧАСТЬ 16/36', callback_data='go_16')
            markup2.add(bat_3)

            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=120,reply_markup=markup)
            await asyncio.sleep(7)
            await call.message.answer("<b>Скачай CupCut и жми на кнопку 👇🏻</b>",reply_markup= markup2)
            if time_flag == 1:
                await asyncio.sleep(10)  # Защита от скипа
            await state.update_data(v14='start')

            # поставить таймер на 30  минут!!
            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v14']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=232)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v14']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=233)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v14']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=235)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v14']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=236)
            else:
                return




    if call.data == 'go_16':
        try:
            if ((await state.get_data())['v14']) == 'start':
                flag = True
            else:
                flag = False

        except:
            flag = True

        if flag == False:
            await call.message.answer(text_stop)

        else:
            update_status(call.message.chat.id, 16)
            await state.update_data(v14='ready')
            await state.update_data(v15='stop')

            markup = types.InlineKeyboardMarkup()
            bat_1 = types.InlineKeyboardButton(text='🔗 ЧАСТЬ 17/36', callback_data='go_17')
            markup.add(bat_1)

            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=124,
                                   reply_markup=markup)
            if time_flag == 1:
                await asyncio.sleep(10)  # Защита от скипа
            await state.update_data(v15='start')

            # поставить таймер на 30  минут!!
            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v15']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=232)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v15']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=233)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v15']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=235)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v15']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=236)
            else:
                return





    if call.data == 'go_17':
        try:
            if ((await state.get_data())['v15']) == 'start':
                flag = True
            else:
                flag = False

        except:
            flag = True

        if flag == False:
            await call.message.answer(text_stop)

        else:
            update_status(call.message.chat.id, 17)
            await state.update_data(v15='ready')
            await state.update_data(v16='stop')

            markup = types.InlineKeyboardMarkup()
            bat_1 = types.InlineKeyboardButton(text='🔗 ЧАСТЬ 18/36', callback_data='go_18')
            markup.add(bat_1)

            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=132,
                                   reply_markup=markup)
            if time_flag == 1:
                await asyncio.sleep(10)  # Защита от скипа
            await state.update_data(v16='start')

            # поставить таймер на 30  минут!!
            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v16']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=232)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v16']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=233)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v16']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=235)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v16']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=236)
            else:
                return



    if call.data == 'go_18':
        try:
            if ((await state.get_data())['v16']) == 'start':
                flag = True
            else:
                flag = False

        except:
            flag = True

        if flag == False:
            await call.message.answer(text_stop)

        else:
            update_status(call.message.chat.id, 18)
            await state.update_data(v16='ready')
            await state.update_data(v17='stop')

            markup = types.InlineKeyboardMarkup()
            bat_1 = types.InlineKeyboardButton(text='🔗 ЧАСТЬ 19/36', callback_data='go_19')
            markup.add(bat_1)

            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=134,
                                   reply_markup=markup)
            if time_flag == 1:
                await asyncio.sleep(10)  # Защита от скипа
            await state.update_data(v17='start')

            # поставить таймер на 30  минут!!
            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v17']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=232)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v17']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=233)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v17']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=235)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v17']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=236)
            else:
                return




    if call.data == 'go_19':
        try:
            if ((await state.get_data())['v17']) == 'start':
                flag = True
            else:
                flag = False

        except:
            flag = True

        if flag == False:
            await call.message.answer(text_stop)

        else:
            update_status(call.message.chat.id, 19)
            await state.update_data(v17='ready')
            await state.update_data(v18='stop')

            markup = types.InlineKeyboardMarkup()
            bat_1 = types.InlineKeyboardButton(text='🔗 ЧАСТЬ 20/36', callback_data='go_20')
            markup.add(bat_1)


            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=136,reply_markup=markup)
            await asyncio.sleep(60)
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=312)
            if time_flag == 1:
                await asyncio.sleep(10)  # Защита от скипа
            await state.update_data(v18='start')

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v18']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=232)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v18']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=233)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v18']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=235)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v18']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=236)
            else:
                return



    if call.data == 'go_20':
        try:
            if ((await state.get_data())['v18']) == 'start':
                flag = True
            else:
                flag = False

        except:
            flag = True

        if flag == False:
            await call.message.answer(text_stop)

        else:
            update_status(call.message.chat.id, 20)
            await state.update_data(v18='ready')
            await state.update_data(v19='stop')

            markup = types.InlineKeyboardMarkup()
            bat_1 = types.InlineKeyboardButton(text='🔗 ЧАСТЬ 21/36', callback_data='go_21')
            markup.add(bat_1)

            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=140,reply_markup=markup)
            await asyncio.sleep(4)
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=314)
            if time_flag == 1:
                await asyncio.sleep(10)  # Защита от скипа
            await state.update_data(v19='start')

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v19']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=232)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v19']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=233)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v19']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=235)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v19']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=236)
            else:
                return



    if call.data == 'go_21':
        try:
            if ((await state.get_data())['v19']) == 'start':
                flag = True
            else:
                flag = False

        except:
            flag = True

        if flag == False:
            await call.message.answer(text_stop)

        else:
            update_status(call.message.chat.id, 21)
            await state.update_data(v19='ready')
            await state.update_data(v20='stop')

            markup = types.InlineKeyboardMarkup()
            bat_1 = types.InlineKeyboardButton(text='ОТПРАВИТЬ Д/З [22/36]', url='t.me/SteveSup')
            bat_2 = types.InlineKeyboardButton(text='СУБТИТРЫ 2 СПОСОБ', callback_data='inshot')
            markup.add(bat_1)
            markup.add(bat_2)

            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=142)
            await asyncio.sleep(3)
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=316, reply_markup=markup)
            await asyncio.sleep(10)
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=317)


            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v20']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=232)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v20']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=233)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v20']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=235)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v20']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=236)
            else:
                return



    if call.data == 'go_22':
        pass
        # Вынесли в домашку



    if call.data == 'go_23':
        try:
            if ((await state.get_data())['v21']) == 'start':
                flag = True
            else:
                flag = False

        except:
            flag = True

        if flag == False:
            await call.message.answer(text_stop)

        else:
            update_status(call.message.chat.id, 23)
            await state.update_data(v21='ready')
            await state.update_data(v22='stop')

            markup = types.InlineKeyboardMarkup()
            bat_1 = types.InlineKeyboardButton(text='🔗 ЧАСТЬ 24/36', callback_data='go_24')
            markup.add(bat_1)

            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=165,
                                   reply_markup=markup)
            if time_flag == 1:
                await asyncio.sleep(10)  # Защита от скипа
            await state.update_data(v22='start')

            # поставить таймер на 30  минут!!

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v22']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=232)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v22']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=233)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v22']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=235)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v22']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=236)
            else:
                return


    if call.data == 'go_24':
        try:
            if ((await state.get_data())['v22']) == 'start':
                flag = True
            else:
                flag = False

        except:
            flag = True

        if flag == False:
            await call.message.answer(text_stop)

        else:
            update_status(call.message.chat.id, 24)
            await state.update_data(v22='ready')
            await state.update_data(v23='stop')

            markup = types.InlineKeyboardMarkup()
            bat_1 = types.InlineKeyboardButton(text='🔗 ЧАСТЬ 25/36', callback_data='go_25')
            markup.add(bat_1)

            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=168,
                                   reply_markup=markup)
            if time_flag == 1:
                await asyncio.sleep(10)  # Защита от скипа
            await state.update_data(v23='start')


            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v23']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=232)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v23']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=233)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v23']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=235)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v23']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=236)
            else:
                return


    if call.data == 'go_25':
        try:
            if ((await state.get_data())['v23']) == 'start':
                flag = True
            else:
                flag = False

        except:
            flag = True

        if flag == False:
            await call.message.answer(text_stop)

        else:
            update_status(call.message.chat.id, 25)
            await state.update_data(v23='ready')
            await state.update_data(v24='stop')

            markup = types.InlineKeyboardMarkup()
            bat_1 = types.InlineKeyboardButton(text='🔗 ЧАСТЬ 26/36', callback_data='go_26')
            markup.add(bat_1)

            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=172,
                                   reply_markup=markup)
            if time_flag == 1:
                await asyncio.sleep(10)  # Защита от скипа
            await state.update_data(v24='start')

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v24']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=232)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v24']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=233)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v24']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=235)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v24']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=236)
            else:
                return


    if call.data == 'go_26':
        try:
            if ((await state.get_data())['v24']) == 'start':
                flag = True
            else:
                flag = False

        except:
            flag = True

        if flag == False:
            await call.message.answer(text_stop)

        else:
            update_status(call.message.chat.id, 26)
            await state.update_data(v24='ready')
            await state.update_data(v25='stop')

            markup = types.InlineKeyboardMarkup()
            bat_1 = types.InlineKeyboardButton(text='🔗 ЧАСТЬ 27/36', callback_data='go_27')
            markup.add(bat_1)

            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=175,reply_markup=markup)
            await asyncio.sleep(3)
            await bot.send_message(chat_id=call.message.chat.id, text=f"""<b>Твоя ссылка👇🏻</b> 
            
https://t.me/kinoo123bot?start={call.message.chat.id}""")

            if time_flag == 1:
                await asyncio.sleep(10)  # Защита от скипа
            await state.update_data(v25='start')

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v25']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=232)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v25']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=233)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v25']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=235)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v25']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=236)
            else:
                return

    if call.data == 'go_27':
        try:
            if ((await state.get_data())['v25']) == 'start':
                flag = True
            else:
                flag = False

        except:
            flag = True

        if flag == False:
            await call.message.answer(text_stop)

        else:
            update_status(call.message.chat.id, 27)
            await state.update_data(v25='ready')
            await state.update_data(v26='stop')

            markup = types.InlineKeyboardMarkup()
            bat_1 = types.InlineKeyboardButton(text='🔗 ЧАСТЬ 28/36', callback_data='go_28')
            markup.add(bat_1)

            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=177,reply_markup=markup)
            await asyncio.sleep(5)
            await bot.send_message(chat_id=call.message.chat.id, text="<b>👇🏻 Cкопируй команду и оправь ее боту: @kinoo123bot</b>")
            await asyncio.sleep(1)
            await bot.send_message(chat_id=call.message.chat.id, text="/stat")
            await asyncio.sleep(10)
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=318)


            if time_flag == 1:
                await asyncio.sleep(10)  # Защита от скипа
            await state.update_data(v26='start')

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v26']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=232)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v26']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=233)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v26']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=235)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v26']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=236)
            else:
                return





    if call.data == 'go_28':
        try:
            if ((await state.get_data())['v26']) == 'start':
                flag = True
            else:
                flag = False

        except:
            flag = True

        if flag == False:
            await call.message.answer(text_stop)

        else:
            update_status(call.message.chat.id, 28)
            await state.update_data(v26='ready')
            await state.update_data(v27='stop')

            markup = types.InlineKeyboardMarkup()
            bat_1 = types.InlineKeyboardButton(text='🙂 МОЙ ТГ КАНАЛ', url = "https://t.me/InstGramotnost")
            bat_2 = types.InlineKeyboardButton(text='ПРОВЕРИТЬ ПОДПИСКУ 29/36', callback_data='go_29')

            markup.add(bat_1)
            markup.add(bat_2)

            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=187,
                                   reply_markup=markup)
            if time_flag == 1:
                await asyncio.sleep(10)  # Защита от скипа
            await state.update_data(v27='start')

            # поставить таймер на 30  минут!!
            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v27']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=232)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v27']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=233)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v27']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=235)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v27']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=236)
            else:
                return



    if call.data == 'go_29':
        try:
            if ((await state.get_data())['v27']) == 'start':
                flag = True
            else:
                flag = False

        except:
            flag = True

        if flag == False:
            await call.message.answer(text_stop)

        else:
            try:
                proverka1 = (await bot.get_chat_member(chat_id = -1002175778067, user_id=call.message.chat.id)).status
            except:
                proverka1 = 'member'

            if proverka1 == 'member'  or proverka1 == 'administrator' or proverka1 == 'creator':
                update_status(call.message.chat.id, 29)
                await bot.send_message(call.message.chat.id, text = "<b>Спасибо за подписку ☺️ будем дружить )</b>")
                await asyncio.sleep(2)

                await state.update_data(v27='ready')
                await state.update_data(v28='stop')

                markup = types.InlineKeyboardMarkup()
                bat_1 = types.InlineKeyboardButton(text='🔗 ЧАСТЬ 30/36', callback_data='go_30')
                markup.add(bat_1)

                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=192,
                                       reply_markup=markup)
                if time_flag == 1:
                    await asyncio.sleep(10)  # Защита от скипа
                await state.update_data(v28='start')

                if time_flag == 1:
                    await asyncio.sleep(86400)
                if ((await state.get_data())['v28']) != 'ready':  # Человек бездействует 24 часа
                    await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=232)
                else:
                    return

                if time_flag == 1:
                    await asyncio.sleep(86400)
                if ((await state.get_data())['v28']) != 'ready':  # Человек бездействует 24 часа
                    await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=233)
                else:
                    return

                if time_flag == 1:
                    await asyncio.sleep(86400)
                if ((await state.get_data())['v28']) != 'ready':  # Человек бездействует 24 часа
                    await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=235)
                else:
                    return

                if time_flag == 1:
                    await asyncio.sleep(86400)
                if ((await state.get_data())['v28']) != 'ready':  # Человек бездействует 24 часа
                    await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=236)
                else:
                    return

            else:
                markup2 = types.InlineKeyboardMarkup()
                bat_2 = types.InlineKeyboardButton(text='ПРОВЕРИТЬ ПОДПИСКУ 29/36', callback_data='go_29')
                markup2.add(bat_2)

                await call.message.answer('<b>Чтобы продолжить обучение, подпишись на мой канал: @InstGramotnost</b>',disable_web_page_preview=True,reply_markup=markup2)





    if call.data == 'go_30':
        try:
            if ((await state.get_data())['v28']) == 'start':
                flag = True
            else:
                flag = False

        except:
            flag = True

        if flag == False:
            await call.message.answer(text_stop)

        else:
            update_status(call.message.chat.id, 30)
            await state.update_data(v28='ready')
            await state.update_data(v29='stop')

            markup = types.InlineKeyboardMarkup()
            bat_1 = types.InlineKeyboardButton(text='🔗 ЧАСТЬ 31/36', callback_data='go_31')
            markup.add(bat_1)

            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=194,
                                   reply_markup=markup)
            if time_flag == 1:
                await asyncio.sleep(10)  # Защита от скипа
            await state.update_data(v29='start')

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v29']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=232)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v29']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=233)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v29']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=235)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v29']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=236)
            else:
                return



    if call.data == 'go_31':
        try:
            if ((await state.get_data())['v29']) == 'start':
                flag = True
            else:
                flag = False

        except:
            flag = True

        if flag == False:
            await call.message.answer(text_stop)

        else:
            update_status(call.message.chat.id, 31)
            await state.update_data(v29='ready')
            await state.update_data(v30='stop')

            markup = types.InlineKeyboardMarkup()
            bat_1 = types.InlineKeyboardButton(text='🔗 ЧАСТЬ 32/36', callback_data='go_32')
            markup.add(bat_1)

            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=197,
                                   reply_markup=markup)
            if time_flag == 1:
                await asyncio.sleep(10)  # Защита от скипа
            await state.update_data(v30='start')

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v30']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=232)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v30']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=233)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v30']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=235)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v30']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=236)
            else:
                return




    if call.data == 'go_32':
        try:
            if ((await state.get_data())['v30']) == 'start':
                flag = True
            else:
                flag = False

        except:
            flag = True

        if flag == False:
            await call.message.answer(text_stop)

        else:
            update_status(call.message.chat.id, 32)
            await state.update_data(v30='ready')
            await state.update_data(v31='stop')

            markup = types.InlineKeyboardMarkup()
            bat_1 = types.InlineKeyboardButton(text='🔗 ЧАСТЬ 33/36', callback_data='go_33')
            markup.add(bat_1)

            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=199,
                                   reply_markup=markup)
            if time_flag == 1:
                await asyncio.sleep(10)  # Защита от скипа
            await state.update_data(v31='start')

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v31']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=232)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v31']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=233)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v31']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=235)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v31']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=236)
            else:
                return




    if call.data == 'go_33':
        try:
            if ((await state.get_data())['v31']) == 'start':
                flag = True
            else:
                flag = False

        except:
            flag = True

        if flag == False:
            await call.message.answer(text_stop)

        else:
            update_status(call.message.chat.id, 33)
            await state.update_data(v31='ready')
            await state.update_data(v32='stop')

            markup = types.InlineKeyboardMarkup()
            bat_1 = types.InlineKeyboardButton(text='🔗 ЧАСТЬ 34/36', callback_data='go_34')
            markup.add(bat_1)

            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=201,
                                   reply_markup=markup)
            if time_flag == 1:
                await asyncio.sleep(10)  # Защита от скипа
            await state.update_data(v32='start')


            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v32']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=232)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v32']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=233)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v32']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=235)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v32']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=236)
            else:
                return



    if call.data == 'go_34':
        try:
            if ((await state.get_data())['v32']) == 'start':
                flag = True
            else:
                flag = False

        except:
            flag = True

        if flag == False:
            await call.message.answer(text_stop)

        else:
            update_status(call.message.chat.id, 34)
            await state.update_data(v32='ready')
            await state.update_data(v33='stop')

            markup = types.InlineKeyboardMarkup()
            bat_1 = types.InlineKeyboardButton(text='🔗 ЧАСТЬ 35/36', callback_data='go_35')
            markup.add(bat_1)

            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=203,reply_markup=markup)
            await asyncio.sleep(4)
            await call.message.answer("<b>Но это еще не все!</b>")

            if time_flag == 1:
                await asyncio.sleep(10)  # Защита от скипа
            await state.update_data(v33='start')

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v33']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=232)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v33']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=233)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v33']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=235)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v33']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=236)
            else:
                return





    if call.data == 'go_35':
        try:
            if ((await state.get_data())['v33']) == 'start':
                flag = True
            else:
                flag = False

        except:
            flag = True

        if flag == False:
            await call.message.answer(text_stop)

        else:
            update_status(call.message.chat.id, 35)
            await state.update_data(v33='ready')
            await state.update_data(v34='stop')

            markup = types.InlineKeyboardMarkup()
            bat_1 = types.InlineKeyboardButton(text='🔗 ЧАСТЬ 36/36', callback_data='go_36')
            markup.add(bat_1)

            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=205,
                                   reply_markup=markup)
            if time_flag == 1:
                await asyncio.sleep(10)  # Защита от скипа
            await state.update_data(v34='start')

            # поставить таймер на 30  минут!!
            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v34']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=232)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v34']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=233)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v34']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=235)
            else:
                return

            if time_flag == 1:
                await asyncio.sleep(86400)
            if ((await state.get_data())['v34']) != 'ready':  # Человек бездействует 24 часа
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=236)
            else:
                return



    if call.data == 'go_36':
        try:
            if ((await state.get_data())['v34']) == 'start':
                flag = True
            else:
                flag = False

        except:
            flag = True

        if flag == False:
            await call.message.answer(text_stop)

        else:
            update_status(call.message.chat.id, 36)
            await state.update_data(v34='ready')

            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=208)
            await asyncio.sleep(3)
            await bot.send_message(chat_id=call.message.chat.id, text="""<b>Мой профиль 👉🏻</b>@SteveSup""")

            # Тут прогреваем и отправляем уведомление о том что человек завершил обучение
            try:
                await bot.send_message(chat_id=logi_voronka, text=f"""📌Прошел воронку
@{call.message.chat.username}
tg://user?id={call.message.chat.id}""")
            except:
                try:
                    await bot.send_message(chat_id=logi_voronka, text=f"""📌Прошел воронку
tg://user?id={call.message.chat.id}""")
                except:
                    pass


            try:
                if time_flag == 1:
                    await asyncio.sleep(1800) # 30 минут
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=265)


                if time_flag == 1:
                    await asyncio.sleep(900) # 15 минут
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=268)


                if time_flag == 1:
                    await asyncio.sleep(3600) # 1 час
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=270)


                if time_flag == 1:
                    await asyncio.sleep(43200) # 12 часов
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=272)


                if time_flag == 1:
                    await asyncio.sleep(86400) # 24 часа

                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=274)
                await asyncio.sleep(3)
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=275)

            except:
                pass
