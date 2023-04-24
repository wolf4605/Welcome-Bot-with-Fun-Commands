import discord
from discord import File
from discord.utils import get
from discord.ext import commands
from easy_pil import Editor, load_image_async, Font, load_image
from PIL import Image
from io import BytesIO
import random
import os

class Bro_Kiss(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.command()
    async def brokiss(self, ctx, member: discord.Member):
        """Too Gay"""
        # list of image URLs
        image_urls = ["https://cdn.discordapp.com/attachments/1099218788362223716/1099219008626110524/diabolik-lovers-anime.gif",
                      "https://cdn.discordapp.com/attachments/1099218788362223716/1099219008961663076/gay-anime.gif",
                      "https://cdn.discordapp.com/attachments/1099218788362223716/1099219009297195049/gay-kiss.gif",
                      "https://cdn.discordapp.com/attachments/1099218788362223716/1099219009645326336/gay-tall-kiss.gif",
                      "https://cdn.discordapp.com/attachments/1099218788362223716/1099219010006044753/kiss-anime.gif",
                      "https://cdn.discordapp.com/attachments/1099218788362223716/1099219010316410980/surrender-kiss.gif",
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
    bot.add_cog(Bro_Kiss(bot))