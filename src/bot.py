import os
import discord
from dotenv import load_dotenv


Is_running = True

load_dotenv()

#Getting Data from User
while Is_running:
    try:
        user_id = int(input("Enter user id: "))
        tries = int(input("Enter a number: "))
        joke = str(input("Enter a message: "))
        Is_running = False
    except ValueError:
        print("Enter a valid data")

#Initiating the bot
intents = discord.Intents().all()
client = discord.Client(intents=intents)
token = os.getenv('TOKEN')

@client.event
async def on_ready():
    print('[DONE]: We have logged in as {0.user}'.format(client))


@client.event
#Making Sure the bot doesn't reply to himself
async def on_message(message):
    print(message.content)
    if message.author == client.user:
        return

#Spamming a User
    if message.content.startswith('$spam'):
        for i in range(1, tries): 
            await message.channel.send(f"<@{user_id}> {joke} ")


client.run(token)


