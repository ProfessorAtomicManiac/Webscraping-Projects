from urllib.request import urlopen
from io import StringIO
import csv

#python HW_4_Part_2.py

textpage = urlopen('http://pythonscraping.com/files/MontyPythonAlbums.csv')\
           .read().decode('ascii', 'ignore')

dataFile = StringIO(textpage) # Convert to string
csvReader = csv.reader(dataFile)

array=[]
for column in csvReader:
    print(column[1])
    array.append(column[1])


firstpop = 0
lastpop = 13

del array[firstpop]
for i in range(1, 8):
    del array[firstpop]
    del array[lastpop]
    lastpop-=2

print(array)
