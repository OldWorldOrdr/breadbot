import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

client = discord.Bot(debug_guilds=[902399321260052551])
cogs_list = [
    'test1',
    'test2',
]

for cog in cogs_list:
    client.load_extension(f'cogs.{cog}')
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)
