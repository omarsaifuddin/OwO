import json
import discord
from discord.ext import commands
import random
def owo_text(text: str) -> str:
    replacements = {
        "r": "w",
        "l": "w",
        "R": "W",
        "L": "W"
    }
    result = ""
    for char in text:
        result += replacements.get(char, char)
    return result

def leet_speak(text: str) -> str:
    replacements = {
        "a": "4",
        "e": "3",
        "l": "1",
        "o": "0",
        "s": "5",
        "t": "7"
    }
    result = ""
    for char in text:
        result += replacements.get(char.lower(), char)
    return result

def homestuck_talk(text: str) -> str:
    replacement_chart = {
        'a': '4',
        'b': '8',
        'c': '(',
        'd': '[)',
        'e': '3',
        'f': 'ph',
        'g': '9',
        'h': '#',
        'i': '1',
        'j': 'j',
        'k': '|<',
        'l': '1',
        'm': '|\\|',
        'n': '/\\/',
        'o': '0',
        'p': 'p',
        'q': 'q',
        'r': 'r',
        's': '5',
        't': '7',
        'u': '|_|',
        'v': '\\/',
        'w': '\\/\\/',
        'x': 'x',
        'y': 'y',
        'z': 'z',
        ' ': ' ',
    }
    
    glub_sounds = {
        'b': 'bl',
        'd': 'dl',
        'f': 'fl',
        'g': 'gl',
        'k': 'kl',
        'l': 'll',
        'm': 'ml',
        'n': 'nl',
        'p': 'pl',
        'r': 'rl',
        's': 'sl',
        't': 'tl',
        'v': 'vl',
    }
    
    glub_glub_sounds = {
        'c': 'cc',
        'j': 'jj',
        'q': 'qq',
        'x': 'xx',
        'z': 'zz',
    }
    
    replacement_chart.update(glub_sounds)
    replacement_chart.update(glub_glub_sounds)
    
    troll_text = []
    current_case = "upper"
    
    for char in text:
        if char.isupper():
            current_case = "upper"
        elif char.islower():
            current_case = "lower"
        
        if char.lower() in replacement_chart:
            if random.random() < 0.1:  # add glub glub sound with 10% chance
                replacement_char = replacement_chart[char.lower()] + 'glub'
            else:
                replacement_char = replacement_chart[char.lower()]
            
            if replacement_char.isalpha():
                if current_case == "upper":
                    replacement_char = replacement_char.upper()
                elif current_case == "lower":
                    replacement_char = replacement_char.lower()
                
            troll_text.append(replacement_char)
        else:
            troll_text.append(char)
    
    return ''.join(troll_text)

with open("config.json") as f:
    config = json.load(f)

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to Discord!")

@bot.command(name="owo")
async def owo(ctx, *, text: str):
    translated_text = owo_text(text)
    await ctx.send(translated_text)

@bot.command(name="leet")
async def leet(ctx, *, text: str):
    translated_text = leet_speak(text)
    await ctx.send(translated_text)

@bot.command(name="homestuck")
async def homestuck(ctx, *, text: str):
    troll_text = homestuck_talk(text)
    await ctx.send(troll_text)

bot.run(config["bot_token"])