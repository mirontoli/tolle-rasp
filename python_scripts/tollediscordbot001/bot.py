import os
import random
import discord
from dotenv import load_dotenv
import urllib.request
import openai

with open('wisdom.txt', 'r', encoding='UTF-8') as txt_file:
    words_of_wisdom = txt_file.readlines()

with open('food.txt', 'r', encoding='UTF-8') as txt_file2:
    dishes = txt_file2.readlines()

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
client = discord.Client(intents=intents)

#openai
openai.api_type = 'azure'
openai.api_base = 'https://smart-gpt.openai.azure.com/'
openai.api_version = '2023-03-15-preview'
openai.api_key = os.getenv('OPENAI_API_KEY')
messages = [{"role":"system","content":"Du är en robot som finns å servern mirongamers p discord. Du heter tollebot001. Du ska anpassa språket till barn. örklara saker enkelt, dra gärna äförelser fån vardagliga livet"}]

#tmp
#messages.append({"role":"user","content":"finns det liv påmars?"})

def ask_gpt(user_prompt):
    if len(user_prompt) < 5:
        return "for kort fraga"
    messages.append({"role":"user","content":user_prompt})

    response = openai.ChatCompletion.create(
            engine="Chat-GPT",
            messages=messages,
            temperature=0.7,
            max_tokens=800,
            top_p=0.95,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None)
    answer = response.choices[0].message.content
    messages.append({"role":"assistant","content":answer})
    return answer

#print('openai response:')
#print(response)


#jokes
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
        response = 'Hej på dig, du 👋👋!\nDu kan testa att skriva "visdom", "mat" eller "joke\nOm du vill prata med ChatGPT skriv "gpt " och din fråga'
    elif message.content.lower() == 'visdom':
        response = random.choice(words_of_wisdom)
    elif message.content.lower() == 'joke':
        #response = "You'll soon hear a joke"
        response = fetch_random_joke()
    elif message.content.lower() == 'mat':
        dish = random.choice(dishes)
        response = f'{dish}\nGlöm inte att äta grönsaker'
    elif message.content.lower().startswith('gpt '):
        # truncate 'gpt ' in the beginning
        user_prompt = message.content[4:]
        print(f'user_prompt: {user_prompt}')
        gpt_answer = ask_gpt(user_prompt)
        response = f'ChatGPT halsar:\n{gpt_answer}'

    await message.channel.send(response)

        

client.run(TOKEN)
