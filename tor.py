import sys
import requests
from bs4 import BeautifulSoup

# Create the session and set the proxies.
proxies = {'http': 'socks5://127.0.0.1:9050',
           'https': 'socks5://127.0.0.1:9050'}

s = requests.Session()
s.proxies = proxies

try:
    r = s.get('https://check.torproject.org/')
except requests.ConnectionError as e:
    print("OOPS!! Connection Error.")
    regular = requests.get('https://check.torproject.org/')
    BS = BeautifulSoup(regular.text, "html.parser")
    METATAG = BS.select('h1.off')[0].text.strip()
    print(METATAG)
except requests.Timeout as e:
    print("OOPS!! Timeout Error")
except requests.RequestException as e:
    print("OOPS!! General Error")
except KeyboardInterrupt:
    print("Ok ok, quitting")
    sys.exit(1)
else:
    print(r.url + " - Reading URL")
    BS = BeautifulSoup(r.text, "html.parser")
    METATAG = BS.select('h1.not')[0].text.strip()
    print(METATAG)
