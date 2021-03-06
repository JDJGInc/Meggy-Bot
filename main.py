import os, discord, aiohttp, motor, motor.motor_asyncio, dns, B
import traceback

# uses the os to grab .env variables(later with os.environ) - it's fairly safe, #the python wrapper I use(it's actually discord.py but the python program treats it as discord), Aiohttp is the way we grab stuff from urlls, etc..., I import motor here for mongodb, then have the mongodb speacil status is motor_asyncio, then dns is the way it connects to it I guess.
from discord.ext import commands

# using commands extenstion trust me without this it would be much more of a pain

discord.http._set_api_version(9)
# sets the api version one because of the new api requires message intents
class MeggyBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def start(self, *args, **kwargs):
        self.session = aiohttp.ClientSession()
        # defines a speacil aiohttp session for the whole bot to be able to use.
        # defines the key to log in.
        # the specific DB it will use.
        await super().start(*args, **kwargs)
        # calls the orginal start method.

    async def close(self):
        await self.session.close()
        # closes the aiohttp session that was the custom one defined for the bot.
        await super().close()
        # calls the orginal close class.

        async def setup_hook(self):
            await self.load_extension("jishaku")

            for filename in os.listdir("./cogs"):
                if filename.endswith(".py"):
                    try:
                        await self.load_extension(f"cogs.{filename[:-3]}")
                    # helps organization commands lol
                    except commands.errors.NoEntryPointError:
                        traceback.print_exec()

        # a must to do this :) and use cogs


# subclasses bot to allow all areas of the client to be able to use the database session.

bot = MeggyBot(command_prefix=commands.when_mentioned_or("m*"), intents=discord.Intents.default())
mongo_url = os.environ.get("DB_data")
DB_client = motor.motor_asyncio.AsyncIOMotorClient(mongo_url)
bot.DB = DB_client["Meggy_Data"]
# defines the bot object without it no bot access
# intents refers to stuff discord uses(just look up it's meaning)


@bot.listen()
async def on_ready():
    print("Bot is Ready")
    print(f"Logged in as {bot.user}")
    print(f"Id: {bot.user.id}")


# when the boot boots up it will print the bot is ready then the name and then id.


@bot.event
async def on_error(event, *args, **kwargs):
    more_information = os.sys.exc_info()
    error_wanted = traceback.format_exc()
    traceback.print_exc()
    # print(more_information[0])


B.b()
# makes flask server that allows an uptime monitor to keep bot up. (allowed by repl.it btw)
bot.run(os.environ["TOKEN"])
# this starts the bot using the private .env variable TOKEN
