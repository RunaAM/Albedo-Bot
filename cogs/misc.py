import discord
from discord.ext import commands
from datetime import datetime
import json
import random

class Meme(commands.Cog):
	def __init__(self, client):
		self.client = client
	@commands.slash_command(guild_ids=[860869454878736384,881207955029110855], name="ale",description="This is for you alec")
	async def ale(self,ctx):
		await ctx.respond("<:emoji_1:871794698887499776> This aint build a bitch u dont get to pick and choose.")
	@commands.slash_command(guild_ids=[860869454878736384,881207955029110855], name="runa",description="runa runa runa runa")
	async def andrei(self,ctx):
		await ctx.respond("<:emoji_1:871794698887499776>")
		await ctx.respond("smack my ass like a drum slurp that dick till it cums ")

	@commands.slash_command(guild_ids=[860869454878736384,881207955029110855], name="cimpoi",description="iu iu iu iu iu")
	async def cimpoi(self,ctx):
		await ctx.respond("IU IU IU IU IU VINE BADE PE LA NOI SA NU VII FARA CIMPOI DA MA CIMPOI DA MA CIMPOI JOACA FETELE A NOI")
	@commands.slash_command(guild_ids=[860869454878736384,881207955029110855], name="chinese",description="i love this")
	async def chinese(self,ctx):
		await ctx.respond("https://www.youtube.com/watch?v=4L-fSsY01TU")
	@commands.slash_command(guild_ids=[860869454878736384,881207955029110855], name="pride",description="BEE WHO YOU ARE")
	async def pride(self,ctx):
		embed = discord.Embed(title='I,Albedo the chief alchemist, have to say "happy pride month!!"',
                          colour=discord.Color.orange())
		embed.set_author(
        name='Albedo',
        icon_url=
        'https://cdn.discordapp.com/attachments/846783543694721087/846783570915098624/gasp.png'
    )
		
		embed.set_image(
        url=
        'https://cdn.discordapp.com/attachments/846783543694721087/848931596609912862/200w.gif'
    )
		embed.timestamp = datetime.utcnow()
		await ctx.respond( embed=embed)
	
def setup(client):
    client.add_cog(Meme(client))