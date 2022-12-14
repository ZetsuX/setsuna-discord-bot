import discord
from discord.ext import commands

guilds = [990445490401341511]

class Checkping(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    
  @commands.slash_command(name="pinger", description="Check Ping", guild_ids=guilds)
  async def pinger(self, ctx):
      embed = discord.Embed(
          title="Current Ping",
          description=f"Ping is `{round(self.bot.latency * 100, 2)}` ms",
          color=ctx.author.color)
      await ctx.respond(embed=embed)

def setup(bot):
  bot.add_cog(Checkping(bot))