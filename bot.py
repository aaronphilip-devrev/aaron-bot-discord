import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import asyncio

# Load environment variables
load_dotenv()

# Bot setup
intents = discord.Intents.default()
intents.messages = True  # Allows the bot to read messages
intents.message_content = True  # Required for slash commands

# Update the bot initialization to use slash commands
bot = commands.Bot(command_prefix=commands.when_mentioned, intents=intents)

# Bot event: on_ready
@bot.event
async def on_ready():
    print(f"{bot.user.name} is online and connected!")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands with Discord.")
    except Exception as e:
        print(f"Failed to sync commands: {e}")

async def main():
    async with bot:
        for cog in ["add", "query","time"]:
            await bot.load_extension(f"commands.{cog}")
        await bot.start(os.getenv("DISCORD_BOT_TOKEN"))

# Run the bot
asyncio.run(main())
