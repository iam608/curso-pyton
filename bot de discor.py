import discord
from discord.ext import commands
import random
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def user(ctx):
    resultado = "IAM " *5
    await ctx.send(resultado)


@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def moneda(ctx):
    numero = random.randint(1,2)
    if numero == 1 :
        respuesta = "moneda de oro"
    elif numero == 2 :
         respuesta = "moneda de plata"
    await ctx.send(respuesta)

bot.run("MTQ3MzEwODI3MDY0MTMxNTk0NA.GLr8l6.oD_qL6ULzFoS6D1QxbOFLYOxcE-c_AkXM-VO8Y")
