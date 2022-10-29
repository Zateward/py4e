import urllib.parse, urllib.request, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Asking for an URL and openind in bytes-object with ".read()"
url  = input('Enter JSON-URL: ')
data = urllib.request.urlopen(url).read()
js = json.loads(data)

#Creating an empty list, then to sum all the values
lst = []

#Finding all the "count" numbers to append and the sum into the list
for numbers in js['comments']:
    #print(numbers)
    lst.append(numbers['count'])

#Printing the total
print('\nTotal:',sum(lst))
