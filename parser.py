import os
import time
from datetime import datetime

import urllib.request
from bs4 import BeautifulSoup

URL = "https://www.rijksmuseum.nl/nl/zien-en-doen/tentoonstellingen/vermeer"
URL_EN = "https://www.rijksmuseum.nl/en/whats-on/exhibitions/vermeer"
CURRENT_TEXT = "De belangstelling voor de tentoonstelling Vermeer is zeer groot. Op dit moment zijn er helaas geen tickets meer beschikbaar. Het Rijksmuseum werkt er hard aan meer mensen de gelegenheid te geven om de tentoonstelling te zien. Vanaf 6 maart geven we een nieuwe update via de website van het Rijksmuseum. "
FETCH_INTERVAL = 10 #secs
INTRO_ELEMENT_CLASS = "intro-text"
MAINTENANCE_TEXT = "The Rijksmuseum website is currently undergoing maintenance"

def fetch_website(url):
    soup = BeautifulSoup(urllib.request.urlopen(url = url), features="html.parser")
    return soup.find("p", class_=INTRO_ELEMENT_CLASS), soup

while True:
    print(f"start parsing {datetime.now()}")

    intro_element, soup = fetch_website(URL)
    if intro_element == None:
        if MAINTENANCE_TEXT in str(soup):
            print("under maintenance...")
        else:
            print("intro section is gone")
            os.system('say "Vermeer update, intro section is gone"')

    else:
        new_text = intro_element.text
        if new_text != CURRENT_TEXT:
            print(f"\n[DUTCH] {URL}\n{new_text}\n\n")
            os.system('say "Vermeer update"')

            intro_element, _ = fetch_website(URL_EN)
            print(f"[ENGLISH] {URL_EN}")
            # print new intro text in English if there's any
            if intro_element:
                print(f"{intro_element.text}\n\n")
                os.system('say "'+intro_element.text+ '"')

    time.sleep(FETCH_INTERVAL)
