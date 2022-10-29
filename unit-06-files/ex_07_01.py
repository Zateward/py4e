file = input('Type the file to open: ')
data = open(file)

for line in data:
    print(line.upper())
