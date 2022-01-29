import requests


def currency_rates(code: str) -> float:
    """возвращает курс валюты `code` по отношению к рублю"""
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    currency_dict = {}
    currency_list = response.text.split('ID=')
    del currency_list[0]
    for element in currency_list:
        exchange_rate = element[(element.find('<Value>') + 7):element.find('</Value>')]
        exchange_rate = float(exchange_rate.replace(',', '.'))
        amendment = int(element[(element.find('<Nominal>') + 9):element.find('</Nominal>')])
        currency_dict[(element[(element.find('<CharCode>')+10):element.find('</CharCode>')])] = exchange_rate/amendment
    result_value = currency_dict.get(code.upper(), None)
    return result_value


print(currency_rates("USD"))
print(currency_rates("eur"))
print(currency_rates("AMD"))
print(currency_rates("noname"))
