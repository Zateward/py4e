from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

sum = 0

url = input('Enter URL: ')
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

for data in soup.find_all('span'):
    number = data.get_text()
    intnumber = int(number)
    sum += intnumber

print('Sum =',sum)
