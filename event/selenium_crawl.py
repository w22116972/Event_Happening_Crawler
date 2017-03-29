import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from bs4 import BeautifulSoup
import re

browser = webdriver.Chrome('/Users/ender/Downloads/chromedriver')
href = []
for url in ['https://www.accupass.com/search/r/1/0/6/0/4/' + str(page) + '/20160101/20161231' for page in range(1501, 1600)]:    
    browser.get(url)
    soup = BeautifulSoup(browser.page_source, 'lxml')
    for ele in soup.select('div.apcss-activity-card.ng-isolate-scope a.apcss-btn.apcss-btn-block.ng-binding.activity-card-status-end'):
        print(ele['href'])
        href.append('http://www.accupass.com/' + ele['href'])

all_data = []
print(len(href))
for url in href:
    data = {}
    browser.get(url)
    soup = BeautifulSoup(browser.page_source, 'lxml')

    # Date
    date_soup = soup.select('ap-gc[gc-dates]')[0]
    date = []
    for t in str(date_soup['gc-dates']).replace('T', '').replace('Z', '').split('/'):
        date.append(t[:10] + ' ' + t[10:-3])
    data['date'] = '~'.join(date)

    # address
    addr_soup = soup.select('ap-gc[gc-location]')[0]
    data['addr'] = str(addr_soup['gc-location'])

    geo = re.findall(r'&sll=.*', soup.select('a[href^=//maps]')[1]['href'])[0][5:].split(',')
    data['lat'] = geo[0]
    data['lng'] = geo[1]
    # find category
    cate = soup.select('a[gtm-name="category"]')
    if len(cate) > 0:
        if len(re.findall(r'[\S]+', cate[0].contents[0])) > 0:
            data['cate'] = str(re.findall(r'[\S]+', cate[0].contents[0])[0])
        else:
            print('cate re has error')
            print(cate[0])
            print(url)
            continue
    else:
        print('No cate')
        print(cate)
        print('####')
        continue
        
    # find title
    title = re.findall(r'>.*<', str(soup.select('div.event-section.apcss-event-view-title > h2')[0]))[0][1:-1]
    data['title'] = title
    all_data.append(data)
browser.close()
print(len(all_data))
with open('accupass_1600.csv', 'w') as f:
    f.write('title,cate,lat,lng,addr,date\n')
    for d in all_data:
        line = d['title'] + ',' + d['cate'] + ',' + d['lat'] + ',' + d['lng'] + ',' + d['addr'] + ',' + d['date'] + '\n'
        f.write(line)
f.close()
