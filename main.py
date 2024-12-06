import json
import os
import random
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
CESKA_LINUX_COPYPASTA = schdic.CESKA_LINUX_COPYPASTA
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
    if str(ctx.message.author) == 'skavenlord58':
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
    elif str(m.author) != "BasedSchizo#7762":
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
                if bool(random.getrandbits(1)):
                    await m.reply(LINUX_COPYPASTA)
                else:
                    await m.reply(CESKA_LINUX_COPYPASTA)
        if "hilfe" in m.content.lower() or "pomoc" in m.content.lower() and "pomocí" not in m.content.lower():
            if random.randint(0, 4) == 1:
                await m.reply(f'''
            „{MOT_HLASKY[random.randint(0, len(MOT_HLASKY) - 1)]}“
                                                                                - Mistr Oogway, {random.randint(470,480)} př. n. l.
            ''')
        if "novinky.cz" in m.content.lower():
            if random.randint(0, 32) == 4:
                await m.reply("Přestaň postovat cringe, bro.")
        if "drž hubu" in m.content.lower() and m.mentions:
            print(m.mentions)
            await m.reply("Ne, ty. 😃")
        if "free primos" in m.content.lower() or "príma džemy" in m.content.lower():
            await m.reply(
                "Neklikejte na odkazy s názvem FREE PRIMOS. Obvykle toto bývá phishing scam. https://www.avast.com/cs-cz/c-phishing")
        if "jsem" in m.content.lower():
            if random.randint(0, 36) == 4:
                kdo = " ".join(m.content.split("jsem")[1].split(".")[0].split(",")[0].split(" ")[1:])
                await m.reply(f'Ahoj, {kdo}. Já jsem táta.')
        if m.content.lower() == "kdo":
            await m.channel.send(f'kdo se ptal?')
        if "zhongli" in m.content.lower():
            await m.reply(f'haha žongli :clown:')
        if "aneurysm" in m.content.lower():
            await m.reply(f'https://www.youtube.com/watch?v=kyg1uxOsAUY')
        if "schizo" in m.content.lower():
            if random.randint(0, 4) == 2: 
                await m.reply(f'doslova já')
        if "?" in m.content.lower():
            if random.randint(0, 32) == 4:
                await m.reply(f'{random.choice(REPLIES)}')
        if "proč " in m.content.lower() or "proc " in m.content.lower():
            if random.randint(0, 8) == 4:
                await m.reply(f'skill issue')
        if "kiryu" in m.content.lower() or "kyriu" in m.content.lower():
            if random.randint(0, 4) == 4:
                await m.reply(f'Kiryu-chaaaaan!')
        if "jsi" in m.content.lower():
            if random.randint(0, 16) == 4:
                kdo = " ".join(m.content.split("jsi")[1].split(" ")[1:])
                await m.reply(f'Tvoje máma je {kdo}.')
        if random.randint(0, 69) == 1:
            await m.reply(f'mňau')
        if random.randint(0, 500000) == 1:
            await m.reply(f'pipík')
        if random.randint(0, 200) == 1:
            await m.reply(f'víš co? raději drž hubu, protože z tohohle jsem chytil rakovinu varlat')
        if "mama" in m.content.lower() or \
            "máma" in m.content.lower() or \
            "mami" in m.content.lower() or \
            "mommy" in m.content.lower() or \
            "mamka" in m.content.lower() or \
            "mamko" in m.content.lower():
            if random.randint(0, 64) == 1:
                try:
                    apiCall = requests.get("https://www.yomama-jokes.com/api/v1/jokes/random/")
                    if apiCall.status_code == 200:
                        await m.reply(f'{apiCall.json()["joke"]}')
                except Exception as exc:
                    print(f"Caught exception:\n {exc}")
        if "lagtrain" in m.content.lower():
            await m.reply(f"https://www.youtube.com/watch?v=UnIhRpIT7nc")
        if "cum zone" in m.content.lower():
            await m.reply(f"https://www.youtube.com/watch?v=j0lN0w5HVT8")
        if "crab rave" in m.content.lower():
            await m.reply(f"https://youtu.be/LDU_Txk06tM?t=75")
        if "já jo" in m.content.lower():
            if random.randint(0, 16) == 1:   
                await m.reply(f"já ne")
        if "já ne" in m.content.lower():
            if random.randint(0, 16) == 1:   
                await m.reply(f"já jo")
        if "chci se zabít" in m.content.lower() or "suicidal" in m.content.lower():
            await m.reply(f"omg don't kill yourself, ur too sexy, haha :catcry:")
        if "v píči" in m.content.lower():
            await m.reply(f"stejně tak moc v píči jako já včera večer v tvojí mámě loool :kekWR:")
        if "buisness" in m.content.lower() \
            or "bussines" in m.content.lower() \
            or "bussiness" in m.content.lower() \
            or "buissnes" in m.content.lower() \
            or "buisnes" in m.content.lower():
            await m.reply(f"KÁMO lmao ukažte si na toho blbečka, co neumí napsat 'business' XDDDD :index_pointing_at_the_viewer: příště raději napiš 'byznys' dík :)")
        if "reminder" in m.content.lower():
            if random.randint(0, 4) == 1:
                await m.reply(f"kind reminder: ur a bitch :)")
        if "youtu.be" in m.content.lower() or "youtube.com" in m.content.lower():
            if random.randint(0, 5) == 1:
                if bool(random.getrandbits(1)):
                    await m.reply(f"recenze: strašnej banger")
                else:
                    await m.reply(f"recenze: cringe ass hovno")
        if m.content.__len__() >= 600:
            await m.reply(f"i ain't reading all of that. im happy for you tho, or sorry that happened. depends on you")
client.run(TOKEN)