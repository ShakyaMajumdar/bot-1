import discord
from discord.ext import commands
import os


game = discord.Game("CAT cat CAT")
bot = commands.Bot(command_prefix="!", help_command = None, activity=game)

token = #
bot.run(token)
