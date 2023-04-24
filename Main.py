#imported ,odules
import discord
from discord import File
from discord.utils import get
from discord.ext import commands
from easy_pil import Editor, load_image_async, Font, load_image
from PIL import Image
from io import BytesIO
import random
import os
from discord.ext.commands import Bot, DefaultHelpCommand

token = "123"     #You Bot Token

intents = discord.Intents.all()
intents.members = True
prefixes = "mew ", "Mew ", "Mew", "mew"

class CustomHelpCommand(DefaultHelpCommand):
    def get_ending_note(self):
        return None

    async def send_pages(self):
        destination = self.get_destination()
        for page in self.paginator.pages:
            embed = discord.Embed(
                                description=page.replace('`', ''),
                                color=random.randint(0, 0xFFFFFF))
            embed.set_author(icon_url=(self.context.bot.user.display_avatar),
                                name="__List of Commands__")
            embed.set_footer(text="For more info on a command use\nmew help <command>.")
            await destination.send(embed=embed)

    def add_indented_commands(self, commands, heading, max_size=None):
        if not commands:
            return
        for command in commands:
            self.paginator.add_line(f'{self.context.prefix}{command.name} -- {command.short_doc}')

def main():
    bot = commands.Bot(command_prefix=prefixes, intents=intents, help_command=CustomHelpCommand())
    
    @bot.event
    async def on_member_join(member):

        #add the channel id in which you want to send the card
        channel = bot.get_channel(990565019039199272)

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
        await channel.send(
        f"<a:sparkling:990720256580386896><a:Bouncy_nya:990722989203021854><a:moon_stars:1064538162518564874> Hey {member.mention} has just joined the cafe!  Hope you have a pawsome time in MoonLightNekos !! <a:moon_stars:1064538162518564874><a:Bouncy_nya:990722989203021854><a:sparkling:990720256580386896>\n━━━━━━━━━━━━━━ ⋆⋅ ☾ ⋅⋆ ━━━━━━━━━━━━━━\n<a:Pastel_Moon:1064529200238833674> Choose a color for your name in <#990733298730934322> channel\n<a:Pastel_Moon:1064529200238833674> You may also gain special role access in <#990730814855712818>\n<a:Pastel_Moon:1064529200238833674> And if you play Toram Online...Tell us briefly of yourself here in <#1008904966590697615> ! We would appreciate it very much (⁠╹⁠▽⁠╹⁠⁠) /"
        )

        #for sending the card
        await channel.send(file=file)

    @bot.event
    async def on_ready():
        print("Bot has connected")
        
        for filename in os.listdir("assets"):
            if filename.endswith(".py"):
                bot.load_extension(f"assets.{filename[:-3]}")
    bot.run(token)

if __name__ == '__main__':
    main()
