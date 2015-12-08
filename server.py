import socket
from conf import HOST, PORT, BACKLOG, SIZE

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(BACKLOG)
while True:
    client, address = s.accept()
    data = client.recv(SIZE)
    if data:
        print "receving data"
        client.send(data)
    client.close()
