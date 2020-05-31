import requests


def get_data(crypto_symbol):
    url = f'https://rest.coinapi.io/v1/ohlcv/{crypto_symbol}/USD/history?period_id=1MTH&time_start=2016-01-01'
    headers = {
        'X-CoinAPI-Key': 'ADD91010-B20A-4DA6-A1F1-323C580AC5AF',
        'Accept': 'application/json',
        
    }
    response = requests.get(url, headers=headers)
    return response.json()