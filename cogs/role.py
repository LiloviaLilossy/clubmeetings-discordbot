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
    
    @commands.command()
    async def cmrole(self, ctx, *, answer):
        if answer.lower() == "no spoilers":
            role = ctx.guild.get_role(763077636577558529)
        elif answer.lower() == "prediction":
            role = ctx.guild.get_role(763078046306795520)
        else:
            return await ctx.send("You need to choose one of the roles: `no spoilers` or `prediction`!")
        await ctx.author.add_roles(role)
        await ctx.send("Done!")
    
    @commands.is_owner()
    @commands.command()
    async def instamute(self, ctx, uid):
        self.instamute_cache.append(uid)
        data = load(open("bot-settings/instamute.json", "r"))
        data["muted"].append(uid)
        dump(data, open("bot-settings/instamute.json", "w"))
        await ctx.send("User was instamuted, if they'll join, I'll add a muted role.")
    
    @commands.is_owner()
    @commands.command()
    async def deinstamute(self, ctx, uid):
        self.instamute_cache.remove(uid)
        data = load(open("bot-settings/instamute.json", "r"))
        data["muted"].remove(uid)
        dump(data, open("bot-settings/instamute.json", "w"))
        await ctx.send("User was deinstamuted, if they'll join, I'll do nothing.")
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        if str(member.id) in self.instamute_cache:
            role = member.guild.get_role(738982557999169627)
            await member.add_roles(role, reason="Is in instamute list.")
            await member.send("You were muted from Doki Doki Club Meetings Discord Server. It's better to ask LiloviaLilossy#4389 for reason.")

def setup(bot):
    bot.add_cog(RoleGiverCog(bot))