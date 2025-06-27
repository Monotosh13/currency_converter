# converter.py

import requests

class CurrencyConverter:
    def __init__(self, api_url="https://api.exchangerate-api.com/v4/latest/USD"):
        self.api_url = api_url
        self.rates = self.get_rates()

    def get_rates(self):
        """Fetches the latest exchange rates from the API."""
        response = requests.get(self.api_url)
        data = response.json()
        return data["rates"]

    def convert(self, amount, from_currency, to_currency):
        """Converts amount from one currency to another."""
        if from_currency != "USD":
            amount = amount / self.rates[from_currency]
        return round(amount * self.rates[to_currency], 2)
#Notes:

#    CurrencyConverter class fetches exchange rates on initialization.

#    get_rates() pulls rates from the API.

#    convert() handles conversion between any two currencies.
