doc = input('Type the file to open it: ')
doc  = open(doc)

dictionary = {}

for lines in doc:
    lines = lines.strip()
    if lines.startswith('From:'):
        lines = lines.split()
        lines = lines[1]
        for times in lines[1]:
            if lines not in dictionary:
                dictionary[lines] = 1
            else:
                dictionary[lines] += 1

print(dictionary)
