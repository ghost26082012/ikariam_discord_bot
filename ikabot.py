import discord
from discord.ext import commands

######################################################################
bot = commands.Bot(command_prefix='!', description='description here')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print('Enter your command')

async def on_message(message):
    if message.content.startswith("!greet"):
        userID = message.author.id
        await bot.send_message(message.channel, "Hello there !!!")
    if message.content.startswith("!help"):
        userID = message.author.id
        await bot.send_message(message.channel, "Help !!!")
                                  
@bot.command()
### Description of command goes here.
async def hello():
    await bot.say('Hello')
                                 
######################################################################

bot.run('NTA5NDg0MDc3ODkyNzYzNjQ4.DsYfWw.eveh1J-vwsXN3kZbXZyk2_gHu18')
