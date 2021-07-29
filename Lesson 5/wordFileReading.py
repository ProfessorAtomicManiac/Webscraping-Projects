from zipfile import ZipFile
from urllib.request import urlopen
from bs4 import BeautifulSoup
from io import BytesIO
import lxml

# python wordFileReading.py

"""
byteFile = BytesIO(wordFile)
document = ZipFile(byteFile)
"""

wordFile = urlopen('http://pythonscraping.com/pages/AWordDocument.docx').read()
byteFile = BytesIO(wordFile) # In binary code
document = ZipFile(byteFile) # convert to zip file
xmlContent = document.read('word/document.xml') # security for sending files. Its like html
wordObj = BeautifulSoup(xmlContent.decode('utf-8'), 'lxml') # makes it readable
textObjs = wordObj.find_all('w:t') # w:t looks for all text in a word document
for txt in textObjs:
    print(txt.text)
