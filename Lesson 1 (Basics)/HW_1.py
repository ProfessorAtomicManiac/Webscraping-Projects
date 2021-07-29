import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.pbs.org/shows")

soup = BeautifulSoup(page.content, 'html.parser')

items = soup.find_all('li', {'class': "shows-dropdown__popular-show"})

for l in items:
  print(l.text)