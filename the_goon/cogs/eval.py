from discord.ext import commands


class Eval(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def eval(self, ctx, *expression: str):
        """Evaluate the given source."""
        try:
            result = eval(' '.join(expression), {})
        except Exception as e:
            await ctx.reply(f'`{e}`')
            return

        code = f'```py\n{" ".join(expression)}\n``````\n{result}\n```'

        await ctx.reply(code)


def setup(bot):
    bot.add_cog(Eval(bot))
