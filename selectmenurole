import discord
from discord.ui import Select, View
from discord.ext import commands

intents = discord.Intents.all()
client = discord.Client(intents=intents)

client = commands.Bot(command_prefix = "-", intents = discord.Intents.all())

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="клубок"))

    print("Кисан проснулся :)")

class RolesView(View):

    # Select Menu

    @discord.ui.select(
        placeholder="Выбрать игры",
        min_values=1,
        max_values=4,
        options=[
            discord.SelectOption(
                label="Minecraft",
                description="",
                emoji=":mine:",
                value="947910054097616936"
            ),
            discord.SelectOption(
                label="Counter strike Global offensive",
                description="",
                emoji=":cs:",
                value="947909872081596417"
            ),
            discord.SelectOption(
                label="Genshin Impact",
                description="",
                emoji=":gi:",
                value="947909653990350858"
            ),
            discord.SelectOption(
                label="War thunder",
                description="",
                emoji=":warth:",
                value="947910192924880946"
            ),
            discord.SelectOption(
                label="PUBG mobile",
                description="",
                emoji=":pubg:",
                value="947910332788142130"
            )
        ]
    )
    # Callback

    async def select_callback(self, select, interaction):

        await interaction.response.defer()

        # Getting Roles

        minecraft = discord.utils.get(interaction.user.guild.roles, name="Minecraft")
        cs = discord.utils.get(interaction.user.guild.roles, name="Counter strike Global offensive")
        gi = discord.utils.get(interaction.user.guild.roles, name="Genshin Impact")
        wt = discord.utils.get(interaction.user.guild.roles, name="War thunder")
        pm = discord.utils.get(interaction.user.guild.roles, name="PUBG mobile")

        # Creating Lists

        roles_to_add = []
        roles_to_remove = []

        # Checking If User Has Counter strike Global offensive Role
        if str(minecraft.id) in select.values:
            if interaction.user in minecraft.members:
                roles_to_remove.append(minecraft)
            else:
                roles_to_add.append(minecraft)

        # Checking If User Has Minecraft Role

        if str(cs.id) in select.values:
            if interaction.user in cs.members:
                roles_to_remove.append(cs)
            else:
                roles_to_add.append(cs)

        # Checking If User Has Genshin Impact Role

        if str(gi.id) in select.values:
            if interaction.user in gi.members:
                roles_to_remove.append(gi)
            else:
                roles_to_add.append(gi)

        # Checking If User Has War thunder Role

        if str(wt.id) in select.values:
            if interaction.user in wt.members:
                roles_to_remove.append(wt)
            else:
                roles_to_add.append(wt)

        # Checking If User Has PUBG mobile Role

        if str(pm.id) in select.values:
            if interaction.user in pm.members:
                roles_to_remove.append(pm)
            else:
                roles_to_add.append(pm)

        # Adding Roles To User

        for role in roles_to_add:
            await interaction.user.add_roles(role)

        # Removing Roles From User

        for role in roles_to_remove:
            await interaction.user.remove_roles(role)

@client.command()
async def stata(ctx):

    view = RolesView()
    await ctx.send("**В какие игры вы играете?**", view=view)
    
client.run('token')
