import pandas as pd
import csv
import requests
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv 
load_dotenv()
TOKEN=os.getenv('DISCORD_TOKEN')
COINAPI=os.getenv('COINAPI')
def graphjson(name):
  date_time=datetime.now()-timedelta(days=2)
  date=date_time.date()
  url = f'https://rest.coinapi.io/v1/ohlcv/BITSTAMP_SPOT_{name}_USD/history?period_id=30MIN&time_start={date}T12:00:00'
  headers = {'X-CoinAPI-Key' : COINAPI}
  response = requests.get(url, headers=headers)
  d = response.json()
  for key in d:
    if(key=='error'):
      return None
  with open ('dx.csv','w', encoding = 'UTF8', newline = '') as f:
    writer = csv.writer(f)
    writer.writerow(['time_open','price_open','price_high','price_low','price_close'])
    for i in d:
      writer.writerow([i['time_open'],i['price_open'], i['price_high'], i['price_low'], i['price_close']])
  return pd.read_csv('dx.csv')  
