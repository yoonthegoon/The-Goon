import discord
from discord.ext import commands


class Python(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def eval(self, ctx, *expression: str):
        """Evaluate a python expression."""

        embed = discord.Embed(title=f'eval: {" ".join(expression)}', color=0x037f03)
        embed.set_author(name="The Goon", url="https://github.com/yoonthegoon/The-Goon",
                         icon_url="https://cdn.discordapp.com/avatars/783779669979693117/84be9f2ab1b9bbb56a6c6c113cae7340.png")

        try:
            result = eval(' '.join(expression), {})
            await ctx.reply(f'```py\n{" ".join(expression)}\n``````\n{result}\n```', mention_author=False)
            return

        except Exception as e:
            embed.description = f'ERROR: {e}'

        await ctx.reply(embed=embed, mention_author=False)

    @commands.command()
    async def exec(self, ctx, *expression: str):
        """Executes python code for Yoon#8579."""

        embed = discord.Embed(title=f'exec: {" ".join(expression)}', color=0x037f03)
        embed.set_author(name="The Goon", url="https://github.com/yoonthegoon/The-Goon",
                         icon_url="https://cdn.discordapp.com/avatars/783779669979693117/84be9f2ab1b9bbb56a6c6c113cae7340.png")

        if ctx.author.id != 586321204047249423:
            embed.description = 'You do not have permission to use this command.' \
                                'You need to be Yoon#8579 to use this command.'
            await ctx.reply(embed=embed, mention_author=False)
            return

        try:
            loc = {}
            exec('result = "Define {result} to return a value"; ' + ' '.join(expression), globals(), loc)
            result = loc['result']
            await ctx.reply(f'```py\n{" ".join(expression)}\n``````\n{result}\n```', mention_author=False)
            return

        except Exception as e:
            embed.description = f'ERROR: {e}'

        await ctx.reply(embed=embed, mention_author=False)


def setup(bot):
    bot.add_cog(Python(bot))
