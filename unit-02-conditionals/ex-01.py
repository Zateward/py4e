hrs = input('Enter the hours you may work: ')
rph = input('Type the money you may recieve per hour: ')

hrs = float(hrs)
rph = float(rph)

if hrs > 40:
    rph = rph*1.5
    print('Pay:',hrs*rph)

else:
    print('Pay:', (hrs*rph))
