import discord
import subprocess
import asyncio
import os
import time
import re
from discord.ext import commands
bot = commands.Bot(command_prefix='git!', description='Warface Bot By Darsh!!')
bot.remove_command("help")
@bot.event
@asyncio.coroutine 
def on_ready():
  print('Logged in as')
  print(bot.user.name)
  print(bot.user.id)
  print('Bot Invite Link => https://discordapp.com/oauth2/authorize?&client_id='+bot.user.id+'&scope=bot&permissions=0' )
@bot.command()
@asyncio.coroutine 
def push(arg1):
    cmd = './git_push.sh {0}'.format(arg1)
    subprocess.call(cmd.split(),shell=False)
    with open ('push.log','r') as pl:
     plog=pl.read()
    yield from bot.say('```' + plog + '```')
@bot.command()
@asyncio.coroutine
def create(arg1, arg2):
    cmd = './create.sh {0} {1}'.format(arg1,arg2)
    subprocess.call(cmd.split(),shell=False)
    with open('cr.log','r') as cr:
      data=cr.read().replace('\n','')
    yield from bot.say('```' + data + '```')
bot.run('NDI4MTIwODUwOTE1NjU1Njgy.DZueIQ.iIGNwk4CQaKd5Qf-TNzcOBBZBnE')
