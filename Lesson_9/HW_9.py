from selenium import webdriver
import pandas
from flask import Flask, render_template

driver = webdriver.Chrome()

quotesList = []
author = []
tags = []

for i in range(1, 11):
    url = 'http://quotes.toscrape.com/js/page/{}'.format(i)
    driver.get(url)

    quotes = driver.find_elements_by_class_name('quote')
    for quote in quotes:
        quoteText = quote.find_element_by_class_name('text').text # Individual quote 'element' not 'elemnts'
        author = quote.find_element_by_class_name('author').text # for "find_element_by_class_name"
        tags = quote.find_element_by_class_name('tags').text

        # To remove special characters
        quoteText = quoteText.replace("“", "")
        quoteText = quoteText.replace("”", "")

        # Another method of converting to .cxv file also less memory
        OneQuote = (quoteText, author, tags)
        quotesList.append(OneQuote)

df = pandas.DataFrame(quotesList, columns=['Quote', 'Author', 'Tags'])

df.to_csv('quotes.csv', index=False)
