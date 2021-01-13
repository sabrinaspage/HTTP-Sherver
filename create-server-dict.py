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

def getWord(data):
    data = data.partition("GET" + " ")[2]
    if data in dictionary.keys():
         data = 'ANSWER ' + dictionary.get(data)
    else:
        data = 'ERROR ' + data + ' does not exist'
    return data

def setDefinition(data):
    data = data.partition("SET" + " ")[2]
    splitData = data.split('-')
    key = splitData[0]
    value = splitData[1]

    dictionary[key] = value
    return key + ' has been set'

def getAll():
    return json.dumps(dictionary)

def clearDict():
    dictionary.clear()
    return 'dictionary has been cleared'

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

            if "GET" in dataReq:
                dataReq = getWord(dataReq)

            if "SET" in dataReq:
                dataReq = setDefinition(dataReq)

            if "ALL" in dataReq:
                dataReq = getAll()
            
            if "CLEAR" in dataReq:
                dataReq = clearDict()
                print(dictionary)

            if not data:
                break

            dataReq = str.encode(dataReq) # turns back to bytes
            conn.sendall(dataReq)