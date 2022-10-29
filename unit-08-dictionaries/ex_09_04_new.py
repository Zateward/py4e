data = input('Type the file to open it: ')
data = open(data)

dictionary = {}

for lines in data:
    lines = lines.strip()
    if lines.startswith('From: '):
        lines = lines.split()
        #print(lines)
        for i in lines[1:2]:
                dictionary[i] = dictionary.get(i, 0) + 1

#print(dictionary)

bigcount = None
bigword = None

for word,count in dictionary.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)
