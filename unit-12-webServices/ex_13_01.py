import urllib.parse, urllib.request, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Asking for a URL and converting to bytes-like object with .read()
url = input('Enter XML-URL: ')
xml = urllib.request.urlopen(url).read()
tree = ET.fromstring(xml)

# Finding all the <count>##</count> values in the url
count = tree.findall('.//count')
#print(count)

total = 0

#Summing all the count values into a variable named 'total' and then printing the total

for sum in count:
    total += int(sum.text)

print('\nTotal:', total)
