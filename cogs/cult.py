from discord.ext import commands
from asyncio import sleep

class CultCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.custom_names = {"Baby":"B̶̛̛̰͎͙͚̝̯̩̣͕͆̀̌̊́̍͊̀̈́̐̊̆̀̓͜͠a̸̡̤̥͔̻͛̀b̸̮̤̜̻̺̱̗̓̏̈̓͗̅͒̆̊͌̾͗̉̋̏͜͝͝ẏ̵̧͖͙̟͕̞̫͛͌̏̾̋͛̐͆͗̈́͆̊̇̏͜", "Countess":"Cult Leader", "muted": "Kicked from the Cult", "Charles": "Cult Butler", "Meetings Bot": "Cult Bot", "Members": "Cultists"}
        self.reverse_names = {"B̶̛̛̰͎͙͚̝̯̩̣͕͆̀̌̊́̍͊̀̈́̐̊̆̀̓͜͠a̸̡̤̥͔̻͛̀b̸̮̤̜̻̺̱̗̓̏̈̓͗̅͒̆̊͌̾͗̉̋̏͜͝͝ẏ̵̧͖͙̟͕̞̫͛͌̏̾̋͛̐͆͗̈́͆̊̇̏͜": "Baby", "Cult Leader": "Countess", "Kicked from the Cult": "muted", "Cult Butler": "Charles", "Cult Bot": "Meetings Bot", "Cultists": "Members"}
    
    @commands.is_owner()
    @commands.group(invoke_without_command=False)
    async def cult(self, ctx):
        return
    
    @cult.command(name="start")
    async def cult_start(self, ctx):
        cm = self.bot.get_guild(730055007226953768)
        for role in cm.roles:
            sleep(2)
            try:
                if role.name in ["Groovy", "Tupperbox"]: 
                    continue
                if role.name in list(self.custom_names):
                    name = self.custom_names[role.name]
                else:
                    name = "Cult " + role.name
                await role.edit(name=name)
            except Exception: 
                pass
        for channel in cm.text_channels:
            sleep(2)
            try:
                name = "cult-"+channel.name
                await channel.edit(name=name)
            except Exception: 
                pass
        for channel in cm.voice_channels:
            sleep(2)
            try:
                name = "Cult "+channel.name
                await channel.edit(name=name)
            except: continue
        await cm.edit(name="Club Meetings Cult")
        self.bot.command_prefix = "cult "
        await cm.me.edit(nick="Cult Bot")
        await ctx.send("All praise the Club Meetings Dev! Prefix is `cult `.")
    
    @cult.command(name="end")
    async def cult_end(self, ctx):
        cm = self.bot.get_guild(730055007226953768)
        for role in cm.roles:
            sleep(2)
            try:
                if role.name in ["Groovy", "Tupperbox"]: 
                    continue
                if role.name in list(self.reverse_names):
                    name = self.reverse_names[role.name]
                else:
                    name = role.name[5:]
                await role.edit(name=name)
            except Exception: 
                pass
        for channel in cm.text_channels:
            sleep(2)
            try:
                name = channel.name[5:]
                await channel.edit(name=name)
            except Exception: 
                pass
        for channel in cm.voice_channels:
            sleep(2)
            try:
                name = channel.name[5:]
                await channel.edit(name=name)
            except Exception: 
                pass
        await cm.edit(name="Doki Doki Club Meetings")
        self.bot.command_prefix = "club "
        await cm.me.edit(nick=None)
        await ctx.send("Cult Days are done. See ya next time. Prefix is `club ` now.")

def setup(bot):
    bot.add_cog(CultCog(bot))
