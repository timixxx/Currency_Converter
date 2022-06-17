from django import forms
import json
import requests

rates_url = 'https://api.exchangerate.host/latest?base=USD?symbols=RUB'

class MoneySum(forms.Form):
    amount = forms.FloatField()

    def exchange(self, amount):
        response = requests.get(rates_url)
        rates = (response).json()
        rub_rate = rates['rates']['RUB']

        return amount * rub_rate

    def get_current(self):
        response = requests.get(rates_url)
        rates = (response).json()
        rub_rate = rates['rates']['RUB']

        return rub_rate
