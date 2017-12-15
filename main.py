import discord
from discord.ext import commands
import random

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix='Insert Token here', description=description, owner_id=372808172051759104)
embed = discord.Embed(colour = discord.Colour(0x00c3ff))
bot.remove_command("help")

@bot.event
async def on_ready():
	print('Logged in as')
	print(bot.user.name)
	print(bot.user.id)
	print(bot.user.avatar_url)
	print('------')
	await bot.change_presence(game=discord.Game(name='> neko!help', type = 3))

@bot.command()
@commands.has_permissions(manage_messages=True)
async def purgeall(ctx, *args):
    """A Buk Fie"""
    await ctx.channel.purge(limit=999)
	
@bot.command()
@commands.is_owner()
async def bot_info(ctx, **colour):
	embed.set_thumbnail(url=bot.user.avatar_url)
	embed.set_author(name="Neko Bot", icon_url=bot.user.avatar_url)
	embed.set_footer(text="Made by Ryu Tsubane© 2017", icon_url=bot.user.avatar_url)
	embed.add_field(name="Name", value=bot.user.name, inline=True)
	embed.add_field(name="ID", value=bot.user.id, inline=True)
	embed.add_field(name="Discord Version", value=discord.__version__, inline=True)
	embed.add_field(name="hello", value="siema", inline=True)
	await ctx.send(embed = embed)

@bot.command()
async def help(ctx):
	await ctx.channel.send(':bust_in_silhouette: General: ```help invite``` :game_die: Fun ```None```')
	
@bot.command()
async def help(ctx):
	await ctx.channel.send('Its ur cumshot' file)
	
@bot.command()
async def say(ctx, args):
	await ctx.channel.send(args)
	
@bot.command()
async def invite(ctx, **colour):
	embed.set_thumbnail(url=bot.user.avatar_url)
	embed.set_author(name="Neko Bot", icon_url=bot.user.avatar_url)
	embed.set_footer(text="Made by Ryu Tsubane© 2017", icon_url=bot.user.avatar_url)
	embed.add_field(name="Invite Link: ", value="INSERT OAUTH", inline=True)
	await ctx.send(embed = embed)

bot.run('INSERT TOKEN HERE') #https://discordapp.com/developers/applications/me
