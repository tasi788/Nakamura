import json
import random
import requests

from discord.ext import commands

bot = commands.Bot(command_prefix='!')

def get_version():
    url = 'https://ddragon.leagueoflegends.com/realms/na.js'
    r = requests.get(url)
    if r.status_code != 200:
        return
    try:
        result = json.loads(r.text.replace('Riot.DDragon.m = ', '').replace(';', ''))
        return result
    except:
        return

def get_champion():
    version = get_version()['v']
    url = f'https://ddragon.leagueoflegends.com/cdn/{version}/data/en_US/champion.json'
    r = requests.get(url)
    if r.status_code != 200:
        return
    try:
        return r.json()
    except:
        return

@commands.command()
async def lol(ctx):
    champion = get_champion()
    one = random.choice(list(champion['data'].keys()))
    await ctx.send(f'{ctx.author.mention} 抽到了 `{one}`')
    
