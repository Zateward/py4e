hrs = input('Enter the hours you may work: ')
try:
    hrs = float(hrs)
except:
    print('Error, please enter numeric input')
    quit()

rph = input('Type the money you may recieve per hour: ')
try:
    rph = float(rph)
except:
    print('Error, please enter numeric input')
    quit()

if hrs > 40:
    rph = rph*1.5
    print('Pay:',hrs*rph)

else:
    print('Pay:', (hrs*rph))
