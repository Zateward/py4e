data = input('Type the file to open it: ')
count = 0
try:
    if data == 'IDK':
        print('Fucking IDIOT...')

    else:
        data = open(data)

        for lines in data:
            lines = lines.rstrip()
            if lines.startswith('From '):
                count = count + 1
                lines = lines.split()
                print(lines[1])

        print('There were',count,'lines that had started with the word "From".')

except :
    print('Invalid file name')
