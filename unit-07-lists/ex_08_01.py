def chop():
    lst = ['banana', 34, 'ZATE', True, None, 73, 'Egoland', False]

    lst.remove('banana')
    lst.remove(False)

    print(lst)
    print('')


def middle():
    lst = ['banana', 34, 'ZATE', True, None, 73, 'Egoland', False]
    #print(lst.index(False))
    x = lst.pop(0), lst.pop(6)
    slst = list(x)
    #slst = slst.split()
    print(lst)
    print(slst)

chop()
middle()
