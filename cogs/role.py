from discord.ext import commands
from discord import Role

class RoleGiverCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener(name="on_member_join")
    async def on_member_join(self, member):
        role = member.guild.get_role(730055612037333062)
        await member.add_roles(role)

def setup(bot):
    bot.add_cog(RoleGiverCog(bot))