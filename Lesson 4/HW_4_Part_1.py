from bs4 import BeautifulSoup
import requests
import urllib
import sys
from PIL import Image
#python HW_4_Part_1.py

page = requests.get('https://en.wikipedia.org/wiki/List_of_national_parks_of_the_United_States')

soup = BeautifulSoup(page.content, 'html.parser')

table = soup.find('table', {"class": "wikitable sortable plainrowheaders"})

rows = table.find_all('tr')

filename = 1

for i in range(1, len(rows)):
    row = rows[i].find_all('td', {"scope": ""})
    img = row[0]
    print(img)
    for link in img.find_all('img'):
        url = link['src']
        imageFile = open(str(filename)+".jpeg", 'wb')
        url = "https:" + url
        imageFile.write(urllib.request.urlopen(url).read())
        imageFile.close()
        filename += 1

images=[]
for i in range(1, 62):
    fname = str(i) +".jpeg"
    images.append(Image.open(fname))

newImage = Image.new('RGB', (1400, 970))


xPos = 0
yPos = 0
for i in range(len(images)):
    newImage.paste(images[i], (xPos, yPos))
    xPos += images[i].size[0] # size[0] is width, siz[1] is height

    # Moves Presidents to a new row when image runs out of space
    if (i%9 == 8):
        xPos = 0
        yPos += images[i].size[1]

newImage.save("Parks.jpg")
