# Import the discord.py library to interact with Discord
import discord
# Import the commands module from discord.ext to create bot commands
from discord.ext import commands
# Import the os module to access environment variables
import os 
# Load the token from the .env file
from dotenv import load_dotenv

load_dotenv() # Load the .env file
TOKEN = os.getenv('DISCORD_TOKEN') # Get the token from the .env file

# Enable the necessary intents (permissions for the bot to access certain events)
intents = discord.Intents.default()  # Start with default intents
intents.members = True  # Enable access to server member events (e.g., joining/leaving)
intents.message_content = True  # Enable access to message content (required for commands)

# Create the bot with a command prefix ("!") and the specified intents
bot = commands.Bot(command_prefix="!", intents=intents)

# Event: This runs when the bot has successfully connected to Discord
@bot.event
async def on_ready():
    # Print a message to the console to confirm the bot is online
    print(f'Logged in as {bot.user.name}')

# Command: This defines a command called "takemic"
@bot.command(name='takemic')
async def take_mic(ctx):
    # Check if the user who sent the command is in a voice channel
    if ctx.author.voice and ctx.author.voice.channel:
        # Get the voice channel the user is in
        channel = ctx.author.voice.channel
        # Get all members in that voice channel
        members = channel.members
        # Loop through each member in the channel
        for member in members:
            # Mute everyone except the person who sent the command
            if member != ctx.author:
                await member.edit(mute=True)
        # Send a message in the text channel confirming the action
        await ctx.send(f"{ctx.author.name} has the mic. Everyone else is muted.")
    else:
        # If the user is not in a voice channel, send an error message
        await ctx.send("You need to be in a voice channel to use this command.")

# Command: This defines a command called "releasemic"
@bot.command(name='releasemic')
async def release_mic(ctx):
    # Check if the user who sent the command is in a voice channel
    if ctx.author.voice and ctx.author.voice.channel:
        # Get the voice channel the user is in
        channel = ctx.author.voice.channel
        # Get all members in that voice channel
        members = channel.members
        # Loop through each member in the channel
        for member in members:
            # Unmute everyone in the channel
            await member.edit(mute=False)
        # Send a message in the text channel confirming the action
        await ctx.send("The mic has been released. Everyone is now unmuted.")
    else:
        # If the user is not in a voice channel, send an error message
        await ctx.send("You need to be in a voice channel to use this command.")

# Run the bot using the token
bot.run(TOKEN)