from urllib.request import urlopen
from io import StringIO
import csv

#python matthewDu_Part2.py

textpage = urlopen('http://pythonscraping.com/files/MontyPythonAlbums.csv')\
           .read().decode('ascii', 'ignore')

dataFile = StringIO(textpage)
csvReader = csv.reader(dataFile)

array = []
for column in csvReader:
    print(column[1])
    array.append(column[1])


first = 0
last = 13

del array[first]
for i in range(1, 8):
    del array[first]
    del array[last]
    last -=2

print(array)
