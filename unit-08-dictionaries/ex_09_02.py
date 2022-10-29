data = input('Type the file to open it: ')
data = open(data)

dictionary = dict()

for line in data:
    line = line.strip()
    if line.startswith('From '):
        line = line.split()
        #print(line)
        #print(day)
        for day in line[2:3]:
            if day not in dictionary:
                dictionary[day] = 1
            else:
                dictionary[day] += 1
print(dictionary)
