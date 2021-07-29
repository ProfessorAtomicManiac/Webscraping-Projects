import requests
from bs4 import BeautifulSoup
from io import BytesIO
from io import StringIO
from urllib.request import urlopen
from zipfile import ZipFile

# python HW_5.py

page = requests.get('https://www.cs.iupui.edu/~yuxia/WebCrawler/WarAndPeaceWord.html')
soup = BeautifulSoup(page.content, 'html.parser')

filename = 0
for link in soup.find_all('a'):
    print(link)
    url = link['href']
    urlFile = urlopen(url).read()
    byteFile = BytesIO(urlFile)
    file = open(str(filename)+".docx", "wb")
    file.write(byteFile.read())
    file.close()
    filename+=1

    document = ZipFile(byteFile)
    """file = open(str(filename)+".docx", "wb")
    file.write(textObjs.read())
    file.close()
    filename+=1"""

    xmlContent = document.read('word/document.xml')
    wordObj = BeautifulSoup(xmlContent.decode('utf-8'), 'lxml')
    textObjs = wordObj.find_all('w:t')
    for txt in textObjs:
        print(txt.text)
