import discord
from discord.utils import get
import os

client = discord.Client()
# id of the channel you have setup as your verify channel
verify_channel_id = 0

@client.event
async def on_ready():
    # get the verify channel id
    for guild in client.guilds:
        for channel in guild.text_channels:
            if channel == "verify":
                verify_channel_id = channel.id
                break
                

# Called when a reaction is added to a message
@client.event
async def on_raw_reaction_add(reaction):
    # check if the reaction came from the correct channel
    if reaction.channel_id == verify_channel_id:
        # Check what emoji was reacted as
        if reaction.emoji == "👍":
            # Add the user role
            verfied_role = get(reaction.server.roles, "verified")
            await client.add_roles(reaction.user_id, verfied_role)
    
    
        
client.run(os.getenv("TOKEN"))
