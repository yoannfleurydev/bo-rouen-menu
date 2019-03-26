#!/usr/bin/env python3

"""
Get the BO menu from your command line
"""

import datetime

from urllib.request import urlopen
from bs4 import BeautifulSoup

URL = "https://www.blockout.fr/bo-rouen/restaurant"

PAGE = urlopen(URL)
SOUP = BeautifulSoup(PAGE, "html.parser")

DAYS = SOUP.select('#sp-page-builder span[style="font-size: 14pt;"]')

_, MONDAY, _, TUESDAY, _, *OTHERS = DAYS
WEDNESDAY, _, THURSDAY, _, FRIDAY, *_ = OTHERS

TITLES = ('Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi')
DAYS = (MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY)

WEEKDAY = datetime.datetime.today().weekday()

print("🗓️ " + TITLES[WEEKDAY] + "\\n🍽️ " + DAYS[WEEKDAY].contents[0].string.strip() + "\\n🥧 " + DAYS[WEEKDAY].contents[1].string + "\\n")

