import asyncio
import random
from pyrogram.raw.functions.messages import GetMessagesViews

async def react(app, message, emodji_list, emodji_wieghts, delay_beetwen_random, channel1_link):
    # Реагируем рандомным эмодзи, с определённой модой
    random_emodji = random.choices(
        emodji_list, weights=emodji_wieghts, k=1)
    # Задержка между сообщениями набирается рандомно
    await asyncio.sleep(random.randint(0, delay_beetwen_random))
    await message.react(emoji=random_emodji[0])
    print(f"REACT ON POST {message.id} with emodji {random_emodji[0]}")
    # Просматриваем пост, чтобы прибавить счётчик просмотров на канале 1
    channels_msgs = []
    try:
        channel = await app.get_chat(chat_id=channel1_link)
        async for msg in app.get_chat_history(chat_id=channel.id,
                                                limit=10):
            channels_msgs.append(msg.id)

        await app.invoke(GetMessagesViews(
            peer=await app.resolve_peer(channel.id),
            id=channels_msgs,
            increment=True
        )
        )

    except Exception as e:
        pass
    # Просматриваем пост, чтобы прибавить счётчик просмотров на канале 2
    channels_msgs1 = []
    try:
        channel1 = await app.get_chat(chat_id=channel2_link)
        async for msg in app.get_chat_history(chat_id=channel1.id,
                                                limit=10):
            channels_msgs.append(msg.id)

        await app.invoke(GetMessagesViews(
            peer=await app.resolve_peer(channel1.id),
            id=channels_msgs1,
            increment=True
        )
        )

    except Exception as e:
        pass
        