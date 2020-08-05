from discord.ext import commands
from discord import Role

class RoleGiverCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def verify(self, ctx):
        role = ctx.guild.get_role(730055612037333062)
        await ctx.author.add_roles(role)

def setup(bot):
    bot.add_cog(RoleGiverCog(bot))