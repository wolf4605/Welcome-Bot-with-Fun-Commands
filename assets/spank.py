import discord
from discord import File
from discord.utils import get
from discord.ext import commands
from easy_pil import Editor, load_image_async, Font, load_image
from PIL import Image
from io import BytesIO
import random
import os


class Spank(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.command()
    async def spank(self, ctx, member: discord.Member):
        """Spank a user"""
        # list of image URLs
        image_urls = ["https://cdn.discordapp.com/attachments/1097782168194912296/1098254998179151952/spank-bunny-naughty-bunny.gif",
                    "https://cdn.discordapp.com/attachments/1097782168194912296/1098254997797490819/spank4.gif",
                    "https://cdn.discordapp.com/attachments/1097782168194912296/1098254997487104080/spank.gif",
                    "https://cdn.discordapp.com/attachments/1097782168194912296/1098254996933443735/spank_3.gif",
                    "https://cdn.discordapp.com/attachments/1097782168194912296/1098254996023300229/spank_1.gif",
                    "https://cdn.discordapp.com/attachments/1097782168194912296/1098254995645792296/rikka-takanashi-bad-girl.gif",
                    "https://cdn.discordapp.com/attachments/1097782168194912296/1098254995289297016/bad-spank.gif",
                    "https://cdn.discordapp.com/attachments/1097782168194912296/1098254994928578591/asobi-asobase-school-girl.gif",
                    "https://cdn.discordapp.com/attachments/1097782168194912296/1098254994379112508/anime-school-girl.gif",
                    "https://cdn.discordapp.com/attachments/1097782168194912296/1098254993989054545/anime-girl.gif",
                    ]
        # randomly select an image URL from the list
        image_url = random.choice(image_urls)

        phrases = [f"{ctx.author.display_name} spanks {member.display_name} ! How naughty 〜",
                f"{ctx.author.display_name} spanks {member.display_name}'s butt !! Oh my 〜 !!",
                f"{ctx.author.display_name} spanked {member.display_name} 〜 kinky...",
                ]
        
        phrase = random.choice(phrases)
        embed = discord.Embed(color=random.randint(0, 0xFFFFFF))
        embed.set_author(name=phrase,
                        icon_url=ctx.author.display_avatar)

        embed.set_image(url=image_url)
        # send the embed as a reply
        await ctx.send(embed=embed)

def setup(bot:commands.Bot):
    bot.add_cog(Spank(bot))