import os, discord, aiohttp,  motor, motor.motor_asyncio, dns 
#uses the os to grab .env variables(later with os.environ) - it's fairly safe, #the python wrapper I use(it's actually discord.py but the python program treats it as discord), Aiohttp is the way we grab stuff from urlls, etc..., I import motor here for mongodb, then have the mongodb speacil status is motor_asyncio, then dns is the way it connects to it I guess.
from discord.ext import commands
#using commands extenstion trust me without this it would be much more of a pain

class MeggyBot(commands.Bot):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    #calls the base _init_ class
    self.DB_client = motor.motor_asyncio.AsyncIOMotorClient(str(os.environ['DB_data']))
    self.DB = self.DB_client["Meggy_Data"]
    self.mod_collection = self.DB["Meggy_data"]

  async def start(self,*args, **kwargs):
    self.session=aiohttp.ClientSession()
    #defines a speacil aiohttp session for the whole bot to be able to use.
    #defines the key to log in.
    #the specific DB it will use.
    await super().start(*args, **kwargs)
    #calls the orginal start method.

  async def close(self):
    await self.session.close()
    #closes the aiohttp session that was the custom one defined for the bot.
    await super().close()
    #calls the orginal close class.

#subclasses bot to allow all areas of the client to be able to use the database session.

bot = MeggyBot(command_prefix=commands.when_mentioned_or("m*"),intents = discord.Intents.all())
#defines the bot object without it no bot access
#intents refers to stuff discord uses(just look up it's meaning)

@bot.listen()
async def on_ready():
  print("Bot is Ready")
  print(f"Logged in as {bot.user}")
  print(f"Id: {bot.user.id}")

#when the boot boots up it will print the bot is ready then the name and then id.

bot.load_extension('jishaku')

for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    try:
      bot.load_extension(f'cogs.{filename[:-3]}')
      #helps organization commands lol
    except commands.errors.NoEntryPointError:
      pass

bot.run(os.environ["TOKEN"])
#this starts the bot using the private .env variable TOKEN
