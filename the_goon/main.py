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
    print(f'We have logged in as {bot.user}')

    print('Guilds')
    for guild in bot.guilds:
        print(f'\t{guild}')


for file in os.listdir('./commands'):
    if file.endswith('.py'):
        bot.load_extension(f'commands.{file[:-3]}')


bot.run(os.getenv('DISCORD_TOKEN'))
