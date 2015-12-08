import Queue
import select
import socket

from conf import ADDRESS, BACKLOG, SIZE

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(0)

print 'starting up on %s port %s' % ADDRESS
server.bind(ADDRESS)
server.listen(BACKLOG)

inputs = [server]
outputs = []
message_queues = {}

while inputs:
    readable, writable, exceptional = select.select(inputs, outputs, inputs)

    for s in readable:
        if s is server:
            connection, client_address = s.accept()
            print 'new connection from', client_address
            connection.setblocking(0)
            inputs.append(connection)
            message_queues[connection] = Queue.Queue()

        else:
            data = s.recv(SIZE)
            if data:
                print 'received from %s' % str(s.getpeername())
                message_queues[s].put(data)
                if s not in outputs:
                    outputs.append(s)
            else:
                print 'closing socket after reading no data'
                inputs.remove(s)
                s.close()
                del message_queues[s]

    for s in writable:
        try:
            next_msg = message_queues[s].get_nowait()
            print 'sending to %s' % str(s.getpeername())
            s.send(next_msg)
        except Queue.Empty:
            print 'output queue for', s.getpeername(), 'is empty'

        outputs.remove(s)

    for s in exceptional:
        print 'handling exceptional condition for', s.getpeername()
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
        s.close()
        del message_queues[s]
