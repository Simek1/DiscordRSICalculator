import discord
from discord.ext import commands
import dotenv
import os
import asyncio
from RSI_calculator import *


dotenv.load_dotenv()

monitoring = []

bot_token = os.getenv('BOT_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
intents.guild_messages = True
intents.guilds = True

bot = commands.Bot(command_prefix='&', intents = intents)


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command()
async def monitor(ctx, timer = "60"):
    if not timer.isnumeric():
        ctx.send("Timer has to be a number (sec)")
    else:
        print(f"Monitoring command has been used on {ctx.channel.id}")
        if ctx.channel.id in monitoring:
            await ctx.send("RSI Monitoring has been turned off on this channel")
            monitoring.remove(ctx.channel.id)
        else:
            await ctx.send("RSI Monitoring has been turned on on this channel")
            monitoring.append(ctx.channel.id)
            await get_RSI(ctx.channel, int(timer))

async def get_RSI(channel, timer):
    channel_id = channel.id
    while channel_id in monitoring:
        data = get_data()
        RSI = calculate_RSI(data)

        if RSI > 70:
            await channel.send(f"RSI is higher than 70! Current RSI: {RSI}")
        elif RSI < 30:
            await channel.send(f"RSI is lower than 30! Current RSI: {RSI}")
        else:
            await channel.send(f"(TEST) Current RSI: {RSI}")
        await asyncio.sleep(timer)

bot.run(bot_token)
