import discord
from discord.ext import commands
import re


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def delete(self, ctx, limit: int):
        """Deletes past number of messages in current channel."""

        embed = discord.Embed(title=f'delete: {limit}', color=0x037f03)
        embed.set_author(name="The Goon", url="https://github.com/yoonthegoon/The-Goon",
                         icon_url="https://cdn.discordapp.com/avatars/783779669979693117/84be9f2ab1b9bbb56a6c6c113cae7340.png")
    
        if not ctx.author.permissions_in(ctx.channel).manage_messages:
            embed.colour = 0x03037f
            embed.description = 'You do not have permission to use this command.' \
                                '\nYou need to be able to manage messages to use this command'
            await ctx.reply(embed=embed, mention_author=False)
            return
    
        try:
            history = ctx.channel.history(limit=limit)
            async for message in history:
                await message.delete()
            embed.description = f'{limit} messages deleted.'
            
        except Exception as e:
            embed.colour = 0x7f0003
            embed.description = f'ERROR: {e}'

        await ctx.reply(embed=embed, mention_author=False)
    
    @commands.command()
    async def kick(self, ctx, member: str, *reason: str):
        """Kicks mentioned member."""

        embed = discord.Embed(title=f'kick: {member}', color=0x037f03)
        embed.set_author(name="The Goon", url="https://github.com/yoonthegoon/The-Goon",
                         icon_url="https://cdn.discordapp.com/avatars/783779669979693117/84be9f2ab1b9bbb56a6c6c113cae7340.png")

        if not ctx.author.permissions_in(ctx.channel).kick_members:
            embed.colour = 0x03037f
            embed.description = 'You do not have permission to use this command.'\
                                '\nYou need to be able to kick members to use this command.'
            await ctx.reply(embed=embed, mention_author=False)
            return
    
        try:
            member = await ctx.guild.fetch_member(int(re.sub("[^0-9]", "", member)))
            reason = " ".join(reason)

            await ctx.guild.kick(member, reason=reason)
            embed.description = f'Successfully kicked {member}'
            if reason:
                embed.description += f'\nReason: {reason}'
            
        except Exception as e:
            embed.colour = 0x7f0003
            embed.description = f'ERROR: {e}'
    
        await ctx.reply(embed=embed, mention_author=False)

    @commands.command()
    async def ban(self, ctx, member: str, *reason: str):
        """Bans mentioned member. Deletes messages from member over the past day."""

        embed = discord.Embed(title=f'ban: {member}', color=0x037f03)
        embed.set_author(name="The Goon", url="https://github.com/yoonthegoon/The-Goon",
                         icon_url="https://cdn.discordapp.com/avatars/783779669979693117/84be9f2ab1b9bbb56a6c6c113cae7340.png")

        if not ctx.author.permissions_in(ctx.channel).ban_members:
            embed.colour = 0x03037f
            embed.description = 'You do not have permission to use this command.' \
                                '\nYou need to be able to ban members to use this command.'
            await ctx.reply(embed=embed, mention_author=False)
            return

        try:
            member = await ctx.guild.fetch_member(int(re.sub("[^0-9]", "", member)))
            reason = " ".join(reason)

            await ctx.guild.ban(member, reason=reason)
            embed.description = f'Successfully banned {member}'
            if reason:
                embed.description += f'\nReason: {reason}'

        except Exception as e:
            embed.colour = 0x7f0003
            embed.description = f'ERROR: {e}'

        await ctx.reply(embed=embed, mention_author=False)


def setup(bot):
    bot.add_cog(Moderation(bot))
