# "Coputepay program with functions"

#Creating the function with 'def'
def computepay():

    #Doing the varibales:
    how = input('Enter the hours of work: ')
    mph = input('Enter the money per hour: ')

    #The program with try/except structure:
    try:
        how = float(how)
        mph = float(mph)

        if how > 40:
            pay = (how*1.5)*mph
            print(pay)
        else:
            print(how*mph)

    except:
        print('Invalid input')

#Running the defined function:
computepay()
