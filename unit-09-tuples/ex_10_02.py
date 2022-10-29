data = input('Type a file to open it: ')
data = open(data)

dictionary = dict()

for line in data:
    line = line.strip()
    if line.startswith('From '):
        line = line.split(':')
        line = line[0]
        line = line.split()
        line = line[::-1]
        hour = line[0]
        #print (hour)
        for i in hour[0]:
            dictionary[hour] = dictionary.get(hour, 0) + 1

lst = []

for hour, count in list(dictionary.items()):
    lst.append((hour, count))

lst.sort()
#print(lst)

for hour, count in lst:
    print(hour, count)
