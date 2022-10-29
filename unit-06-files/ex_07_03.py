data = input('Type the .txt file to open it: ')

data = data.lower()
if data == 'na na boo boo':
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
    quit()

else:
    try:
        data = open(data)
        count = 0
        sum = 0


        for line in data:
            line = line.rstrip()
            if not line.startswith('X-DSPAM-Confidence:'):
                continue

            number = float(line[20:])
            count = count + 1
            sum = sum + number

        print('Avergae SPAM Confidence:',(sum/count))

    except :
        print("Couldn't find", '"'+data+'"', 'file.')
