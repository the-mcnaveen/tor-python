#!/usr/bin/env python

import sys
import requests

# Create the session and set the proxies.
proxies = {'http': 'socks5://127.0.0.1:9050',
           'https': 'socks5://127.0.0.1:9050'}

s = requests.Session()
s.proxies = proxies

try:
    ## User input
    LINK = input('\033[1;32mEnter a URL: = \033[1;m')
    r = s.get(LINK)
except requests.ConnectionError as e:
    print("OOPS!! Connection Error")
except requests.Timeout as e:
    print("OOPS!! Timeout Error")
except requests.RequestException as e:
    print("OOPS!! General Error (Enter a Valid URL) - Add HTTP/HTTPS infront of the URL")
except KeyboardInterrupt:
    print("Ok ok, quitting")
    sys.exit(1)
else:
    print(r.url + " - is an Current Live and Active URL")
