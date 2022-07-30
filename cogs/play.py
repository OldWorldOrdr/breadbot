import discord
from discord.ext import commands

class Play(commands.Cog):
    def __init__(self, client):
        self.client = client
    @discord.slash_command(name ="play", description ="Play a song")
    async def play(self, ctx):
        await ctx.respond("Play what? Fortnite?")
def setup(client):
    client.add_cog(Play(client))
