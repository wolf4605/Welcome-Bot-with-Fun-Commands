import discord
from discord import File
from discord.utils import get
from discord.ext import commands
from easy_pil import Editor, load_image_async, Font, load_image
from PIL import Image
from io import BytesIO
import random
import os

class Punch(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.command()
    async def punch(self, ctx:commands.context, member: discord.Member):
        """Punch Some A**hole"""
        # list of image URLs
        image_urls = ["https://cdn.discordapp.com/attachments/1097837597298016286/1099942758296338452/anime-rezero.gif",
                      "https://cdn.discordapp.com/attachments/1097837597298016286/1099942758690607144/anya-forger-damian-spy-x-family.gif",
                      "https://cdn.discordapp.com/attachments/1097837597298016286/1099942759013548093/kimihito-monster-musume.gif",
                      "https://cdn.discordapp.com/attachments/1097837597298016286/1099942759391051837/one-punch-man-saitama.gif",
                      "https://cdn.discordapp.com/attachments/1097837597298016286/1099942759772717107/rimuru-rimuru-punch.gif",
                      "https://cdn.discordapp.com/attachments/1097837597298016286/1099942760141832242/rin243109-blue-exorcist.gif",
                    ]
        # randomly select an image URL from the list
        image_url = random.choice(image_urls)

        phrases = [f"{ctx.author.display_name} punched {member.display_name}!!! In you face 👊.",
                   f"{ctx.author.display_name} punched {member.display_name}!!! You can't see me 🖐️.",
                ]
        
        phrase = random.choice(phrases)
        embed = discord.Embed(color=random.randint(0, 0xFFFFFF))
        embed.set_author(name=phrase,
                        icon_url=ctx.author.display_avatar)

        embed.set_image(url=image_url)
        # send the embed as a reply
        await ctx.send(embed=embed)

def setup(bot:commands.Bot):
    bot.add_cog(Punch(bot))