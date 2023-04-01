import os
import time
from datetime import datetime

import urllib.request
from bs4 import BeautifulSoup

URL = "https://www.rijksmuseum.nl/"
VERMEER_URL = "https://www.rijksmuseum.nl/nl/tickets?variantKey=e6486c94-1206-48af-1c8f-08da8a58df4b"
FETCH_INTERVAL = 30 #secs
MAINTENANCE_TEXT = "The Rijksmuseum website is currently undergoing maintenance"
CLOSE_TEXT = "Tijdelijk gesloten"

def fetch_website(url):
    soup = BeautifulSoup(urllib.request.urlopen(url = url, timeout = 3), features="html.parser")
    return soup

while True:
    print(f"start parsing {datetime.now()}")
    try:
        soup = fetch_website(VERMEER_URL)
        if MAINTENANCE_TEXT in str(soup):
            print("under maintenance...")
        elif CLOSE_TEXT in str(soup):
            print("TEMPORARILY CLOSED")
        else:
            os.system('say "Vermeer update, it is live now"')
    except Exception as e:
        print("exception", e)

    time.sleep(FETCH_INTERVAL)
