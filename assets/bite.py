import discord
from discord import File
from discord.utils import get
from discord.ext import commands
from easy_pil import Editor, load_image_async, Font, load_image
from PIL import Image
from io import BytesIO
import random
import os

class Bite(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.command()
    async def bite(self, ctx, member: discord.Member):
        """Bite Someone"""
        # list of image URLs
        image_urls = ["https://cdn.discordapp.com/attachments/1097837629833224192/1099230277454286888/anime-bite_1.gif",
                      "https://cdn.discordapp.com/attachments/1097837629833224192/1099230277764661248/anime-bite_2.gif",
                      "https://cdn.discordapp.com/attachments/1097837629833224192/1099230278070837328/anime-bite_3.gif",
                      "https://cdn.discordapp.com/attachments/1097837629833224192/1099230278418976788/anime-bite_4.gif",
                      "https://cdn.discordapp.com/attachments/1097837629833224192/1099230278725156874/anime-bite.gif",
                      "https://cdn.discordapp.com/attachments/1097837629833224192/1099230279098454086/anime-cute.gif",
                      "https://cdn.discordapp.com/attachments/1097837629833224192/1099230279488520253/bite.gif",
                      "https://cdn.discordapp.com/attachments/1097837629833224192/1099230279857623090/re-zero-rem.gif",
                    ]
        # randomly select an image URL from the list
        image_url = random.choice(image_urls)

        phrases = [f"{ctx.author.display_name} is nibbling {member.display_name} !",
                   f"{ctx.author.display_name} is biting {member.display_name} ! Owie...",
                   f"{ctx.author.display_name} has bitten {member.display_name} !!",
                   f"{ctx.author.display_name} is biting {member.display_name} ! That must have hurt...",
                ]
        
        phrase = random.choice(phrases)
        embed = discord.Embed(color=random.randint(0, 0xFFFFFF))
        embed.set_author(name=phrase,
                        icon_url=ctx.author.display_avatar)

        embed.set_image(url=image_url)
        # send the embed as a reply
        await ctx.send(embed=embed)
def setup(bot:commands.Bot):
    bot.add_cog(Bite(bot))
