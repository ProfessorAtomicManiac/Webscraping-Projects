from urllib.request import urlopen
from bs4 import BeautifulSoup

# python navigator.py

startPage="https://en.wikipedia.org/"

pages = set()

def getPage(url): #function getting defined
    try:
        if not url.startswith('http'):
            url = startPage+url
        page= urlopen(url)
        print(url)
        soup = BeautifulSoup(page,'html.parser')
        for link in soup.find_all('a'):
            if 'href' in link.attrs:
                if (link.attrs['href'] not in pages):
                    pages.add(link.attrs['href'])
                    if (len(pages)>100): # pages it has seen, not length of href cuz otherwise it will run forever
                        break
                    getPage(link.attrs['href'])
    except:
        return
        """ It tries the code inside the try thingy,
            but if you get 404 error (runtime error)
            then you can return and try again"""

getPage("")
