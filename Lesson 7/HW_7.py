from selenium import webdriver
from bs4 import BeautifulSoup
import requests

driver = webdriver.Chrome()

for i in range(1, 51):
    url = "http://books.toscrape.com/catalogue/page-{}.html".format(i)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    books = soup.find_all('article', {'class':'product_pod'})
    for book in books:
        rating4 = book.find('p', {"class": "star-rating Four"})
        rating5 = book.find('p', {"class": "star-rating Five"})
        if (rating4 != None):
            bookUrl = book.find_all('a')
            urlbook = bookUrl[0].attrs['href']

            page = requests.get('http://books.toscrape.com/catalogue/{}'.format(urlbook))
            pageDriver = ('http://books.toscrape.com/catalogue/{}'.format(urlbook))

            # This is not necessary but I used it to make sure that the books were 4/5-stars
            driver.implicitly_wait(10)
            driver.get(pageDriver)

            soup2 = BeautifulSoup(page.text, "html.parser")
            summary = soup2.find_all('p')
            print(summary[3].text)

        elif (rating5 != None):
            bookUrl = book.find_all('a')
            urlbook = bookUrl[0].attrs['href']

            page = requests.get('http://books.toscrape.com/catalogue/{}'.format(urlbook))
            pageDriver = ('http://books.toscrape.com/catalogue/{}'.format(urlbook))

            # This is not necessary but I used it to make sure that the books were 4/5-stars
            driver.implicitly_wait(10)
            driver.get(pageDriver)
            soup2 = BeautifulSoup(page.text, "html.parser")

            summary = soup2.find_all('p')
            print(summary[3].text)

        else:
            continue
