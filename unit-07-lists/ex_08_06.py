#Creating empty lists to later append them the input data...
maximum = []
minimum = []

#Creating the loop:
while True:
    numbers = input('Type a number: ')
    if numbers == 'done':
        break

    else:
        #Creating the try/except:
        try:
            numbers = float(numbers)

        except :
            print('Invalid input')
            continue

        #Appending numbers to the empty lists (maximum and minimum):
        if numbers not in maximum:
            maximum.append(numbers)

        if numbers not in minimum:
            minimum.append(numbers)

#Searching the maximum and minimum values with max() and min() functions:
maximum = max(maximum)
minimum = min(minimum)

print('Maximum: ',maximum)
print('Minimum: ',minimum)
