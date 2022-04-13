import discord, typing
from discord.ext import commands


class Owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def cog_check(self, ctx):
        return await self.bot.is_owner(ctx.author)

    @commands.command(brief="Adds Users from Mod List")
    async def addmod(self, ctx, *, user: typing.Optional[typing.Union[discord.User, int]] = None):
        if user is None:
            await ctx.send("Please provide a valid user")
        elif user:
            try:
                db = self.bot.DB
                collection = db["Mods"]
                user_id = user.id
                post = {"ModId": user_id}
                await collection.insert_one(post)
                await ctx.send(f"Added {user.id} as a mod.")
            except Exception as e:
                await ctx.send(e)

    @commands.command(brief="Removes Users from Mod List")
    async def removemod(self, ctx, *, user: typing.Union[discord.User, int] = None):
        if user is None:
            await ctx.send("Please provide a valid user")
        elif user:
            try:
                db = self.bot.DB
                collection = db["Mods"]
                user_id = user.id
                post = {"ModId": user_id}
                await collection.delete_one(post)
                await ctx.send(f"Removed {user.id} as a mod.")
            except Exception as e:
                await ctx.send(e)


async def setup(bot):
    await bot.add_cog(Owner(bot))
