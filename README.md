# Discord RSI Bot

This is a simple Discord bot that fetches RSI values for the SOL/USDT pair from Bybit at 1-hour intervals. When the bar closes, it calculates the RSI and sends an alert if the RSI is over 70 or below 30.

## Requirements

- Docker
- Python 3.11.3+
- Discord bot token

## Setup

1. Create a discord bot on the [Discord site](https://discord.com/developers/docs/intro).
2. Add the bot to your server and give it administrator permissions.
3. Clone the repository.
4. Edit a `config.py` file with your configuration values (you only need to set the Discord bot token, the rest of the values have default settings)
5. Build the Docker image from `Dockerfile`.
6. Run the Docker container.
7. Type the &monitor command in a channel where you want to receive RSI notifications from the bot. Type &monitor again to deactivate monitoring. You can also type &monitor with an integer value to set a different period than 14 for RSI calculation. For example:
   ```
   &monitor 20
   ```
   This starts monitoring and the RSI will be calculated with a period of 20 (the period will be automatically reduced if there is too little data).
   
## Configuration

Edit a `config.py` file in the root directory of the project with the following content:

```python
import os
import dotenv

dotenv.load_dotenv()

bot_token = os.getenv('BOT_TOKEN') #You can write you token there or in .env file in field "BOT_TOKEN"
interval = "60" #It's one hour interval, according to API you can change that to 1, 3, 5, 15, 30, 60, 120, 240, 360 and 720 minutes
period = "14" #RSI calculation period, it can be changed there or when running a &monitor command
```
