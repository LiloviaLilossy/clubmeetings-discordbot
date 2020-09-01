from discord.ext import commands
from json import load

token = (load(open("bot-settings/token.json", "r")))["token"]

bot = commands.Bot(command_prefix="club ")
bot.load_extension("jishaku")

bot.run()