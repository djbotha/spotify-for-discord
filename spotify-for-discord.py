# These are the dependecies. The bot depends on these to function, hence the name. Please do not change these unless your adding to them, because they can break the bot.
import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import sys

# setup Bot
client = Bot(description="Dad Bot by iggnore", command_prefix=">", pm_help = False)

# open private key file
key_file = open('./discord_key.txt', 'r')
if not key_file:
	print('File discord_key.txt can\'t be found')
	sys.exit(0)

# read private key from file
api_key = key_file.read().splitlines()[0]
if not api_key:
	print('No API key in discord_key.txt')
	sys.exit(0)

# close private key file
key_file.close()
@client.event
async def on_ready():
	print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')

	print('--------')
	
	
	print('Use this link to invite {}:'.format(client.user.name))
	print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))

# Counts entries in #weekly-challenges
@client.event
async def on_message(message):
	# make a small announcement in the current channel
	if message.content.lower().startswith("i'm "):
		await client.send_message(message.channel, content='Hi {}, i\'m Dad'.format(message.content[4:]))
	

client.run(str(api_key)) # Send API key from opened file
