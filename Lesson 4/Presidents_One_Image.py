import requests
from bs4 import BeautifulSoup
import pandas as pd
import urllib

# New Libraries
import sys
from PIL import Image

#python Presidents_One_Image.py

url = "https://en.wikipedia.org/wiki/List_of_Presidents_of_the_United_States"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
tb = soup.find('table', class_='wikitable')

url=[]
filename = 1
mainURL = "https:"
for link in tb.find_all('img'):
    url = link['src']
    if (url):
        url = mainURL + url
        print(url)
        imagefile = open(str(filename)+".jpg", 'wb')
        imagefile.write(urllib.request.urlopen(url).read())
        imagefile.close()
        filename +=1

# New Code
images=[]
for i in range(1, 46):
    fname = str(i) +".jpg"
    images.append(Image.open(fname))

newImage = Image.new('RGB', (1400, 1000))


xPos = 0
yPos = 0
for i in range(len(images)):
    newImage.paste(images[i], (xPos, yPos))
    xPos += images[i].size[0] # size[0] is width, siz[1] is height

    # Moves Presidents to a new row when image runs out of space
    if (i%9 == 8):
        xPos = 0
        yPos += images[i].size[1]

newImage.save("Presidents.jpg")
