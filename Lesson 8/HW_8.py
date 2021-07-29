import pandas
from bs4 import BeautifulSoup
import requests
from flask import Flask

page = requests.get('https://indianapolis.craigslist.org/search/sss?query=computer&sort=rel&search_distance=10&postal=46033')
soup = BeautifulSoup(page.text, "html.parser")

productLn=[]
priceLn=[]

items = soup.find_all('li', class_='result-row')

for item in items:
    title = item.find('a', class_='result-title hdrlnk').text
    productLn.append(title)
    price = item.find('span', class_='result-price').text
    priceLn.append(price)

extractedData = pandas.DataFrame(
  {"Product": productLn,
   "Price": priceLn

})

extractedData.to_csv('craigHW.csv', index=False)
#Gets rid of the first column that just lists the numbers

app = Flask(__name__)

@app.route('/')
def showItems():
    items = pandas.read_csv(
        'C:\\Users\\djxgh\\Desktop\\Web Crawler\\Lesson 8\\craigHW.csv'
    )
    return '<h1> Hi, here are the items:</h1> ' + items.to_html()

if __name__ == '__main__':
    app.run()
