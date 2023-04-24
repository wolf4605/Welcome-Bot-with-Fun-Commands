import discord
from discord import File
from discord.ext import commands
from easy_pil import Editor, Font, load_image
import random

class Welcome(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    
    

    @commands.command()
    async def welcome(self, ctx: commands.context, member: discord.Member):

        """Create a welcome card"""

        pos = sum(m.joined_at < member.joined_at for m in member.guild.members
            if m.joined_at is not None)

        if pos == 1:
            te = "st"
        elif pos == 2:
            te = "nd"
        elif pos == 3:
            te = "rd"
        else:
            te = "th"
        # list of possible background images
        backgrounds = ["wlcbg.jpg", "wlcbg2.jpg", "wlcbg3.jpg"]

            # randomly select a background image
        random.shuffle(backgrounds)

        for selected_background in backgrounds:

            background = Editor(selected_background)


            # Card 1
            if selected_background == "wlcbg.jpg":
                background = Editor("wlcbg.jpg")
                profile_image = load_image(str(member.display_avatar.url))

                profile = Editor(profile_image).resize((200, 200)).circle_image()
                rose = Font("rose.ttf", size=40)
                rose1 = Font("rose.ttf", size=30)
                vicky = Font("bazoka.ttf", size=30)

                background.paste(profile, (175, 100))
                background.ellipse(
                    (175, 100),
                    200,
                    200,
                    outline="#e68694",
                    stroke_width=8,
                )

                background.text(
                    (300, 350),
                    "Welcome to Your New Home",
                    color="#ff7f87",
                    font=rose,
                    align="center",
                )

                background.text(
                    (300, 410),
                    f"{member.guild.name}",
                    color="#e68694",
                    font=vicky,
                    align="center",
                )

                background.text(
                    (300, 450),
                    f"You Are The {pos}{te} Member",
                    color="#e2973f",
                    font=rose1,
                    align="center",
                )
                #Use elif when adding more pitures
            elif selected_background == "wlcbg3.jpg":
                background = Editor("wlcbg3.jpg")
                profile_image = load_image(str(member.display_avatar.url))

                profile = Editor(profile_image).resize((200, 200)).circle_image()
                rose = Font("rose.ttf", size=40)
                rose1 = Font("rose.ttf", size=30)
                vicky = Font("bazoka.ttf", size=30)

                background.paste(profile, (580, 120))
                background.ellipse(
                    (580, 120),
                    200,
                    200,
                    outline="#1f5db6",
                    stroke_width=8,
                )

                background.text(
                    (650, 350),
                    "Welcome to Your New Home",
                    color="#1f5db6",
                    font=rose,
                    align="center",
                )

                background.text(
                    (650, 410),
                    f"{member.guild.name}",
                    color="#8c75b9",
                    font=vicky,
                    align="center",
                )

                background.text(
                    (650, 450),
                    f"You Are The {pos}{te} Member",
                    color="#e088aa",
                    font=rose1,
                    align="center",
                )
            else: 
                background = Editor("wlcbg2.jpg")
                profile_image = load_image(str(member.display_avatar.url))

                profile = Editor(profile_image).resize((200, 200)).circle_image()
                rose = Font("rose.ttf", size=40)
                rose1 = Font("rose.ttf", size=30)
                vicky = Font("bazoka.ttf", size=30)

                background.paste(profile, (590, 100))
                background.ellipse(
                    (590, 100),
                    200,
                    200,
                    outline="#a69cd3",
                    stroke_width=8,
                )

                background.text(
                    (670, 350),
                    "Welcome to Your New Home",
                    color="#8c7fc4",
                    font=rose,
                    align="center",
                )

                background.text(
                    (670, 410),
                    f"{member.guild.name}",
                    color="#ffadbc",
                    font=vicky,
                    align="center",
                )

                background.text(
                    (670, 450),
                    f"You Are The {pos}{te} Member",
                    color="#f9b9a9",
                    font=rose1,
                    align="center",
                )

        file = File(fp=background.image_bytes, filename="wlcbg.jpg")

        #if you want to message more message then you can add like this
        await ctx.send(
            f"<a:sparkling:990720256580386896><a:Bouncy_nya:990722989203021854><a:moon_stars:1064538162518564874> Hey {member.mention} has just joined the cafe!  Hope you have a pawsome time in MoonLightNekos !! <a:moon_stars:1064538162518564874><a:Bouncy_nya:990722989203021854><a:sparkling:990720256580386896>\n━━━━━━━━━━━━━━ ⋆⋅ ☾ ⋅⋆ ━━━━━━━━━━━━━━\n<a:Pastel_Moon:1064529200238833674> Choose a color for your name in <#990733298730934322> channel\n<a:Pastel_Moon:1064529200238833674> You may also gain special role access in <#990730814855712818>\n<a:Pastel_Moon:1064529200238833674> And if you play Toram Online...Tell us briefly of yourself here in <#1008904966590697615> ! We would appreciate it very much (⁠╹⁠▽⁠╹⁠⁠) /"
        )

        #for sending the card
        await ctx.send(file=file)

def setup(bot: commands.Bot):
    bot.add_cog(Welcome(bot))