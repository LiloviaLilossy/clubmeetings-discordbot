from discord.ext import commands
from json import load, dump

class Counter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        file = load(open("bot-settings/counter.json", "r"))
        try: file[message.author.id] +=1
        except: file[message.author.id] = 1
        dump(file, open("bot-settings/counter.json", "w"))
    
    @commands.command()
    async def msgcount(self, ctx):
        file = load(open("bot-settings/counter.json", "r"))
        msglist = list(file.items())
        msglist.sort(key=lambda i: i[1])
        await ctx.send(f"Messages: {file[str(ctx.author.id)]}, #{msglist.index(str(ctx.author.id))+1} on leaderboard")

def setup(bot):
    bot.add_cog(Counter(bot))