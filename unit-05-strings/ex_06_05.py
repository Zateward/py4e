# Separating the number from the text and converting the number in a float value:
str = 'X-DSPAM-Confidence: 0.8475 '

#The find method: find(sub[, start[, end]])
inpos = str.find(':')
#print(inpos)
num = (float(str[18+2:]))
print(num)
