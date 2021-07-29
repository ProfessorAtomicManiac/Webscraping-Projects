from zipfile import ZipFile
from urllib.request import urlopen
from bs4 import BeautifulSoup
from io import BytesIO

import PyPDF2

#python PDFreader.py

"""
pdfFile = open('document.pdf', 'rb')
pdfReader = PyPDF2.PdFileReader(pdFile)
"""

pdfFile = urlopen('http://pythonscraping.com/pages/warandpeace/chapter1.pdf')
# No need to use .read
file = open("chapter1.pdf", "wb") # wb = written bytes
file.write(pdfFile.read())
file.close() #It is like downloading an image file

"""YOU MUST USE ADOBE ACROBAT IN ORDER TO READ THE FILE
OR ELSE IT WILL LOOK LIKE A BUNCH OF SCRAMBED EGGS
OTHERWISE DO THIS:"""

pdfFile = open("chapter1.pdf", "rb") # rb = reading bytes
pdfReader = PyPDF2.PdfFileReader(pdfFile)

print(pdfReader.numPages) # self-explainable
""" There are 7 pages but it is numbered like this:
0, 1, 2, 3, 4, 5, 6"""

# must seperates them into pages to extract text
for i in range(pdfReader.numPages): # for loop starts at 0
    pageObj = pdfReader.getPage(i)
    print(pageObj.extractText())

pdfFile.close() # to prevent file damage
