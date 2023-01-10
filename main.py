import json
import os
import aiohttp
import random
import asyncio
import datetime as dt
import disnake
from disnake import Message
from disnake.ext import commands
import requests

import decimdictionary as decdi 
import schizodict as schdic

from dotenv import load_dotenv


# preload all useful stuff
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
TEXT_SYNTH_TOKEN = os.getenv('TEXT_SYNTH_TOKEN')
PREFIX = os.getenv('BOT_PREFIX')

MOT_HLASKY = decdi.MOT_HLASKY
LINUX_COPYPASTA = decdi.LINUX_COPYPASTA
REPLIES = ("Ano.", "Ne.", "Perhaps.")

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
        if "linux" in m.content.lower() and not "gnu/linux" in m.content.lower():
            if random.randint(0, 64) == 4:
                await m.reply(LINUX_COPYPASTA)
        if "hilfe" in m.content.lower() or "pomoc" in m.content.lower() and "pomocí" not in m.content.lower():
            await m.reply(f'''
            „{MOT_HLASKY[random.randint(0, len(MOT_HLASKY) - 1)]}“
                                                                                - Mistr Oogway, {random.randint(470,480)} př. n. l.
            ''')
        if "novinky.cz" in m.content.lower():
            await m.reply("Přestaň postovat cringe, bro.")
        if "drž hubu" in m.content.lower():
            print(m.mentions)
            await m.reply("Ne, ty. 😃")
        if "free primos" in m.content.lower() or "príma džemy" in m.content.lower():
            await m.reply(
                "Neklikejte na odkazy s názvem FREE PRIMOS. Obvykle toto bývá phishing scam. https://www.avast.com/cs-cz/c-phishing")
        if "jsem" in m.content.lower():
            if random.randint(0, 32) == 4:
                kdo = " ".join(m.content.split("jsem")[1].split(" ")[1:])
                await m.reply(f'Ahoj, {kdo}. Já jsem táta.')
        if m.content.lower() == "kdo":
            await m.channel.send(f'kdo se ptal?')
        if "zhongli" in m.content.lower():
            await m.reply(f'haha žongli :clown:')
        if "aneurysm" in m.content.lower():
            await m.reply(f'https://www.youtube.com/watch?v=kyg1uxOsAUY')
        if "schizo" in m.content.lower():
            await m.reply(f'doslova já')
        if "?" in m.content.lower():
            if random.randint(0, 32) == 4:
                await m.reply(f'{random.choice(REPLIES)}')
        if "jsi" in m.content.lower():
            if random.randint(0, 32) == 4:
                kdo = " ".join(m.content.split("jsi")[1].split(" ")[1:])
                await m.reply(f'Tvoje máma je {kdo}.')
        if random.randint(0, 169696969) == 1:
            await m.reply(f'mňau')
        if random.randint(0, 500000) == 1:
            await m.reply(f'pipík')
        if ["mama", "mamko", "mami"] in m.content.lower():
            try:
                apiCall = requests.get("https://api.yomomma.info/")
                if apiCall.status_code == 200:
                    await m.reply(f'{apiCall.json()["joke"]}')
            except Exception as exc:
                print(f"Caught exception:\n {exc}")
            
            
client.run(TOKEN)