import discord
from discord.ui import View
from discord.ext import commands

intents = discord.Intents.all()
client = discord.Client(intents=intents)

client = commands.Bot(command_prefix = "-", intents = discord.Intents.all())

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="клубок"))

    print("Кисан проснулся :)")


class GameRole(View):

	def __init__(self):
		super().__init__(timeout = None)

	# Select Menu

	@discord.ui.select(
		placeholder = "Выберите для получения роли",
		min_values = 0,
		max_values = 5,
		options = [
			discord.SelectOption(
				label = "Minecraft",
				description = "",
				emoji = "<:minecraft:1005452339009835079>",
				value = "947910054097616936"
			),
			discord.SelectOption(
				label = "Counter strike Global offensive",
				description="",
				emoji = "<:cs:947572308971782264>",
				value = "947909872081596417"
			),
			discord.SelectOption(
				label = "Genshin Impact",
				description = "",
				emoji = "<:gi:947574602282963114>",
				value = "947909653990350858"
			),
			discord.SelectOption(
				label = "War Thunder",
				description = "",
				emoji = "<:warth:947583191617777676>",
				value = "947910192924880946"
			),
			discord.SelectOption(
				label="PUBG Mobile",
				description="",
				emoji="<:pubg:947916451623354398>",
				value="947910332788142130"
			)
		]
	)

	# Callback

	async def select_callback(self, select, interaction):

		await interaction.response.defer()

		minecraft_role = discord.utils.get(interaction.user.guild.roles, name = "Minecraft")
		csgo_role = discord.utils.get(interaction.user.guild.roles, name = "Cs Go")
		genshinimpact_role = discord.utils.get(interaction.user.guild.roles, name = "Genshin Impact")
		warthunder_role = discord.utils.get(interaction.user.guild.roles, name = "War thunder")
		pubgmobile_role = discord.utils.get(interaction.user.guild.roles, name="PUBG Mobile")

		list_roles = [csgo_role, genshinimpact_role, minecraft_role, warthunder_role, pubgmobile_role]

		for role in interaction.user.roles:
			for rolelist in list_roles:
				if role == rolelist:
					if role not in select.values:
						await interaction.user.remove_roles(role)

		if len(select.values) != 0:
			for choice in select.values:
				if choice == "947910054097616936":
					await interaction.user.add_roles(minecraft_role)
				elif choice == "947909872081596417":
					await interaction.user.add_roles(csgo_role)
				elif choice == "947909653990350858":
					await interaction.user.add_roles(genshinimpact_role)
				elif choice == "947910192924880946":
					await interaction.user.add_roles(warthunder_role)
				elif choice == "947910332788142130":
					await interaction.user.add_roles(pubgmobile_role)

@client.command()
async def gamerole(ctx):

    view = GameRole()
    await ctx.send("**В какие игры вы играете?** <:vibepepe:955574694193561740>", view=view)

    
client.run('token')
