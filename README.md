# Finance_Friend 
* Welcome to our Bot.
## Inspiration Behind The Project
* Cryptocurrency is a wave of revolution in the currency sector of the world. It is ceratinly a concept that intrigues many of us who keep a regular track of their investments and a keen eye on the market prices. So, we decided to create a discord bot which keeps the user updated about the latest in the cryptocurrency area and also can be added to any server.
## WHAT THE PROJECT DOES?
* The bot lets you browse through latest news about cryptocurrency. It also lets you know about the risky investments as well as the top trending cryptocurencies. Value of a particular cryptocurrency can be calculated in any currency of the user's choice. ALong with this, a detailed progression graph for a particular cryptocurrency is also generated on user's request.
The bot works on certain commands which are to be prefixed by "!".
## HOW IT WAS BUILT?
* We made the crypto bot using python and we used discord module, a a news API and a market API to get statistics. 
## CHALLENGES WE FACED
* The very first challenge, obviously was to learn how to generate a bot and learn the syntax for creating a working bot. Extracting data using API Keys and formatting the data in a presentable way was another challenge. The toughest challenege though, was to create an OHCLV graph using data from API and then sending it to the discord channel.
## HOW TO RUN?
* https://discord.gg/7PxzKZdt
* Use the above link to join the server
### The Crypto Bot Uses The Following Libraries/Modules(If they aren't installed use the following commands):
* Discord -> pip install discord
* PLotly -> pip install plotly
* Csv -> pip install csv
* Dotenv -> pip install dotenv
* Json -> pip install json
* Datetime -> pip install datetime
* Requests -> pip install requests
* Os -> pip install os
* Asyncio -> pip install asyncio
* Graphs -> pip install graphs
* Kaleido -> pip install -U kaleido
### COMMANDS AVAILABLE WHEN THE BOT IS RUNNING(com)
* !list => displays a list of abbrevations for some popular bitcoins which will be used further in other inputs
* !crypto <abbreviation_of_cryptocurrency> <abbreviation_of_currency> (Example: !crypto BTC USD)
* !top10 (Example: !top10)
* !risky (Example: !risky)
* !graph <abbreviation_of_cryptocurrency> (Example: !graph BTC)
* !news <name_of_cryptocurrency> (Example: !news bitcoin)
* !help => displays a help box for you to use the bot easily
* !help news => displays a help box and instruction format to get news
* !help crypto => displays a help box and instructions format to get information about a particular cryptocurrency
* !help graph => displays a help box and input format for a graph to be generated
* !help top10 => displays a help box and instruction format to get the top 10 trending cryptocurrencies list
* !help risky => displays a help box and input format to get the information about risky cryptocurrencies
### Replit
* The code for this bot runs on replit but if the bot( is showing offline, then the code available in this repository can be cloned and the Libraries above are to be downloaded. Then go to the next section of this readme.
### Running on terminal
* Once you are in the server and all the above librarires are available on your laptop:
* Run the command:- python3 crypto.py
* The above command will run the bot and the commands in the section(com) can be used!
* [Screenshot from 2022-04-17 23-07-32](https://user-images.githubusercontent.com/70737554/163726021-3da92d7f-4a02-47e4-bf3e-8f27f9bc71db.png)
* 
![Screenshot from 2022-04-17 23-07-42](https://user-images.githubusercontent.com/70737554/163726031-f6a57742-44f0-469b-b50c-e9a43c63d725.png)
![Screenshot from 2022-04-17 23-07-46](https://user-images.githubusercontent.com/70737554/163726034-74eaf4d3-adbd-4fc6-b522-dfddd0a4ff89.png)
![Screenshot from 2022-04-17 23-07-54](https://user-images.githubusercontent.com/70737554/163726042-22e74648-ff91-46ef-b4b9-1c9f05f6232f.png)

![Screenshot from 2022-04-17 23-08-00](https://user-images.githubusercontent.com/70737554/163726045-17804e08-b366-4944-bc8e-b0f204386323.png)
