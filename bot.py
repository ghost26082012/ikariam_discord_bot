# For hosting on Heroku we'll need to use the OS library to pull the Token 
# from the Enviroment Variables

import os, discord
from discord.ext.commands import Bot

# We'll need to substitute the Prefix for an Enviroment Variable
BOT_PREFIX = os.environ['!'] # -Prfix is need to declare a Command in discord ex: !pizza "!" being the Prefix
TOKEN = os.environ['NTA5NDg0MDc3ODkyNzYzNjQ4.DsYfWw.eveh1J-vwsXN3kZbXZyk2_gHu18'] # The token is also substituted for security reasons

client = Bot(command_prefix=BOT_PREFIX)

# this is an event which is triggered when something happens in Discord 
# in this case on_ready() is called when the bot logs on
#you can checkthe Discord API Documentaion for more event Functions 
# here: https://discordapp.com/developers

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name="Ikariam"))
    
# below this line you can put custom Functions

client.run(TOKEN)
