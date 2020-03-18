import urllib
from urllib import parse
from discord.ext import commands
import discord, datetime, time
import asyncio
import datetime
import logging
from time import perf_counter
import requests
import bs4
from bs4 import BeautifulSoup


class cmds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='help')
    @commands.guild_only()
    @commands.bot_has_permissions(manage_messages=True)
    @commands.cooldown(1, 15, commands.BucketType.guild)
    async def help(self, ctx):
        try:
            await ctx.message.delete()

            prefix = ctx.prefix

            # help 1
            embed = discord.Embed(colour = 0xfca7f5, description="""Welcome to the commands page! Here you will be able to view every single command you have access to.\n\t** **\n""")
            embed.set_thumbnail(url=self.bot.user.avatar_url)
            embed.set_author(name='List Of Commands​',icon_url=ctx.author.avatar_url)
            embed.add_field(name=f"{prefix}help", value="Show this message.", inline=False)
            embed.add_field(name=f"{prefix}say [text]", value="Sends the messesge on [text].", inline=False)
            embed.add_field(name=f"{prefix}coinflip", value="Sends either Heads or Tails.", inline=False) 
            embed.add_field(name=f"{prefix}invite", value="Sends the invite link of the bot.", inline=False)
            embed.add_field(name=f"{prefix}stats", value="Sends the bot stats.", inline=False)
            embed.add_field(name=f"{prefix}ping", value="Sends the bot latency.", inline=False)
            embed.add_field(name=f"{prefix}hug", value="Hugs you <3.", inline=False)
            embed.add_field(name=f"{prefix}youtube [text]", value="Searches anything on youtube.", inline=False)
            embed.add_field(name=f"{prefix}useravatar [user]", value="Gets the avatar of the mentioned user.", inline=False)
            

            await ctx.message.author.send(embed=embed)

            # help 2
            embed = discord.Embed(colour = 0xfca7f5, description='Welcome to the admin commands page! here you will be able to view every single command admins have access to.')
            embed.set_author(name='Admin Commands',icon_url=ctx.author.avatar_url)
            embed.add_field(name=f"{prefix}kick [user]", value="Kicks the [user].", inline=False)
            embed.add_field(name=f"{prefix}ban [user]", value="Bans the [user].", inline=False)
            embed.add_field(name=f"{prefix}purge [amount]", value="delete [amount] messages.", inline=False)
            embed.add_field(name=f"{prefix}geo [ip address]", value="Locates an ip address around the globe, its not that accurate but it gets the work done.(Don't Do this on public channels.)", inline=False)
            embed.add_field(name=f"{prefix}setservername [test]", value="Sets the server name from [text].", inline=False)
            embed.add_field(name="Made by", value="JDS#2131")
            embed.add_field(name='My Github', value="https://github.com/JDS-py/")


            await ctx.message.author.send(embed=embed)

        except:
            pass

    @commands.command()
    async def ping(self, ctx):
        stre = self.bot.latency * 1000
        em = discord.Embed(title=f'Bot Latency: {int(stre)}ms', colour=0xfca7f5)
        em.set_author(name='Nikoru Yamagashi')
        

        await ctx.send(embed=em)

    @commands.command(pass_context=True, aliases=['yt', 'vid', 'video'])
    async def youtube(self, ctx, *, msg):
        f"""Search for videos on YouTube.
        Usage:
        {ctx.prefix}yt (query)
        """
        search = parse.quote(msg)
        response = requests.get(
            "https://www.youtube.com/results?search_query={}".format(search), verify=False).text
        result = BeautifulSoup(response, "html.parser")
        emy = discord.Embed(colour=0xfca7f5, description="Youtube Search")
        emy.set_author(name="Searching...", icon_url="https://cdn.discordapp.com/attachments/678969206456188973/689652145326522414/output-onlinepngtools.png")
        await ctx.send(embed=emy, delete_after = 5)
        await asyncio.sleep(5)
        await ctx.send("https://www.youtube.com{}".format(result.find_all(attrs={'class': 'yt-uix-tile-link'})[0].get('href')))




    @commands.command(
        name='purge',
        hidden=True,
    )
    async def purge(
        self, ctx,
        num_messages: int,
    ):
        """Clear <n> messages from current channel"""
        if ctx.author.guild_permissions.administrator:
            channel = ctx.message.channel
            await ctx.message.delete()
            await channel.purge(limit=num_messages, check=None, before=None)
            return True

        else:
            await ctx.send("You don't have the permission to use this command.")


    @commands.command(name='invite', aliases=['bot'])
    async def invite(self, ctx):
        await ctx.trigger_typing()
        embed = discord.Embed(
            colour=0xfca7f5,
        )
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        embed.set_author(name=self.bot.user.name,icon_url=ctx.author.avatar_url)
        embed.add_field(
            name="Touch the link below to invite the bot",
            value=f"[Invite me](https://discordapp.com/api/oauth2/authorize?client_id={self.bot.user.id}&permissions=8&scope=bot)"
        )
        try:
            await ctx.message.author.send(embed=embed)
        except:
            pass


    @commands.command()
    async def useravatar(self, ctx, user: discord.Member=None):
    	if user is None:
    		user = ctx.author
    	avataru = discord.Embed(title="{}'s Avatar".format(user.name), color=0xfca7f5, timestamp=datetime.datetime.utcnow())
    	avataru.set_image(url=user.avatar_url)
    	await ctx.send(embed=avataru)

 

    
def setup(bot):
    bot.add_cog(cmds(bot))
