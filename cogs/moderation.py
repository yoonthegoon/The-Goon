import discord
from discord.ext import commands


embed = discord.Embed(color=0x037f03)
embed.set_author(name="The Goon", url="https://github.com/yoonthegoon/The-Goon", 
                 icon_url="https://cdn.discordapp.com/avatars/783779669979693117/84be9f2ab1b9bbb56a6c6c113cae7340.png")


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def delete(self, ctx, limit: int):
        """Deletes past {limit} messages in current channel."""
        embed.title = f'delete: {limit}'
    
        if not ctx.author.permissions_in(ctx.channel).manage_messages:
            embed.description = 'You do not have permission to use this command.' \
                                'You need to be able to manage messages to use this command'
            await ctx.reply(embed=embed, mention_author=False)
            return
    
        try:
            history = ctx.channel.history(limit=limit)
            async for message in history:
                await message.delete()
            embed.description = f'{limit} messages deleted.'
            
        except Exception as e:
            embed.description = f'ERROR: {e}'

        await ctx.reply(embed=embed, mention_author=False)
    
    @commands.command()
    async def kick(self, ctx, user: discord.abc.Snowflake, reason: str = None):
        """Kicks mentioned user."""
        embed.title = f'kick: {user}'
        if reason:
            embed.title += f'\nreason: {reason}'

        if not ctx.author.permissions_in(ctx.channel).kick_members:
            embed.description = 'You do not have permission to use this command.'\
                                'You need to be able to kick members to use this command.'
            await ctx.reply(embed=embed, mention_author=False)
            return
    
        try:
            await ctx.guild.kick(user, reason=reason)
            
        except Exception as e:
            embed.description = f'ERROR: {e}'
    
        await ctx.reply(embed=embed, mention_author=False)


def setup(bot):
    bot.add_cog(Moderation(bot))
