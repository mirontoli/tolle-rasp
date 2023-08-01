import os
import random
import discord
from dotenv import load_dotenv
import urllib.request

with open('wisdom.txt', 'r', encoding='UTF-8') as txt_file:
    words_of_wisdom = txt_file.readlines()

with open('food.txt', 'r', encoding='UTF-8') as txt_file2:
    dishes = txt_file2.readlines()

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
print(f'token is {TOKEN}')
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
client = discord.Client(intents=intents)


headers = {
    'Accept': 'text/plain',
    'User-Agent': 'tolle-rasp (https://github.com/mirontoli/tolle-rasp)' #if not provided you'll get 403 Forbidden
    }

url = 'https://icanhazdadjoke.com/'
request = urllib.request.Request(url, headers=headers)
def fetch_random_joke():
    resp = urllib.request.urlopen(request)
    contents = resp.read().decode('UTF-8') # if not decoded the text is prepended with b'
    return contents

@client.event
async def on_ready():
    guild = client.guilds[0] # assumption, TODO find right guild
    members = '\n - '.join([member.name for member in guild.members])
    print(
        f'{client.user} has connected to Discord!\n'
        f'guild.name: {guild.name}\n'
        f'Guild members:\n - {members}'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        print(f'message.author: {message.author}')
        return
    response = "tmp"
    #print(f'message: {message}')
    print(f'message.content: {message.content}')
    if message.content.lower() == "hej":
        response = 'Hej på dig, du 👋👋!\nDu kan testa att skriva "visdom", "mat" eller "joke"'
    if message.content.lower() == 'visdom':
        response = random.choice(words_of_wisdom)
    if message.content.lower() == 'joke':
        #response = "You'll soon hear a joke"
        response = fetch_random_joke()
    if message.content.lower() == 'mat':
        dish = random.choice(dishes)
        response = f'{dish}\nGlöm inte att äta grönsaker'

    await message.channel.send(response)

        

client.run(TOKEN)
