import json
import os
import sys

import discord
from discord.ext import commands
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

if not os.path.isfile("config.json"):
    sys.exit("'config.json' not found! Add it and try again.")
else:
    with open("config.json") as file:
        config = json.load(file)


class General(commands.Cog, name="price"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="getprice",
                      description="Displays the price of a given currency symbol in USD (Syntax: !getprice {currency symbol})")
    @commands.has_role("Co-Founder")
    async def get_price(self, context, symbol):
        embed = discord.Embed(color=0x3f00fc,
                              description=f"The current price of `{symbol.upper()}` is **`{self.get_price_helper(symbol.strip().upper())} USD`**")
        await context.send(embed=embed)

    @staticmethod
    def get_price_helper(currency):
        key = 'c9107b23-aa25-4d10-8948-ff6e3c2c6739'
        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        parameters = {
            'start': '1',
            'limit': '5000',
            'convert': 'USD'
        }
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': key,
        }

        session = Session()
        session.headers.update(headers)

        try:
            response = session.get(url, params=parameters)
            data = json.loads(response.text)
            data = data['data']
            for dict in data:
                if dict['symbol'] == currency:
                    return round(float(dict['quote']['USD']['price']), 3)

        except (ConnectionError, Timeout, TooManyRedirects, KeyError, ValueError) as e:
            print(e)


def setup(bot):
    bot.add_cog(General(bot=bot))
