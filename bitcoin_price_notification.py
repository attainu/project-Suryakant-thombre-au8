import sys
import time
from datetime import datetime
from api_data import get_latest_bitcoin_price, price_limit, currency, alert_interval, platform
from ifttt import post_to_ifttt_webhook
from time import sleep

# Price Threshold
limit = price_limit

#funtions to print data in different colors
def print_red(skk):
    print("\033[91m {}\033[00m" .format(skk))


def print_green(skk):
    print("\033[92m {}\033[00m" .format(skk))


def print_yellow(skk):
    print("\033[93m {}\033[00m" .format(skk))


def print_cyan(skk):
    print("\033[96m {}\033[00m" .format(skk))


def print_purple(skk):
    print("\033[94m {}\033[00m" .format(skk))


def bitcoin_server_interface():
    print_green(""" BITCOIN_PRICE_NOTIFICATION """)
    print_cyan("""You can choose from variety of currencies for your alerts
            Try one of the following
        """)
    print_cyan(""" USD >>> US Dollars""")
    print_green(" INR >>> Indian Rupee")
    print_red(" EUR >>> Euros")
    print_yellow(" CNY >>> Chinese Yuan Renminbi")
    print_purple(" GBP >>> UK Pound Sterling")
    print(""" You will start getting notifications via """ + platform)


bitcoin_server_interface()


def main():
    alert_number = 0

    while True:
        # Prints Alert Data in console
        rate = get_latest_bitcoin_price()
        date = datetime.now()

        # Prints Current Rate
        print(" Current Rate "+"in " + currency.upper()+" ==>", )
        print_red("%.2f" % rate)

        # Prints alert date
        print(" Alert date ==>", )
        alert_date = datetime.now().strftime('%d.%m.%Y')
        print_yellow(alert_date)

        # Prints alert time
        alert_time = datetime.now().strftime('%H:%M:%S')
        print(" Alert time ==>", )
        print_cyan(alert_time)

        # Prints Alert number
        alert_number += 1
        print(" Alert number :", alert_number)
        print(" *********************************")

        # Send a alert in case rate is below limit
        # Sends Alert to telegram Channel
        if platform.lower() == 'telegram' and rate < limit:
            post_to_ifttt_webhook(
                'Bitcoin_price_alert', rate)

        # Sends Alert to email
        if platform.lower() == 'email' and rate < limit:
            post_to_ifttt_webhook(
                'bitcoin_price_update_email', "%.2f" % rate)

        # Sleep period between two notifications
        time.sleep(alert_interval * 30)


if __name__ == '__main__':
    main()