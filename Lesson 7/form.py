import requests

form = {'firstname': 'man', 'lastname': 'guy'}
page = requests.post("http://pythonscraping.com/pages/files/processing.php", \
                     data = form) # Not .get()
print(page.text)
