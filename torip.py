#!/usr/bin/env python

import requests

def get_tor_session():
    session = requests.session()
    # Tor uses the 9050 port as the default socks port
    session.proxies = {'http':  'socks5://127.0.0.1:9050',
                       'https': 'socks5://127.0.0.1:9050'}
    return session

# Make a request through the Tor connection
session = get_tor_session()
print('IP Given by TOR')
print(session.get("https://api.ipify.org/").text)

# Following prints your normal public IP
print('Your Public IP')
print(requests.get("https://api.ipify.org/").text)
