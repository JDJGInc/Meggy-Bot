import discord
from discord.ext import commands
import typing
import random 

mod_list = [479766831494856724,455569859086909491,270932420532895745,361712001954611210]

class Mod(commands.Cog):
  def __init__(self,bot):
    self.bot = bot

  async def cog_check(self, ctx):
    return ctx.author.id in mod_list

  @commands.command(help="fetch invite details")
  async def fetch_invite(self,ctx,*invites:typing.Union[discord.Invite, str]):
    for x in invites:
      if isinstance(x,discord.Invite):
        if x.guild:
          image = x.guild.icon_url
          guild = x.guild
          guild_id = x.guild.id
        if x.guild is None:
          guild = "Group Chat"
          image = "https://i.imgur.com/pQS3jkI.png"
          guild_id = "Unknown"
        embed=discord.Embed(title=f"Invite for {guild}:",color=random.randint(0, 16777215))
        embed.set_author(name="Discord Invite Details:",icon_url=(image))
        embed.add_field(name="Inviter:",value=f"{x.inviter}")
        embed.add_field(name="User Count:",value=f"{x.approximate_member_count}")
        embed.add_field(name="Active User Count:",value=f"{x.approximate_presence_count}")
        embed.add_field(name="Invite Channel",value=f"{x.channel}")
        embed.set_footer(text=f"ID: {guild_id}\nInvite Code: {x.code}\nInvite Url: {x.url}")
        await ctx.send(embed=embed)
        
      if isinstance(x,str):
        await ctx.send(content=f"it returned as {x}. It couldn't fetch it :(")

def setup(bot):
  bot.add_cog(Mod(bot))
  