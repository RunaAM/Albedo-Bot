@client.command()
async def pull(ctx,banner):
	weaponrand = random.randint(0,len(weaponstandard)-1)
	charrand = random.randint(0,len(charstandard))
	embed = discord.Embed(colour=discord.Color.blurple())
	embed.add_field(name='4 star ',value=charstandard[charrand],inline=True)
	embed.set_thumbnail(url=charstdicon[charrand])
	if(banner=='standard'):
		for i in range(1,10):
			rand = random.randint(1,90)
			print(ctx.message.author.id)
			if(rand %37 ==0):
				weapon = random.randint(1,4)
				if(weapon == 4):
					charrand = random.randint(0,len(fiveweaponstand)-1)
					embed.add_field(name='5 star ',value=fiveweaponstand[charrand],inline=True)
					embed.set_thumbnail(url=fivewicon[charrand])
				else:
					charrand = random.randint(0,len(fivestandard)-1)
					embed.add_field(name='5 star ',value=fivestandard[charrand],inline=True)
					embed.set_thumbnail(url=fivestdicon[charrand])
					
			elif(rand%10 ==0):
				charrand = random.randint(0,len(charstandard)-1)
				embed.add_field(name='4 star ',value=charstandard[charrand],inline=True)
				
			else:
				weaponrand = random.randint(0,len(weaponstandard)-1)
				embed.add_field(name='3 star ',value=weaponstandard[weaponrand],inline=True)

		with open('data/users.json', 'w') as f:
			json.dump(users, f)
		embed.set_author(name='Albedo')
		embed.timestamp = datetime.utcnow()
		await ctx.send( embed=embed)
	elif(banner=="event"):
		for i in range(1,10):
			

			rand = random.randint(1,90)
			fifty = 0
			print(rand)	
			if(rand %37 ==0):
				weapon = random.randint(1,8)
				if(fifty ==1):
					weapon =1
				if(weapon == 8):
					charrand = random.randint(0,len(fiveweaponstand)-1)
					embed.add_field(name='5 star ',value=fiveweaponstand[charrand],inline=True)
					embed.set_thumbnail(url=fivewicon[charrand])
					fifty = 1
					
				elif(weapon <8 and weapon >4):
					charrand = random.randint(0,len(fivestandard)-1)
					embed.add_field(name='5 star ',value=fivestandard[charrand],inline=True)
					embed.set_thumbnail(url=fivestdicon[charrand])
					fifty = 1
					
				else:
					embed.add_field(name='5 star ',value='Ayaka',inline=True)
					embed.set_thumbnail(url="https://img.game8.co/3313080/2cae7dd671c21d14eff9fdd945e07da2.png/show")
					users[ctx.message.author.id]['Ayaka'] +=1
			elif(rand%10 ==0):
				character = random.randint(1,2)
				if(character ==1):
					charrand = random.randint(0,len(charstandard)-1)
					embed.add_field(name='4 star ',value=charstandard[charrand],inline=True)
				else:
					charrand = random.randint(0,len(fourevent)-1)
					embed.add_field(name='4 star ',value=fourevent[charrand],inline=True)
			else:
				weaponrand = random.randint(0,len(weaponstandard)-1)
				embed.add_field(name='3 star ',value=weaponstandard[weaponrand],inline=True)
		
		embed.set_author(name='Albedo')
		embed.timestamp = datetime.utcnow()
		await ctx.send( embed=embed)