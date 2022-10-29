import re

data = input('Type a file to open it: ')
if len(data) < 1:
    data = 'mbox-short.txt'
data = open(data)

lst = []
count = 0

for lines in data:
    numbers = re.findall('[0-9]+',lines)
    if len(numbers) == 0:
        continue
    #numbers = int(numbers)
    #print(numbers)
    for i in numbers:
        #print(i)
        count += 1
        lst.append(i)

lst = [int(elements) for elements in lst]

#print(lst)
sum = sum(lst)
print(sum)
#print(int(sum/count))
