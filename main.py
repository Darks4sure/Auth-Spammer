import discord
from discord.ext import commands
from discord import app_commands


TOKEN = 'MTMzNjg0NDkwNzYyMDMzNTczMA.GWGZgT.w2SDX1n3I_3gohjUzyLijo1HU4H2DYh5cM6oOg'


intents = discord.Intents.all()


bot = commands.Bot(command_prefix="!", intents=intents)


@bot.tree.command(name="sendmessage")
async def send_message(interaction: discord.Interaction, message: str):
    
    if isinstance(interaction.channel, discord.DMChannel):
        
        await interaction.response.send_message(f"MSG BHEJDIYA LODU: {message}")
        await interaction.user.send(message)  
    else:
        
        await interaction.response.send_message(f"{message}")
        await interaction.channel.send(message)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    
    await bot.tree.sync()


bot.run(TOKEN)
