import socket

server = "127.0.0.1"
port = 6969

newsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
newsocket.connect((server, port))
newsocket.sendall("Hello")
received_data = newsocket.recv(4096)
print received_data
newsocket.close()