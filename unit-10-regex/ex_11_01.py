import re

data = input('Type a file to open it: ')
if len(data) < 1:
    data = 'mbox-short.txt'

odata = open(data)
count = 0

while True:
    ui = input('Enter a regular expression: ')
    if ui == 'done': break
    else:
        for lines in odata:
            word = re.findall(ui, lines)
            if len(word) < 1:
                continue
            print(word)
            if word == word:
                count = count + 1
    print(data, 'had', count, 'lines that matched:', ui)
