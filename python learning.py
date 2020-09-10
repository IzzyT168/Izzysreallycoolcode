#Variables:
#Containers for storing data values. A variable is created the moment you first assign a value to it. E.g 
x=5
y= "Izzy"
print(x)
print(y)
#Variables do not need to be declared with any partciular type, can change type after set. E.g
x = 6
x = "Izzy"
print (x)

#Variable names
#A variable name MUST start with the letter or the _ character.
#It cannot start with a number.
#It can only contain alpha-numeric character and underscores. (A-Z, 0-9 and _)
#Variable names are case sensntive. age, Age and AGE are all different. 

#Assigning value to multiple variables 
#Py allows to sign multiple varaibles to one line. E.g
x, y, z, = "Izzy1","Izzy2","Izzy3"
print (x)
print (y)
print (z)

#Also able to assign same value to multiple variables in one line. E.g
x = y = x = "Izzy"
print (x)
print (y)
print (z)






 @bot.command()
                            async def on_message(message):
                            if message.content.startswith('$ping') :
                            await ctx.send(f'pong! {round(client.latency * 1000)}ms')

