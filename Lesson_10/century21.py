import requests
from bs4 import BeautifulSoup
import pandas
import matplotlib.pyplot as plt

addresses = []
prices = []
numBeds = []

for i in range(0, 5):
    try:
        url = 'https://www.century21.com/real-estate/carmel-in/LCINCARMEL/?s={}'.format(i*20)
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")

        houses = soup.find_all('div', class_='property-card-primary-info')
        for house in houses:
            price = house.find('a', class_="listing-price").text
            price = price.replace('\n', '')
            price = price.strip()
            price = price.replace('$', '')
            price = price.replace(',', '')
            bed = house.find('div', class_="property-beds")
            if (bed == None):
                bed = 'N/A'
            else:
                bed = bed.text
                bed = bed.replace('\n', '')
                bed = bed.strip()
            address = house.find('div', class_="property-address").text
            address = address.replace('\n', '')
            address = address.strip()
            #print(address, price, bed)
            addresses.append(address)
            prices.append(int(price))
            numBeds.append(bed)
    except:
        print("error")

housesdf = pandas.DataFrame(
    {
        'Address': addresses,
        'Price': prices,
        'Beds': numBeds
    })
#print(housesdf)
housesdf.to_csv('carmelHouses.csv')

housesdf.hist(column="Price")
housesdf.plot.bar() #As to change the graph units/stuff like that, you should be look up the documentation
plt.show()
