#Defining a function
def count():

    word = input('Type a word or sentence: ')
    letter_to_find = input('Type the letter you wanna count in your word or sentence:')
    count = 0

    #Doing th loop to find a specific letter:
    for letter in word:
        if letter == letter_to_find:
            count = count + 1

    #Printing the Numbers of the input terms:
    print ('There are',count,'"'+letter_to_find+'"','in:',word)

#Excecuting the previously defined function:
count()
