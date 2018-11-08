import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def greet(ctx):
    await ctx.send(":smiley: :wave: Hello, there!")
    
# This tell the Interpreter that this function is a command for discord
@client.command(name="greet") # 'name' is literaly the name of the command
                              # this is what you type after the prefix
async def exampleCommand(): # commands can also take paramenters this example takes none
                            # but if it does have paramenter when the command is called it'll need
                            # them or else the command won't work
  
  await client.say("Hello there!!")

bot.run('NTA5NDg0MDc3ODkyNzYzNjQ4.DsYfWw.eveh1J-vwsXN3kZbXZyk2_gHu18')
