import json
import os
import platform
import sys
import discord
from discord.ext import commands

if not os.path.isfile("config.json"):
    sys.exit("'config.json' not found! Add it and try again.")
else:
    with open("config.json") as file:
        config = json.load(file)


class general(commands.Cog, name="general"):
    def __init__(self, bot):
        self.bot = bot

    # shows the bot's information
    @commands.command(name="botinfo", description="Display the bot's info")
    @commands.has_role("Co-Founder")
    async def info(self, context):
        embed = discord.Embed(
            description="Price Bot",
            color=0xD5059D
        )
        embed.set_author(
            name="Bot Information"
        )
        embed.add_field(
            name="Created by:",
            value="heisenbaig#8473",
            inline=True
        )
        embed.add_field(
            name="Python Version:",
            value=f"{platform.python_version()}",
            inline=True
        )
        embed.add_field(
            name="Prefix:",
            value=f"{config['bot_prefix']}",
            inline=False
        )
        embed.set_footer(
            text=f"Requested by {context.message.author}"
        )
        await context.send(embed=embed)

    # shows the server's information
    @commands.command(name="server-info", description="Display the server's info")
    @commands.has_role("Co-Founder")
    async def serverinfo(self, context):
        server = context.message.guild
        roles = [x.name for x in server.roles]
        role_length = len(roles)
        if role_length > 50:
            roles = roles[:50]
            roles.append(f">>>> Displaying[50/{len(roles)}] Roles")
        roles = ", ".join(roles)
        channels = len(server.channels)
        time = str(server.created_at).split(" ")[0]

        embed = discord.Embed(
            title="**Server Name:**",
            description=f"{server}",
            color=0x42F56C
        )
        embed.set_thumbnail(
            url=server.icon_url
        )
        embed.add_field(
            name="Owner",
            value=f"{context.guild.owner}\n{context.guild.owner_id}"
        )
        embed.add_field(
            name="Server ID",
            value=server.id
        )
        embed.add_field(
            name="Member Count",
            value=server.member_count
        )
        embed.add_field(
            name="Text/Voice Channels",
            value=f"{channels}"
        )
        embed.add_field(
            name=f"Roles ({role_length})",
            value=roles
        )
        embed.set_footer(
            text=f"Created at: {time}"
        )
        await context.send(embed=embed)

    # ping a bot to check if it's alive or not
    @commands.command(name="ping", description="Check if the bot is alive")
    @commands.has_role("Co-Founder")
    async def ping(self, context):
        embed = discord.Embed(
            title="🏓 Pong!",
            description=f"The bot latency is {round(self.bot.latency * 1000)}ms.",
            color=0xD5059D
        )
        await context.send(embed=embed)

    # get the invite link of the bot
    @commands.command(name="invite", description="Get the invite link of the bot in DM")
    @commands.has_role("Co-Founder")
    async def invite(self, context):
        embed = discord.Embed(
            description=f"Invite me by clicking [here](https://discordapp.com/oauth2/authorize?&client_id={config['application_id']}&scope=bot&permissions=470150263).",
            color=0xD5059D
        )
        try:
            # To know what permissions to give to your bot, please see here: https://discordapi.com/permissions.html and remember to not give Co-Founderistrator permissions.
            await context.author.send(embed=embed)
            await context.send("I sent you a private message!")
        except discord.Forbidden:
            await context.send(embed=embed)

    # makes bot say whatever u want
    @commands.command(name="say", description="Makes bot say whatever you want")
    @commands.has_role("Co-Founder")
    async def say(self, context, message):
        try:
            await context.send(content=message)
        except discord.Forbidden:
            await context.send(content=message)

    # makes bot say whatever u want in an embed
    @commands.command(name="embed", description="Makes bot say whatever u want in an embed")
    @commands.has_role("Co-Founder")
    async def say_embed(self, context, message):
        embed = discord.Embed(
            description=f"{message}",
            color=0xD5059D
        )
        try:
            await context.send(embed=embed)
        except discord.Forbidden:
            await context.send(embed=embed)

    # # give role
    # @commands.command(name="addrole", description="Give role to a member")
    # @commands.has_permissions(manage_roles=True)
    # async def add_role(self, context, member: discord.Member, role: discord.Role):
    #     await member.add_roles(role)
    #     await context.send(embed=discord.Embed(description=f"`{member.display_name}` has been given a role called: **{role.name}**", color=0xD5059D))


def setup(bot):
    bot.add_cog(general(bot))
