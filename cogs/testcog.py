from discord.ext import commands

class TestCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def observer(self, context):
        await context.author.add_role("見学者")

    @commands.command()
    async def participant(self, context):
        await context.author.add_role("参加者")


def setup(bot):
    bot.add_cog(TestCog(bot))