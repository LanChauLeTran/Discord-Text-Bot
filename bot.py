import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform

client = Bot(description="Randy", command_prefix="Randy!", pm_help = True)

@client.event
async def on_ready():
    print("Hi I'm Randy!")
   
@client.command()
async def greet(*args):
    await client.say("Beef and lamb?")
    await asyncio.sleep(1)

client.run('Mzk2OTM0ODE3NjY2NTY0MDk3.DSop4A.ZuTQyqH6DVaR6MEzKC5YbPTBX1M')

