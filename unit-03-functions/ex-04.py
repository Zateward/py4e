def computegrade():

    grade = input('Enter your grade: ')

    try:
        grade = float(grade)

        if grade > 10:
            print('Bad score')
        elif grade >= 9:
            print('A')
        elif grade >= 8:
            print('B')
        elif grade >= 7:
            print('C')
        elif grade >= 6:
            print('D')
        elif grade < 6 and grade >= 0:
            print('F')
        elif grade < 0:
            print('Bad score')

    except:
        print('Bad score')

computegrade()
