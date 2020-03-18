from discord.ext import commands
import discord
from datetime import date, datetime, timedelta
import datetime
import json
import asyncio
import json
import traceback
import sys
logs = {}
joins = {}
timeout = 0.1

class events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot   
def setup(bot):
    bot.add_cog(events(bot))