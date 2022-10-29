data = input('Type the file to open it: ')
data = open(data)

dictionary = {}


for lines in data:
    lines = lines.strip()
    if lines.startswith('From:'):
        lines = lines.split()
        #print(lines[1])
        for mail in lines[1:3]:
            dictionary[mail] = dictionary.get(mail,0) + 1

mmesagges = max(dictionary,key=dictionary.get)
print(mmesagges,dictionary[mmesagges])
