#!/usr/bin/env python

import sys
import requests

# Create the session and set the proxies.
proxies = {'http': 'socks5://127.0.0.1:9050',
           'https': 'socks5://127.0.0.1:9050'}

s = requests.Session()
s.proxies = proxies

# Make a request through the Tor connection
try:
    r = s.get('https://api.ipify.org/')
except requests.ConnectionError as e:
    print("OOPS!! Connection Error - May be Tor is Not Enabled")
except requests.Timeout as e:
    print("OOPS!! Timeout Error")
except requests.RequestException as e:
    print("OOPS!! General Error")
except KeyboardInterrupt:
    print("Ok ok, quitting")
    sys.exit(1)
else:
    print('IP Given by TOR')
    print(r.text)

    print('Your Public IP')
    print(requests.get("https://api.ipify.org/").text)
