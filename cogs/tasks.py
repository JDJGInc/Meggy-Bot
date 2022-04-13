from discord.ext import commands, tasks
import discord
import asyncio


class Tasks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.status_task.start()

    @tasks.loop(seconds=40)
    async def status_task(self):
        await self.bot.change_presence(
            status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name="m*help")
        )
        await asyncio.sleep(40)

    @status_task.before_loop
    async def before_status_task(self):
        await self.bot.wait_until_ready()


async def setup(bot):
    await bot.add_cog(Tasks(bot))
