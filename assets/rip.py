import discord
from discord import File
from discord.utils import get
from discord.ext import commands
from easy_pil import Editor, load_image_async, Font, load_image
from PIL import Image
from io import BytesIO
import random
import os

class RIP(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.command()
    async def rip(self, ctx):
        """Commit Sucide"""

        # list of image URLs
        image_urls = ["https://cdn.discordapp.com/attachments/1097839574870405164/1099215525537656892/anime-alone.gif",
                      "https://cdn.discordapp.com/attachments/1097839574870405164/1099215525881581598/anime-emotionless.gif",
                      "https://cdn.discordapp.com/attachments/1097839574870405164/1099215526242299934/exhausted-tired.gif",
                      "https://cdn.discordapp.com/attachments/1097839574870405164/1099215526636560434/falling-over.gif",
                      "https://cdn.discordapp.com/attachments/1097839574870405164/1099215526988877834/kanokari-anime-fall.gif",
                      "https://cdn.discordapp.com/attachments/1097839574870405164/1099215527412510814/reina-aharen-aharen-san-wa-hakarenai.gif",
                      "https://cdn.discordapp.com/attachments/1097839574870405164/1099215527743852544/suicide.gif",
                     ]
        # randomly select an image URL from the list
        image_url = random.choice(image_urls)

        phrases = [f"{ctx.author.display_name} died a lonely death 💀",
                   f"{ctx.author.display_name}... 🪦 RIP",
                   f"May {ctx.author.display_name} rest peacefully",
                   f"{ctx.author.display_name} died!! One more weight off this world 💀",
                ]
        
        phrase = random.choice(phrases)
        embed = discord.Embed(color=random.randint(0, 0xFFFFFF))
        embed.set_author(name=phrase,
                        icon_url=ctx.author.display_avatar)

        embed.set_image(url=image_url)
        # send the embed as a reply
        await ctx.send(embed=embed)
def setup(bot:commands.Bot):
    bot.add_cog(RIP(bot))