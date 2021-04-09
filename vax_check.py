import glob
import json
import pickle
import smtplib
import time
import webbrowser
from datetime import datetime
from email.message import EmailMessage
from urllib.request import urlopen

import config

PROVIDER_IDS = [1000, 1019]
URL = 'https://am-i-eligible.covid19vaccine.health.ny.gov/api/list-providers'
URL_PRESCREENER = 'https://am-i-eligible.covid19vaccine.health.ny.gov/Public' \
                  '/prescreener '
DEBUG = True
PICKLED_PATH = 'providers*.pkl'


def pickle_response(response):
    with open(PICKLED_PATH, 'wb') as handle:
        pickle.dump(response, handle, pickle.DEFAULT_PROTOCOL)


def unpickle_response():
    paths = glob.glob(PICKLED_PATH)
    path = paths[0]
    with open(path, 'rb') as handle:
        response = pickle.load(handle)
    return response


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
    if DEBUG:
        pickle_response(providers)
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
