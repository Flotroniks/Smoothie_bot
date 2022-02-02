import discord
from discord.ext import commands
import score


#client = discord.Client()
filestk = open('token.token', "r")
token = filestk.read()

client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))



@client.command()
async def rootme(ctx):
           
        await ctx.send(score.rootme())
    

    
client.run(token)