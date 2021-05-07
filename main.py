import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.content.startswith("!meet") or message.content.startswith("-meet"):
        await message.channel.send(":loud_sound: https://meet.google.com/qqk-yosc-uok :loud_sound:")
    if message.content.startswith("!python") or message.content.startswith("-python"):
        await message.channel.send(":sparkling_heart: Python é um amorzinho :sparkling_heart:")

client.run(os.getenv("TOKEN"))
