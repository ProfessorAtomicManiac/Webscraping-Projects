import pandas
from bs4 import BeautifulSoup
import requests

page = requests.get('https://ncov2019.live/')
soup = BeautifulSoup(page.text, "html.parser")

countryTable = soup.find('element_to_be_clickable', class_='sortable_table_world')

for item in items:
    title = item.find('a', class_='result-title hdrlnk').text
    productLn.append(title)
    price = item.find('span', class_='result-price').text
    priceLn.append(price)

extractedData = pandas.DataFrame(
  {"Product": productLn,
   "Price": priceLn

})

extractedData.to_csv('craig.csv', index=False)
#Gets rid of the first column that just lists the numbers
