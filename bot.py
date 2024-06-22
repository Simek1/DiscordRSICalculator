import discord
import dotenv
import os
from discord.ext import tasks


dotenv.load_dotenv()

bot_token = os.getenv('BOT_TOKEN')
print(bot_token)

client = discord.Client(intents = discord.Intents.default())


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(bot_token)
