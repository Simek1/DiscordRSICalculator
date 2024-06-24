import discord
from discord.ext import commands
import dotenv
import os
import websockets
import json
from RSI_calculator import *


dotenv.load_dotenv()

monitoring = False

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
async def monitor(ctx, period = "14"):
    global monitoring
    if not monitoring:
        await ctx.channel.send("RSI monitoring has been turned on")
        monitoring = True
        if not period.isnumeric():
            ctx.channel.send("Period has to be a number")
        else:
            async with websockets.connect("wss://stream.bybit.com/v5/public/spot") as websocket:
                subscribe_message = {
                    "op": "subscribe",
                    "args": ["kline.60.SOLUSDT"]
                }
                await websocket.send(json.dumps(subscribe_message))
                
                async for message in websocket:
                    if not monitoring:
                        break
                    msg = json.loads(message)
                    if "data" in msg and msg["data"][0]["interval"] == "60":
                        await handle_data(msg, ctx.channel, int(period))
    else:
        await ctx.channel.senx("RSI monitoring has been turned off")
        monitoring = False

bot.run(bot_token)
