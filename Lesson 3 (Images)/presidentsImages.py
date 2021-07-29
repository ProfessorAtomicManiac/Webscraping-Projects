from bs4 import BeautifulSoup
import requests
import pandas as pd
import urllib

#python presidentsImages.py

page = requests.get('https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States')

soup = BeautifulSoup(page.content, 'html.parser')

tb = soup.find('table', {"class": "wikitable"})

filename = 1
for link in tb.find_all('img'):
    url = link['src'] # in brackets cuz its not a function
    print(url)
    imageFile = open(str(filename)+".jpeg", 'wb') # wb = Write Bytes
    url = "https:" + url
    imageFile.write(urllib.request.urlopen(url).read())
    imageFile.close()
    filename += 1
