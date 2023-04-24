import discord
from discord import File
from discord.utils import get
from discord.ext import commands
from easy_pil import Editor, load_image_async, Font, load_image
from PIL import Image
from io import BytesIO
import random
import os

class Hug(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.command()
    async def hug(self, ctx, member: discord.Member):
        """Hug a User"""
        # list of image URLs
        image_urls = ["https://cdn.discordapp.com/attachments/1097782488392273920/1098162907541422152/Hug.gif",
                    "https://cdn.discordapp.com/attachments/1097782488392273920/1098162899958108230/Hug_4.gif",
                    "https://cdn.discordapp.com/attachments/1097782488392273920/1098162851790733332/hug-hugs.gif",
                    "https://cdn.discordapp.com/attachments/1097782488392273920/1098162848330428526/Hug_3.gif",
                    "https://cdn.discordapp.com/attachments/1097782488392273920/1098162801199026296/chobits-hideki-motosuwa.gif",
                    "https://cdn.discordapp.com/attachments/1097782488392273920/1098162797638078524/Hug_2.gif",
                    "https://cdn.discordapp.com/attachments/1097782488392273920/1098162754411560980/anime-hug.gif",
                    "https://cdn.discordapp.com/attachments/1097782488392273920/1098162662946385930/anime-hug_1.gif",
                    "https://cdn.discordapp.com/attachments/1097782488392273920/1098162656487157860/anime-hug_2.gif",
                    "https://cdn.discordapp.com/attachments/1097782488392273920/1098162554511044618/anime-happy.gif",
                    ]
        # randomly select an image URL from the list
        image_url = random.choice(image_urls)

        phrases = [f"{ctx.author.display_name} hugged {member.display_name}!!! UwU",
                f"{ctx.author.display_name} gives {member.display_name} a big bear hug !!",
                f"{ctx.author.display_name} warmly hugs {member.display_name}. Aww~",
                f"{ctx.author.display_name} cuddles {member.display_name}!!!",
                f"{ctx.author.display_name} squeezes {member.display_name}!!!",
                ]
        
        phrase = random.choice(phrases)
        embed = discord.Embed(color=random.randint(0, 0xFFFFFF))
        embed.set_author(name=phrase,
                        icon_url=ctx.author.display_avatar)

        embed.set_image(url=image_url)
        # send the embed as a reply
        await ctx.send(embed=embed)

def setup(bot:commands.Bot):
    bot.add_cog(Hug(bot))