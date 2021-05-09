import discord
from discord.ext import commands
import random

class Meggy(commands.Cog):
  def __init__(self,bot):
    self.bot = bot

  @commands.command()
  async def quote(self,ctx):
    meggy_quotes = ["I know a guy..","Im gonna down her in ink!!!","Hey! Cheating is a legitimate strategy","woomy"]
    await ctx.send(random.choice(meggy_quotes))

  @commands.command()
  async def meggyemotes(self,ctx):
    meggy_emotes=self.bot.get_guild(825565680879403018).emojis
    await ctx.send(random.choice(meggy_emotes))

def setup(bot):
  bot.add_cog(Meggy(bot))


