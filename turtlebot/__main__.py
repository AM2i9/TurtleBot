import os

import discord
from dislash import Option

import turtlebot.log
from turtlebot.bot import TurtleBot
from turtlebot.parser import TurtleLang, ParseError
from turtlebot.turtle import Turtle

try:
    import dotenv

    dotenv.load_dotenv()
except ImportError:
    pass

turtlebot.log.setup_log()

drawing_size = (500, 500)

turt = TurtleBot.create()

bot_description = """Draw things using a Turtle script!

**Syntax:**
Commands, or single letters, are given to the bot, followed by a number. The number could be a number of pixels, degrees, or a 1 or 0 for true and false.
Each command is seperated by a comma.

Here's a quick example, for drawing a 100x100 square:
```
F100,R90,F100,R90,F100,R90,F100,R90
```

**Commands:**
- `F<n>`: Move the pointer forward `n` pixels.
- `B<n>`: Move the pointer backwords `n` pixels.
- `L<n>`: Turn the poniter left `n` degrees.
- `R<n>`: Turn the pointer right `n` degrees.
- `A<n>`: Set the angle of the pointer.
- `P<n>`: Set the pen state. `n` can be `0` for off, `1` for on.

**Running your script:**
Your script can be run using the `/draw` slash command.
```
/draw <code>
```
"""

help_embed = discord.Embed(
    title="TurtleBot", description=bot_description, color=discord.Colour.green()
)

help_embed.set_footer(text="Created by Patrick Brennan (AM2i9)")


def run_code(_code):
    code = _code.replace("`", "")
    turtle = Turtle(*drawing_size, (255, 255, 255))
    parser = TurtleLang(turtle)

    parser.parse(code)
    return turtle.save_as_bytes()


@turt.interaction_client.command(
    name="help",
    description="Get help on how to use TurtleBot",
)
async def help(inter):

    if not help_embed.thumbnail:
        help_embed.set_thumbnail(url=turt.user.avatar_url)
    return await inter.reply(embed=help_embed)


@turt.interaction_client.command(
    name="draw",
    description="Draw some turtle code.",
    options=[Option("code", "Turtle code", required=False)],
)
async def draw(inter, code: str = None):

    if not code:
        if not help_embed.thumbnail:
            help_embed.set_thumbnail(url=turt.user.avatar_url)
        return await inter.reply(embed=help_embed)

    try:
        image = run_code(code)
    except ParseError as e:
        await inter.reply(f"There was an error when parsing your script: ```{e}```")
        return

    await inter.reply("Drawing...")
    await inter.followup(
        f"{inter.author.mention}. Here is your Turtle's drawing!",
        file=discord.File(image, filename="turtle0.png"),
    )


turt.run(os.environ.get("TOKEN"))
