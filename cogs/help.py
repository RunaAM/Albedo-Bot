import discord
from discord.ext import commands

from discord.commands import Option

class Help(commands.Cog):
	guilds_id=[860869454878736384,968887343119482940]
	def __init__(self, client):
		self.client = client
	@commands.slash_command(guild_ids=guilds_id, name="help",description="Help is on the way")
	async def help(self,ctx,type=Option(str, "Enter help page", required = 	True, default = 'help')):
		if type == "help":
			embed=discord.Embed(title="Help menu", description="principal menu", color=0xcc30cf)
			embed.set_author(name="Albedo's rules")
			embed.add_field(name="music player", value="/help music", inline=True)
			embed.add_field(name="wish simulator", value="/help wish", inline=True)
			embed.add_field(name="misc", value="/help misc", inline=True)
			embed.set_footer(text="Albedo-bot")
			await ctx.respond(embed=embed)
		elif type == 'music':
			embed=discord.Embed(title="Help menu", description="Music player", color=0xcc30cf)
			embed.set_author(name="Albedo's rules")
			embed.add_field(name="Not available", value="in construction", inline=True)
			
			
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
			embed.add_field(name="/ping", value="ping pong", inline=True)
			embed.add_field(name="/nsfw", value="umm", inline=True)
			embed.add_field(name="/runa", value="runa", inline=True)

			embed.set_footer(text="Albedo-bot")
			await ctx.respond(embed=embed)
def setup(client):
	client.add_cog(Help(client))