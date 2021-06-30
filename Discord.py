import discord
import time
from discord.ext import tasks

client = discord.Client()
named_tuple = time.localtime()  # get struct_time



@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@tasks.loop(seconds=0.1)
async def called_once_a_day():
    named_tuple = time.localtime()
    channel1 = client.get_channel(811294454170255412)
    channel2 = client.get_channel(811294481227448360)
    channel3 = client.get_channel(811294510587183154)
    channel4 = client.get_channel(811294535409336320)

    if str(time.strftime("%H:%M:%S", named_tuple)) == "23:59:59":
        await channel1.send(file=discord.File(r'/media/neoxide44/My Passport/Data/Terrarium 1/T1data' + str(time.strftime("%m-%d", named_tuple)) + '.csv'))
        await channel2.send(file=discord.File(r'/media/neoxide44/My Passport/Data/Terrarium 2/T2data' + str(time.strftime("%m-%d", named_tuple)) + '.csv'))
        await channel3.send(file=discord.File(r'/media/neoxide44/My Passport/Data/Terrarium 3/T3data' + str(time.strftime("%m-%d", named_tuple)) + '.csv'))
        await channel4.send(file=discord.File(r'/media/neoxide44/My Passport/Data/Terrarium 4/T4data' + str(time.strftime("%m-%d", named_tuple)) + '.csv'))
        time.sleep(86160)


@called_once_a_day.before_loop
async def before():
    await client.wait_until_ready()


called_once_a_day.start()
client.run("Nzg0MDU1MTQwNjU1MDM4NTA4.X8juQA.8OKJp8N6LZVXCzpdXz2JGHhfQ5Y")
