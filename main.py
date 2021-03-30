import os
#uses the os to grab .env variables(later with os.environ) - it's fairly safe
import discord
#the python wrapper I use(it's actually discord.py but the python program treats it as discord)
from discord.ext import commands
#using commands extenstion trust me without this it would be much more of a pain

bot = commands.Bot(command_prefix=commands.when_mentioned_or("m*"),intents = discord.Intents.all()
#defines the bot object without it no bot access
#intents refers to stuff discord uses(just look up it's meaning)

@bot.listen()
async def on_ready():
  print("Bot is Ready")
  print(f"Logged in as {bot.user}")
  print(f"Id: {bot.user.id}")

#when the boot boots up it will print the bot is ready then the name and then id.

for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    try:
      bot.load_extension(f'cogs.{filename[:-3]}')
      #helps organization commands lol
    except commands.errors.NoEntryPointError:
      pass

bot.run(os.environ["TOKEN"])
#this starts the bot using the private .env variable TOKEN