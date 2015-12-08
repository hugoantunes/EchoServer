import socket
from conf import HOST, PORT, SIZE

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send('Hello, world')
data = s.recv(SIZE)
print 'Received:', data
