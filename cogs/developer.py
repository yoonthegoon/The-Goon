import discord
from discord.ext import commands
import itertools
from replit import db


class Developer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def delete(self, ctx, n: int):
        """Deletes past <n> messages (including command)."""
        for role in ctx.author.roles:
            if role.permissions.manage_messages or role.permissions.administrator or ctx.author.guild_permissions.administrator or ctx.author.id == 586321204047249423:
                history = ctx.channel.history(limit=n)
                async for message in history:
                    await message.delete()
                return

        embed = discord.Embed(title=f'Delete: {n}', description='You do not have permission to use this command.', color=0x037f03)
        embed.set_author(name="The Goon", url="https://github.com/yoonthegoon/The-Goon", icon_url="https://cdn.discordapp.com/avatars/783779669979693117/84be9f2ab1b9bbb56a6c6c113cae7340.png")

        await ctx.reply(embed=embed, mention_author=False)

    @commands.command()
    async def write(self, ctx, message):
        """Deletes command and sends message. Requires permission to manage messages"""
        for role in ctx.author.roles:
            if role.permissions.manage_messages or role.permissions.administrator or ctx.author.guild_permissions.administrator or ctx.author.id == 586321204047249423:
                await ctx.message.delete()
                await ctx.send(message)
                return

        embed = discord.Embed(title=f'Write: {message}', description='You do not have permission to use this command.', color=0x037f03)
        embed.set_author(name="The Goon", url="https://github.com/yoonthegoon/The-Goon", icon_url="https://cdn.discordapp.com/avatars/783779669979693117/84be9f2ab1b9bbb56a6c6c113cae7340.png")

        await ctx.reply(embed=embed, mention_author=False)

    @commands.command()
    async def react(self, ctx, reaction, message_id: int):
        """Reacts an emoji to a given message id."""
        try:
            for role in ctx.author.roles:
                if (role.permissions.read_message_history and role.permissions.add_reactions) or role.permissions.administrator or ctx.author.guild_permissions.administrator or ctx.author.id == 586321204047249423:
                    message = await ctx.channel.fetch_message(message_id)
                    await message.add_reaction(reaction)
                    return
        except Exception as e:
            await ctx.reply(f'`{e}`', mention_author=False)
            return

        embed = discord.Embed(title=f'React: {reaction, message_id}', description='You do not have permission to use this command.', color=0x037f03)
        embed.set_author(name="The Goon", url="https://github.com/yoonthegoon/The-Goon", icon_url="https://cdn.discordapp.com/avatars/783779669979693117/84be9f2ab1b9bbb56a6c6c113cae7340.png")

        await ctx.reply(embed=embed, mention_author=False)

    @commands.command()
    async def reaction_role_add(self, ctx, message_id, *args):
        """Assigns roles to users who react accordingly to given message."""
        embed = discord.Embed(title=f'Reaction role: {message_id, args}', color=0x037f03)
        embed.set_author(name="The Goon", url="https://github.com/yoonthegoon/The-Goon", icon_url="https://cdn.discordapp.com/avatars/783779669979693117/84be9f2ab1b9bbb56a6c6c113cae7340.png")
        print(args)
        try:
            for role in ctx.author.roles:
                if role.permissions.manage_roles or role.permissions.administrator or ctx.author.guild_permissions.administrator or ctx.author.id == 586321204047249423:
                    if message_id in db.keys():
                        embed.description = 'Reaction role already added.'
                        await ctx.reply(embed=embed, mention_author=False)
                        return
                    else:
                        i = iter(args)
                        o = itertools.zip_longest(i, i, fillvalue=None)
                        kwargs = dict(o)
                        db[message_id] = {kw: kwargs[kw] for kw in args}
                        embed.description = 'Reaction role added.'
                        await ctx.reply(embed=embed, mention_author=False)
                        return

        except Exception as e:
            await ctx.reply(f'`{e}`', mention_author=False)
            return

        embed.description = 'You do not have permission to use this command.'

        await ctx.reply(embed=embed, mention_author=False)


def setup(bot):
    bot.add_cog(Developer(bot))
