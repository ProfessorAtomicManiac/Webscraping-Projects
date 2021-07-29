import PyPDF2
import requests
from PyPDF2 import PdfFileMerger
from bs4 import BeautifulSoup
from io import BytesIO
from urllib.request import urlopen

# python WarAndPeacePDF.py

page = requests.get('https://www.cs.iupui.edu/~yuxia/WebCrawler/WarAndPeace.html')
soup = BeautifulSoup(page.content, 'html.parser')

filename = 0
for link in soup.find_all('a'):
    url = link['href']
    pdfFile = urlopen(url)
    file = open(str(filename)+".pdf", "wb")
    file.write(pdfFile.read())
    file.close()
    filename+=1

pdfMerger = PyPDF2.PdfFileMerger()
for i in range(filename):
    pdfMerger.append(PyPDF2.PdfFileReader(str(i)+".pdf"), 'rb')

with open("Merged.pdf", 'wb') as f: # Automatically closes the file
    pdfMerger.write(f)

pdfFile = open("Merged.pdf", "rb") # rb = reading bytes
pdfReader = PyPDF2.PdfFileReader(pdfFile)

print(pdfReader.numPages)


for i in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(i)
    print(pageObj.extractText())

pdfFile.close()

"""
file = open("Merged.pdf", "wb")
pdfMerger.write(file)
file.close()
"""

#----------------------------------------------------------------

pdfmerge = PdfFileMerger()

for i in range(1, 11):
    break
    # This method also works
    """filename = "Chapter"+str(i)+'.pdf'
    pdf = urlopen('https://www.cs.iupui.edu/~yuxia/WebCrawler/WarAndPeace'+filename)
    file = open('pdf/'+filename, 'wb')
    file.write(pdf.read())
    file.close()
    pdfmerge.append('pdf/'+filename)"""
"""
pdfmerge.write('AllChapters.pdf')
pdfmerge.close()"""
