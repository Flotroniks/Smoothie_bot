import discord
from discord.ext import commands
import score


#client = discord.Client()
filestk = open('token.token', "r")
token = filestk.read()

client = commands.Bot(command_prefix='!')

@client.command(name="cryptohack",help="Show cryptohack score")
async def cryptohack(ctx):
        await ctx.send(score.cryptohack())

@client.command(name="rootme",help="Show root me score")
async def rootme(ctx):
        await ctx.send(score.rootme())

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    




    

    
client.run(token)