import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform

client = Bot(description="Randy", command_prefix="Randy!", pm_help = True)

@client.event
async def on_ready():
     
    print('http://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))
    print("Hi I'm Randy!")
   
@client.command()
async def greet(*args):
   
    await client.say("Beef and lamb?")
    await asyncio.sleep(1)


f = open("token.txt", "r")
client.run(f.read())
f.close()
