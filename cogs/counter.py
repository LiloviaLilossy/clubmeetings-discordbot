from discord import Embed, Colour
from discord.ext import commands
from json import load, dump
import datetime

class Counter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        file = load(open("bot-settings/counter.json", "r"))
        try: file[str(message.author.id)] +=1
        except: file[str(message.author.id)] = 1
        dump(file, open("bot-settings/counter.json", "w"))
    
    @commands.command()
    async def msgcount(self, ctx):
        file = load(open("bot-settings/counter.json", "r"))
        msglist = list(file.items())
        msglist.sort(key=lambda i: i[1], reverse=True)
        for id, count in msglist:
            if int(id) == ctx.author.id:
                member = msglist.index((id, count))
                break
        await ctx.send(f"Messages: {file[str(ctx.author.id)]}, #{member+1} on leaderboard")
    
    @commands.command()
    async def leaderboard(self, ctx):
        roles = [740608292979474443, 730076720308420681, 730055873069711440, 734050572088508448, 740564108377718846, 744545560295374858, 744559294959059065]
        e = Embed(color=Colour.gold())
        e.description = "Club Meetings Leaderboard!"
        e.timestamp = datetime.datetime.utcnow()
        text = ""
        file = load(open("bot-settings/counter.json", "r"))
        msglist = list(file.items())
        msglist.sort(key=lambda i: i[1], reverse=True)
        for id, count in msglist:
            breaking = False
            member = ctx.guild.get_member(int(id))
            for role in member.roles:
                if role.id in roles:
                    breaking = True
            if breaking: continue
            text += f"#{msglist.index((id, count))+1} - {member.mention} ({count} messages) \n"
        e.add_field(name="There are only members without custom roles.", value=text)
        await ctx.send(embed=e)

def setup(bot):
    bot.add_cog(Counter(bot))