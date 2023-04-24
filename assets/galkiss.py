import discord
from discord import File
from discord.utils import get
from discord.ext import commands
from easy_pil import Editor, load_image_async, Font, load_image
from PIL import Image
from io import BytesIO
import random
import os

class Gal_Kiss(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.command()
    async def galkiss(self, ctx, member: discord.Member):
        """Some Girl to Girl Action"""
        # list of image URLs
        image_urls = ["https://cdn.discordapp.com/attachments/1099218931824205864/1099219792893857872/kiss-anime.gif",
                      "https://cdn.discordapp.com/attachments/1099218931824205864/1099219793279729824/lesbian_1.gif",
                      "https://cdn.discordapp.com/attachments/1099218931824205864/1099219793657204837/lesbian.gif",
                      "https://cdn.discordapp.com/attachments/1099218931824205864/1099219794059874385/sakura-trick-yuu.gif",
                      "https://cdn.discordapp.com/attachments/1099218931824205864/1099219794399608904/yuri-kiss-yuri.gif",
                    ]
        # randomly select an image URL from the list
        image_url = random.choice(image_urls)

        phrases = [f"{ctx.author.display_name} kisses {member.display_name} ～ 💖 ",
                f"{ctx.author.display_name} smooches {member.display_name} !! How cute～",
                f"{ctx.author.display_name} kisses {member.display_name}!! Muwaaah",
                f"{ctx.author.display_name} kisses {member.display_name}!!! Things are heating up...",
                ]
        
        phrase = random.choice(phrases)
        embed = discord.Embed(color=random.randint(0, 0xFFFFFF))
        embed.set_author(name=phrase,
                        icon_url=ctx.author.display_avatar)

        embed.set_image(url=image_url)
        # send the embed as a reply
        await ctx.send(embed=embed)

def setup(bot:commands.Bot):
    bot.add_cog(Gal_Kiss(bot))