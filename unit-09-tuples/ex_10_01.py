data = input('Type the file to open it: ')
data = open(data)

dictionary = {}

for lines in data:
    lines = lines.strip()
    if lines.startswith('From '):
        lines = lines.split()
        lines = lines[1]
        #print (lines)
        for i in lines[0]:
            #print (i)
            dictionary[lines] = dictionary.get(lines , 0) + 1

#print (dictionary)

lst = []

for email, count in list(dictionary.items()):
    lst.append((count, email))

lst.sort(reverse=True)
#print(lst)

for count, email in lst[:1]:
    print(email,count)
