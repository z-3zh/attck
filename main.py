from bs4 import BeautifulSoup
import requests  # python3.6   pip install requests
from pyquery import PyQuery as pq  # python3.6   pip install pyquery
import csv

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


def spider(url):
    data_list = []
    try:
        response = requests.get(url)
        doc = pq(response.text)
        for item in doc(".card-body").find("div").items():
            data_list.append(item.text().replace(u'\xa0', ''))
    except Exception as e:
        print("url: {}, error: {}".format(url, e))
    return data_list


# def get_info(url):
#     req = requests.get(url).text
#     soup = BeautifulSoup(req, "lxml")
#     data = soup.findAll('div', class_='card-body')
#     print(data.findAll('span', class_='h5 card-title'))

def write_csv(result):
    with open('result.csv', 'a') as csv_file:
        writer = csv.writer(csv_file)
        for f in result:
            writer.writerow([f])


if __name__ == '__main__':
    url = 'https://attack.mitre.org/tactics/enterprise/'
    # u = 'https://attack.mitre.org/techniques/T1591/'
    # write_csv(spider(u))
    for tu in get_taurl(url):
        for s in get_techurl(main_url + tu):
            print('start:%s' %(s))
            write_csv(spider(main_url + s))
            print('stop:%s' %(s))

    # url_list = [
    #     "https://attack.mitre.org/techniques/T1591/"
    # ]  # ["T1591", "T1592", "T1591"] 添加url即可  以,分隔
    # for url in url_list:
    #     print(spider(url))


# this is dev branches

# this master branches

# this is dev 2

# this is dev3

# this is dev4

# this is master 1

# master 2

# this is master 3
