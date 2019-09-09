import discord
from discord.ext import commands

from command import lol


bot = commands.Bot(command_prefix='!')
bot.add_command(lol)
bot.run('<token>')
