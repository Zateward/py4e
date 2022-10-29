import urllib.parse, urllib.request, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
position = input('Enter position: ')
ttr = input('Enter times to repeat: ')
lst = []

for lqs in range(int(ttr)):
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup.find_all('a')
    url = tags[int(position) - 1].get('href', None)
    print(url)
    lst.append(url)

for name in tags:
    if lst[len(lst) - 1] is name.get('href', None):
        print(name.contents[0])
