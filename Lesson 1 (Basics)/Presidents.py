from bs4 import BeautifulSoup
import requests
import pandas

page = requests.get('https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States')

soup = BeautifulSoup(page.content, 'html.parser')

table = soup.find('table', {'class': "wikitable"})
row = table.find_all('tr')
print(row.text)