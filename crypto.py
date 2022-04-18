import discord
from discord.ext import commands
import os
import plotly.graph_objects as go
import plotly.io as pio
from dotenv import load_dotenv 
from top_crypto import marketvalue, cryptovalue, top_crypto
from crypto_news import  setup
from graphs import graphjson
load_dotenv()
TOKEN=os.getenv('DISCORD_TOKEN')
APIKEY=os.getenv('APIKEY')
NEWSKEY=os.getenv('NEWSKEY')
bot=commands.Bot(command_prefix='!')
setup(bot)
@bot.event
async def on_ready():
  print("Bot is running")
@bot.command(name='list', help='Abbreviations of cryptocurrency names')
async def list(ctx):
    embed = discord.Embed(title = 'Keywords to know', description = 'Abbreviations of cryptocurrency names', color = discord.Color.blue())       
    l = ['Bitcoin','Ethereum','Tether','Binance Coin','USD Coin','XRP (Ripple)','Solana','Cardano','Terra','Avalanche']
    l_abb = ['BTC','ETH','USDT','BNB','USDC','XRP','SOL','ADA','LUNA','AVAX']

    for i in range (0,10):
      embed.add_field(name = l[i], value = l_abb[i], inline = True)
    await ctx.send(embed = embed)
    return
 
@bot.command(name="crypto", help="Gives details about a cryptocurrency.\nInput in the format,\n!crypto <crypto_abbreviation> <currency_abbreviation>")
async def crypto(ctx, name=None, currency=None):
  try:
    amount=cryptovalue(name, currency)  
    description="Checkout information about your favorite Cryptocurrency"
    embed= discord.Embed(title="Crypto Information", description=description, color= discord.Color.blue())
    embed.add_field(name="Price", value=f"{currency} {amount[0]:.4f}", inline=True)
    if amount[1] is None:
      amount[1]="Unlimited"
    embed.add_field(name="Full From", value=str(amount[7]), inline=True)
    embed.add_field(name="Max Supply", value=str(amount[1]), inline=True)
    embed.add_field(name="Current Supply", value=str(amount[2]), inline=True)
    embed.add_field(name="Percentage change(1H)", value=str(amount[3]), inline=True)
    embed.add_field(name="Percentage change(1D)", value=str(amount[4]), inline= True)
    embed.add_field(name="Percentage change(W)", value=str(amount[5]), inline= True)
    await ctx.send(embed=embed)
  except KeyError:
    await ctx.send(f"Invalid Input format. Use !help to know about commands")
@bot.command(name="top10", help="Information on top10 cryptocurrency\nType '!top10' and press ENTER")
async def top10(ctx):
  try:
    value=top_crypto()
    description="10 Crypto Bytes for you"
    embed= discord.Embed(title="Top 10 Cryptocurrency", description=description, color= discord.Color.green())
    count=1
    for x in value:
      if(count<=10):
        embed.add_field(name=f"{count}.", value=f"{x} ${value[x]:.2f}")
      count+=1
    await ctx.send(embed=embed)
  except: await ctx.send(f"Invalid Input format. Use !help to know about commands")
@bot.command(name="risky", help="Information on Risky investments\nType '!risky' and press ENTER")
async def risky(ctx):
  value=top_crypto()
  market=marketvalue()
  description="High risk High Reward"
  embed= discord.Embed(title="12 Risky Cryptocurrency", description=description, color= discord.Color.green())
  count=1
  for i in value:
    if(count<=12 and float(market[i])<1 and float(value[i])<0.6 and float(value[i])>0.05):
      embed.add_field(name=f"{count}.", value=f"{i} ${value[i]:.4f}")
      count+=1
  await ctx.send(embed=embed)
@bot.command(name="graph", help="Gives graph of crypto\nInput in the format,\n!graph <crypto_abbreviation>")
async def graph(ctx, name):
    df=graphjson(name)
    if df is None:
      await ctx.send(f"Graph of {name} is not available. Use !help to know commands")
    else:
      fig = go.Figure(data = go.Ohlc(x = df['time_open'],open = df['price_open'], high = df['price_high'], low = df['price_low'], close = df['price_close']))
      pio.write_image(fig,'test1.png')
      image = discord.File('test1.png')
      await ctx.send(file = image)
bot.run(TOKEN)
