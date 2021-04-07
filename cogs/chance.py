import discord
from discord.ext import commands
from random import *


embed = discord.Embed(color=0x037f03)
embed.set_author(name="The Goon", url="https://github.com/yoonthegoon/The-Goon",
                 icon_url="https://cdn.discordapp.com/avatars/783779669979693117/84be9f2ab1b9bbb56a6c6c113cae7340.png")


class Chance(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def flip(self, ctx, limit: int = 1):
        """Flips a coin a given number of times."""
        embed.title = f'flip: {limit}'

        try:
            flip_results = [choice(('Heads', 'Tails')) for _ in range(limit)]
            if len(flip_results) == 1:
                embed.description = flip_results[0]
            else:
                description = ', '.join(flip_results)
                embed.description = description
                embed.description += f'\n(Heads: {description.count("Heads")}, Tails: {description.count("Tails")})'

        except Exception as e:
            embed.description = f'ERROR: {e}'

        await ctx.reply(embed=embed, mention_author=False)

    @commands.command()
    async def choose(self, ctx, *expressions: str):
        """Choose one out of given options."""
        embed.title = f'choose: {" ".join(expressions)}'

        try:
            embed.description = choice(expressions)

        except Exception as e:
            embed.description = f'ERROR: {e}'

        await ctx.reply(embed=embed, mention_author=False)

    @commands.command()
    async def roll(self, ctx, dice: str = '1d6'):
        """Rolls dice in NdN format"""
        embed.title = f'roll: {dice}'

        try:
            rolls, limit = map(int, dice.split('d'))
            roll_results = [randint(1, limit) for _ in range(rolls)]
            embed.description = str(sum(roll_results))
            if len(roll_results) > 1:
                embed.description += f' = ({" + ".join(map(str, roll_results))})'

        except Exception as e:
            embed.description = f'ERROR: {e}'

        await ctx.reply(embed=embed, mention_author=False)


def setup(bot):
    bot.add_cog(Chance(bot))
