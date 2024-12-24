from discord.ext import commands
from discord import app_commands
from utils.api import post_to_api

class TimeCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="time", description="Get the time at which you mentioned something")
    @app_commands.describe(
        query="The time at which you mentioned something"
    )
    async def time(self, interaction, query: str):
        """Get the time at which you mentioned something"""
        response = post_to_api("/time", {"query": query})
        answer_str = response["answer"]
        
        # Remove curly braces and split by comma
        answer_str = answer_str.strip('{}').split(',')
        # Join with newlines
        answer_str = "\n".join(answer_str)
        await interaction.response.send_message(answer_str)

async def setup(bot):
    await bot.add_cog(TimeCommand(bot))