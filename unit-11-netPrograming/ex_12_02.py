import socket

link = input('Enter URL: ')
url = link.split('/')

count = 0

try:
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((url[2], 80))
    cmd = 'GET'+' '+link+' '+'HTTP/1.0\r\n\r\n'
    cmd = cmd.encode()
    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        count += len(data)
        if len(data) < 1: break
        data = data.decode()

        if count > 3000:
            remain_count = 3002 - count
            print(data[:remain_count], end='')
        elif count == count:
            print(data)

    print('\nCount:',count)
    #print(remain_count)

except:
    print('Invalid URL')
