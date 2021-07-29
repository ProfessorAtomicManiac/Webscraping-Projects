from urllib.request import urlopen

# python War_and_peace.py

textpage = urlopen('http://www.pythonscraping.com/pages/warandpeace/chapter1.txt')

print(textpage.read().decode('utf-8')) # .read gets the text and .decode reads the \n for example
