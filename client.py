import socket
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP_address = "localhost"
Port = 1234
server.connect((IP_address, Port))

name = input("Name: ")
server.send(bytes(name, "UTF-8"))

message = server.recv(2048).decode('utf-8')
print(message)

while True:
    message = input()
    server.send(bytes(message, "UTF-8"))
    print("<You>" + message)
server.close()
