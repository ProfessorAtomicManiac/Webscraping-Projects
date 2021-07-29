from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen

pages = set()

def getPage(url): #function getting defined

    try:
        page= urlopen(url)
        print(url)
        soup = BeautifulSoup(page,'html.parser')
        for link in soup.find_all('a'):
            if 'href' in link.attrs:
                if (link.attrs['href'] == '/courses/75661'):
                    page = urlopen('https://carmel.instructure.com'+link.attrs['href'])
                    soup = BeautifulSoup(page, 'html.parser')
                    print(soup)
    except:
        return

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/76.0'
}

login_data = {
    'utf8': "✓",
    'authenticity_token': "xVcqrOXl641vSb+7tTYM+AbiO434xONFJnY6/2oyKK6NOBL5oIHA7loC59b2V36XUIRUwaqroHZkN13NAGFf7w==",
    'redirect_to_ssl': "1",
    'pseudonym_session[unique_id]':	"",
    'pseudonym_session[password]': "",
    'pseudonym_session[remember_me]': "0"
}

with requests.Session() as s:
    url = 'https://carmel.instructure.com/login/ldap'
    r = s.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    login_data['authenticity_token'] = soup.find('input', attrs={'name': 'authenticity_token'})['value']

    r = s.post('https://carmel.instructure.com/', login_data, headers)

    print(getPage('https://carmel.instructure.com/'))

"""
s = requests.Session()

s.post('https://carmel.instructure.com/login/ldap', headers, login_data)
#logged in! cookies saved for future requests.
r2 = s.get('https://carmel.instructure.com/?login_success=1')
print(r2)
#cookies sent automatically!
#do whatever, s will keep your cookies intact :)
"""
