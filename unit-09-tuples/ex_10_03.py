import string

data = input('Type a text to see the letter frequency: ')

data = data.lower()
data = data.translate(data.maketrans('','', string.punctuation))
data = data.translate(data.maketrans('','', string.digits))
data = data.translate(data.maketrans('','', string.whitespace))
data = data.translate(data.maketrans('','', 'á'))
data = data.translate(data.maketrans('','', 'é'))
data = data.translate(data.maketrans('','', 'í'))
data = data.translate(data.maketrans('','', 'ó'))
data = data.translate(data.maketrans('','', 'ú'))

dictionary = {}

for letter in data:
    dictionary[letter] = dictionary.get(letter, 0) + 1

#print(dictionary)
lst = list()

for k,v in list(dictionary.items()):
    lst.append((k,v))

lst.sort()

for k,v in lst:
    print(k+':',v)
