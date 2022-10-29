text = open('romeo.txt')
lst = list()

for words in text:
    words = words.rstrip()
    words = words.split()
    #print(words)
    for i in range(len(words)):
        #print(words[i])
        if words[i] not in lst:
            lst.append(words[i])

lst.sort()
print(lst)
