import discord
from discord.ext import commands


embed = discord.Embed(color=0x037f03)
embed.set_author(name="The Goon", url="https://github.com/yoonthegoon/The-Goon",
                 icon_url="https://cdn.discordapp.com/avatars/783779669979693117/84be9f2ab1b9bbb56a6c6c113cae7340.png")


class Python(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def eval(self, ctx, *expression: str):
        """Evaluate a python expression."""
        embed.title = f'eval: {" ".join(expression)}'

        try:
            result = eval(' '.join(expression), {})
            await ctx.reply(f'```py\n{" ".join(expression)}\n``````\n{result}\n```', mention_author=False)
            return

        except Exception as e:
            embed.description = f'ERROR: {e}'

        await ctx.reply(embed=embed, mention_author=False)

    @commands.command()
    async def exec(self, ctx, *expression: str):
        """Executes python code."""
        embed.title = f'exec: {" ".join(expression)}'

        if ctx.author.id != 586321204047249423:
            embed.description = 'You do not have permission to use this command.'
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
