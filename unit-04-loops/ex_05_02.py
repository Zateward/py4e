# Making "None" variables allows you to assign them a value later...
max_num = None
min_num = None

# Making the loop program:
while True:
    number = input('Type a number: ')
    if number == 'done' or number == 'DONE' or number == 'Done':
        break
    else:
        try:
            number = float(number)

            # Making the min_num and max_num works:
            if max_num is None or number > max_num:
                max_num = number

            if min_num is None or number < min_num:
                min_num = number
        except :
            print('Invalid input')

        continue

print('Max number is',max_num)
print('Min number is',min_num)
