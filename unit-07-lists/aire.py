poem = open('aire.txt')
lst = []

for lines in poem:
    lines = lines.rstrip()
    lines = lines.split()
    #print(lines)
    for i in range(len(lines)):
        #print(lines[i])
        if lines[i] not in lst:
            lst.append(lines[i])

lst.sort()
print(lst)
