import asyncio
import os
from pyrogram import Client, idle, filters
from config import *
logins_list = []
apps = []
channel1 = channel1_link.split("/")[-1]
channel2 = channel2_link.split("/")[-1]
channel3 = channel3_link.split("/")[-1]

for root, dirs, files in os.walk("./sessions/"):
    for file in files:
        if(file.endswith(".session")):    
            logins_list.append(file.split(".")[0])

async def main():
    for login in logins_list:
        apps.append(Client(login, "14107984", "6507fadc1d76c1d8f3c0957690d9ec86", workdir="./sessions/"))
       
    for app in apps:
        await app.start()
        await app.join_chat(channel1)
        await app.join_chat(channel2)
        await app.join_chat(channel3)

        print("Joined in all 3 channels")
    for app in apps:
        await app.stop()

asyncio.run(main())

