from urllib.request import urlopen
from io import StringIO
import csv

# python Albums.py

textpage = urlopen('https://www.pythonscraping.com/files/MontyPythonAlbums.csv')\
           .read().decode('ascii', 'ignore') # Converts to AXCII, ignores errors

dataFile = StringIO(textpage) # Convert to string
csvReader = csv.reader(dataFile)

for row in csvReader:
  print(row[0], row[1]) # prints each row since CSV has rows and columns
