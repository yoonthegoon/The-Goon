import discord
import logging
import os
# import sqlite3  TODO: use database to store shit
from discord.ext import commands
from server import start_thread


logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

intents = discord.Intents.default()
intents.presences = True
intents.members = True

bot = commands.Bot(command_prefix='?', intents=intents)


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(name='?help', type=discord.ActivityType.listening))

    print(f'We have logged in as {bot.user}')

    print('Guilds')
    for guild in bot.guilds:
        print(f'\t{guild}')


@bot.event
async def on_raw_reaction_add(payload: discord.RawReactionActionEvent):
    if payload.message_id != 829495413186494495:
        return
    pid = payload.emoji.id
    guild = bot.get_guild(payload.guild_id)

    # Minecraft
    if pid == 826890083957342248:
        role = guild.get_role(815380690102779944)
    # League
    elif pid == 826890607665479751:
        role = guild.get_role(721762056939765810)
    # DnD
    elif pid == 826890581237956659:
        role = guild.get_role(735643555124478022)
    else:
        return
    await payload.member.add_roles(role)


@bot.event
async def on_raw_reaction_remove(payload: discord.RawReactionActionEvent):
    if payload.message_id != 829495413186494495:
        return
    pid = payload.emoji.id
    guild = bot.get_guild(payload.guild_id)
    member = await guild.fetch_member(payload.user_id)

    # Minecraft
    if pid == 826890083957342248:
        role = guild.get_role(815380690102779944)
    # League
    elif pid == 826890607665479751:
        role = guild.get_role(721762056939765810)
    # DnD
    elif pid == 826890581237956659:
        role = guild.get_role(735643555124478022)
    else:
        return
    await member.remove_roles(role)


@bot.command()
async def links(ctx):
    """Quick links for Yoon#8579"""

    embed = discord.Embed(color=0x037f03)
    embed.set_author(name="The Goon", url="https://github.com/yoonthegoon/The-Goon",
                     icon_url="https://cdn.discordapp.com/avatars/783779669979693117/84be9f2ab1b9bbb56a6c6c113cae7340.png")

    if ctx.author.id == 586321204047249423:
        embed.description = ('https://replit.com/@YunisYilmaz/The-Goon\n'
                             'https://uptimerobot.com/dashboard?ref=website-header#mainDashboard\n'
                             'https://discordpy.readthedocs.io/en/latest/ext/commands/api.html')
    else:
        embed.description = 'You do not have permission to use this command.' \
                            'You need to be Yoon#8579 to use this command.'

    await ctx.reply(embed=embed, mention_author=False)


for file in os.listdir('cogs'):
    if file.endswith('.py'):
        bot.load_extension(f'cogs.{file[:-3]}')


start_thread()  # keeps main.py running on repl.it

bot.run(os.getenv('DISCORD_TOKEN'))
