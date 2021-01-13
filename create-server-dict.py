import socket
import json

dictionary = {
    "satiate": "satisfy fully",
    "shrill": "sharp piercing",
    "unfeigned": "not pretended sincere",
    "sidestep": "step to one side",
    "abeyance": "suspended action"
}

HOST = '127.0.0.1' # Standard loopback interface address (localhost)
PORT = 65432 # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept() # socket object and address info returned
                            # blocked (suspended) when waiting for a client connection
    with conn:
        print('Connected by', addr)
        while True: # infinite loop
            data = conn.recv(1024)
            dataReq = data.decode() # turns to string
            dataReq = dataReq.partition("GET" + " ")[2]

            if dataReq in dictionary.keys():
                dataReq = 'ANSWER ' + dictionary.get(dataReq)
            else:
                dataReq = 'ERROR ' + dataReq + ' does not exist'
            if not data:
                break
            dataReq = str.encode(dataReq) # turns back to bytes
            conn.sendall(dataReq)