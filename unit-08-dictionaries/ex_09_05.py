data = input('Type the file to open it: ')
data = open(data)

dictionary = {}

for lines in data:
    lines = lines.strip()
    if lines.startswith('From: '):
        lines = lines.split('@')
        #print(lines[1])
        direction = lines[1:2]
        #print(direction)
        for drt in direction:
            dictionary[drt] = dictionary.get(drt,0) + 1

print(dictionary)
