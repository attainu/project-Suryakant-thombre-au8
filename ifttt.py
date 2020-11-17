import requests


ifttt_webhook_url = 'https://maker.ifttt.com/trigger/Bitcoin_price_alert/with/key/dckC6CkdtaRaDDjgLtl64LXBoNbC1sW98e9ZfthRLUx'

requests.post(ifttt_webhook_url)
# 

def post_to_ifttt_webhook(event, value):

    # The payload that will be sent to IFTTT service
    data = {'value1': value}
    ifttt_event_url = ifttt_webhook_url.format(
        event)  # Inserts our desired event
    # Sends a HTTP POST request to the webhook URL
    requests.post(ifttt_event_url, data=data)