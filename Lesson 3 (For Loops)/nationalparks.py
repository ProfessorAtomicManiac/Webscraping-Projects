from bs4 import BeautifulSoup
import requests
import pandas as pd

#python nationalparks.py

page = requests.get('https://en.wikipedia.org/wiki/List_of_national_parks_of_the_United_States')

soup = BeautifulSoup(page.content, 'html.parser')

table = soup.find('table', {"class": "wikitable sortable plainrowheaders"})

parkNames = []
states = []

# This gets each row which is stored in an array
rows = table.find_all('tr')
for i in range(1, len(rows)):
    # This will get every 'a' tag in each row 'i'. One from the 1st row, another from the second row, etc
    links = rows[i].find_all('a')
    parkName = links[0].text
    state = links[2].text
    parkNames.append(parkName)
    states.append(state)
    #print(parkName, state)

parks = pd.DataFrame(
    {'Park Name': parkNames,
     'Location': states})
parks.to_csv('parks.csv')
