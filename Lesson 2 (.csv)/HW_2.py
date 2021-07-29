# service@easyfuncoding.com

from bs4 import BeautifulSoup
import requests
import pandas

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=39.97839000000005&lon=-86.12612999999999#.XpnJichKiUl')

soup = BeautifulSoup(page.content, 'html.parser')

ul = soup.find('ul', {"id": "seven-day-forecast-list"})

periodList=[]
descList=[]
tempList=[]

# period

period = ul.find_all('p', {"class": "period-name"})

for l in period:
  periodList.append(l.text)


# short desc

desc = ul.find_all('p', {"class": "short-desc"})

for l in desc:
  descList.append(l.text)


# temperature
hightemp=[]
lowtemp=[]
temp_high = ul.find_all('p', {"class": "temp temp-high"})
temp_low = ul.find_all('p', {"class": "temp temp-low"})

for l in temp_high:
  hightemp.append(l.text)

for l in temp_low:
  lowtemp.append(l.text)

for i in range(4):
  tempList.append(hightemp[i])
  tempList.append(lowtemp[i])

tempList.append(hightemp[4])

# CSV File

extractedData = pandas.DataFrame(
  {"Period": periodList,
   "Short Description": descList,
   "Temperature": tempList

})

extractedData.to_csv('weather.csv')
