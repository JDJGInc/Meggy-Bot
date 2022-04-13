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

  @commands.command(brief = "shows a random meggy gif.")
  async def meggy_moment(self, ctx):
    meggy_moment =["https://c.tenor.com/bB4IW7ri8wwAAAAM/cheating-is-a-legitimate-strategy-playing-dirty.gif", "https://c.tenor.com/XKGDBCyyDwIAAAAM/smg4-salute.gif", "https://c.tenor.com/eN3XmlYns1QAAAAM/i-know-a-guy-ive-got-the-hookup.gif", "https://c.tenor.com/qbSI4uWB4PQAAAAM/im-gonna-drown-her-in-ink-meggy.gif"]
    await ctx.send(random.choice(meggy_moment))

async def setup(bot):
  await bot.add_cog(Meggy(bot))


