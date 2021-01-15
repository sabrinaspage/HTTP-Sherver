import selectors
import socket
import types

HOST = '127.0.0.1' # The server's hostname or IP address
PORT = 65432 # The port used by the server
sel = selectors.DefaultSelector()

def service_connection(key, mask):
    sock = key.fileobj
    data = key.data

    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024) # should be ready to read
        if recv_data:
            data.outb += recv_data
        else:
            print('closing connection to', data.addr)
            sel.unregister(sock)
            sock.close()
    if mask & selectors.EVENT_WRITE:
        if data.outb:
            print('echoing', repr(data.outb), 'to', data.addr)
            sent = sock.send(data.outb) # should be ready to write
            data.outb = data.outb[sent:]

def accept_wrapper(sock):
    conn, addr = sock.accept() # socket object and address returned
    print('accepted connection from', addr)
    conn.setblocking(False)
    data = types.simpleNamespace(addr=addr, inb=b'', outb=b'')
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    sel.register(conn, events, data=data)

# listening socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as lsock:
    lsock.bind((HOST, PORT))
    lsock.listen()

    print('listening on', (HOST, PORT))
    lsock.setblocking(False) # socket can no longer block

    sel.register(lsock, selectors.EVENT_READ, data=None) # monitored with select() for events you're interested in
    while True:
        events = sel.select(timeout=None) # blocks until there are sockets ready for I/O
                                          # we wait for events on one or more sockets
        for key, mask in events:
            if key.data is None:
                accept_wrapper(key.fileobj)
            else:
                service_connection(key, mask)