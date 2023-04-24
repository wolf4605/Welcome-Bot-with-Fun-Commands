import discord
from discord import File
from discord.utils import get
from discord.ext import commands
from easy_pil import Editor, load_image_async, Font, load_image
from PIL import Image
from io import BytesIO
import random
import os

class Pout(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.command()
    async def pout(self, ctx):
        """The name says it all"""

        # list of image URLs
        image_urls = ["https://cdn.discordapp.com/attachments/1099140243724177579/1099255409933549589/noela-angry.gif",
                      "https://cdn.discordapp.com/attachments/1099140243724177579/1099255409581236256/cute-pouting.gif",
                      "https://cdn.discordapp.com/attachments/1099140243724177579/1099255409216344136/anime-fan27-pout.gif",
                      "https://cdn.discordapp.com/attachments/1099140243724177579/1099255411061817406/pouts-pout.gif",
                      "https://cdn.discordapp.com/attachments/1099140243724177579/1099255410671755294/pouting-angry.gif",
                      "https://cdn.discordapp.com/attachments/1099140243724177579/1099255410336223283/pout-anime.gif",
                    ]
        # randomly select an image URL from the list
        image_url = random.choice(image_urls)

        phrases = [f"{ctx.author.display_name} just pouted!!! awww~~~😊",
                   f"{ctx.author.display_name} pouted~~Kawaii~~"
                ]
        
        phrase = random.choice(phrases)
        embed = discord.Embed(color=random.randint(0, 0xFFFFFF))
        embed.set_author(name=phrase,
                        icon_url=ctx.author.display_avatar)

        embed.set_image(url=image_url)
        # send the embed as a reply
        await ctx.send(embed=embed)
def setup(bot:commands.Bot):
    bot.add_cog(Pout(bot))