# Python program to implement server side of chat room.
import socket

from _thread import *

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP_address = "0.0.0.0"

Port = 1234

server.bind((IP_address, Port))
server.listen(100)

list_of_clients = {}


def clientthread(conn, addr, name):
    conn.send(bytes(f"Welcome to this chat {name}!", "UTF-8"))

    while True:
        try:
            message = conn.recv(2048)
            if message.decode('utf-8'):
                message_to_send = "<" + name + "> " + message.decode('utf-8')
                print(message_to_send)

                broadcast(message_to_send, conn)

            else:
                remove(conn)

        except:
            continue


def broadcast(message, connection):
    for client in list_of_clients:
        if list_of_clients[client][0] != connection:
            try:
                list_of_clients[client][0].send(bytes(message, "utf-8"))
            except:
                list_of_clients[client][0].close()

                # if the link is broken, we remove the client
                remove(list_of_clients[client])


def remove(connection):
    if connection in list_of_clients:
        list_of_clients.pop(connection)


while True:
    conn, addr = server.accept()

    name = conn.recv(2048).decode('utf8')

    list_of_clients[name] = (conn, addr)

    print(name + " connected")

    start_new_thread(clientthread, (conn, addr, name))

conn.close()
server.close()
