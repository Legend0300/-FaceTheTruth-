# bot.py
import os
import random
import discord
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv("GUILD2")
GUILD2 = os.getenv("GUILD2")

# client = discord.Client()

# @client.event
# async def on_ready():
#     print(f'{client.user.name} has connected to Discord!')

# @client.event
# async def on_member_join(member):
#     await member.create_dm()
#     await member.dm_channel.send(
#         f'Hi {member.name}, welcome to my Discord server!'
#     )

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    for guild2 in client.guilds:
        if guild2.name == GUILD2:
            break
    # print(f"{client.user} is connected to discord")
    # print(f"The guild name is: {guild} and id is: {guild.id}")


    # members = '\n - '.join([member.name for member in guild.members])
    # print(f'Guild Members:\n - {members}')
    print(
    f'{client.user} is connected to the following guild:\n'
    f'{guild.name}(id: {guild.id})\n'
    )

@client.event
async def on_member_join(member):
    await member.send(f'Hi {member.name}, welcome to my Discord server!')

@client.event
async def on_message(message):
    print(message.author.display_name)
    if message.author == client.user:
        return
    Fortnite_roast = [
        f"get good at the game 0 PR and 0 Earning player {message.author.mention}",
        (
            f"dogshit player get a life! {message.author.mention}"
        ),
        f"{message.author.mention} You have two parts of brain, 'left' and 'right'. In the left side, there's nothing right. In the right side, there's nothing left." ,
        f"{message.author.mention} Do you wanna lose ten pounds of ugly fat? Cut off your head!" ,
        f"{message.author.mention} Shock me, say something intelligent." ,
        f"{message.author.mention} Your parents hated you so much you bath toys were an iron and a toaster"
    ]
    if message.content == "I like Fortnite":
        response = random.choice(Fortnite_roast)
        await message.channel.send(response)
    if message.author != client.user:
        if message.author.display_name == "Legend":
            response = random.choice(Fortnite_roast)
            await message.channel.send("Hi Legend!")
        elif message.author.display_name == "BARRY":
            response = random.choice(Fortnite_roast)
            await message.channel.send("144Hz wala bot Barry")
        elif message.author.display_name == "Assasin":
            response = random.choice(Fortnite_roast)
            await message.channel.send("1000 Arena points wala bot")
        elif message.author.display_name == "":
            response = random.choice(Fortnite_roast)
            await message.channel.send("0 mechanics wala controller player")
        elif message.author.display_name == "i dont take anti depressants":
            await message.channel.send("Shut up despessed kid")
        elif message.author.display_name == "👑𝐊𝟗 𝐃𝐫𝐚𝐠𝐨𝐧":
            await message.channel.send("weeb 0w0")    
        else:
            response = random.choice(Fortnite_roast)
            await message.channel.send(response)
        

client.run(TOKEN)
