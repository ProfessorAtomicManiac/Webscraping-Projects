import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.nba.com/players")

soup = BeautifulSoup(page.content, 'html.parser')

box = soup.find('section', {'class': "row nba-player-index__row"})

for l in (soup.find_all('p', {'class': "nba-player-index__name"})):
	print(l.contents[0], " ", l.contents[2])

for role in (soup.find_all('div', {'class': "nba-player-index__details"})):
	print(role.contents[0].text)
	print(role.contents[1].text)
	extractedData = pandas.DataFrame{
    		{"First Name": fnList,
    		{"Last Name": lnList
  	})

  extractedData = pandas.Dataframe

# print(p.contents[0], " ", p.contents[2]) # becomes a list and includes tags but you can remove it
# details = p.nextsibling (Same level on html file but has to have the same parent element)
# print(details.text)