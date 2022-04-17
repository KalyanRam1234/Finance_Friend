from datetime import datetime, timedelta
import requests
import discord
from discord.ext import commands
import asyncio
from dotenv import load_dotenv 
import os
load_dotenv()
APIKEY=os.getenv('APIKEY')
NEWSKEY=os.getenv('NEWSKEY')
bot=commands.Bot(command_prefix='!')
def cryptonews(name):
  date_time=datetime.now()-timedelta(days=14)
  date=date_time.date()
  new_name=name.lower()
  response = requests.get("https://newsapi.org/v2/everything?q={}&from={}&language=en&sortBy=publishedAt&apiKey={}".format(new_name,date,NEWSKEY))
  articles=response.json()["articles"]
  headlines_list = []
  number = 1
  for news in articles:
    headlines_list.append([number,news['source']['name'],news['title'],news['url']])
    number = number + 1
  return headlines_list
class News(commands.Cog):
    def __init__(self, client):
      self.client=client
    @commands.command(name="news", help="Get the latest news on your favorite Cryptocurrency\nInput in the format,\n'!news' <cryptocurrency_name>, and then enter the serial number of the article you want to read.")
    async def news(self, ctx, name):
      news=cryptonews(name)
      check=[]
      i=0
      description="Choice One Article: "
      embed= discord.Embed(title= name.upper()+" " +"Crypto News", description=description, color= discord.Color.green())
      for x in news:
        if(i<10 and x[2] not in check):
          check.append(x[2])
          embed.add_field(name=f"{i+1}.",value=f"Source: {x[1]} \nHeadline: {x[2]}", inline=False)
          i+=1
        elif(i>=10): break
      await ctx.send(embed=embed)
      try:
        msg = await self.client.wait_for('message', timeout=100.0, check=lambda x : x.channel == ctx.channel and x.author == ctx.author)
      except asyncio.TimeoutError:
        await ctx.reply("You took too long!")
      await ctx.send(news[int(msg.content)-1][3])
def setup(client):
  client.add_cog(News(client))