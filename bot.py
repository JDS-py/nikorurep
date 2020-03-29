import discord
import os
from discord.ext import commands
import discord.utils
import datetime
import asyncio
import json
import random
from random import randint
import youtube_dl
import socket
import re
import requests
from dhooks import Webhook, File
import sys
import logging
import time
from time import perf_counter


def get_prefix(bot, message):
    prefixes = ['y!', 'r$']

    if not message.guild:
        return '?'

    return commands.when_mentioned_or(*prefixes)(bot, message)

lapi_key = ""

client = commands.Bot(command_prefix = get_prefix)

client.remove_command("help")

now = datetime.datetime.now()

hook = Webhook('')

hostname = socket.gethostname()   

IPAddr = socket.gethostbyname(hostname)

@client.event
async def on_ready():
    activity = discord.Activity(name=f'{len(client.guilds)} servers | y!help', type=discord.ActivityType.watching)
    await client.change_presence(activity=activity)
    hook3.send(f'Logged Onto Nikoru Yamagashi {round(client.latency * 1000)}ms')
    hook3.send("Running version " + discord.__version__ + " of Discord.py")
    hook3.send(now.strftime("%Y-%m-%d %H:%M:%S"))
    hook3.send(hostname)
    hook3.send(IPAddr)
    print(client.user.name + ' has connected to Discord!')
    print('ID : [' + str(client.user.id) + ']')
    with open('logs/log.txt', 'a') as f:
        time = datetime.datetime.now()
        f.write(f'[log] {time} - {client.user.name} - {client.user.id} \n')

@client.event
async def on_resumed():
    print("Resumed connectivity!")

@client.command()
async def stats(ctx):
    embed = discord.Embed(title='Stats', color=0xfca7f5)
	
    embed.add_field(name="Latency", value=f"{round(client.latency * 1000)}ms", inline=False)
        
    embed.add_field(name='Server count', value=f'{len(client.guilds)}', inline=False)

    await ctx.send(embed=embed)

@client.command()
async def say(ctx, *, arg):
    await ctx.send(arg)
    

@client.command()
async def coinflip(ctx):
    choices = ["Tails", "Heads"]
    rancoin = random.choice(choices)
    await ctx.send(rancoin)

@client.command(pass_context=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    if ctx.author.guild_permissions.administrator:
        await member.kick(reason=reason)
        await ctx.send("Member has been kicked from the server.")
    else:
        await ctx.send("You don't have the permission to use this command.")


@client.command(name='setservername', aliases=['setguildname'])
async def setservername(ctx, *, arg):
    if ctx.author.guild_permissions.administrator:
        await ctx.message.delete()
        await ctx.guild.edit(name=arg)
    else:
        await ctx.message.delete()
        await ctx.send("You don't have the permission to use this command.")


@client.command(pass_context=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    if ctx.author.guild_permissions.administrator:
        await member.ban(reason=reason)
        await ctx.send("Member has been banned from the server.")
    else:
        await ctx.send("You don't have the permission to use this command.")
@client.command()
async def hug(ctx):
    yes = ["(づ｡◕‿‿◕｡)づ", "(っ˘̩╭╮˘̩)っ ", "(っಠ‿ಠ)っ ", "(づ￣ ³￣)づ "]
    hug = random.choice(yes)
    await ctx.send(hug)

def lookup_ip(ip_address):
	response = requests.get(f'https://api.ipdata.co/{ip_address}?api-key={lapi_key}')
	response_json = json.loads(response.text)
	return f'''
```
IP: {str(response_json['ip'])}

IP LOCATION INFO

City: {str(response_json['city'])}
Region: {str(response_json['region'])}
Region code: {str(response_json['region_code'])}
Country: {str(response_json['country_name'])}
Country code: {str(response_json['country_code'])}
Flag: {str(response_json['emoji_flag'])}
Continent: {str(response_json['continent_name'])}
Continent code: {str(response_json['continent_code'])}
Postal code: {str(response_json['postal'])}
Latitude: {str(response_json['latitude'])}
Longitude: {str(response_json['longitude'])}
Calling code: {str(response_json['calling_code'])}
Time zone: {str(response_json['time_zone']['name'])}
Time zone current time: {str(response_json['time_zone']['current_time'])}
Currency: {str(response_json['currency']['name'])}
Currency code: {str(response_json['currency']['code'])}
Currency symbol: {str(response_json['currency']['symbol'])}
Language: {str(response_json['languages'][0]['name'])}
Native language: {str(response_json['languages'][0]['native'])}


BASIC INFO

asn: {str(response_json['asn']['asn'])}
Name: {str(response_json['asn']['name'])}
Domain: {str(response_json['asn']['domain'])}
Route: {str(response_json['asn']['route'])}
Type: {str(response_json['asn']['type'])}


EXTRA INFO

TOR: {str(response_json['threat']['is_tor'])}
Proxy: {str(response_json['threat']['is_proxy'])}
Anonymous: {str(response_json['threat']['is_anonymous'])}
Abuser: {str(response_json['threat']['is_known_abuser'])}
Threat: {str(response_json['threat']['is_threat'])}
Bogon: {str(response_json['threat']['is_bogon'])}```'''

@client.command(name='geo', aliases=['ip'])
async def geo(ctx, *, ip):
    if ctx.author.guild_permissions.administrator:
	#above is the description for the command
	#runs the command
	    try:
            

		    ip_address = socket.gethostbyname(ip)
		#sends the info about the ip
		    await ctx.message.author.send(lookup_ip(ip_address))

	    except socket.gaierror:
		    await ctx.send('There is no such an ip or domain')

	    except:
		    await ctx.send('Error has occured!')
		    print('Error has occured!')
    else:
        await ctx.message.delete()
        await ctx.send("You don't have the permission to use this command.")

extensions = [
    'cogs.events',
    'cogs.owner',
    'cogs.cmds'
]

if __name__ == "__main__":
    for ext in extensions:
        client.load_extension(ext)





client.run("bot_token")
