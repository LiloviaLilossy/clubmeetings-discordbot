from discord.ext import commands
from discord import Role
from json import load, dump

class RoleGiverCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.instamute_cache = load(open("bot-settings/instamute.json", "r"))["muted"] or []
    
    @commands.command()
    async def verify(self, ctx):
        role = ctx.guild.get_role(730055612037333062)
        await ctx.author.add_roles(role)
    
    @commands.is_owner()
    @commands.command()
    async def instamute(self, ctx, id):
        self.instamute_cache.append(id)
        data = load(open("bot-settings/instamute.json", "r"))
        data["muted"].append(id)
        dump(data, open("bot-settings/instamute.json", "w"))
        await ctx.send("User was instamuted, if they'll join, I'll add a muted role.")
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        if str(member.id) in self.instamute_cache:
            role = member.guild.get_role(738982557999169627)
            await member.add_roles(role, reason="Is in instamute list.")
            await member.send("You were muted from Doki Doki Club Meetings Discord Server. It's better to ask LiloviaLilossy#4389 for reason.")

def setup(bot):
    bot.add_cog(RoleGiverCog(bot))