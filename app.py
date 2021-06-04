import discord
import re

patterns = "(iam|i'm|i am|im)\s(\S*)\s?((\S*)?)"

client = discord.Client()

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    content = message.content.lower()
    botName = str(client.user)[:str(client.user).find("#")]
    filtered = re.findall(patterns, content)[0]

    if len(filtered) == 4:
        name = f"{filtered[1]} {filtered[2]}" if filtered[2] != "" else f"{filtered[1]}"
        await message.channel.send(f"Nice to meet you, {name}. I'm {botName}")


client.run("")