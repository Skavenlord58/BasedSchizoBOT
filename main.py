import json
import os
import aiohttp
import random
import asyncio
import datetime as dt
import disnake
from disnake import Message
from disnake.ext import commands

from dotenv import load_dotenv
import schizodict as schdic

# preload all useful stuff
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
TEXT_SYNTH_TOKEN = os.getenv('TEXT_SYNTH_TOKEN')
PREFIX = os.getenv('BOT_PREFIX')

# add intents for bot and command prefix for classic command support
intents = disnake.Intents.all()
client = disnake.ext.commands.Bot(command_prefix=PREFIX, intents=intents)

# on_ready event - happens when bot connects to Discord API
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.command()
async def say(ctx, *args):
    if str(ctx.message.author) == 'SkavenLord58#0420':
        await ctx.message.delete()
        await ctx.send(f'{" ".join(args)}')
    else:
        print(f'{ctx.message.author} tried to use "say" command.')

@client.event
async def on_message(m: Message):
    if not m.content:
        pass
    elif m.content[0] == PREFIX:
        # nutnost aby jely commandy    
        await client.process_commands(m)
    elif str(m.author) != "Based Schizo#7762":
        if  m.content.lower().startswith("hodný bot"):
            await m.add_reaction("🙂")
        if "windows" in m.content.lower():
            await m.add_reaction("😔")
        if "debian" in m.content.lower():
            await m.add_reaction("💜")
        if "všechno nejlepší" in m.content.lower():
            await m.add_reaction("🥳")
            await m.add_reaction("🎉")
        if "kdo je negr?" in m.content.lower():
            await m.channel.send("Decim je negr.")
        if "kdo je based schizo?" in m.content.lower():
            await m.channel.send("To jsem já!")
client.run(TOKEN)