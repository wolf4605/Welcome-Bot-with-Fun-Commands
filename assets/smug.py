import discord
from discord import File
from discord.utils import get
from discord.ext import commands
from easy_pil import Editor, load_image_async, Font, load_image
from PIL import Image
from io import BytesIO
import random
import os

class Smug(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.command()
    async def smug(self, ctx, member: discord.Member):
        """Smug at someone"""
        # list of image URLs
        image_urls = ["https://cdn.discordapp.com/attachments/1098468936338649168/1099951975300349993/anime-eyebrow-raise.gif",
                      "https://cdn.discordapp.com/attachments/1098468936338649168/1099951975652659332/anime-konata.gif",
                      "https://cdn.discordapp.com/attachments/1098468936338649168/1099951976042741870/futakana-smug-anime.gif",
                      "https://cdn.discordapp.com/attachments/1098468936338649168/1099951976353116251/gawr-gura-smug.gif",
                      "https://cdn.discordapp.com/attachments/1098468936338649168/1099951976705429525/kroni-smug-face.gif",
                      "https://cdn.discordapp.com/attachments/1098468936338649168/1099951977024208967/panda-clip-smug.gif",
                    ]
        # randomly select an image URL from the list
        image_url = random.choice(image_urls)

        phrases = [f"{ctx.author.display_name} makes a smug face at {member.display_name} !",
                   f"{ctx.author.display_name} conceitedly smugs at {member.display_name} !! 🤭 ",
                ]
        
        phrase = random.choice(phrases)
        embed = discord.Embed(color=random.randint(0, 0xFFFFFF))
        embed.set_author(name=phrase,
                        icon_url=ctx.author.display_avatar)

        embed.set_image(url=image_url)
        # send the embed as a reply
        await ctx.send(embed=embed)

def setup(bot:commands.Bot):
    bot.add_cog(Smug(bot))