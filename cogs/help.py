import discord
from discord.ext import commands
from datetime import datetime
import json
import random
from discord.commands import Option

class Help(commands.Cog):
	def __init__(self, client):
		self.client = client
	@commands.slash_command(guild_ids=[860869454878736384,881207955029110855], name="help",description="Help is on the way")
	async def help(self,ctx,type=Option(str, "Enter help page", required = 	True, default = 'help')):
		if type == "help":
			embed=discord.Embed(title="Help menu", description="principal menu", color=0xcc30cf)
			embed.set_author(name="Albedo's rules")
			embed.add_field(name="music player", value="a!help music", inline=True)
			embed.add_field(name="wish simulator", value="a!help wish", inline=True)
			embed.add_field(name="misc", value="a!help misc", inline=True)
			embed.set_footer(text="Albedo-bot")
			await ctx.respond(embed=embed)
		elif type == 'music':
			embed=discord.Embed(title="Help menu", description="Music player", color=0xcc30cf)
			embed.set_author(name="Albedo's rules")
			embed.add_field(name="a!join", value="the bot joins the voice channel", inline=True)
			embed.add_field(name="a!search [value]", value="will show the first 5 results", inline=True)
			embed.add_field(name="a!play [url]", value="plays the url or adds to the queue", inline=True)
			embed.add_field(name="a!pause", value="pauses the video", inline=True)
			embed.add_field(name="a!resume", value="resumes the video", inline=True)
			embed.add_field(name="a!skip", value="skips the video", inline=True)
			embed.add_field(name="a!queue", value="shows the list of the songs in queue", inline=True)
			embed.add_field(name="a!leave", value="the bot leaves the voice channel", inline=True)
			
			embed.set_footer(text="Albedo-bot")
			await ctx.respond(embed=embed)
		elif type == 'wish':
			embed=discord.Embed(title="Help menu", description="Wish simulator", color=0xcc30cf)
			embed.set_author(name="Albedo's rules")
			embed.add_field(name="a!pull", value="Uses the genshin like gacha system WITHOUT PITY", inline=True)
			embed.set_footer(text="Albedo-bot")
			await ctx.respond(embed=embed)
		elif type == 'misc':
			embed=discord.Embed(title="Help menu", description="Misc", color=0xcc30cf)
			embed.set_author(name="Albedo's rules")
			embed.add_field(name="/pride", value="be who you are", inline=True)
			embed.add_field(name="/runa", value="runa runa runa", inline=True)
			embed.add_field(name="/ale", value="ale", inline=True)
			embed.add_field(name="/ping", value="ping pong", inline=True)
			embed.add_field(name="/cimpoi", value=" iuiuiuiu", inline=True)
			embed.add_field(name="/chinese", value=" best song ever", inline=True)
			embed.set_footer(text="Albedo-bot")
			await ctx.respond(embed=embed)
def setup(client):
	client.add_cog(Help(client))