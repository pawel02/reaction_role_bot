import discord
from discord.utils import get
import os

client = discord.Client()

# Get the id of the verify channel
@client.event
async def on_ready():
    for guild in client.guilds:
        for channel in guild.text_channels:
            if str(channel).strip() == "verify":
                # id of the channel you have setup as your verify channel
                global verify_channel_id
                verify_channel_id = channel.id
                break

# Called when a reaction is added to a message
@client.event 
async def on_raw_reaction_add(reaction):
    # check if the reaction came from the correct channel
    if reaction.channel_id == verify_channel_id:
        # Check what emoji was reacted as
        if str(reaction.emoji) == "👍":
             # Add the user role
            verified_role = get(reaction.member.guild.roles, name = "verified")
            await reaction.member.add_roles(verified_role)

        # Add your other roles here

client.run(os.getenv("TOKEN")) 