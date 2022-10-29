word = input('Type a word: ')

#Slice notation = [start:stop:step]
word = word[::-1]

#Printing letter by letter in new line each one
for letter in word:
    print(letter)
