import socket
from conf import ADDRESS, SIZE

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect(ADDRESS)

server.send('Hello, world')
data = server.recv(SIZE)
print 'Received:', data
