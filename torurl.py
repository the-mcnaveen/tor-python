import sys
import time
import requests
import cloudscraper
from halo import Halo

# Create the session and set the proxies.
proxies = {'http': 'socks5://127.0.0.1:9050',
           'https': 'socks5://127.0.0.1:9050'}

# User Agent
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'}

# Start Session
s = cloudscraper.create_scraper() # https://github.com/Anorov/cloudflare-scrape/issues/103
# Proxy Connection
s.proxies = proxies
# Bypass Cloudflare Enabled website - https://support.cloudflare.com/hc/en-us/articles/203306930-Does-Cloudflare-block-Tor-
scraper = cloudscraper.create_scraper(sess=s, delay=10)
# Terminal Spinner
spinner = Halo(text='Fetching...', color='cyan')

try:
    LINK = input('Enter a URL: ')
    spinner.start()
    time.sleep(5)
    spinner.text = 'Reading the Given URL...'
    response = scraper.get(LINK, headers=headers)
    time.sleep(5)
    spinner.stop()
except requests.URLRequired as e:
    spinner.start()
    time.sleep(2)
    spinner.color = 'red'
    spinner.text = 'URL Error - Empty URL or Wrong URL'
    time.sleep(2)
    spinner.fail('URL Validation Error')
    spinner.stop()
    print("OOPS!! Connection Error - May be the URL is Not Valid or Can't Bypass them")
except requests.Timeout as e:
    print("OOPS!! Timeout Error")
except requests.RequestException as e:
    spinner.start()
    time.sleep(2)
    spinner.color = 'red'
    spinner.text = 'Wrong URL or Empty Field'
    time.sleep(2)
    spinner.fail('Wrong URL or Empty Field')
    spinner.stop()
    print("OOPS!! General Error (Enter a Valid URL) - Add HTTP/HTTPS infront of the URL")
except (KeyboardInterrupt, SystemExit):
    spinner.stop()
    print("Ok ok, quitting")
    sys.exit(1)
else:
    if response.history:
        print("URL was redirected")
    for resp in response.history:
        print(resp.status_code, resp.url)
        print("Final destination:")
        print(response.status_code, response.url)
        break
    else:
        print(response.status_code, response.url + " - Current Live and Active URL")
