import discord
from discord import File
from discord.utils import get
from discord.ext import commands
from easy_pil import Editor, load_image_async, Font, load_image
from PIL import Image
from io import BytesIO
import random
import os

class Wanted(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.command()
    async def wanted(self, ctx, member: discord.Member, reward="10,000,000", ctx1="."):
        """Create a wanted poster of someone"""
        background = Editor("wanted.jpg")
        profile_image = load_image(str(member.display_avatar))
        profile = Editor(profile_image).resize((330, 340))
        run = Font("rundeck.ttf", size=40)
        run = Font("rundeck.ttf", size=35)
        
        background.paste(profile, (137, 253))
        background.rectangle(
            (137, 253),
            330,
            340,
            outline="black",
            stroke_width=8,
        )

        background.text(
            (300, 630),
            f"Name:  {member.display_name}",
            color="black",
            font=run,
            align="center",
        )

        background.text(
            (300, 720),
            f"Guild: {member.guild.name}",
            color="black",
            font=run,
            align="center",
        )

        background.text(
            (300, 815),
            f"REWARD ${reward} {ctx1}",
            color="#000000",
            font=run,
            align="center",
        )

        file = File(fp=background.image_bytes, filename="wanted.jpg")

        #if you want to message more message then you can add like this
        await ctx.send(
            f"Heya {member.mention}! The cops are on your tail."
        )

        #for sending the card
        await ctx.send(file=file)

def setup(bot:commands.Bot):
    bot.add_cog(Wanted(bot))