import discord
from discord import File
from discord.utils import get
from discord.ext import commands
from easy_pil import Editor, load_image_async, Font, load_image
from PIL import Image
from io import BytesIO
import random
import os

class Poke(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.command()
    async def poke(self, ctx, member: discord.Member):
        """Poke someone"""

        # list of image URLs
        image_urls = ["https://cdn.discordapp.com/attachments/1099140487975276675/1099251937423138927/anime-poke.gif",
                      "https://cdn.discordapp.com/attachments/1099140487975276675/1099251937813217371/anime-sleep.gif",
                      "https://cdn.discordapp.com/attachments/1099140487975276675/1099251938215854081/boob-poke.gif",
                      "https://cdn.discordapp.com/attachments/1099140487975276675/1099251938547212288/boop-anime.gif",
                      "https://cdn.discordapp.com/attachments/1099140487975276675/1099251938886959115/poke_1.gif",
                      "https://cdn.discordapp.com/attachments/1099140487975276675/1099251939251847249/poke_2.gif",
                      "https://cdn.discordapp.com/attachments/1099140487975276675/1099251939683876864/poke.gif",
                    ]
        # randomly select an image URL from the list
        image_url = random.choice(image_urls)

        phrases = [f"{ctx.author.display_name} poked {member.display_name}...",
                   f"{ctx.author.display_name} just poked {member.display_name}!!!"
                ]
        
        phrase = random.choice(phrases)
        embed = discord.Embed(color=random.randint(0, 0xFFFFFF))
        embed.set_author(name=phrase,
                        icon_url=ctx.author.display_avatar)

        embed.set_image(url=image_url)
        # send the embed as a reply
        await ctx.send(embed=embed)
def setup(bot:commands.Bot):
    bot.add_cog(Poke(bot))