import discord
from discord.ext import commands

class Test2(commands.Cog):
    def __init__(self, client):
        self.client = client
    @discord.slash_command(name ="test2", description ="test1 test cmd")
    async def test1(self, ctx):
        await ctx.respond("test 2 worked")
def setup(client):
    client.add_cog(Test2(client))
