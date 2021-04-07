import discord
from discord.ext import commands
import logging
import os
from server import start_thread
import re
from replit import db


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


@bot.event
async def on_raw_reaction_add(payload: discord.RawReactionActionEvent):
    if str(payload.message_id) not in db.keys():
        return
    if payload.emoji.name not in db[str(payload.message_id)]:
        return
    role = int(re.sub("[^0-9]", "", db[str(payload.message_id)][payload.emoji.name]))
    guild = bot.get_guild(payload.guild_id)
    await payload.member.add_roles(guild.get_role(role))


@bot.event
async def on_raw_reaction_remove(payload: discord.RawReactionActionEvent):
    if str(payload.message_id) not in db.keys():
        return
    if payload.emoji.name not in db[str(payload.message_id)]:
        return
    role = int(re.sub("[^0-9]", "", db[str(payload.message_id)][payload.emoji.name]))
    guild = bot.get_guild(payload.guild_id)
    member = await guild.fetch_member(payload.user_id)
    await member.remove_roles(guild.get_role(role))


@bot.command()
async def links(ctx):
    """Quick links for Yoon#8579"""
    if ctx.author.id == 586321204047249423:
        embed = discord.Embed(color=0x037f03)
        embed.set_author(name="The Goon", url="https://github.com/yoonthegoon/The-Goon",
                         icon_url="https://cdn.discordapp.com/avatars/783779669979693117/84be9f2ab1b9bbb56a6c6c113cae7340.png")
        embed.description = ('https://replit.com/@YunisYilmaz/The-Goon\n'
                             'https://uptimerobot.com/dashboard?ref=website-header#mainDashboard\n'
                             'https://discordpy.readthedocs.io/en/latest/ext/commands/api.html')
        await ctx.reply(embed=embed, mention_author=False)


for file in os.listdir('cogs'):
    if file.endswith('.py'):
        bot.load_extension(f'cogs.{file[:-3]}')


intents = discord.Intents.default()
intents.presences = True
intents.members = True

start_thread()  # keeps main.py running on repl.it

bot.run(os.getenv('DISCORD_TOKEN'))
