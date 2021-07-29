from selenium import webdriver
import pandas

driver = webdriver.Chrome()

quotesList = []

for i in range(1, 11):
    url = 'http://quotes.toscrape.com/js/page/{}' .format(i)
    driver.get(url)

    quotes = driver.find_elements_by_class_name('quote') # Multiple quotes so its a list
    for quote in quotes:
        print(quote.find_element_by_class_name('text'))
        quoteText = quote.find_element_by_class_name('text').text # Individual quote 'element' not 'elemnts'
        author = quote.find_element_by_class_name('author').text # for "find_element_by_class_name"

        # To remove special characters
        quoteText = quoteText.replace("“", "")
        quoteText = quoteText.replace("”", "")

        # Another method of converting to .cxv file also less memory
        OneQuote = (quoteText, author)
        quotesList.append(OneQuote)

df = pandas.DataFrame(quotesList, columns=['Quote', 'Author'])

df.to_csv('quotes.csv', index=False)
