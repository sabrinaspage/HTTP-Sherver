import socket
import time

HOST = '127.0.0.1' # The server's hostname or IP address
PORT = 65432 # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    for x in range(6):
        time.sleep(2)
        s.send(b'hi ')
        data = s.recv(1024) # receive the data sent to the server
        print('Received', repr(data))