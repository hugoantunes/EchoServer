import socket
from conf import ADDRESS, BACKLOG, SIZE

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(0)

server.bind(ADDRESS)
server.listen(BACKLOG)

while True:
    client, address = server.accept()
    data = client.recv(SIZE)
    if data:
        print "receving data"
        client.send(data)
    client.close()
