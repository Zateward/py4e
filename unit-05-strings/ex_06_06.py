print('ß')
print('ß'.lower())
#The "ß" is equivalent to "ss"
print('ß'.casefold())

str = 'My mom is the best of all moms in the world!'
print(str.split())

str = 'I am awesome'
print(str.replace('awesome','the best'))

str = 'ThIS Is awESoMe'
print(str.swapcase())

str = """This is line 1
This is line 2
This is line 3"""
print(str.splitlines())

str = "Hola, What's hanning"
print(str.index("What's"))

str = 'My name is Luis Eduardo'.lower()
print(str.startswith('my'.lower()))
