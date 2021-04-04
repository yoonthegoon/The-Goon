import discord
from discord.ext import commands
import logging
import os


logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


bot = commands.Bot(command_prefix='?')


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(name='?help', type=discord.ActivityType.listening))

    print(f'We have logged in as {bot.user}')

    print('Guilds')
    for guild in bot.guilds:
        print(f'\t{guild}')


@bot.command('tar')
async def tar(ctx):
    if ctx.author.id in (586321204047249423, 586321204047249423):  # Tara
        await ctx.message.add_reaction('💩')


for file in os.listdir('cogs'):
    if file.endswith('.py'):
        bot.load_extension(f'cogs.{file[:-3]}')


bot.run(os.getenv('DISCORD_TOKEN'))
