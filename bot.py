import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='-', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Cześć, jestem bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 10):
    await ctx.send("he" * count_heh)

@bot.command()
async def chat(ctx):
    await ctx.send("chatchatchatchatchatchatchatchatchatchat")

bot.run("MTMwOTg4NTA2NTk3MDMxOTM3MA.GifKEB.NiMECx3PEomir1sxvEHVe_4gYu3BjrxuCjeEgI")