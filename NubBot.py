# Import data files and variables

import random
import asyncio
import aiohttp
from discord import Game, Status
from discord.ext.commands import Bot
from discord import *
import time


# Bot Prefix

BOT_PREFIX = ("?")

# Bot "client" as Bot Object

client = Bot(command_prefix=BOT_PREFIX)

# Function to check for ID

def check_for_id(name):
    temp_list = []
    start = False
    end = False
    final_name = ""
    for i in name:
        temp_list.append(i)
    for j in range(len(temp_list)):
        if start == False :
            if temp_list[j] == "<":
                if temp_list[j+1] == "@":
                    start = True
        if start == True:
            if end == False:
                final_name += temp_list[j]
        if start == True:
            if temp_list[j] == ">":
                end = True
                break
    return final_name

# Function to get link

def get_link(entered_text):
    lowered_text = entered_text.lower()
    return_link = ""
    for i in lowered_text:
        if i == " ":
            return_link+= "-"
        else:
            return_link +=i
    return return_link


# Commands list: 8ball, clear, ptype, hello (and help default)



# 8ball Command 

@client.command(name='8ball',
                description="Answers a yes/no question",
                brief="Answers from the beyond",
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True)
async def eight_ball(context):
    possible_responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'Definitely',
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)


# clear Command

@client.command(description = "Clears 2-100 messages. Cannot delete messages older than 2 weeks", brief = "Clears messages", pass_context = True)
async def clear(ctx, number):
    if ctx.message.author.server_permissions.manage_messages:
        mgs = [] #Empty list to put all the messages in the log
        number = int(number) #Converting the amount of messages to delete to an integer
        async for x in client.logs_from(ctx.message.channel, limit = number):
           mgs.append(x)
        await client.delete_messages(mgs)
        mssg = await client.send_message(ctx.message.channel, "Deleted %s messages :smiley:" % number)
        await asyncio.sleep(1.5)
        await client.delete_message(mssg)
    else: 
        mssg = "You do not have permission to clear messages."
        await client.send_message(ctx.message.channel, mssg)


# ptype Command

@client.command(brief = "Sends typing condition", description = "Sends typing condition in the current channel for 10 seconds" , pass_context = True)
async def ptype(ctx):
    await client.send_typing(ctx.message.channel)


# hello Command

@client.command(name='hi',
                description="Greets the person",
                brief="Greets",
                aliases=['hey', 'hello'],
                pass_context=True)
async def hello(context):
    possible_responses = [
        'Hi',
        'Hello',
        'Hey',
        'Hmm.. Hullo',
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention + " :smile:")


# invite Command (creates invite link for current server)

@client.command(description = "Creates server invite. You can declare how many times the invite can be used, before expiring. Default is 3", brief = "Creates an invite link for the server", pass_context = True)
async def invite(ctx, maxuses = 3):
        inviteLinq = await client.create_invite(destination = ctx.message.channel, xkcd = True, max_uses = maxuses)
        await client.send_message(ctx.message.channel, inviteLinq)
        await client.send_message(ctx.message.channel, "\nThe Invite link can be used maximum ``" + str(maxuses) + "`` time(s). You can use ``?invite <max_uses>`` to create a new invite link. Default 3.")

 
# pokemon Command

@client.command(name='strategy',
                description="Sends the image of Pokemon with their best strategy to use",
                brief="Pokemon data and strategy",
                pass_context=True)
async def strategy(context):
    imageURL = "https://img.pokemondb.net/artwork/"+ get_link(context.message) + ".jpg"
    strategy_link = "https://www.smogon.com/dex/sm/pokemon/"+get_link
    mssg = "Strategy: " + strategy_link
    embed = Embed()
    embed.set_image(url = imageURL)
    await client.send_message(message.channel, embed = embed)
    await client.send_message(message.channel, mssg)        



#--------------------------- End of Commands


# Event


@client.event
async def on_message(message):
    print(str(message.author.id) + "  " + message.content)
    channel = message.channel
    lowered_message = message.content.lower()
    if lowered_message == 'cool' and message.author.id != "439432635735998475":
        await client.send_message(message.channel, 'Who is cool? Mention the person o.O')

        def check(msg):
            return msg.content.startswith('<@')

        message = await client.wait_for_message(author=message.author, check=check)
        name = message.content
        await client.send_message(message.channel, '{} is cool indeed'.format(name))



    if lowered_message == 'hoo' and message.author.id == "360854725744263169":
        imageURL = ["https://media.discordapp.net/attachments/420521281645969408/446001002521559041/owls-moving-their-heads.gif","https://media.discordapp.net/attachments/420521281645969408/446001333061943306/tenor.gif?width=346&height=300","https://media.discordapp.net/attachments/420521281645969408/446001509235294208/tumblr_m5s1w4rLz71r4zr2vo1_500.gif?width=400&height=216","https://media.discordapp.net/attachments/420521281645969408/446001692765454336/de4c41d5524d2594349011a49f3e859f.gif","https://media.discordapp.net/attachments/420521281645969408/446002979708076055/b316d2f1f5f49043236b8453eb75a6be.gif?width=215&height=300"]
        embed = Embed()
        embed.set_image(url = random.choice(imageURL))
        await client.send_message(message.channel, 'Hoo?')
        await client.send_message(message.channel, embed = embed)


    if (lowered_message == 'boo' or lowered_message == "boo!") and message.author.id == "391086228457521153":
        imageURL = ["https://media.discordapp.net/attachments/393640794181074955/441232120497831936/unknown.png","https://media.discordapp.net/attachments/393640794181074955/443010713032720384/unknown.png?width=400&height=145","https://media.discordapp.net/attachments/393640794181074955/443010946034696201/unknown.png?width=280&height=300","https://media.discordapp.net/attachments/393640794181074955/443011437288226816/unknown.png?width=271&height=300","https://media.discordapp.net/attachments/393640794181074955/443011628284510209/unknown.png?width=400&height=300", "https://media.discordapp.net/attachments/393640794181074955/443360673528021004/unknown.png?width=300&height=300"]
        embed = Embed()
        embed.set_image(url=random.choice(imageURL))
        await client.send_message(message.channel, 'BOO!!')
        await client.send_message(message.channel, embed = embed)


    if (lowered_message == 'meow') and message.author.id == "400442895087173643":
        imageURL = ["https://media.discordapp.net/attachments/402165631363055618/445924453730484235/image.jpg?width=400&height=225","https://media.discordapp.net/attachments/402165631363055618/445924486714228757/image.jpg?width=400&height=225","https://media.discordapp.net/attachments/402165631363055618/445924536626577409/image.gif","https://media.discordapp.net/attachments/402165631363055618/445924589734723586/image.png?width=400&height=226","https://media.discordapp.net/attachments/402165631363055618/445924632026021899/image.jpg?width=400&height=223","https://media.discordapp.net/attachments/402165631363055618/445924675818749952/image.gif?width=400&height=221","https://media.discordapp.net/attachments/402165631363055618/445924714859331606/image.gif?width=377&height=301","https://media.discordapp.net/attachments/402165631363055618/445924742235684874/image.jpg","https://media.discordapp.net/attachments/402165631363055618/445924762422870016/image.jpg?width=400&height=225","https://media.discordapp.net/attachments/402165631363055618/445924776113078284/image.jpg?width=400&height=300","https://media.discordapp.net/attachments/402165631363055618/445924787928170496/image.jpg?width=198&height=300","https://media.discordapp.net/attachments/402165631363055618/445924800381059073/image.jpg","https://media.discordapp.net/attachments/402165631363055618/445924823282221067/image.png?width=400&height=225","https://media.discordapp.net/attachments/402165631363055618/445924847449669634/image.jpg?width=400&height=224","https://media.discordapp.net/attachments/402165631363055618/445924889069879306/image.jpg","https://media.discordapp.net/attachments/402165631363055618/445924966018318356/image.gif?width=400&height=300","https://media.discordapp.net/attachments/402165631363055618/445925014613786624/image.png?width=329&height=300","https://media.discordapp.net/attachments/402165631363055618/445925047564238858/image.png?width=190&height=300","https://media.discordapp.net/attachments/402165631363055618/445925073929371648/image.png?width=281&height=300","https://media.discordapp.net/attachments/402165631363055618/445926009338986506/image.jpg?width=400&height=209"]
        embed = Embed()
        embed.set_image(url=random.choice(imageURL))
        await client.send_message(message.channel, 'Meow.')
        await client.send_message(message.channel, embed = embed)



    if lowered_message == 'test' and message.author.id != "439432635735998475":
        msg = "Pass :smiley: {}".format(message.author.mention)
        await client.send_message(message.channel, msg)


    if message.author.id == "362681379604922378" and (message.content.startswith("say") or message.content.startswith("Say")) and message.author.id != "439432635735998475":
        msg = message.content[3:]
        await client.delete_message(message)
        await client.send_message(message.channel, msg)



    if '[mid]' in lowered_message and message.author.id != "439432635735998475":
        li = lowered_message.split()
        for i in range(len(li)):
            if "[mid]" in li[i]:
                addition = li[i][5:12]
            await client.send_message(channel, 'Pokemon:   ' + "https://www.pokemonlegends.com/monster.php?mid="+addition + "  :wink: ")

    await client.process_commands(message)


# Default event during Bot Initiation

@client.event
async def on_ready():
    await client.change_presence(game=Game(name="Pokemon Legends"), status=Status("idle"))
    print("Logged in as " + client.user.name)


# List of servers bot is currently in. Updated every 10 mins

async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(600)
# Token

TOKEN = "NDM5NDMyNjM1NzM1OTk4NDc1.DcTFEA.Xqd1Z3RtUjeRc8tXuVWhml7O1ws" 


# Run Bot

client.loop.create_task(list_servers())
client.run(TOKEN)
