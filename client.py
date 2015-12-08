import socket
from conf import ADDRESS, SIZE

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect(ADDRESS)

server.send('''
oi
''')
data = server.recv(SIZE)
print data


server.send('''
tudo bem ?
''')
data = server.recv(SIZE)
print data


server.send('''
tudo otimo e vc ?
''')
data = server.recv(SIZE)
print data

server.send('''
que bom =D
''')
data = server.recv(SIZE)
print data

