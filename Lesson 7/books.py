from bs4 import BeautifulSoup
import requests
import pandas

titles=[]
prices=[]

for i in range(1, 51):
    url = "http://books.toscrape.com/catalogue/page-{}.html".format(i)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    books = soup.find_all('article', {'class':'product_pod'})
    for book in books:
        title = book.find('h3').find('a')['title']
        price = book.find('p', class_='price_color').text
        priceClean = ' '.join(i for i in price if i.isdigit() or i=='.')
        print(title, " " , priceClean)

bookData = pandas.DataFrame(
    {"Title": title,
     "Price": price

})

bookData.to_csv('books.csv')

"""
page = requests.get('http://books.toscrape.com/')

soup = BeautifulSoup(page.content, 'html.parser')

ol = soup.find('ol', {"class": "row"})

li = ol.find_all('li')

titleLn=[]
priceLn=[]

for i in li:
    title = i.find('h3').text
    price = i.find('p', {"class": "price_color"}).text
    print(title)
    print(price)
    titleLn.append(title)
    priceLn.append(price)

extractedData = pandas.DataFrame(
    {"Title": titleLn,
     "Price": priceLn

})

extractedData.to_csv('books.csv')
"""
