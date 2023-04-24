import discord
from discord import File
from discord.utils import get
from discord.ext import commands
from easy_pil import Editor, load_image_async, Font, load_image
from PIL import Image
from io import BytesIO
import random
import os

class Slap(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.command()
    async def slap(self, ctx, member: discord.Member):
        """Slap a User"""
        # list of image URLs
        image_urls = ["https://cdn.discordapp.com/attachments/1097837550871248896/1098197475317256242/anime-slap_1.gif",
                    "https://cdn.discordapp.com/attachments/1097837550871248896/1098197475694760026/girl-slap.gif",
                    "https://cdn.discordapp.com/attachments/1097837550871248896/1098197476130955348/shounen-maid-cat.gif",
                    "https://cdn.discordapp.com/attachments/1097837550871248896/1098197476487467117/slap_1.gif",
                    "https://cdn.discordapp.com/attachments/1097837550871248896/1098197476839804970/slap_2.gif",
                    "https://cdn.discordapp.com/attachments/1097837550871248896/1098197477192114226/slap.gif",
                    "https://cdn.discordapp.com/attachments/1097837550871248896/1098197477615734825/slap-bet-chisa-iori.gif",
                    "https://cdn.discordapp.com/attachments/1097837550871248896/1098197478911791114/slap-bitch-slap.gif",
                    "https://cdn.discordapp.com/attachments/1097837550871248896/1098197479620616273/tsuki-tsuki-ga.gif",
                    ]
        # randomly select an image URL from the list
        image_url = random.choice(image_urls)

        phrases = [f"{ctx.author.display_name} is slapping {member.display_name}!!",
                f"{ctx.author.display_name} slapped {member.display_name}",
                f"{ctx.author.display_name} has slapped {member.display_name}. Ouchies",
                f"{ctx.author.display_name} slaps {member.display_name} out of existance !!!",
                ]
        
        phrase = random.choice(phrases)
        embed = discord.Embed(color=random.randint(0, 0xFFFFFF))
        embed.set_author(name=phrase,
                        icon_url=ctx.author.display_avatar)

        embed.set_image(url=image_url)
        # send the embed as a reply
        await ctx.send(embed=embed)

def setup(bot:commands.Bot):
    bot.add_cog(Slap(bot))