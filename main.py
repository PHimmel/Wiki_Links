from bs4 import BeautifulSoup as Bs
from urllib import request
import urllib

x = 20
link_stem = 'https://en.wikipedia.org/'
link = 'https://en.wikipedia.org/wiki/Finance'

while x >= 0:
    raw_html = urllib.request.urlopen(link).read()
    soup = Bs(raw_html, 'html.parser')
    for n in soup.find_all('p'):
        for a in n.find_all('a'):
            if not soup.find('b'):
                break
            part = a.get('href')
            if part is None:
                continue
            if '/wiki/' in part:
                link = f'{link_stem}{part}'
                break
    print(link)
    x -= 1

