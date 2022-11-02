from ast import arg
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()


intents = discord.Intents().all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='$', intents=intents)

token = os.getenv('TOKEN')



@client.event
async def on_ready():
    print('[DONE]: We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    print(message.content)
    if message.author == client.user:
        return

    if message.content.startswith('$blabla'):
        user_id = "@752934151124025387"
        for i in range(1, 200):
            await message.channel.send(f"🤣😂🤣😂🤣🤣😂😂🤣😂😁")

@bot.command(name="test")
async def test(arg):
    print("zssssssssss")
    await arg.channel.send("bom bom")
    print(arg)

client.run(token)


