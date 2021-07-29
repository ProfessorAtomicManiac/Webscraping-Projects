from bs4 import BeautifulSoup
import requests
import pandas as pd
import urllib
import sys
from PIL import Image
#python HW_3_Part_2.py

page = requests.get('https://en.wikipedia.org/wiki/List_of_national_parks_of_the_United_States')

soup = BeautifulSoup(page.content, 'html.parser')

table = soup.find('table', {"class": "wikitable sortable plainrowheaders"})

rows = table.find_all('tr')

filename = 1

for i in range(1, len(rows)):
    row = rows[i].find_all('td', {"scope": ""})
    img = row[0]
    print(img)
    for link in img.find_all('img'):
        url = link['src']
        imageFile = open(str(filename)+".jpeg", 'wb')
        url = "https:" + url
        imageFile.write(urllib.request.urlopen(url).read())
        imageFile.close()
        filename += 1
