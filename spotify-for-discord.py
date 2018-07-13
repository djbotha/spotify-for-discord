# These are the dependecies. The bot depends on these to function, hence the name. Please do not change these unless your adding to them, because they can break the bot.
import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import sys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# get spotify credentials from environment variables
client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# setup Bot
client = Bot(description="Spotify Searcher by iggnore", command_prefix=".", pm_help = False)

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
	return await client.change_presence(game=discord.Game(name='sick tracks 🎸')) #This is buggy, let us know if it doesn't work.

# Counts entries in #weekly-challenges
@client.event
async def on_message(message):
	if message.content.startswith('.song '):
		results = sp.search(q=message.content[6:], limit=1, type='track') 
		url = 'https://open.spotify.com/track/{}'.format(results['tracks']['items'][0]['id'])
		await client.send_message(message.channel, content=url)
	elif message.content.startswith('.track '):
		results = sp.search(q=message.content[7:], limit=1, type='track') 
		url = 'https://open.spotify.com/track/{}'.format(results['tracks']['items'][0]['id'])
		await client.send_message(message.channel, content=url)
	elif message.content.startswith('.album '):
		results = sp.search(q=message.content[7:], limit=1, type='album') 
		url = 'https://open.spotify.com/album/{}'.format(results['albums']['items'][0]['id'])
		await client.send_message(message.channel, content=url)
	elif message.content.startswith('.artist '):
		results = sp.search(q=message.content[8:], limit=1, type='artist') 
		url = 'https://open.spotify.com/artist/{}'.format(results['artists']['items'][0]['id'])
		await client.send_message(message.channel, content=url)

async def dontcrash():
    channels = client.get_all_channels()
    asyncio.sleep(45)

client.loop.create_task(dontcrash())
client.run(str(api_key)) # Send API key from opened file
