from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import argparse

parser = argparse.ArgumentParser(description='Bitcoin Alert Help')

# Parsed command line arguments
# Currency argument with USD as default value
parser.add_argument('currency', nargs='?', type=str, default='USD',
                    help='Currency Code eg: USD ,INR')

# Limit argument with 10000$ as default value
parser.add_argument('limit', nargs='?', type=int, default=10000,
                    help='Price Limit eg: 1000')

# interval argument with 0.1 minutes as default value
parser.add_argument('interval', nargs='?', type=float, default=0.1,
                    help='Alert Interval(in minutes) eg:5')

# Platform argument with Telegram as default value
parser.add_argument('platform', nargs='?', type=str, default='telegram',
                    help='Destination(Platform where you want the notification) eg: Telegram,Twitter')
args = parser.parse_args()

# Storing all arguments in differnt variable for usage convenience
currency = args.currency
price_limit = args.limit
alert_interval = args.interval
platform = args.platform

# API url for fetching cryptocurrency data
bitcoin_api_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
# Parameters to get desired data from API
parameters = {
    'start': '1',
    'limit': '2',
    'convert': currency.upper()
}
# data type and API key to fetch data
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '7d860567-c929-46f6-bca3-a11b2c0bba6e',
}

session = Session()
session.headers.update(headers)


def get_latest_bitcoin_price():
    try:
        response = session.get(bitcoin_api_url, params=parameters)
        data = json.loads(response.text)
        return float(data["data"][0]['quote'][currency.upper()]['price'])
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)