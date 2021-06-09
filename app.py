import discord, re, random, os
from dotenv import load_dotenv

load_dotenv()

client = discord.Client()
TOKEN = os.getenv("DISCORD_TOKEN")

patterns = "(?:i\s*(?:m*|am|'m))\s(\w*)\s?(?:(\w*)?)"
replies = ["Hello", "Nice to meet you "]

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    content = message.content.lower()
    botName = str(client.user)[:str(client.user).find("#")]
    regexSearch = re.search(patterns, content)

    if regexSearch != None:
        regexGroup = regexSearch.groups()
        name = f"{regexGroup[0]} {regexGroup[1]}" if regexGroup[1] != "" else f"{regexGroup[0]}"
        reply = replies[random.randint(0, len(replies) - 1)]
        await message.channel.send(f"{reply}, {name}. I'm {botName}")


client.run(TOKEN)