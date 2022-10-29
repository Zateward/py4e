total = 0
count = 0

while True:
    number = input('Enter a number: ')
    if number == 'done':
        break
    else:
        try:
            number = float(number)
            count = count + 1
            #print(count)
            total = total + number
            continue
        except:
            print('Invalid input')
            continue
print(count, total, (total/count))
