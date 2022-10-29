#Opening the .txt file and creating an empty dictionary.
file = open('words.txt')
dwords = dict()

#Doing the
for words in file:
    words = words.split()
    for word in words:
        if word not in dwords:
            dwords[word] = word

print(dwords)
print('')
print('cell' in dwords)
