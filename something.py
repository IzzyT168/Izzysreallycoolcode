import discord 
import random
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
    if message.content=='$q' :
        await message.channel.send('Hey queen, I saw you post you hate men on your profile and I just want to say I totally agree, even though I am one (ugh). I do want to say that I am one of the good ones though, but I thoroughly condemn the rest of my gender. All these bad lovers not being able to make your orgasm haha imagine,just letting you know tough if it was ME, wou would be a goddam sprinkler rn')
    elif message.content == '$h' :
        await message.channel.send('I drink tons of horse cum to kill the demon in my stomach who constantly tells me not to drink horse cum. Do you know how hard it is to acquire a gallon of horse cum a day and also hold a job and a family? No you dont. Neither do I because I dont actually have a job or a family which makes acquiring horse cum a little harder and easier at the same time.')
    elif message.content=='$c' :
        await message.channel.send('Hello bitch, nice TITS ahahahahah milky millky milky baby thristy mommy baby want milk suck suck suck suck hahahaha stupid cunt give me those big udders you slut hahahaha tits tit titty me your caveman me use big titty for big bitty hahaha honk honk honk slut cunt mommy honk honk milky baby want more now honk honk honk pitter patter on those big mommy milkies hee hee hee haha haaaa haaaa cant stop the milk truck coming through honk honk all aboard the titty train hee hee wooo wooooooo honk honk honk!!!')