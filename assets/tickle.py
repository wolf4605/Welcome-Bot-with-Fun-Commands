import discord
from discord import File
from discord.utils import get
from discord.ext import commands
from easy_pil import Editor, load_image_async, Font, load_image
from PIL import Image
from io import BytesIO
import random
import os

class Tickle(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.command()
    async def tickle(self, ctx, member: discord.Member):
        """Tickle Someone"""
        # list of image URLs
        image_urls = ["https://cdn.discordapp.com/attachments/1099140658675073104/1099938818976661537/tickle-laugh.gif",
                      "https://cdn.discordapp.com/attachments/1099140658675073104/1099938818662092821/saikin-yatotta-maid-ga-ayashii-anime-tickle.gif",
                      "https://cdn.discordapp.com/attachments/1099140658675073104/1099938818326532117/neptune.gif",
                      "https://cdn.discordapp.com/attachments/1099140658675073104/1099938817999388745/date-a-live-date-a-live-iv.gif",
                      "https://cdn.discordapp.com/attachments/1099140658675073104/1099938817659637770/cute-anime.gif",
                      "https://cdn.discordapp.com/attachments/1099140658675073104/1099938817068253234/anime-tickle.gif",
                      "https://cdn.discordapp.com/attachments/1099140658675073104/1099938816669782086/anime-cat-girl-anime.gif",
                    ]
        # randomly select an image URL from the list
        image_url = random.choice(image_urls)

        phrases = [f"{ctx.author.display_name} tickled {member.display_name}!!! hehehe",
                   f"{ctx.author.display_name} is tickling {member.display_name}!!! tickle tickle tickle",
                ]
        
        phrase = random.choice(phrases)
        embed = discord.Embed(color=random.randint(0, 0xFFFFFF))
        embed.set_author(name=phrase,
                        icon_url=ctx.author.display_avatar)

        embed.set_image(url=image_url)
        # send the embed as a reply
        await ctx.send(embed=embed)

def setup(bot:commands.Bot):
    bot.add_cog(Tickle(bot))