import discord
from discord.ext import commands
import os
import requests


def degrees_to_cardinal(d):
    """https://gist.github.com/RobertSudwarts/acf8df23a16afdb5837f"""

    dirs = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
            "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
    ix = int((d + 11.25)/22.5)
    return dirs[ix % 16]


class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # TODO: switch out dictionary library with API instead of scraper
    @commands.command()
    async def define(self, ctx, word: str):
        """Define a given word"""

        embed = discord.Embed(title=f'define: {word}', color=0x037f03)
        embed.set_author(name="The Goon", url="https://github.com/yoonthegoon/The-Goon",
                         icon_url="https://cdn.discordapp.com/avatars/783779669979693117/84be9f2ab1b9bbb56a6c6c113cae7340.png")

        try:
            from dictionary import define  # custom library (...\envs\The-Goon\Lib\dictionary)

            r = define(word)

            embed.url = f'https://www.wordnik.com/words/{word}'
            for li in r['ul']:
                if li > 4:
                    break
                embed.add_field(name=r['ul'][li][0]['abbr'], value=r['ul'][li][1], inline=False)
            embed.set_footer(text=r['source'])

        except Exception as e:
            embed.colour = 0x7f0003
            embed.description = f'ERROR: {e}'

        await ctx.reply(embed=embed, mention_author=False)
    
    @commands.command()
    async def weather(self, ctx, *city):
        """Gives the current weather for a city"""
        q = " ".join(city)

        embed = discord.Embed(title=f'weather: {q}', color=0x037f03)
        embed.set_author(name="The Goon", url="https://github.com/yoonthegoon/The-Goon",
                         icon_url="https://cdn.discordapp.com/avatars/783779669979693117/84be9f2ab1b9bbb56a6c6c113cae7340.png")

        try:
            api_key = os.getenv('OWM_TOKEN')

            r = requests.get(f'https://api.openweathermap.org/data/2.5/weather'
                             f'?q={",".join(q.split(", "))}&appid={api_key}&units=imperial')
            json = r.json()
            print(json)

            embed.url = f'https://www.openstreetmap.org/#map=12/{json["coord"]["lat"]}/{json["coord"]["lon"]}'
            embed.description = f'{json["main"]["temp"]:.1f}°F. Feels like {json["main"]["feels_like"]:.0f}°F. {json["weather"][0]["description"].capitalize()}'
            embed.set_thumbnail(url=f'https://openweathermap.org/img/wn/{json["weather"][0]["icon"]}@2x.png')
            embed.add_field(name='High / Low', value=f'{json["main"]["temp_max"]:.1f}°F/{json["main"]["temp_min"]:.1f}°F', inline=True)
            embed.add_field(name='Wind', value=f'{json["wind"]["speed"]}mph {degrees_to_cardinal(json["wind"]["deg"])}', inline=True)
            embed.add_field(name='Humidity', value=f'{json["main"]["humidity"]}%', inline=True)
            embed.add_field(name='Pressure', value=f'{json["main"]["pressure"] * 0.02953:.1f}in', inline=True)
            embed.add_field(name='Visibility', value=f'{json["visibility"] * 0.0006213712:.1f}mi' if json["visibility"] != 10000 else 'High', inline=True)

        
        except Exception as e:
            embed.colour = 0x7f0003
            embed.description = f'ERROR: {e}'
        
        await ctx.reply(embed=embed, mention_author=False)


def setup(bot):
    bot.add_cog(Utility(bot))
