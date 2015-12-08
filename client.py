import socket
from conf import ADDRESS, SIZE

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect(ADDRESS)

server.send('''
    Hello, world
    Nice to meet you!
''')
data = server.recv(SIZE)
print data
