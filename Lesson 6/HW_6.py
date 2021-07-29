import requests
from bs4 import BeautifulSoup
import requests

url = 'https://www.imdb.com/search/title/?series=tt0285335&view=simple&sort=release_date,asc&start=1'
bru = 'https://www.imdb.com/search/title/?series=tt0285335&view=simple&sort=release_date,asc&start=51'
for pg in range(1, 362, 50):
    page = requests.get(url, params={})


soup = BeautifulSoup(page.content, 'html.parser')

table = soup.find('table', {"class": "wikitable sortable plainrowheaders"})
