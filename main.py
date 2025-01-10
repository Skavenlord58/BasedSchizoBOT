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
RECENZE = schdic.RECENZE
REPLIES = ("Ano.", "Ne.", "Perhaps.")
SADPENIS_ID = 786624092706046042
IGNORE_CH = [786624092706046042, 1042052161338626128, 1276805111506796605, 324465236209958922, 276789712318889984,
             1150244662133653534, 1034927837263704074, 1034513061182197810]

# add intents for bot and command prefix for classic command support
intents = disnake.Intents.all()
client = disnake.ext.commands.Bot(command_prefix=PREFIX, intents=intents)


# on_ready event - happens when bot connects to Discord API
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.command()
async def say(ctx, *args):
    message = ctx.message
    if str(message.author) == 'skavenlord58':
        await message.delete()
        await ctx.send(f'{" ".join(args)}')
    else:
        print(f'{message.author} tried to use "say" command.')


@client.event
async def on_message(m: Message):
    if not m.content:
        return

    if m.content[0] == PREFIX:
        # nutnost aby jely commandy    
        await client.process_commands(m)
        return

    if str(m.author) == "BasedSchizo#7762":
        return

    if m.channel.id in IGNORE_CH:
        return

    await maybe_answer(m)


async def maybe_answer(m: Message):
    content = m.content.lower()
    if content.startswith("hodný bot"):
        await m.add_reaction("🙂")
    if "windows" in content:
        if random.randint(0, 4) == 2:
            await m.add_reaction("😔")
    if "debian" in content:
        if random.randint(0, 4) == 2:
            await m.add_reaction("💜")
    if "všechno nejlepší" in content:
        await m.add_reaction("🥳")
        await m.add_reaction("🎉")
    if "kdo je negr?" in content:
        await m.channel.send("Decim je negr.")
    if "kdo je based schizo?" in content:
        await m.channel.send("To jsem já!")
    if "linux" in content and not "gnu/linux" in content:
        if random.randint(0, 64) == 4:
            if bool(random.getrandbits(1)):
                await m.reply(LINUX_COPYPASTA)
            else:
                await m.reply(CESKA_LINUX_COPYPASTA)
    if "hilfe" in content or "pomoc" in content and "pomocí" not in content:
        if random.randint(0, 3) == 1:
            await m.reply(f'''
            „{MOT_HLASKY[random.randint(0, len(MOT_HLASKY) - 1)]}“
                                                                                - Mistr Oogway, {random.randint(470, 480)} př. n. l.
            ''')
    if "novinky.cz" in content:
        if random.randint(0, 32) == 4:
            await m.reply("Přestaň postovat cringe, bro.")
    if "drž hubu" in content and m.mentions:
        print(m.mentions)
        await m.reply("Ne, ty. 😃")
    if "free primos" in content or "príma džemy" in content:
        await m.reply(
            "Neklikejte na odkazy s názvem FREE PRIMOS. Obvykle toto bývá phishing scam. https://www.avast.com/cs-cz/c-phishing")
    if "jsem" in content:
        if random.randint(0, 36) == 4:
            kdo = " ".join(m.content.split("jsem")[1].split(".")[0].split(",")[0].split(" ")[1:])
            await m.reply(f'Ahoj, {kdo}. Já jsem táta.')
    if content == "kdo":
        await m.channel.send(f'kdo se ptal?')
    if "zhongli" in content:
        await m.reply(f'haha žongli :clown:')
    if "aneurysm" in content:
        await m.reply(f'https://www.youtube.com/watch?v=kyg1uxOsAUY')
    if "schizo" in content:
        if random.randint(0, 4) == 2:
            await m.reply(f'doslova já')
    if "?" in content:
        if random.randint(0, 32) == 4:
            await m.reply(f'{random.choice(REPLIES)}')
    if "proč " in content or "proc " in content:
        if random.randint(0, 8) == 4:
            await m.reply(f'skill issue')
    if "kiryu" in content or "kyriu" in content:
        if random.randint(0, 4) == 4:
            await m.reply(f'Kiryu-chaaaaan!')
    if "jsi" in content:
        if random.randint(0, 16) == 4:
            kdo = " ".join(m.content.split("jsi")[1].split(" ")[1:])
            await m.reply(f'Tvoje máma je {kdo}.')
    if "negr" in content:
        if random.randint(0, 6969):
            await m.reply(f'taky nesnáším negry :+1:')
    if "žid" in content:
        if random.randint(0, 8000):
            await m.reply(f'taky nesnáším židy :+1:')
    if "buzna" in content:
        if random.randint(0, 3000):
            await m.reply(f'taky nesnáším buzny :+1:')
    if "israel" in content or "izrael" in content:
        if random.randint(0, 8000):
            await m.reply(f'další důkaz, že rakouský malíř umřel moc brzo :pensive:')
    if random.randint(0, 6969) == 1:
        await m.reply(f'mňau')
    if random.randint(0, 500000) == 1:
        await m.reply(f'pipík')
    if random.randint(0, 6969) == 1:
        if m.channel.id != SADPENIS_ID:
            await m.reply(f'víš co? raději drž hubu, protože z tohohle jsem chytil rakovinu varlat')
        else:
            await m.reply(
                f'dissnul bych tě, ale budu hodnej, takže uhhh to bude dobrý, wishing the best for you :slight_smile: :+1:')
    if any(word in content for word in ["mama", "máma", "mami", "mommy", "mamka", "mamko"]):
        if random.randint(0, 64) == 1:
            try:
                apiCall = requests.get("https://www.yomama-jokes.com/api/v1/jokes/random/")
                if apiCall.status_code == 200:
                    await m.reply(f'{apiCall.json()["joke"]}')
            except Exception as exc:
                print(f"Caught exception:\n {exc}")
    if "lagtrain" in content:
        await m.reply(f"https://www.youtube.com/watch?v=UnIhRpIT7nc")
    if "cum zone" in content:
        await m.reply(f"https://www.youtube.com/watch?v=j0lN0w5HVT8")
    if "crab rave" in content:
        await m.reply(f"https://youtu.be/LDU_Txk06tM?t=75")
    if "já jo" in content:
        if random.randint(0, 16) == 1:
            await m.reply(f"já ne")
    if "já ne" in content:
        if random.randint(0, 16) == 1:
            await m.reply(f"já jo")
    if "chci se zabít" in content or "suicidal" in content:
        await m.reply(f"omg don't kill yourself, ur too sexy, haha <:catcry:1158475025473622167>")
    if "v píči" in content:
        await m.reply(f"stejně tak moc v píči jako já včera večer v tvojí mámě loool <:kekWR:1063089161587933204>")
    if any(misspelling in content for misspelling in ["buisness", "bussines", "bussiness", "buissnes", "buisnes"]):
        await m.reply(
            f"KÁMO lmao ukažte si na toho blbečka, co neumí napsat 'business' XDDDD :index_pointing_at_the_viewer: příště raději napiš 'byznys' dík :)")
    if "reminder" in content:
        if random.randint(0, 4) == 1:
            await m.reply(f"kind reminder: ur a bitch :)")
    if "youtu.be" in content or "youtube.com" in content:
        if random.randint(0, 5) == 1:
            await m.reply(RECENZE[random.randint(0, len(RECENZE) - 1)])
    if content.__len__() >= 625:
        await m.reply(f"i ain't reading all of that. im happy for you tho, or sorry that happened. depends on you")
    if "špatný bot" in content or "spatny bot" in content:
        await m.reply(f"i'm trying my best :pensive:")
    if "podle mě" in content or "myslím si" in content:
        if bool(random.getrandbits(1)):
            await m.reply(f"Souhlasím.")
        else:
            await m.reply(f"Rozhodně nesouhlasím.")


client.run(TOKEN)
