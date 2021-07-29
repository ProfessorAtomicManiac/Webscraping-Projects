from bs4 import BeautifulSoup
import requests
import pandas as pd

page = requests.get('http://www.pythonscraping.com/pages/page3.html')

soup = BeautifulSoup(page.content, 'html.parser')

tb = soup.find('table', {"id": "giftList"})
tr = tb.find_all('tr')
total = 0
nums = 0

for i in range(1, len(tr)):
    rows = tr[i].find_all('td')
    price = rows[2].text
    print(price)
    price = price.replace("$", "")
    price = price.replace(",", "")

    total += float(price)
    nums += 1

print("The average price is: ", total/nums)


#python averagecost.py
