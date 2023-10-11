import discord
import sqlite3
from config import *
import time
import math
import asyncio


conn = sqlite3.connect('info.db')
cursor = conn.cursor()
client = discord.Client()





@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    global logchannel 
    logchannel = client.get_channel(channelid)
    global userobj 
    userobj = client.get_user(userid)

@client.event
async def on_presence_update(before, after):
    await asyncio.sleep(3)

    current_time = math.floor(time.time())

    
      
    if before.id == userid:
        if before.status != after.status:
            await logchannel.send(f'Status changed from {before.status} to {after.status}.\nTimestamp - <t:{current_time}:R>')


        elif before.activities != after.activities:
            act = before.activities
            aft = after.activities
            activiteslistbef = []
            activiteslistaft = []
            befact = ' '
            aftact = ' '
            for a in act:
                activiteslistbef.append(str(a.name))

            for a in aft:
                activiteslistaft.append(str(a.name))
                print(a.name)
            befact = ', '.join(activiteslistbef)
            aftact = ', '.join(activiteslistaft)

               
            await logchannel.send(f'Activities changed.\nBefore: {befact} / After: {aftact}\nTimestamp - <t:{current_time}:R>')



client.run(discordtoken)
    