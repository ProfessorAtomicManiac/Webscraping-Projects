# python3.7 powerschool.py
import requests
from bs4 import BeautifulSoup

link = 'https://powerschool.ccs.k12.in.us/guardian/home.html'

login_data = {
    'dbpw': '6eaebef809b1c8b7b9de68775662427a',
    'translator_username': '',
    'translator_password': '',
    'translator_ldappassword': '',
    'returnUrl': '',
    'serviceName': 'PS Parent Portal',
    'serviceTicket': '',
    'pcasServerUrl': '/',
    'credentialType': 'User Id and Password Credential',
    'ldappassword': '20hS>A>A>U>S>O>06',
    'account': 'charlesding',
    'pw': 'd605fca08bc1e82f70e22e3e5f9df827',
    'translatorpw': ''
}

with requests.Session()as s:
    r = s.get(link)
    soup = BeautifulSoup(r.content, 'lxml')
    login_data['pstoken'] = soup.find('input', attrs={'name': 'pstoken'})['value']
    login_data['contextData'] = soup.find('input', attrs={'name': 'contextData'})['value']

    r = s.post(link, data=login_data)
    print(r.text)
