import requests
import json
import os
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from dotenv import load_dotenv 
load_dotenv()
APIKEY=os.getenv('APIKEY')
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': APIKEY,
}
def marketvalue():
  parameters={
    'convert':'USD'
  }
  try:
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    response = requests.get(url, params=parameters, headers=headers)
    data = json.loads(response.text)
    new={}
    for x in data['data']:
      new[x['name']]=x['quote']['USD']['market_cap_dominance']
    return new
  except (ConnectionError, Timeout, TooManyRedirects) as e:
      print(e)
def cryptovalue(name, currency):
  parameters = {
  'convert':currency
  }
  try:
      url = f'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol={name}'
      response = requests.get(url, params=parameters, headers=headers)
      amount = json.loads(response.text)
      value=amount['data'][name]
      X=value['quote'][currency]
      return [X['price'], value['max_supply'], value['circulating_supply'], X['percent_change_1h'], X['percent_change_24h'], X['percent_change_7d'], X['percent_change_30d'], value['name']]
  except (ConnectionError, Timeout, TooManyRedirects) as e:
      print(e)
def top_crypto():
  parameters={
    'convert':'USD'
  }
  try:
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    response = requests.get(url, params=parameters, headers=headers)
    data = json.loads(response.text)
    new={}
    for x in data['data']:
      new[x['name']]=x['quote']['USD']['price']
    return new
  except (ConnectionError, Timeout, TooManyRedirects) as e:
      print(e)