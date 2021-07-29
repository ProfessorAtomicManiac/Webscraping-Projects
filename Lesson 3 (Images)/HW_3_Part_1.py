from bs4 import BeautifulSoup
import requests
import pandas as pd
import urllib

#python HW_3.py

page = requests.get('https://en.wikipedia.org/wiki/AFI%27s_100_Years...100_Movies')

soup = BeautifulSoup(page.content, 'html.parser')

tb = soup.find('table', {"class": "sortable wikitable"})

rows = tb.find_all('tr')
for i in range(1, len(rows)):
    content = rows[i].find_all('a')
    movie = content[0].text
    print(movie)
