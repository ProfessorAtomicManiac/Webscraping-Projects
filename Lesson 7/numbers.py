from selenium import webdriver

url = "https://www.cs.iupui.edu/~yuxia/WebCrawler/JavascriptExample.html"
driver = webdriver.Chrome()

driver.implicitly_wait(10) # sometimes the page doesn't load yet
driver.get(url)
# quote is found in the css part of the website
num = driver.find_element_by_id('txt')
# Not a list object
print(num.text)
