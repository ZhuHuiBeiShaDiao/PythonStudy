from urllib.request import urlopen
from bs4 import BeautifulSoup
from lxml import etree
import time

html = urlopen('https://bbs.pediy.com/')
time.sleep(5)
bsobj = BeautifulSoup(html, 'html.parser')
sels = bsobj.select('#marquee > a')

for sel in sels:
    href = sel.get('href')
    name = sel.text
    out = name[10:] + href[2:]
    print(out)

print('LXML')
e = etree.parse('pediy.html', etree.HTMLParser())
xesls = e.xpath('//*[@id="marquee"]/a')

for xesl in xesls:
    href = xesl.get('href')
    name = xesl.text
    out = name[9:] + ',' + href
    print(out)

