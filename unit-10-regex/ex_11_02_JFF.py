import re

print(sum([int(i) for i in re.findall('[0-9]+',open(input('Type a file to open it: ')).read())]))
