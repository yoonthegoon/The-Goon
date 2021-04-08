import discord
from discord.ext import commands


embed = discord.Embed(color=0x037f03)
embed.set_author(name="The Goon", url="https://github.com/yoonthegoon/The-Goon",
                 icon_url="https://cdn.discordapp.com/avatars/783779669979693117/84be9f2ab1b9bbb56a6c6c113cae7340.png")


class Configuration(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # @commands.command()
    # async def prefix(self, ctx, pre: str):
    #     """Change command prefix."""
    #
    #     embed.title = f'prefix: {pre}'
    #
    #     try:
    #         self.bot.command_prefix = pre
    #         embed.description = 'Success?'
    #
    #     except Exception as e:
    #         embed.description = f'ERROR: {e}'
    #
    #     await ctx.reply(embed=embed, mention_author=False)

    # @commands.group()
    # async def reaction_role(self, ctx):
    #     embed.title = 'reaction role'
    #
    #     try:
    #         embed.description =


def setup(bot):
    bot.add_cog(Configuration(bot))
