import discord; import os;

async def ChangeActivity(client,activity):
    if(activity == "playing"):
        await client.change_presence(activity=discord.Game(name=os.getenv('game-name')))
    elif(activity == "listening"):
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=os.getenv('song-name')))
    elif(activity == "watching"):
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=os.getenv('movie-name')))
    elif(activity == "streaming"):
        await client.change_presence(activity=discord.Streaming(name=os.getenv('twitch-name'), url=os.getenv('twitch-url')))