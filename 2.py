
import socket
from select import select


to_monitor = []

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 5001))
server_socket.listen()

def accept_connection(server_socket):
    client_socket, addr = server_socket.accept()
    print('connection From', addr)

    to_monitor.append(client_socket)

def send_message(client_socket):

    request = client_socket.recv(4096)

    if request:
        response = 'Hello \n'.encode()
    else:
        client_socket.close()

def event_loop():
    while True:

        ready_to_ready, _, _ = select(to_monitor, [], [])

        for sock in ready_to_ready:
            print(sock)
            if sock == server_socket:
                accept_connection(sock)
            else:
                send_message(sock)


to_monitor.append(server_socket)
event_loop()