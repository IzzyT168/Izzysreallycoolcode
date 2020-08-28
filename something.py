import discord 

import pw
TOKEN = pw.TOKEN

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content=='$p' :
        await message.channel.send('poggies')
    elif message.content == '$q' :
        await message.channel.send('Hey queen, I saw you post you hate men on your profile and I just want to say I totally agree, even though I am one (ugh). I do want to say that I am one of the good ones though, but I thoroughly condemn the rest of my gender. Btw your tits are pretty dope lol I hadn’t noticed until now')
    elif message.content == '$h' :
        await message.channel.send('I drink tons of horse cum to kill the demon in my stomach who constantly tells me not to drink horse cum. Do you know how hard it is to acquire a gallon of horse cum a day and also hold a job and a family? No you dont. Neither do I because I dont actually have a job or a family which makes acquiring horse cum a little harder and easier at the same time.')

client.run(TOKEN)