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
    data = [[cell for cell in row.find_all('td')[1:2]]
            for row in soup.find_all("tr", class_=True)]
    for d in data:
        techurls.append(d[0].findAll('a')[0]['href'])
    return techurls


def get_info(url):
    for u in get_techurl(url):
        print(get_techurl(u))


if __name__ == '__main__':
    url = 'https://attack.mitre.org/tactics/enterprise/'
    # u = 'https://attack.mitre.org/tactics/TA0002'
    # get_techurl(u)
    for tu in get_taurl(url):
        for s in get_techurl(main_url + tu):
            print(s)




