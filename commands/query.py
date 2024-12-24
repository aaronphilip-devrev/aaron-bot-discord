from discord.ext import commands
from discord import app_commands
from utils.api import post_to_api

class QueryCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="query", description="Query the knowledge base")
    @app_commands.describe(
        query="The query to search for"
    )
    async def query(self, interaction, query: str):
        """Query the knowledge base"""
        response = post_to_api("/query", {"query": query})
        answer_str = "\n".join(response["answer"])
        await interaction.response.send_message(answer_str)

async def setup(bot):
    await bot.add_cog(QueryCommand(bot))