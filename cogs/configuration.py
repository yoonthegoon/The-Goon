import discord
from discord.ext import commands
import sqlite3


def dev_role_check(ctx: discord.ext.commands.Context) -> bool:
    roles = ctx.author.roles
    for role in roles:
        if role.name in ('dev', 'developer', 'Dev', 'Developer'):
            return True
    return False


class Configuration(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def prefix(self, ctx, p: str):
        """Change my prefix for this server."""

        embed = discord.Embed(title=f'prefix: {p}', color=0x037f03)
        embed.set_author(name="The Goon", url="https://github.com/yoonthegoon/The-Goon",
                         icon_url="https://cdn.discordapp.com/avatars/783779669979693117/84be9f2ab1b9bbb56a6c6c113cae7340.png")

        # TODO: write prefix command to use db
        # if not (ctx.author.permissions_in(ctx.channel).administrator or dev_role_check(ctx)):
        #     embed.colour = 0x03037f
        #     embed.description = 'You do not have permission to use this command.'\
        #                         '\nYou need to have role "Dev" to use this command.'
        #     await ctx.reply(embed=embed, mention_author=False)
        #     return
        #
        # try:
        #     con = sqlite3.connect('the_goon.db')
        #     cur = con.cursor()
        #
        #     cur.execute(f'INSERT INTO prefixes VALUES ({ctx.guild.id}, "{p}")')
        #     for row in cur.execute('SELECT * FROM prefixes'):
        #         print(row)
        #
        #     con.commit()
        #     con.close()
        #
        #     embed.description = f'Successfully changed prefix to "{p}"'
        #
        # except Exception as e:
        #     embed.colour = 0x7f0003
        #     embed.description = f'ERROR: {e}'

        await ctx.reply(embed=embed, mention_author=False)


def setup(bot):
    bot.add_cog(Configuration(bot))
