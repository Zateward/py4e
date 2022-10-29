import urllib.request, urllib.parse, urllib.error

try:
    url = input('Enter URL: ')
    file = urllib.request.urlopen(url)
    count = 0

    for line in file:
        line = line.decode()
        count += len(line)

        if count > 3000:
            remain_count = 3000 - count
            print(line[:remain_count], end='')
        elif count == count:
            print(line, end='')

    print('\nCount:',count)
except:
    print('Invalid URL')
