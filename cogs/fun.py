from discord.ext import commands

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def hug(self, ctx, *, text):
        await ctx.send(f"*{ctx.author.mention} hugs {text}*")
    
    @commands.command()
    async def cookie(self, ctx):
        await ctx.send(f"{ctx.author.mention} got a cookie from server's storage!")
    
    @commands.command()
    async def milk(self, ctx):
        await ctx.send(f"{ctx.author.mention} got some milk from server's storage!")
    
    @commands.command()
    async def meetings(self, ctx):
        await ctx.send("You can get all season link here: https://www.dokidokimodclub.com/mod/146")

def setup(bot):
    bot.add_cog(Fun(bot))