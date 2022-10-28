import random

while True:
    wrd = input(''.rstrip())
    if wrd == 'done':
        break
    else:
        print (random.randint(0,10))
        continue
