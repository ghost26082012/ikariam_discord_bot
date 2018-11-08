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

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user: # this is to prevent crashing via infinite loops
        return
      
#conditional branches for commands go below here
      
if message.content.startswith('!hello'): # a simple hello Command
    msg = 'Hello {0.author.mention}'.format(message)
    await client.send_message(message.channel, msg)
    
bot.run('NTA5NDg0MDc3ODkyNzYzNjQ4.DsYfWw.eveh1J-vwsXN3kZbXZyk2_gHu18')
