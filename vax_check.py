import json
import smtplib
import time
import webbrowser
from datetime import datetime
from email.message import EmailMessage
from urllib.request import urlopen

import config

# Javits Center both Pfizer and J&J
PROVIDER_IDS = [1000, 1019]
URL = 'https://am-i-eligible.covid19vaccine.health.ny.gov/api/list-providers'
URL_PRESCREENER = 'https://am-i-eligible.covid19vaccine.health.ny.gov/Public' \
                  '/prescreener '


def send_email(provider_name, vaccine_brand):
    msg = EmailMessage()
    msg['Subject'] = 'Vax appointment available at {} - {}'.format(
        provider_name,
        vaccine_brand)
    msg['From'] = 'VaxCheckNYC'
    msg['To'] = config.gmail
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(config.gmail, config.password)
    s.send_message(msg)
    s.quit()


def check(provider_ids):
    response = urlopen(URL)
    response_json = json.load(response)

    providers = response_json['providerList']
    for provider in providers:
        if provider['providerId'] in provider_ids:
            available_apts = provider['availableAppointments']
            if available_apts not in ['NAC', 'N']:
                now = datetime.now().strftime('%B %d, %Y %H:%M:%S')
                print('Appointments available!', now)
                webbrowser.open(URL_PRESCREENER)
                send_email(provider['providerName'], provider['vaccineBrand'])
            else:
                print('No appointments at {} - {} '.format(
                    provider['providerName'],
                    provider['vaccineBrand']))


if __name__ == '__main__':
    while True:
        time.sleep(3)
        check(PROVIDER_IDS)
