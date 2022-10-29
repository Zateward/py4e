data = input('Type the .txt file to open it: '.capitalize())
data = open(data)
count = 0
sum = 0
#print(data)

for line in data:
    line = line.rstrip()
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    #print(line)
    number = float(line[20:])
    #print(line.index('0')) """That's to Check where the number starts."""
    #print(type(number))
    count = count + 1
    #print(count)
    sum = sum + number

    #print(number)
#print(sum)
print('Avergae SPAM Confidence:',(sum/count))
