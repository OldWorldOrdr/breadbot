import discord
from discord.ext import commands

class Test1(commands.Cog):
    def __init__(self, client):
        self.client = client
    @discord.slash_command(name ="test1", description ="test1 test cmd")
    async def test1(self, ctx):
        await ctx.respond("test 1 worked")
def setup(client):
    client.add_cog(Test1(client))
