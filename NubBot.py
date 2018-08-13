# Import data files and variables

import random
import asyncio
import aiohttp
from discord import Game, Status
from discord.ext.commands import Bot
from discord import *
import time
import os
from itertools import cycle


#Bot Token

TOKEN = (os.environ.get('TOKEN'))

# Bot Prefix

BOT_PREFIX = ("?")

# Bot "client" as Bot Object

client = Bot(command_prefix=BOT_PREFIX)

#Removing default help command

#client.remove_command("help")

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


# ping Command

@client.command(brief = "Calculates the ping", description = "Calculates and sends ping between bot and user", pass_context=True)
async def ping(ctx):
    before = int(round(time.time() * 1000))
    message = await client.send_message(ctx.message.channel,"Pong!")
    after = int(round(time.time() * 1000))
    ping = (after - before)
    await client.edit_message(message, "Pong!  `"+str(ping)+ "ms`")


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
async def strategy(context, pokemon):
    imageURL = "https://img.pokemondb.net/artwork/"+ get_link(pokemon) + ".jpg"
    strategy_link = "https://www.smogon.com/dex/sm/pokemon/"+get_link(pokemon)
    mssg = "Strategy: " + strategy_link
    embed = Embed()
    embed.set_image(url = imageURL)
    await client.send_message(context.message.channel, embed = embed)
    await client.send_message(context.message.channel, mssg)        


# serstatus Command

@client.command(brief="Shows server status", description= "Shows the number of users in the server", pass_context=True)
async def serstatus(ctx):
    x = "There are currently `"+str(len(ctx.message.server.members)) +"` users in the server. Do `?ping` to get the server ping."
    await client.send_message(ctx.message.channel, x)


# avatar Command

@client.command(brief= "Shows avatar", description = "Shows a given member's avatar (default is user)", pass_context= True)
async def avatar(ctx, user= message.user.ID)
    if user!="":
        name = check_for_id(user)
        url = name.avatar_url()
        embed=Embed()
        embed.set_image(url = url)
        await client.send_message(ctx.message.channel, embed= embed)


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

        
    if (lowered_message == 'bleh') and message.author.id == "391086228457521153":
        imageURL = ["https://images-ext-1.discordapp.net/external/LVj84zA8BFKDHu6h6A1jQ5Y8CVcySt5SzNoLbsMyZkA/https/cdn.discordapp.com/attachments/396733003834851358/447460536787927040/hug-S1UJ_Jncf.gif","https://images-ext-1.discordapp.net/external/PyIQYB5FsXbRJfd3I6qmNTgAqKsxOMtgK1qQNIULtUw/%3Ffit%3D780%252C330%26ssl%3D1/https/i0.wp.com/mindoverblown.com/wp-content/uploads/2017/07/Anime-characters-perfect-in-a-different-show-feat.jpg?width=400&height=170","https://pa1.narvii.com/6523/8c453e4cb3df1bbe545c177323ede4e4156dfadd_hq.gif","https://78.media.tumblr.com/6dac8a095c475639b589cbe7fd583eaa/tumblr_ot5y5r3B391w7cvmoo1_500.gif","https://78.media.tumblr.com/68b1b25484ea9646062c7b4f587b6344/tumblr_p33p2ksSrd1wn2b96o1_500.gif","https://images-ext-1.discordapp.net/external/ZmbO-vBxnxxExaUqbsn7ByIp9ENlRJv7Ff9fGq9S-GY/https/steamusercontent-a.akamaihd.net/ugc/156899501292204029/EDAC908524C0B27D938F5C57844AD009830CDE72/"]#""]
        embed = Embed()
        embed.set_image(url=random.choice(imageURL))
        await client.send_message(message.channel, 'blehh..')
        await client.send_message(message.channel, embed = embed)
        
        
    if (lowered_message == 'meow') and message.author.id == "400442895087173643":
        imageURL = ["https://media.discordapp.net/attachments/402165631363055618/445924453730484235/image.jpg?width=400&height=225","https://media.discordapp.net/attachments/402165631363055618/445924486714228757/image.jpg?width=400&height=225","https://media.discordapp.net/attachments/402165631363055618/445924536626577409/image.gif","https://media.discordapp.net/attachments/402165631363055618/445924589734723586/image.png?width=400&height=226","https://media.discordapp.net/attachments/402165631363055618/445924632026021899/image.jpg?width=400&height=223","https://media.discordapp.net/attachments/402165631363055618/445924675818749952/image.gif?width=400&height=221","https://media.discordapp.net/attachments/402165631363055618/445924714859331606/image.gif?width=377&height=301","https://media.discordapp.net/attachments/402165631363055618/445924742235684874/image.jpg","https://media.discordapp.net/attachments/402165631363055618/445924762422870016/image.jpg?width=400&height=225","https://media.discordapp.net/attachments/402165631363055618/445924776113078284/image.jpg?width=400&height=300","https://media.discordapp.net/attachments/402165631363055618/445924787928170496/image.jpg?width=198&height=300","https://media.discordapp.net/attachments/402165631363055618/445924800381059073/image.jpg","https://media.discordapp.net/attachments/402165631363055618/445924823282221067/image.png?width=400&height=225","https://media.discordapp.net/attachments/402165631363055618/445924847449669634/image.jpg?width=400&height=224","https://media.discordapp.net/attachments/402165631363055618/445924889069879306/image.jpg","https://media.discordapp.net/attachments/402165631363055618/445924966018318356/image.gif?width=400&height=300","https://media.discordapp.net/attachments/402165631363055618/445925014613786624/image.png?width=329&height=300","https://media.discordapp.net/attachments/402165631363055618/445925047564238858/image.png?width=190&height=300","https://media.discordapp.net/attachments/402165631363055618/445925073929371648/image.png?width=281&height=300","https://media.discordapp.net/attachments/402165631363055618/445926009338986506/image.jpg?width=400&height=209"]
        embed = Embed()
        embed.set_image(url=random.choice(imageURL))
        await client.send_message(message.channel, 'Meow.')
        await client.send_message(message.channel, embed = embed)

        
    if (lowered_message == 'requip') and message.author.id == "400442895087173643":
        imageURL = ["https://media.discordapp.net/attachments/402165631363055618/477772573493690368/image.jpg?width=275&height=410","https://media.discordapp.net/attachments/402165631363055618/477772610071953438/image.jpg?width=440&height=410", "https://media.discordapp.net/attachments/402165631363055618/477772669249388544/image.png?width=316&height=301","https://media.discordapp.net/attachments/402165631363055618/477772704527810560/image.png?width=283&height=300","https://media.discordapp.net/attachments/402165631363055618/477772738313060353/image.png?width=226&height=300","https://media.discordapp.net/attachments/402165631363055618/477772782470430721/image.jpg?width=253&height=300","https://media.discordapp.net/attachments/402165631363055618/477772825042878465/image.jpg?width=259&height=300","https://media.discordapp.net/attachments/402165631363055618/477772865933017089/image.jpg?width=333&height=300","https://media.discordapp.net/attachments/402165631363055618/477772903698399233/image.jpg?width=355&height=411","https://media.discordapp.net/attachments/402165631363055618/477772944752246784/image.png?width=273&height=300","https://media.discordapp.net/attachments/402165631363055618/477772976754917386/image.png?width=362&height=410","https://media.discordapp.net/attachments/402165631363055618/477773003455725568/image.jpg?width=291&height=301","https://media.discordapp.net/attachments/402165631363055618/477773042593038336/image.jpg?width=276&height=410","https://media.discordapp.net/attachments/402165631363055618/477773066899030026/image.png?width=312&height=411","https://media.discordapp.net/attachments/402165631363055618/477773094522716161/image.png?width=350&height=301","https://media.discordapp.net/attachments/402165631363055618/477773118497357836/image.jpg?width=347&height=410","https://media.discordapp.net/attachments/402165631363055618/477773157734940672/image.jpg?width=400&height=246","https://media.discordapp.net/attachments/402165631363055618/477773187292332055/image.png?width=400&height=221","https://media.discordapp.net/attachments/402165631363055618/477773268216971265/image.jpg","https://media.discordapp.net/attachments/402165631363055618/477773297656791051/image.jpg?width=400&height=225","https://media.discordapp.net/attachments/402165631363055618/477773319567966208/image.jpg","https://media.discordapp.net/attachments/402165631363055618/477773337859457025/image.jpg?width=400&height=238","https://media.discordapp.net/attachments/402165631363055618/477773357350256640/image.png?width=375&height=410","https://media.discordapp.net/attachments/402165631363055618/477773369526321152/image.png?width=300&height=300","https://media.discordapp.net/attachments/402165631363055618/477773403479343104/image.jpg?width=287&height=410","https://media.discordapp.net/attachments/402165631363055618/477773671323271175/image.jpg?width=300&height=300"]
        embed = Embed()
        embed.set_image(url=random.choice(imageURL))
        await client.send_message(message.channel, 'Requip!')
        await client.send_message(message.channel, embed = embed)

        
    if (lowered_message == "howl") and message.author.id == "439988331871338497":
        imageURL = ["https://media.discordapp.net/attachments/464042876502802432/468523117363462160/Cute-Wolf-cute-wolf-zone-16877321-641-479.jpg?width=400&height=299","https://media.discordapp.net/attachments/464042876502802432/468523117363462164/images_4.jpeg","https://media.discordapp.net/attachments/464042876502802432/468523117854064640/images_5.jpeg","https://media.discordapp.net/attachments/464042876502802432/468523117854064641/e5f9a899ce639ded114d0bb84be7c3c0-wolf-puppies-baby-wolves.jpg?width=398&height=301","https://media.discordapp.net/attachments/464042876502802432/468523118378614794/images_1.jpeg","https://media.discordapp.net/attachments/464042876502802432/468523118378614795/images_3.jpeg","https://media.discordapp.net/attachments/464042876502802432/468523118378614796/Running-wolf-1920x1200.jpg?width=400&height=250","https://media.discordapp.net/attachments/464042876502802432/468523119171207178/images_2.jpeg","https://media.discordapp.net/attachments/464042876502802432/478242888619393034/images_7.jpeg","https://media.discordapp.net/attachments/464042876502802432/478242888619393036/wolf-alamy.jpg?width=400&height=300","https://media.discordapp.net/attachments/464042876502802432/478242889126772747/WolfHowl.jpg?width=304&height=301","https://media.discordapp.net/attachments/464042876502802432/478242889592209418/636670335232345710-AP-Wolf-Relocation-39408799.jpeg?width=400&height=301", "https://media.discordapp.net/attachments/464042876502802432/478242889592209419/gray-wolf-snow.ngsversion.1466004545814.adapt.945.1.jpg?width=400&height=225","https://media.discordapp.net/attachments/464042876502802432/478242890188062730/tumblr_o1hn1e01xP1qbxi45o2_500.gif?width=400&height=241","https://media.discordapp.net/attachments/464042876502802432/478242890808688671/tumblr_o0cq2e7pF31s5uok8o1_400.gif"]
        embed = Embed()
        embed.set_image(url=random.choice(imageURL))
        await client.send_message(message.channel, 'Howll!!')
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

#@client.event
#async def on_ready():
#    await client.change_presence(game=Game(name="Pokemon Legends"))

# Magic

#Statuses

status_ = ["dnd","online","idle"]

async def change_status():
    await client.wait_until_ready()
    msgs = cycle(status_)
    
    while not client.is_closed:
        current_status = next(msgs)
        await client.change_presence(game = Game(name = "Pokemon Legends"), status = current_status)
        await asyncio.sleep(2)
 

# List of servers bot is currently in. Updated every 10 mins

async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(600)
        
# Run Bot

client.loop.create_task(list_servers())
client.loop.create_task(change_status())
client.run(TOKEN)
