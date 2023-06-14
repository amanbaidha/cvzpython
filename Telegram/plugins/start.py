from .. import bot
from telethon import events
import asyncio


@bot.on(events.NewMessage(incoming= True,pattern="/start"))
async def start(event):
  await event.reply("Hello this is Jaat_love_bot")
 
@bot.on(events.NewMessage(incoming= True,pattern="/get"))
async def start(event):
  a = await event.reply("Hello this is get command")
  await asyncio.sleep(3)
  await a.edit("this is edited a msg")
  
@bot.on(events.NewMessage(incoming= True,pattern="/eval"))
async def start(event):
  await event.reply("Hello this is eval command")