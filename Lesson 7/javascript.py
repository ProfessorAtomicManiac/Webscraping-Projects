from selenium import webdriver

url = "http://www.webscrapingfordatascience.com/complexjavascript/"
driver = webdriver.Chrome() # .exe file must be in the same folder as the python script
"""driver = webdriver.Chrome(executable_path="C:\\Chrome\\chromedriver.exe")
which lists the file's location. This computer's webdriver is in PATH"""

driver.implicitly_wait(10) # sometimes the page doesn't load yet
driver.get(url)
# quote is found in the css part of the website
quotes = driver.find_elements_by_class_name('quote')
# It is a list object
for quote in quotes:
    print(quote.text)
