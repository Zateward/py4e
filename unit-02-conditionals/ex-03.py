grade = input('Enter your grade:')
grade = float(grade)

if grade > 10:
    print('Your grade is not valid.'.upper())
elif grade >= 9:
    print('A')
elif grade >= 8:
    print('B')
elif grade >= 7:
    print('C')
elif grade >= 6:
    print('D')
elif grade < 6:
    print('F')
