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
    async def cupcake(self, ctx):
        await ctx.send(f"{ctx.author.mention} got a cupcake from server's storage! Don't forget to thank Natsuki for this!")
    
    @commands.command()
    async def tea(self, ctx):
        await ctx.send(f"{ctx.author.mention} got some tea from server's storage! Don't forget to thank Yuri for this!")

    @commands.command()
    async def waffle(self, ctx):
        await ctx.send(f"{ctx.author.mention} got two waffles from server's storage! Don't forget to thank countess for this!")

    @commands.command()
    async def coffee(self, ctx):
        await ctx.send(f"{ctx.author.mention} got some coffee from server's storage! Don't forget to thank Monika for this!")
    
    @commands.command()
    async def meetings(self, ctx):
        await ctx.send("You can get all season link here: https://www.dokidokimodclub.com/mod/146\n Season 2 Episode 1 link: https://www.dokidokimodclub.com/mod/173/")

def setup(bot):
    bot.add_cog(Fun(bot))