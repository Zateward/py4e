import socket

link = input('Enter URL: ')
url = link.split('/')

try:
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((url[2], 80))
    cmd = 'GET'+' '+link+' '+'HTTP/1.0\r\n\r\n'
    cmd = cmd.encode()
    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        print(data.decode().strip(),end='')

    mysock.close()

except:
    print('Invalid URL')
