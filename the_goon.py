import discord
from discord.ext.commands import Bot
import os
import random


bot = Bot(command_prefix='?')


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    print(f'{bot.guilds}')


@bot.command(name='roll', \
             help='?roll d n; Rolls n dice with d sides. Defaults to d=6, n=1.')
async def roll(ctx, d=6, n=1):
    if d > 0 and n > 0:
        result = [random.randint(1,d) for i in range(int(n))]
    else:
        result = 'Please use valid numbers :rolling_eyes:'
    await ctx.send(result)


bot.run(os.environ.get('DISCORD_TOKEN'))
