from bs4 import BeautifulSoup
import requests
import urllib

#python warandpeace.py

page = requests.get('http://www.pythonscraping.com/pages/warandpeace.html')

soup = BeautifulSoup(page.content, 'html.parser')

char = soup.find_all('span', {"class": "green"})
print(len(char))

# You could also consider capitalization
princeCnt = soup.find_all(text="the prince")
print(len(princeCnt))
