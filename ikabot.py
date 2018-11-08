import discord
from discord.ext import commands

######################################################################
bot = commands.Bot(command_prefix='!', description='description here')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print('Enter your command')
                                  
@bot.command()
### Description of command goes here.
async def hello():
    await bot.say('Hello!!')

### Description of command goes here.
async def greet():
    await bot.say('Greeting!!')
######################################################################

bot.run('NTA5NDg0MDc3ODkyNzYzNjQ4.DsYfWw.eveh1J-vwsXN3kZbXZyk2_gHu18')
