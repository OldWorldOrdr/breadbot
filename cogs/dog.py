import discord
import json
from discord.ext import commands

class Play(commands.Cog):
    def __init__(self, client):
        self.client = client
    @discord.slash_command(name ="dog", description ="Dog picture")
    async def play(self, ctx):
        await ctx.respond("Pretend this text is a dog")
def setup(client):
    client.add_cog(Play(client))
