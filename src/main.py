import discord
from discord.ext import commands
import os

#import all of the cogs
from help import help_cog
from music import music_cog

bot = commands.Bot(command_prefix='/',intents=discord.Intents.default())

#remove the default help command so that we can write out own
bot.remove_command('help')

#register the class with the bot
bot.add_cog(help_cog(bot))
bot.add_cog(music_cog(bot))

#start the bot with our token
bot.run(os.getenv("TOKEN"))