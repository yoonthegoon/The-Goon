import discord
from discord.ext import commands


class Python(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def eval(self, ctx, *expression: str):
        """Evaluate an expression."""
        try:
            result = eval(' '.join(expression), {})
        except Exception as e:
            await ctx.reply(f'`{e}`', mention_author=False)
            return

        code = f'```py\n{" ".join(expression)}\n``````\n{result}\n```'

        await ctx.reply(code, mention_author=False)

    @commands.command()
    async def exec(self, ctx, *expression: str):
        """Executes python code, but only for Yoon#8579."""
        if ctx.author.id != 586321204047249423:
            embed = discord.Embed(title=f'Exec: {" ".join(expression)}', description='You do not have permission to use this command.', color=0x037f03)
            embed.set_author(name="The Goon", url="https://github.com/yoonthegoon/The-Goon", icon_url="https://cdn.discordapp.com/avatars/783779669979693117/84be9f2ab1b9bbb56a6c6c113cae7340.png")

            await ctx.reply(embed=embed, mention_author=False)
            return

        try:
            links = 'links = ["https://replit.com/@YunisYilmaz/The-Goon", "https://uptimerobot.com/", "https://discordpy.readthedocs.io/en/latest/api.html"]; '
            loc = {}
            exec(links + 'out = "Define <out> to return a value"; ' + ' '.join(expression), globals(), loc)
            result = loc['out']
            code = f'```py\n{" ".join(expression)}\n``````\n{result}\n```'
        except Exception as e:
            await ctx.reply(f'`{e}`', mention_author=False)
            return

        await ctx.reply(code, mention_author=False)


def setup(bot):
    bot.add_cog(Python(bot))
