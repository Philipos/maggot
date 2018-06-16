#Maggot bot by Philip 

import discord 
from discord.ext import commands 
from discord.ext.commands import Bot 
import asyncio 

bot = commands.Bot(command_prefix="!") 

@bot.event 
async def on_ready():
    print ("Ready")  

    

@bot.command(pass_context=True)
async def ping(ctx): 
    await bot.say(":ping_pong: Pong!")  

@bot.command(pass_context=True)
async def pong(ctx): 
    await bot.say(":ping_pong: Ping!") 

@bot.command(pass_context=True)
async def info(ctx): 
    await bot.say("Bot made by Philip! :ok_hand:") 

@bot.command(pass_context=True)
async def check(ctx, user: discord.Member): 
    await bot.say("The users name is: {}".format(user.name))
    await bot.say("The users ID is: {}".format(user.id))
    await bot.say("The users status is: {}".format(user.status)) 
    await bot.say("The users highest role is: {}".format(user.top_role))
    await bot.say("The user joined at: {}".format(user.joined_at)) 

@bot.command(pass_context=True)
async def say(ctx, *args): 
    messg = ' '.join(args)
    await bot.delete_message(ctx.message)
    await bot.say(messg) 

@bot.command(pass_context=True)
async def amit(ctx): 
    await bot.say("FAT GUY") 

@bot.command(pass_context=True)
async def annonce(ctx, *args): 
    if ctx.message.author.server_permissions.administrator: 
        channel = bot.get_channel("457329765016403998")
        mesg = ' '.join(args)
        await bot.delete_message(ctx.message)
        return await bot.send_message(channel, mesg)  
    else: 
        await bot.say("Incorrect Permission")

@bot.event 
async def on_member_join(member): 
    role = discord.utils.get(member.server.roles, name="User") 
    await bot.add_roles(member, role)  

@bot.command(pass_context=True)
@commands.has_role('FATOT')
async def admin(ctx, user: discord.Member):
    role = discord.utils.get(user.server.roles, name="Admin")
    role2 = discord.utils.get(user.server.roles, name="User")
    await bot.add_roles(user, role) 
    await bot.remove_roles(user, role2)
    await bot.say("Given admin to: {}".format(user.name)) 

@bot.command(pass_context=True) 
@commands.has_role('FATOT')
async def unadmin(ctx, user: discord.Member):
    role = discord.utils.get(user.server.roles, name="Admin")
    role2 = discord.utils.get(user.server.roles, name="User")
    await bot.remove_roles(user, role) 
    await bot.add_roles(user, role2)
    await bot.say("Removed admin from: {}".format(user.name)) 

@bot.command(pass_context=True)
async def idiot(ctx):
    await bot.say("Answer: Amit is an idiot") 

@bot.command(pass_context=True)
async def sudo(ctx): 
    if ctx.message.author.server_permissions.administrator: 
        await bot.say("Has Permission")
    else: 
        await bot.say("ACCESS DENIED")












bot.run("NDU3MzE2NTE1MDEyOTM1NzAy.DgZqPg.BgrRK-g5WcwO_Eny7AE4wsvGfCM")
