import discord
from discord.ext import commands
import random


class Roll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def roll(self, ctx, dice: str):
        """Rolls a dice in NdN format."""
        try:
            rolls, limit = map(int, dice.split('d'))
        except Exception:
            await ctx.reply('`Format has to be in NdN!`')
            return

        roll_results = [random.randint(1, limit) for _ in range(rolls)]
        result = str(sum(roll_results))
        result += f' = ({" + ".join(map(str, roll_results))})' if rolls > 1 else ''

        embed = discord.Embed(title=f'Roll: {dice}', description=result, color=0x03037f)
        embed.set_author(name="The Goon", icon_url="https://cdn.discordapp.com/avatars/783779669979693117/84be9f2ab1b9bbb56a6c6c113cae7340.png")

        await ctx.reply(embed=embed)


def setup(bot):
    bot.add_cog(Roll(bot))
