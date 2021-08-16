import logging
import asyncio

import discord
from discord.ext import commands
from dislash import InteractionClient

log = logging.getLogger("bot")


class TurtleBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        self.ready = False

        super().__init__(*args, **kwargs)

        self.interaction_client = InteractionClient(self)

    async def on_ready(self):
        if not self.ready:
            self.ready = True

            # The print statement is here for the sole reason of satisfying my server's "running" conditions
            print("Logged in")

            log.info(f"Bot logged in as {self.user}")

        else:
            log.info("Bot reconnected")

    @classmethod
    def create(cls):
        loop = asyncio.get_event_loop()

        intents = discord.Intents.none()
        return cls(
            command_prefix=commands.when_mentioned_or("turt!"),
            loop=loop,
            intents=intents,
        )
