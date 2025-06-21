from discord.ext import commands
from discord import app_commands, Interaction
from utils.groq import get_idea
from datetime import datetime

# Simple log with timestamp
def log(msg):
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}] {msg}")

class IdeaCommands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        log("✅ IdeaCommands cog loaded")

    @app_commands.command(name="3d_iso", description="Generate a 3D isometric art concept")
    async def iso_idea(self, interaction: Interaction):
        log(f"🔧 Command received: /3d_iso from {interaction.user}")
        await interaction.response.defer(thinking=True)
        prompt = "Generate a creative concept for 3D isometric art (provide only name and brief description)"
        log("📤 Sending request to Groq API...")
        log(f"📝 Prompt: {prompt[:100]}{'...' if len(prompt) > 100 else ''}")
        idea, tokens = get_idea(prompt)
        log(f"📄 Response: {idea[:150]}{'...' if len(idea) > 150 else ''}")
        log(f"📊 Tokens used: {tokens}")
        await interaction.followup.send(f"🎨 **Isometric Art Concept**:\n{idea}")

    @app_commands.command(name="3d_block", description="Generate a 3D city block concept")
    async def block_idea(self, interaction: Interaction):
        log(f"🔧 Command received: /3d_block from {interaction.user}")
        await interaction.response.defer(thinking=True)
        prompt = "Create a concept for a 3D city block with buildings and streets (provide only name and brief description)"
        log("📤 Sending request to Groq API...")
        log(f"📝 Prompt: {prompt[:100]}{'...' if len(prompt) > 100 else ''}")
        idea, tokens = get_idea(prompt)
        log(f"📄 Response: {idea[:150]}{'...' if len(idea) > 150 else ''}")
        log(f"📊 Tokens used: {tokens}")
        await interaction.followup.send(f"🏙️ **City Block Concept**:\n{idea}")

    @app_commands.command(name="3d_building", description="Generate a 3D building concept")
    async def building_idea(self, interaction: Interaction):
        log(f"🔧 Command received: /3d_building from {interaction.user}")
        await interaction.response.defer(thinking=True)
        prompt = "Design a creative 3D building concept from any architectural style (provide only name and brief description)"
        log("📤 Sending request to Groq API...")
        log(f"📝 Prompt: {prompt[:100]}{'...' if len(prompt) > 100 else ''}")
        idea, tokens = get_idea(prompt)
        log(f"📄 Response: {idea[:150]}{'...' if len(idea) > 150 else ''}")
        log(f"📊 Tokens used: {tokens}")
        await interaction.followup.send(f"🏛️ **Building Concept**:\n{idea}")

async def setup(bot: commands.Bot):
    await bot.add_cog(IdeaCommands(bot))
