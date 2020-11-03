import requests
import lxml
from bs4 import BeautifulSoup

main_url = "https://attack.mitre.org"
finalurls = []

def get_taurl(url):
    taurls = []
    req = requests.get(url).text
    soup = BeautifulSoup(req, "lxml")
    tables = soup.findAll('table')
    tab = tables[0]
    for tr in tab.findAll('tr'):
        for td in tr.findAll('td'):
            for h in td.findAll('a',href=True):
                taurls.append(h['href'])
    return list(set(taurls))


def get_techurl(url):
    techurls = []
    req = requests.get(url).text
    soup = BeautifulSoup(req, "lxml")
    tables = soup.findAll('table')
    tab = tables[0]
    for tr in tab.findAll('tr'):
        for td in tr.findAll('td'):
            for h in td.findAll('a',href=True):
                techurls.append(h['href'])
    return list(set(techurls))

def get_finalurls(url):
    for u in get_techurl(url):
        print(get_techurl(u))

if __name__ == '__main__':
    url = 'https://attack.mitre.org/tactics/enterprise/'
    for tu in get_taurl(url):
        print(get_techurl(main_url + tu))




