import discord
from discord.ext import commands


embed = discord.Embed(color=0x037f03)
embed.set_author(name="The Goon", url="https://github.com/yoonthegoon/The-Goon",
                 icon_url="https://cdn.discordapp.com/avatars/783779669979693117/84be9f2ab1b9bbb56a6c6c113cae7340.png")


class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def define(self, ctx, word: str):
        """Define a given word"""

        embed.title = f'define: {word}'

        try:
            from dictionary import define

            r = define(word)

            embed.title = 'wordnik'
            embed.url = f'https://www.wordnik.com/words/{word}'
            embed.add_field(name="source", value=r['source'], inline=False)
            for li in r['ul']:
                embed.add_field(name=r['ul'][li][0]['abbr'], value=r['ul'][li][1], inline=False)

        except Exception as e:
            embed.colour = 0x7f0003
            embed.description = f'ERROR: {e}'

        await ctx.reply(embed=embed, mention_author=False)


def setup(bot):
    bot.add_cog(Utility(bot))
