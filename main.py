import requests
import lxml
from bs4 import BeautifulSoup

def get_info(url):
    req = requests.get(url).text
    soup = BeautifulSoup(req, "lxml")
    for link in soup.find_all('td'):
        print()

if __name__ == '__main__':
    url = 'https://attack.mitre.org/tactics/enterprise/'
    get_info(url)




