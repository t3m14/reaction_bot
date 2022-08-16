import random
import asyncio
import os
from config import *
from pyrogram import Client, idle, filters
from pyrogram.raw.functions.messages import GetMessagesViews
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime, timedelta
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
import logging

logging.basicConfig()
logging.getLogger('apscheduler').setLevel(logging.DEBUG)
# Служебные глобальные переменные
account_counter= 0
logins_list = []
apps = []
accounts_to_use = 0
hour_counter = 1
async def test(*args):
    text = args[0]
    emodji_list = args[1]
    emodji_wieghts = args[2]
    delay_beetwen_random = args[3]
    message = args[4]
    print(text)
    random_emodji = random.choices(
        emodji_list, weights=emodji_wieghts, k=1)
    # Задержка между сообщениями набирается рандомно
    await asyncio.sleep(random.randint(0, delay_beetwen_random))
    await message.react(emoji=random_emodji[0])
    print(f"REACT ON POST {message.id} with emodji {random_emodji[0]}")
# Чтение сессий из текущей папки
for root, dirs, files in os.walk("./sessions"):
    for file in files:
        if(file.endswith(".session")):
            logins_list.append(file.split(".")[0])
               
async def react(client, app, emodji_list, emodji_wieghts, delay_beetwen_random, message):
    # Реагируем рандомным эмодзи, с определённой модой
    random_emodji = random.choices(
        emodji_list, weights=emodji_wieghts, k=1)
    # Задержка между сообщениями набирается рандомно
    await asyncio.sleep(random.randint(0, delay_beetwen_random))
    await message.react(emoji=random_emodji[0])
    print(f"REACT ON POST {message.id} with emodji {random_emodji[0]}")
    # Просматриваем пост, чтобы прибавить счётчик просмотров на канале 1
    # channels_msgs = []
    # try:
    #     channel = await app.get_chat(chat_id=channel1_link)
    #     async for msg in app.get_chat_history(chat_id=channel.id,
    #                                             limit=10):
    #         channels_msgs.append(msg.id)

    #     await app.invoke(GetMessagesViews(
    #         peer=await app.resolve_peer(channel.id),
    #         id=channels_msgs,
    #         increment=True
    #     )
    #     )

    # except Exception as e:
    #     pass
    # # Просматриваем пост, чтобы прибавить счётчик просмотров на канале 2
    # channels_msgs1 = []
    # try:
    #     channel1 = await app.get_chat(chat_id=channel2_link)
    #     async for msg in app.get_chat_history(chat_id=channel1.id,
    #                                             limit=10):
    #         channels_msgs.append(msg.id)

    #     await app.invoke(GetMessagesViews(
    #         peer=await app.resolve_peer(channel1.id),
    #         id=channels_msgs1,
    #         increment=True
    #     )
    #     )

    # except Exception as e:
    #     pass
async def reaction(client, app, message, emodji_list, emodji_list_advert, delay_beetwen_random, emodji_wieghts,emodji_wieghts_advert, fst_to, sec_to, tth_to, fth_to, fst, sec, tth, fth, advert_rand_from, advert_rand_to):
            # Функция для генерации количества реакций по часам от 1 до 4
       
            def generate_accouts_to_react(account):
                first = random.randint(fst, fst_to)
                second = first + random.randint(sec, sec_to)
                third = second + random.randint(tth, tth_to)
                fourth = third + random.randint(fth, fth_to)
                return [first, second, third, fourth]
            
                
            global account_counter
            global accounts_to_use
            account_counter += 1
            all_accs = len(logins_list)
            # Проверка на наличие ссылок в тексте

            if message.entities or message.caption_entities:
                print("ADVERT POST " + str(message.id))
                print( advert_rand_from)
                print(advert_rand_to)
                if account_counter <= random.randint(advert_rand_from, advert_rand_to):
                   await react(emodji_list, emodji_wieghts, delay_beetwen_random, message)
            else:
                print("ACC COUNTER = " + str(account_counter))
                if account_counter <= all_accs:
                    loop = asyncio.get_event_loop()
                    if account_counter < generate_accouts_to_react(all_accs)[0]:
                        print("FIRST QUATTER")

                        await react(emodji_list, emodji_wieghts, delay_beetwen_random, message)
                    elif account_counter < generate_accouts_to_react(all_accs)[1]:
                        print("SECOND QUATTER + RUN DATE " + str(datetime.now() + timedelta(seconds=delay_beetwen_random)))

                        scheduler.add_job(react, "date", run_date=datetime.now() + timedelta(seconds=delay_beetwen_random), args=(client, app, emodji_list, emodji_wieghts, delay_beetwen_random, message))
                        # scheduler.add_job(test, "date", run_date=datetime.now() + timedelta(seconds=delay_beetwen_random), args=["44444444444444444444444444444444444444444444444", emodji_wieghts, delay_beetwen_random, message])

                    elif account_counter < generate_accouts_to_react(all_accs)[2]:
                        print("THIRD QUATTER")
                        # scheduler.add_job(test, "date", run_date=datetime.now() + timedelta(seconds=delay_beetwen_random * 2), args=["44444444444444444444444444444444444444444444444", emodji_wieghts, delay_beetwen_random, message])

                        scheduler.add_job(react, "date", run_date=datetime.now() + timedelta(seconds=delay_beetwen_random * 2), args=(client, app, emodji_list, emodji_wieghts, delay_beetwen_random, message))
                    elif account_counter < generate_accouts_to_react(all_accs)[3]:
                        print("FOURTH QUATTER")
                        scheduler.add_job(react, "date", run_date=datetime.now() + timedelta(seconds=delay_beetwen_random * 3), args=(client, app, emodji_list, emodji_wieghts, delay_beetwen_random, message))
                        # scheduler.add_job(test, "date", run_date=datetime.now() + timedelta(seconds=delay_beetwen_random * 3), args=["44444444444444444444444444444444444444444444444", emodji_list, emodji_wieghts, delay_beetwen_random, message])

                print(f"POST GETTED (post id is {message.id})")
                if account_counter >= all_accs:
                    account_counter = 0
                   
# Основная функция
async def main():
    # Получаем глобальные переменные: с количеством всех аккаунтов и счётчик часов
    # Заполняем лист приложений
    for login in logins_list:
        apps.append(Client(login, api_id, api_hash, workdir="./sessions"))
    # Каждую включаем по очереди
    for app in apps:
        print("SESSION OK")
        await app.start()
        # Хендлер на пост на одном из каналов
        @app.on_message(filters.chat(channel1_link.split("/")[-1]))
        async def first_channel_handler(client, message):
            print("THE TASK IS CREATED FOR " + str(message.id))
            loop = asyncio.get_event_loop()
            await loop.create_task(reaction(client,
                app,
                message,
                emodji_list1,
                emodji_list_advert1,
                delay_beetwen_random1,
                emodji_wieghts1,
                emodji_wieghts_advert1,
                fst1_to,
                sec1_to,
                tth1_to,
                fth1_to,
                fst1,
                sec1,
                tth1,
                fth1,
                advert_rand_from1,
                advert_rand_to1
            ))
        @app.on_message(filters.chat(channel2_link.split("/")[-1]))
        async def second_channel_handler(client, message):
            print("THE TASK IS CREATED FOR " + str(message.id))
            loop = asyncio.get_event_loop()
            await loop.create_task(reaction(client,
                app,
                message,
                emodji_list2,
                emodji_list_advert2,
                delay_beetwen_random2,
                emodji_wieghts2,
                emodji_wieghts_advert2,
                fst2_to,
                sec2_to,
                tth2_to,
                fth2_to,
                fst2,
                sec2,
                tth2,
                fth2,
                advert_rand_from2,
                advert_rand_to2
            ))
        @app.on_message(filters.chat(channel3_link.split("/")[-1]))
        async def first_channel_handler(client, message):
            print("THE TASK IS CREATED FOR " + str(message.id))
            loop = asyncio.get_event_loop()
            await loop.create_task(reaction(client,
                app,
                message,
                emodji_list3,
                emodji_list_advert3,
                delay_beetwen_random3,
                emodji_wieghts3,
                emodji_wieghts_advert3,
                fst3_to,
                sec3_to,
                tth3_to,
                fth3_to,
                fst3,
                sec3,
                tth3,
                fth3,
                advert_rand_from3,
                advert_rand_to3
            ))
        

    # Ждём новых действий
    await idle()
    # Останавливаем все приложения
    for app in apps:
        await app.stop()


 
# Запускаем main функцию
if __name__ == "__main__":
    
    jobstores = {
        'default': SQLAlchemyJobStore(url='sqlite:///te333st.sqlite')
    }

    scheduler = AsyncIOScheduler(jobstores=jobstores)
    loop = asyncio.get_event_loop()
    scheduler.start()
    loop.run_until_complete(main())
