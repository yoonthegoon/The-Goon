import discord
from discord.ext import commands
import random


class Choose(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description='For when you wanna settle the score some other way')
    async def choose(self, ctx, *choices: str):
        """Chooses between multiple options."""
        result = random.choice(choices)

        embed = discord.Embed(title=f'Choose between: {", ".join(choices)}', description=result, color=0x037f03)
        embed.set_author(name="The Goon", url="https://github.com/yoonthegoon/The-Goon", icon_url="https://cdn.discordapp.com/avatars/783779669979693117/84be9f2ab1b9bbb56a6c6c113cae7340.png")

        await ctx.reply(embed=embed, mention_author=False)


def setup(bot):
    bot.add_cog(Choose(bot))
