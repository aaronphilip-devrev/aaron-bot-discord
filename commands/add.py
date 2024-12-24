from discord.ext import commands
from discord import app_commands
from utils.api import post_to_api

class AddCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="add", description="Add new content to the knowledge base")
    @app_commands.describe(
        content="The content to add",
        tags="Space-separated tags (optional)"
    )
    async def add(self, interaction, content: str, tags: str = ""):
        """Add new content to the knowledge base"""
        # Convert space-separated tags string to list
        tags_list = tags.split() if tags else []
        
        # Prepare data
        data = {"content": content, "tags": tags_list}

        # Send data to FastAPI endpoint
        response = post_to_api("/add", data)

        # Handle API response
        if "message" in response and response["message"] == "Entry added successfully!":
            await interaction.response.send_message(
                f"✅ Successfully added entry: **{content}**\nTags: {', '.join(tags_list)}"
            )
        else:
            error = response.get("error", "Unknown error occurred.")
            await interaction.response.send_message(
                f"❌ Failed to add entry. Error: {error}"
            )

async def setup(bot):
    await bot.add_cog(AddCommand(bot))
