import requests

form = {'name': 'bruh', 'gender': 'M', 'pizza': 'like', 'fries': 'like', 'salad': '', 'haircolor': 'black', 'comments': 'bruh'}
page = requests.post("http://www.webscrapingfordatascience.com/postform2/", \
                     data = form) # Not .get()
print(page.text)
